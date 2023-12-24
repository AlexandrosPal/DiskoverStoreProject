import json
import sys
sys.path.append("/home/ec2-user/DiskoverProject")

def upload_json(file):
    file = json.dumps(file, indent=3, default=str)

    with open('assets/sales.json', 'w') as sales:
        sales.write(str(file))

    return True