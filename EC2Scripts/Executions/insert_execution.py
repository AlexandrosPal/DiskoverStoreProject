import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from AWS import upload_file
from Processes import get_records
from Processes import upload_json
from Utils import config

from uuid import uuid4


correlation_id = uuid4()
input_bucket = config.get('buckets', 'bucket.input')

records = get_records(correlation_id)
processed = upload_json(correlation_id, records)
result = upload_file(correlation_id, 'assets/sales.json', input_bucket)