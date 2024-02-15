import boto3
import sys
import os


def send_sns(topic, message):

    sns = boto3.client('sns')
    if message == "analysis-success":
        send_success_sns = sns.publish(
            TopicArn = topic,
            Message = 'Analysis ran successfully'
        )

    elif message == "analysis-fail":
        send_fail_sns = sns.publish(
            TopicArn = topic, 
            Message= 'Analysis failed'
        )
    elif message == "restock-success":
        send_success_sns = sns.publish(
            TopicArn = topic,
            Message = "Restock proccess ran successfully"
        )
    elif message == "restock-fail":
        send_fail_sns = sns.publish(
            TopicArn = topic,
            Message = "Restock proccess failed"
        )
