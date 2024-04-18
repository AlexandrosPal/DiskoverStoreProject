import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from random import randint

from Database import DiskoverDB
from Utils import flow_logger, build_log_message, build_log_error


def restock_products(correlation_id):
    try:
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

            restock_amount = randint(min, max)
            flow_logger.info(build_log_message(correlation_id, f"Product with id: {product['_id']} restocked {restock_amount} items to {product['instock'] + restock_amount}"))
            result = DiskoverDB.products.update_one({"_id": product['_id']}, {"$inc": {"instock": restock_amount}})

        return result
    
    except Exception as e:
        flow_logger.error(build_log_error(correlation_id, e))

# restock_products()
