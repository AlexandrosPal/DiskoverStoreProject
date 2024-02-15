import json
import sys
# sys.path.append("/home/ec2-user/DiskoverProject/assets")

def upload_json(file):
    file = json.dumps(file, indent=3, default=str)
    file_path = '/home/ec2-user/DiskoverProject/assets/sales.json'

    with open(file_path, 'w') as sales:
        sales.write(str(file))

    return True
