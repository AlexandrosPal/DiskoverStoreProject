import json
from pymongo import MongoClient
import boto3

secret_name = "MongoDB_Credentials"

sm = boto3.client('secretsmanager')
response = sm.get_secret_value(SecretId=secret_name)
secret = response['SecretString']
secret = json.loads(secret)

db = MongoClient(secret['CONNECTION_STRING'])

list = db.list_database_names()

def lambda_handler(event, context):

    return 'ok'
