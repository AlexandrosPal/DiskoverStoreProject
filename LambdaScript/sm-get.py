import json
import boto3

secret_name = "MongoDB_Credentials"

sm = boto3.client('secretsmanager')
response = sm.get_secret_value(SecretId=secret_name)
secret = response['SecretString']

secret = json.loads(secret)
