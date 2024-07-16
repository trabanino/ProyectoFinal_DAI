-- Populate Categoria table
INSERT INTO Categoria (Nombre) VALUES
('Lácteos'),
('Frutas y Verduras'),
('Carnes'),
('Panadería'),
('Bebidas'),
('Limpieza'),
('Conservas'),
('Snacks');

-- Populate Producto table
INSERT INTO Producto (Nombre, Precio, Cantidad, Descripcion, Proveedor, categoria_id) VALUES
('Leche Entera', 1.05, 100, 'Leche entera de vaca, 1 litro', 'Lácteos del Valle', 1),
('Yogur Natural', 0.75, 50, 'Pack de 4 yogures naturales', 'Yogures Frescos', 1),
('Plátanos', 1.20, 80, 'Plátanos de Canarias, 1 kg', 'Frutas del Sur', 2),
('Tomates', 1.50, 60, 'Tomates maduros, 1 kg', 'Huerta Local', 2),
('Pechuga de Pollo', 4.50, 30, 'Pechuga de pollo fresca, 500g', 'Aves del Campo', 3),
('Pan de Molde', 1.80, 40, 'Pan de molde integral, 750g', 'Panadería García', 4),
('Coca-Cola', 1.60, 100, 'Botella de Coca-Cola, 2 litros', 'Coca-Cola Company', 5),
('Agua Mineral', 0.60, 150, 'Botella de agua mineral, 1.5 litros', 'Manantiales Puros', 5),
('Detergente Lavadora', 5.95, 25, 'Detergente líquido, 40 lavados', 'Limpieza Total', 6),
('Papel Higiénico', 3.50, 50, 'Pack de 12 rollos', 'Papelera Suave', 6),
('Atún en Lata', 1.20, 80, 'Atún en aceite de oliva, 80g', 'Conservas del Mar', 7),
('Garbanzos Cocidos', 0.90, 60, 'Garbanzos cocidos en conserva, 400g', 'Legumbres La Abuela', 7),
('Patatas Fritas', 1.30, 70, 'Bolsa de patatas fritas, 150g', 'Snacks Crujientes', 8),
('Aceite de Oliva', 4.50, 40, 'Aceite de oliva virgen extra, 1 litro', 'Olivos Andaluces', 7),
('Huevos', 2.20, 50, 'Docena de huevos frescos', 'Granja Feliz', 1),
('Manzanas', 1.80, 70, 'Manzanas Golden, 1 kg', 'Frutas del Norte', 2),
('Jamón Serrano', 5.50, 20, 'Jamón serrano en lonchas, 200g', 'Ibéricos de Calidad', 3),
('Arroz', 1.25, 100, 'Arroz redondo, 1 kg', 'Arroces del Levante', 7),
('Pasta de Dientes', 1.80, 45, 'Pasta dentífrica, 75ml', 'Sonrisas Brillantes', 6),
('Cerveza', 3.80, 60, 'Pack de 6 latas de cerveza, 33cl cada una', 'Cervezas Artesanas', 5);