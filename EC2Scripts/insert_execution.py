import sys
sys.path.append("/home/ec2-user/DiskoverProject")

from generate_records import get_records
from upload_to_s3 import upload_file
from upload_json import upload_json


records = get_records()
processed = upload_json(records)
result = upload_file('assets/sales.json', 'diskover-input')