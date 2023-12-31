from boto3 import resource
from datetime import datetime

import json
from decimal import Decimal


# Insertar datos en DynamoDb
class Dynamo:
    def __init__(self) -> None:
        # TODO ->> Cambiar el nombre de la tabla (Table(xxxxxx)) y/o agregar más tablas
        self.demo_table = resource("dynamodb").Table(
            "datos_medicos"
        )  # acceso a la tabla

    # TODO ->> Modificar esta sentencia para que encaje con la tabla
    def insert(self, id: int, sex: str, age: int, height: int, weight: int, sight_left: float, sight_right: float,
               SBP: float, DBP: float, BLDS: float, tot_chole: float, gamma_GTP: float, SMK_stat_type_cd: float,
               DRK_YN: str):
        print("Insertando datos en dynamo")

        item = {  # elementos de la tabla
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

        item = json.loads(json.dumps(item), parse_float=Decimal)

        response = self.demo_table.put_item(
            Item=item
        )
        print(f"Insert response: {response}")

    def get_items(self) -> list:
        item_list = []
        dynamo_response = {'LastEvaluatedKey': False}

        while 'LastEvaluatedKey' in dynamo_response:
            if dynamo_response['LastEvaluatedKey']:
                dynamo_response = self.demo_table.scan(
                    ExclusiveStartKey=dynamo_response['LastEvaluatedKey']
                )
            else:
                dynamo_response = self.demo_table.scan()

            # agregar items
            for i in dynamo_response['Items']:
                item_list.append(i)

        return item_list

    def show_data(self, table):
        for registro in self.get_items():
            # print(registro)
            table.insert("", 0, text=registro["id"], values=(registro["sex"], registro["age"], registro["height"],
                                                             registro["weight"], registro["sight_left"], registro["sight_right"],
                                                             registro["SBP"], registro["DBP"], registro["BLDS"],
                                                             registro["tot_chole"], registro["gamma_GTP"], registro["SMK_stat_type_cd"],
                                                             registro["DRK_YN"]))
