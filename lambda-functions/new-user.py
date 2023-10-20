# this lambda function creates a new is triggered by the /new-user endpoint, and creates an entry in the table with the name and description params
# the function generates a UUID for the entry, which is used as the dynamoDB's partition key, and makes up the body of the API endpoint's return message
import json
import boto3
import uuid

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("jitto-dynamodb")
    
    name = str(event['name'])
    description = str(event['description'])
    id = str(uuid.uuid4())
    
    table.put_item(Item={'id':id, 'name': name, 'description': description})
    return {
        'statusCode': 200,
        'body': json.dumps(id)
    }
