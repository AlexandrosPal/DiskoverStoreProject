# Standard Libraries
import sys

# Files
sys.path.append("/home/ec2-user/DiskoverProject/MongoDB")
from Schema.sales_coll_validator import sales_validator
from connection_script import client


# Create new Database
DiskoverDB = client.DiskoverDB


# # Create sales collection
# parameters = {"validator": sales_validator, "capped": True, "size": 20000, "max": 350}
# sales_coll = DiskoverDB.create_collection("sales", **parameters)


# # Create products collection
# products_coll = DiskoverDB.create_collection("products")

# # Create product_details collection
# product_details_coll = DiskoverDB.create_collection("product_details")
