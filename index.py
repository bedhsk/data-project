import csv

from modules.mongo import Mongo
from modules.dynamo import Dynamo
from modules.mariadb import MariaDB

dynamo_base = Dynamo()
maria_base = MariaDB()
mongo_base = Mongo()

def get_data():
    with open('data.csv', newline='') as data:
        lector = csv.reader(data, delimiter=';', quotechar='"')
        for row in lector:
            print("Sexo: ", row[0], "otro: ", row[1])

get_data()

# # !INSERT DATA DYNAMO
# for i in range(50):
#     dynamo_base.insert(f"cus-10{i}", f"ord-10{i}", "pending")

# # !INSERT DATA MARIADB
# for i in range(50):
#     maria_base.insert(f"cus-10{i}", f"ord-10{i}", "pending")
# maria_base.close_connections()

# # !INSERT DATA MONGODB
# for i in range(50):
#     mongo_base.insert(f"cus-10{i}", f"ord-10{i}", "pending")
# mongo_base.close_connection()