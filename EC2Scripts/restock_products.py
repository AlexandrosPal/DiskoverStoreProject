from random import randint
import sys

sys.path.append("/home/ec2-user/DiskoverProject")
from MongoDB.BuildScript.build_db_script import DiskoverDB

def restock_products():
    products = DiskoverDB.products.find()
    for product in products:
        if product["instock"] < 0:
            min, max = 80, 85
        elif product["instock"] < 10:
            min, max = 60, 75
        elif product["instock"] < 20:
            min, max = 50, 60
        elif product["instock"] < 30:
            min, max = 50, 55
        elif product["instock"] > 60:
            min, max = 15, 20
        elif product["instock"] > 70:
            min, max = 5, 10
        elif product["instock"] > 80:
            min, max = 1, 7
        elif product["instock"] > 90:
            min, max = 1, 5
        else:
            min, max = 45, 50 
        result = DiskoverDB.products.update_one({"_id": product['_id']}, {"$inc": {"instock": randint(min, max)}})

    return result

# restock_products()
