import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_filename = event['Records'][0]['s3']['object']['key']

    json_object = s3_client.get_object(Bucket=bucket,Key=json_filename)
    jsonFileReader = json_object['Body'].read()                         #Read the response from the Body
    jsonDict = json.loads(jsonFileReader)                               #Convert the response into a dictionary
    
    table = dynamodb.Table('ProductsAndQuantities')
    table.put_item(Item=jsonDict)

    print(bucket)
    print(json_filename)
    print(str(event))
    return 'Execution Success'