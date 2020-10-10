1. Create a IAM role for accessing S3, DynamoDB and CloudWatch Logs 

1. Create a DynamoDB Table with a primary key.

2. Create a S3 bucket for processing the Json files.

4. Create a lambda function with this code.

5. Create a trigger S3 bucket with EVENT_TYPE = Object Create and suffix .json[so when ever a json file will be uploaded to this bucket trigger will be executed].

Execution -
Uplaod the products.json file to s3 bucket, check for the cloudWatch logs and verify if the data was inserted to DynamoDB table.






