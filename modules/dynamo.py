from boto3 import resource
from datetime import datetime


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
        response = self.demo_table.put_item(
            Item={  # elementos de la tabla
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
        )
        print(f"Insert response: {response}")
