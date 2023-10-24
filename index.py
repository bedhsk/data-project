import csv

from modules.mongo import Mongo
from modules.dynamo import Dynamo
from modules.mariadb import MariaDB

dynamo_base = Dynamo()
maria_base = MariaDB()
mongo_base = Mongo()


def get_data():
    data_route = "data.csv"
    with open(data_route, newline="") as data:
        lector = csv.reader(data, delimiter=";", quotechar='"')
        for i, row in enumerate(lector):
            lectura = maria_base.cursor.lastrowid

            if lectura is None:
                lectura = 0
            else:
                lectura = int(lectura)

            if i > lectura:
                # !INSERT DATA DYNAMO
                dynamo_base.insert(i, row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5]), float(
                    row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), row[12])

                # !INSERT DATA MONGODB
                mongo_base.insert(i, row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5]), float(
                    row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), row[12])

                # !INSERT DATA MARIADB
                maria_base.insert(row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5]), float(
                    row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), row[12])


get_data()

# close connections
# maria_base.close_connections()
mongo_base.close_connection()
