import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from AWS import upload_file
from Processes import get_records
from Processes import upload_json
from Utils import config


input_bucket = config.get('buckets', 'bucket.input')

records = get_records()
processed = upload_json(records)
result = upload_file('assets/sales.json', input_bucket)