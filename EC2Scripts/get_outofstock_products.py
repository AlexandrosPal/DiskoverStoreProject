import sys

sys.path.append("/home/ec2-user/DiskoverProject")
from MongoDB.BuildScript.build_db_script import DiskoverDB

def get_outofstock_products():
    products = DiskoverDB.products.find({"instock": 0}, {"_id": 1})

    return products
