import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from AWS import send_sns
from Processes import restock_products
from Utils import config

from uuid import uuid4


correlation_id = uuid4()
sns_arn = config.get('sns', 'sns.arn')

try:
    restock_products(correlation_id)
    send_sns(correlation_id, sns_arn, "restock-success")
except Exception as e:
    send_sns(correlation_id, sns_arn, "restock-fail", e)
