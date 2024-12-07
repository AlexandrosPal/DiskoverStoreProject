import boto3
from botocore.exceptions import ClientError
from datetime import date

from Utils import get_file_in_binary

def deploy_lambda(func_name, zip_file):
    lambda_client = boto3.client('lambda')
    response = lambda_client.update_function_code(
        FunctionName=func_name,
        ZipFile=zip_file
    )

def deploy_lambda_layer():
    lambda_client = boto3.client('lambda')

    layer_name = 'python'
    description = f'Latest Lambda layer from {date.today()}'
    zip_file_content = get_file_in_binary('python.zip')

    response = lambda_client.publish_layer_version(
        LayerName=layer_name,
        Description=description,
        Content={
            'ZipFile': zip_file_content
        },
        CompatibleRuntimes=[
            'python3.9',
        ]
    )
    return f'{response['LayerVersionArn']}'

def update_lambda_layers(lambda_arn, layer_arn):
    lambda_client = boto3.client('lambda')

    response = lambda_client.update_function_configuration(
        FunctionName=lambda_arn,
        Layers=[layer_arn]
    )