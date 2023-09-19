import csv

from modules.mongo import Mongo
from modules.dynamo import Dynamo
from modules.mariadb import MariaDB

dynamo_base = Dynamo()
maria_base = MariaDB()
mongo_base = Mongo()


def get_data():
    data_route = "C:\\Users\\brian\\code\\python\\autoinsert\\data.csv"
    with open(data_route, newline="") as data:
        lector = csv.reader(data, delimiter=";", quotechar='"')
        for i, row in enumerate(lector):
            documento = open("cuenta.txt", newline="")
            lectura = int(documento.readline())
            if i > lectura:
                # !INSERT DATA MARIADB
                maria_base.insert(
                    row[0],
                    int(row[1]),
                    int(row[2]),
                    int(row[3]),
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                    float(row[7]),
                    float(row[8]),
                    float(row[9]),
                    float(row[10]),
                    float(row[11]),
                    row[12],
                )
                # !INSERT DATA DYNAMO
                dynamo_base.insert(
                    i,
                    row[0],
                    int(row[1]),
                    int(row[2]),
                    int(row[3]),
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                    float(row[7]),
                    float(row[8]),
                    float(row[9]),
                    float(row[10]),
                    float(row[11]),
                    row[12],
                )
                # !INSERT DATA MONGODB
                mongo_base.insert(
                    i,
                    row[0],
                    int(row[1]),
                    int(row[2]),
                    int(row[3]),
                    float(row[4]),
                    float(row[5]),
                    float(row[6]),
                    float(row[7]),
                    float(row[8]),
                    float(row[9]),
                    float(row[10]),
                    float(row[11]),
                    row[12],
                )
                documento.close()
                documento = open("cuenta.txt", "w", newline="")
                documento.write(str(i))

        documento = open("cuenta.txt", "w", newline="")
        documento.write("0")
        documento.close()


get_data()

# close connections
maria_base.close_connections()
mongo_base.close_connection()