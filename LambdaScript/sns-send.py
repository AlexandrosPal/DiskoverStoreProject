import boto3

sns_client = boto3.client('sns')
res = sns_client.publish(
    TopicArn="arn:aws:sns:eu-central-1:419022735529:S3-Input", 
    Message="success"
)
