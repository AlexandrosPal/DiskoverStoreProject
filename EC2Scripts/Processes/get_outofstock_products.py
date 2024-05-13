import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from Utils import config
from Database import DiskoverDB

def get_outofstock_products() -> list[dict]:
    products = DiskoverDB.products.find({"instock": 0}, {"_id": 1})

    return products