import sys
from pathlib import Path
sys.path.append(f'{str(Path('.').absolute())}/EC2Scripts')

from Utils import flow_logger, build_log_message, build_log_error

import boto3


def send_sns(topic, message, e=None):

    try:
        sns = boto3.client('sns')
        if message == "analysis-success":
            send_success_sns = sns.publish(
                TopicArn = topic,
                Message = 'Analysis ran successfully'
            )
            flow_logger.info(build_log_message(f'Sent sns to topic: {topic}, and message: {message}'))

        elif message == "analysis-fail":
            send_fail_sns = sns.publish(
                TopicArn = topic, 
                Message= f'Analysis failed: {e}'
            )
            flow_logger.info(build_log_message(f'Sent sns to topic: {topic}, and message: {message}'))

        elif message == "restock-success":
            send_success_sns = sns.publish(
                TopicArn = topic,
                Message = "Restock proccess ran successfully"
            )
            flow_logger.info(build_log_message(f'Sent sns to topic: {topic}, and message: {message}'))

        elif message == "restock-fail":
            send_fail_sns = sns.publish(
                TopicArn = topic,
                Message = f"Restock proccess failed: {e}"
            )
            flow_logger.info(build_log_message(f'Sent sns to topic: {topic}, and message: {message}'))
        
    except Exception as e:
        flow_logger.error(build_log_error(e))
