from random import choice, randint
from datetime import datetime as dt
import sys

# Files
sys.path.append("\DiskoverProject")
from MongoDB.BuildScript.build_db_script import DiskoverDB


def generate(object):
    # For price
    if object.startswith("D") == True:
        price = DiskoverDB.products.find({"_id": object}, {"_id": 0, "price": 1})
        
        return list(price)[0]["price"]

    match object:
        # For order
        case "order":
            db_orders = list(DiskoverDB.sales.find({}, {"_id": 0, "order_id": 1}))
            orders = []
            for order in db_orders:
                orders.append(order["order_id"])

            while True:
                order = f"O{randint(0, 4):03d}"
                if order in orders:
                    pass
                else:
                    return order

        # For product
        case "product":
            db_products = list(DiskoverDB.products.find({}, {"_id": 1}))
            products = []
            for product in db_products:
                products.append(product["_id"])

            return choice(products)
        
        # For quantity
        case "quantity":
            return randint(1, 10)


sale = {
    "order_id": generate("order"),
    "product_id": generate("product"),
    "quantity": generate("quantity")
}

sale["price"] = generate(sale["product_id"])
sale["revenue"] = sale["quantity"] * sale["price"]
sale["date"] = dt.now()


result = DiskoverDB.sales.insert_one(sale)
print(result)







# result = DiskoverDB.products.insert_many(
#     [
#         {
#             "_id": "D001",
#             "name": "Samsung 870 EVO 512GB",
#             "price": 35,
#             "instock": 47
#         },
#         {
#             "_id": "D002",
#             "name": "Western Digital Blue 1TB",
#             "price": 50,
#             "instock": 63
#         }
#     ]
# )
# print(result)