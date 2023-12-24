import json
import boto3
from pymongo import MongoClient
from botocore.exceptions import ClientError

sm = boto3.client('secretsmanager')
s3 = boto3.client('s3')
sns = boto3.client('sns')

secret_name = "MongoDB_Credentials"
response = sm.get_secret_value(SecretId=secret_name)
secret = response['SecretString']
secret = json.loads(secret)

client = MongoClient(secret['CONNECTION_STRING'])
DiskoverDB = client.DiskoverDB


def lambda_handler(event, context):
    try:
        object = s3.get_object(Bucket='diskover-input', Key='sales.json')
        sales = json.loads(object['Body'].read().decode('utf-8'))
        response = DiskoverDB.sales.insert_many(sales)

        s3.put_object(Bucket='diskover-output', Key='sales.json', Body=str(sales))
        
        s3.delete_object(Key='sales.json', Bucket='diskover-input')
        
        send_success_sns = sns.publish(
            TopicArn="arn:aws:sns:eu-central-1:419022735529:S3-Input", 
            Message= 'Lambda function succeded'
        )
        
    except Exception as e:
        send_failed_sns = sns.publish(
            TopicArn="arn:aws:sns:eu-central-1:419022735529:S3-Input", 
            Message='Lambda function failed'
        )
        print(e)
    
    return event