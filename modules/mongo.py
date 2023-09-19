import pymongo


class Mongo:
    def __init__(self) -> None:
        # TODO ->> Modificar la DATABASE Y COLECTION para agregar datos
        MONGO_HOST = "localhost"
        MONGO_PORT = "27017"
        MONGO_TIME_OUT = 1000

        MONGO_DATABASE = "datos"
        MONGO_COLECTION = "medidas"

        MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/"

        try:
            self.client = pymongo.MongoClient(
                MONGO_URI, serverSelectionTimeoutMS=MONGO_TIME_OUT
            )
            print("mongo_connection_successful")

            # database
            self.database = self.client[MONGO_DATABASE]
            self.collection = self.database[MONGO_COLECTION]
        except pymongo.errors.ServerSelectionTimeoutError as tiemeout:
            print("Tiempo excedido " + tiemeout)
        except pymongo.errors.ConnectionFailure as connectionError:
            print("Error de conexión" + connectionError)

    # TODO ->> Modificar esta sentencia para añadir datos
    def insert(
        self,
        id: int,
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
        try:
            document = {
                "id": id,  # partition key
                "sex": sex,
                "age": age,
                "height": height,
                "weight": weight,
                "sight_left": sight_left,
                "sight_right": sight_right,
                "SBP": SBP,
                "DBP": DBP,
                "BLDS": BLDS,
                "tot_chole": tot_chole,
                "gamma_GTP": gamma_GTP,
                "SMK_stat_type_cd": SMK_stat_type_cd,
                "DRK_YN": DRK_YN,
            }
            self.collection.insert_one(document)
        except pymongo.errors.ConnectionFailure as connectionError:
            print(connectionError)

    def close_connection(self):
        self.client.close()
