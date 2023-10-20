# This lambda function is triggered by the /get-all-users endpoint, which returns all the items in the table
import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("jitto-dynamodb")
    data_raw = table.scan()['Items']
    return {
        'statusCode': 200,
        'body': json.dumps(data_raw)
    }
