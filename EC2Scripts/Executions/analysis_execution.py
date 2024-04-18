import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from AWS import upload_file
from AWS import empty_bucket
from AWS import send_sns
from Processes import generate_plots
from Processes import fill_report
from Utils import config
from Utils import flow_logger

from uuid import uuid4


env = os.environ.get('env')
correlation_id = uuid4()
main_bucket = config.get('buckets', 'bucket.main')
archive_bucket = config.get('buckets', 'bucket.archive')
sns_arn = config.get('sns', 'sns.arn')
success_message = config.get('sns', 'sns.analysis.message.success')
fail_message = config.get('sns', 'sns.analysis.message.fail')

log_message = {
    'correlation_id': str(correlation_id),
    'env': env, 
    'variables': {
        'main_bucket': main_bucket, 
        'archive_bucket': archive_bucket, 
        'sns_arn': sns_arn
        }
    }
flow_logger.debug(log_message)

try:
    generate_plots(correlation_id)
    fileName = fill_report(correlation_id, main_bucket)
    empty_bucket(correlation_id, main_bucket)
    upload_file(correlation_id, f"assets/{fileName}", main_bucket)

    fileName = fill_report(correlation_id, archive_bucket)
    upload_file(correlation_id, f"assets/{fileName}", archive_bucket)
    send_sns(correlation_id, sns_arn, success_message)

except Exception as e:
    send_sns(sns_arn, fail_message, e)
