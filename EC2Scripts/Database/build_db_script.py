import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from Utils import config, flow_logger, build_log_message

from .sales_coll_validator import sales_validator
from .connection_script import client


# Create new/Connect to a Database
database = config.get('database', 'database.name')
DiskoverDB = client[database]
flow_logger.debug(build_log_message('dev', f"Connected to database: {database}"))


# # Create sales collection
# parameters = {"validator": sales_validator, "capped": True, "size": 20000, "max": 350}
# sales_coll = DiskoverDB.create_collection("sales", **parameters)


# # Create products collection
# products_coll = DiskoverDB.create_collection("products")

# # Create product_details collection
# product_details_coll = DiskoverDB.create_collection("product_details")
