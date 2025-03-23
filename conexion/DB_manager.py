import mysql.connector
from mysql.connector import Error

class DBManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establece la conexión con la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
    
    def close(self):
        """Cierra la conexión con la base de datos"""
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

    def execute_query(self, query, values=None):
        """Ejecuta una consulta SQL de tipo SELECT, INSERT, UPDATE, DELETE"""
        cursor = self.connection.cursor()
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            # Si la consulta es un SELECT, obtener el resultado
            if cursor.with_rows:
                result = cursor.fetchall()  # Leer todos los resultados
                cursor.nextset()  # Mover al siguiente conjunto de resultados si existe
            else:
                result = None

            self.connection.commit()  # Asegurar commit si es necesario
            cursor.close()  # Cerrar cursor
            # Si la consulta fue de tipo INSERT, UPDATE o DELETE y no hubo error, retornar True
            if result is None:  # Esto indica que no hay resultado de consulta SELECT
                return True
            return result  # Si es un SELECT, retorna el resultado de las filas
        
        except Error as e:
            # Verificar si el código de error es 1062 (duplicate entry)
            if "1062" in str(e):
                print("Error: El correo ya está registrado.")
            else:
                print(f"Error al ejecutar la consulta: {e}")
            
            cursor.close()  # Cerrar el cursor en caso de error
            return None

