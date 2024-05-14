import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
import boto3
from botocore.exceptions import ClientError

from Utils import flow_logger, build_log_message, build_log_error


def upload_file(correlation_id: str, file_name: str, bucket: str, object_name=None) -> str:

    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ContentType': 'application/pdf'})
        flow_logger.info(build_log_message(correlation_id, f"Uploaded file: {file_name}, to bucket: {bucket}"))
    except ClientError as e:
        flow_logger.error(build_log_error(correlation_id, e))
        return False
    return True