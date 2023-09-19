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
        for i, row in enumerate(lector):
            # # !INSERT DATA MARIADB
            maria_base.insert(i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            # # !INSERT DATA DYNAMO
            dynamo_base.insert(i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            # # !INSERT DATA MONGODB
            mongo_base.insert(i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])

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