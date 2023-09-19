# Insertar datos en MariaDB
import mysql.connector as mariadb


class MariaDB:
    def __init__(self) -> None:
        # TODO ->> Reemplazar database
        self.connection = mariadb.connect(
            user="root", password="bbbbbbb7", host="localhost", database="datos_medicos"
        )

        if self.connection.is_connected():
            print("mariadb_connection_succesfull")

            # Cursor para ejectuar consulta
            self.cursor = self.connection.cursor()

    def insert(
        self,
        sex: str,
        age: int,
        height: int,
        weight: int,
        sight_left: float,
        sight_right: float,
        SBP: float,
        DBP: float,
        BLDS: float,
        tot_chole: float,
        gamma_GTP: float,
        SMK_stat_type_cd: float,
        DRK_YN: str,
    ):
        # !INSERT DATA MARIADB
        # TODO ->> Cambiar las sentencias de insert
        sql = "INSERT INTO Medidas (sex, Age, Height, Weight, SightLeft, SightRight, SBP, DBP, BLDS, Tot_Chole, GammaGTP, SMKStartTypeCd, DRK_YN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        values = (
            sex,
            age,
            height,
            weight,
            sight_left,
            sight_right,
            SBP,
            DBP,
            BLDS,
            tot_chole,
            gamma_GTP,
            SMK_stat_type_cd,
            DRK_YN,
        )

        self.cursor.execute(sql, values)  # ejecutar

        self.connection.commit()  # confirmar cambios

    def close_connections(self):
        # Cerrar el cursor y la conexión
        self.cursor.close()
        self.connection.close()
