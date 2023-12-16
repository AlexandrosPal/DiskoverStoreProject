import sys
from datetime import datetime as dt
import pymongo
from random import choice, randint
import csv

# Files
sys.path.append("\DiskoverProject")
from MongoDB.BuildScript.build_db_script import DiskoverDB


def fill_products():
    with open("data\disks.csv", "r") as data:
        disks = csv.reader(data)
        next(disks)

        for disk in disks:
            product = {
                "_id": disk[0],
                "name": disk[1],
                "price": disk[2],
                "instock": randint(0,50)
            }
            result = DiskoverDB.products.insert_one(product)
            print(result)


def fill_product_details():
    with open("data\disks.csv", "r") as data:
        disks = csv.reader(data)
        next(disks)

        for disk in disks:
            product = {
                "product_id": disk[0],
                "price_unit": "€",
                "type": disk[3],
                "storage": disk[4],
                "storage_unit": disk[5],
                "manufacturer": disk[6],
                "read_speed": disk[7],
                "read_speed_unit": disk[8],
                "write_speed": disk[9],
                "write_speed_unit": disk[10],
                "size": disk[11],
                "size_unit": disk[12]
            }
            result = DiskoverDB.product_details.insert_one(product)
            print(result)



# fill_products()
fill_product_details()