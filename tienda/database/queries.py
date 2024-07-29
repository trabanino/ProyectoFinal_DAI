from tienda.database.conexion import create_connection
from mysql.connector import Error
# unico a login
import logging
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

# unico a productos


import logging

def handle_register_process(user, name, email, password):
    connection = create_connection()
    if connection is None:
        return False, "Fallo al conectar con la DB"

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Usuario (user, Nombre, Email, password) VALUES (%s, %s, %s, %s)
        """
        print(f"Executing query: {query} with values: {(user, name, email, password)}")  # Debug print
        cursor.execute(query, (user, name, email, password))
        connection.commit()
        return True, "Registro exitoso"
    except Exception as e:
        logging.error(f"Error al registrar el nuevo usuario: {e}")
        print(f"Error al registrar el nuevo usuario: {e}")  # Debug print
        return False, f"Error al registrar el nuevo usuario: {e}"
    finally:
        if connection:
            cursor.close()
            connection.close()
