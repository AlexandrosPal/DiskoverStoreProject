import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from Utils import flow_logger, build_log_message, build_log_error

import boto3


env = os.environ.get('env')

def send_sns(correlation_id: str, topic: str, message: str, e=None):

    try:
        sns = boto3.client('sns')
        if message == "analysis-success":
            send_success_sns = sns.publish(
                TopicArn = topic,
                Message = f'{str(env).upper()}: Analysis ran successfully'
            )
            flow_logger.info(build_log_message(correlation_id, f"Sent sns to topic: {topic}, and message: {message}"))

        elif message == "analysis-fail":
            send_fail_sns = sns.publish(
                TopicArn = topic, 
                Message= f"{str(env).upper()}: Analysis failed: {e}"
            )
            flow_logger.info(build_log_message(correlation_id, f"Sent sns to topic: {topic}, and message: {message}"))

        elif message == "restock-success":
            send_success_sns = sns.publish(
                TopicArn = topic,
                Message = f"{str(env).upper()}: Restock proccess ran successfully"
            )
            flow_logger.info(build_log_message(correlation_id, f"Sent sns to topic: {topic}, and message: {message}"))

        elif message == "restock-fail":
            send_fail_sns = sns.publish(
                TopicArn = topic,
                Message = f"{str(env).upper()}: Restock proccess failed: {e}"
            )
            flow_logger.info(build_log_message(correlation_id, f"Sent sns to topic: {topic}, and message: {message}"))
        
    except Exception as e:
        flow_logger.error(build_log_error(correlation_id, e))
