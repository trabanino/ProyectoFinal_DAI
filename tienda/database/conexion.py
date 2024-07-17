import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='sql.trabanino.xyz',
            user='app_user',
            password='app_password',
            database='store_app'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar con MariaDB", e)
        return None