from tienda.database.conexion import create_connection

def handle_login_attempt(username, password, ip_address):
    try:
        connection = create_connection()
        if connection is None:
            return False, "Fallo al conectar con la BD"
        cursor = connection.cursor()

        cursor.execute("SELECT Password FROM Usuario WHERE user = %s", (username,))
        result = cursor.fetchone()
        if result and result[0] == password:
            return True, "Login exitoso"
        else:
            cursor.execute("SELECT COUNT(*) FROM IPs WHERE ip_address = %s AND attempt_time > (NOW() - INTERVAL 1 DAY)", (ip_address,))
            attempts = cursor.fetchone()[0]
            if attempts < 10:
                cursor.execute("INSERT INTO IPs (ip_address) VALUES (%s)", (ip_address,))
                connection.commit()
                return False, "Login fallido: Usuario o contraseña incorrectos"
            else:
                return False, "Login fallido: Demasiados intentos desde esta dirección IP"
    finally:
        if connection:
            connection.close()

def get_categories():
    try:
        connection = create_connection()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute("SELECT id, Nombre, imagen FROM Categoria")
        categories = cursor.fetchall()
        return categories
    finally:
        if connection:
            connection.close()

def get_products_by_category(category_id):
    try:
        connection = create_connection()
        if connection is None:
            return []
        cursor = connection.cursor()
        cursor.execute("SELECT Nombre, Precio, Imagen FROM Producto WHERE categoria_id = %s", (category_id,))
        products = cursor.fetchall()
        return products
    finally:
        if connection:
            connection.close()


#test

