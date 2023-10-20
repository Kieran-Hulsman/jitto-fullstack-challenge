# This lambda function is triggered by the /get-user endpoint, which returns the name and description associated with the id param
import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("jitto-dynamodb")
    
    id = event['id']
    
    response = table.query(
        KeyConditionExpression = boto3.dynamodb.conditions.Key('id').eq(id)
    )
    user = response['Items'][0]
    name = user['name']
    description = user['description']
    
    data = {
        "name": name,
        "description": description
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
    