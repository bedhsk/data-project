from boto3 import resource
from datetime import datetime

# Insertar datos en DynamoDb
class Dynamo:
    def __init__(self) -> None:
        self.demo_table = resource('dynamodb').Table('demo-dynamo-python') # acceso a la tabla

    def insert(self, customer_id: str, order_id: str, status_name: str):
        print(f'demo_insert')
        response = self.demo_table.put_item(
            Item={ # elementos de la tabla
                'customer_id': customer_id,  # partition key
                'order_id': order_id,  # sort key
                'status': status_name,
                'created_date': datetime.now().isoformat()
            }
        )
        print(f'Insert response: {response}')