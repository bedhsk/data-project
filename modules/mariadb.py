# Insertar datos en MariaDB
import mysql.connector as mariadb
from datetime import datetime

class MariaDB:
    def __init__(self) -> None:
        # TODO ->> Reemplazar database
        self.connection = mariadb.connect(
            user = "root",
            password = "bbbbbbb7",
            host = "localhost",
            database = "autoinsert"
        )

        if self.connection.is_connected():
            print("connection succesfull")

        # Cursor para ejectuar consulta
            self.cursor = self.connection.cursor()

    def insert(self, customer_id: str, order_id: str, status_name: str):
        # !INSERT DATA MARIADB
        # TODO ->> Cambiar las sentencias de insert
        sql = "INSERT INTO Demo (customer_id, order_id, created_date, status) VALUES (%s, %s, %s, %s);"
        time = datetime.now().isoformat()
        values = (customer_id, order_id, time, status_name)

        self.cursor.execute(sql, values) # ejecutar

        self.connection.commit() # confirmar cambios

    def close_connections(self):
        # Cerrar el cursor y la conexión
        self.cursor.close()
        self.connection.close()