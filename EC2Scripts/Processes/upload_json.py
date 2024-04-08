import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import json

from Utils import config
from Utils import flow_logger, build_log_message, build_log_error


def upload_json(file):
    try:
        file = json.dumps(file, indent=3, default=str)
        file_path = "assets/sales.json"

        with open(file_path, 'w') as sales:
            sales.write(str(file))

        flow_logger.info(build_log_message('Uploaded json successfully'))
        return True
    
    except Exception as e:
        flow_logger.error(build_log_error(e))