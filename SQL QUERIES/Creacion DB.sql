-- Create the database
CREATE DATABASE IF NOT EXISTS store_app;
USE store_app;

-- Create Usuario table
CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Create Admin table
CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Create Categoria table
CREATE TABLE Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL
);

-- Create Producto table
CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Cantidad INT NOT NULL,
    Descripcion TEXT,
    Proveedor VARCHAR(100),
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id)
);

-- Create Orden table
CREATE TABLE Orden (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Usuario INT,
    Total DECIMAL(10, 2) NOT NULL,
    Fecha DATETIME NOT NULL,
    Status ENUM('Pendiente', 'Completada', 'Cancelada') NOT NULL,
    FOREIGN KEY (Usuario) REFERENCES Usuario(id)
);

-- Create OrdenProducto table (junction table for many-to-many relationship)
CREATE TABLE OrdenProducto (
    orden_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (orden_id, producto_id),
    FOREIGN KEY (orden_id) REFERENCES Orden(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id)
);