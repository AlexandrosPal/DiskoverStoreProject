import boto3
import json

lamb = boto3.client('lambda')
payload = json.dumps({"body": "data"})

response = lamb.invoke(
    FunctionName='demo-layer',
    Payload=payload
)
