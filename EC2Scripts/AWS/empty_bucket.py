import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import boto3

from Utils import flow_logger, build_log_message, build_log_error


def empty_bucket(correlation_id, bucket_name):
    try:
        s3 = boto3.resource('s3')

        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        flow_logger.info(build_log_message(correlation_id, f"Emptied bucket: {bucket_name}"))
    except Exception as e:
        flow_logger.error(build_log_error(correlation_id, e))