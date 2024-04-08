import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from Processes import generate_plots
from Processes import fill_report
from AWS import upload_file
from AWS import empty_bucket
from AWS import send_sns
from Utils import config
from Utils import flow_logger


env = os.environ.get('env')
main_bucket = config.get('buckets', 'bucket.main')
archive_bucket = config.get('buckets', 'bucket.archive')
sns_arn = config.get('sns', 'sns.arn')
success_message = config.get('sns', 'sns.analysis.message.success')
fail_message = config.get('sns', 'sns.analysis.message.fail')

log_message = {
    'env': env, 
    'variables': {
        'main_bucket': main_bucket, 
        'archive_bucket': archive_bucket, 
        'sns_arn': sns_arn
        }
    }
flow_logger.debug(log_message)

try:
    generate_plots()
    fileName = fill_report(main_bucket)
    empty_bucket(main_bucket)
    upload_file(f"assets/{fileName}", main_bucket)

    fileName = fill_report(archive_bucket)
    upload_file(f"assets/{fileName}", archive_bucket)
    send_sns(sns_arn, success_message)

except Exception as e:
    send_sns(sns_arn, fail_message, e)
