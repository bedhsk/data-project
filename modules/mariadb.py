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
            print("mariadb_connection_succesfull")

        # Cursor para ejectuar consulta
            self.cursor = self.connection.cursor()

    def insert(self, id: str, age: int, height: int, weight: int, sight_left: float, sight_right: float, SBP: float, DBP: float, BLDS: float, tot_chole: float, gamma_GTP: float, SMK_stat_type_cd:float, DRK_YN: str):
        # !INSERT DATA MARIADB
        # TODO ->> Cambiar las sentencias de insert
        sql = "INSERT INTO Demo (id, age, height, weight, sight_left, sight_right, SBP, DBP, BLDS, tot_chole, gamma_GTP, SMK_stat_type_cd, DRK_YN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        time = datetime.now().isoformat()
        values = (id, age, height, weight, sight_left, sight_right, SBP, DBP, BLDS, tot_chole, gamma_GTP, SMK_stat_type_cd, DRK_YN)

        self.cursor.execute(sql, values) # ejecutar

        self.connection.commit() # confirmar cambios

    def close_connections(self):
        # Cerrar el cursor y la conexión
        self.cursor.close()
        self.connection.close()