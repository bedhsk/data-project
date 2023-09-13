import pymongo


class Mongo:
    def __init__(self) -> None:
        MONGO_HOST = "localhost"
        MONGO_PORT = "27017"
        MONGO_TIME_OUT = 1000

        MONGO_DATABASE = "test"
        MONGO_COLECTION = "autoinsert"

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

    def insert(self, customer_id: str, order_id: str, status_name: str):
        try:
            document = {
                "customer_id": customer_id,
                "order_id": order_id,
                "created_date": "hoy",
                "status": status_name,
            }
            self.collection.insert_one(document)
        except pymongo.errors.ConnectionFailure as connectionError:
            print(connectionError)

    def close_connection(self):
        self.client.close()
