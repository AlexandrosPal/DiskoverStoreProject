import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

from typing import Any, Dict, List

from Database import DiskoverDB

def get_outofstock_products() -> List[Dict[str, Any]]:
    products: list = DiskoverDB.products.find({"instock": 0}, {"_id": 1})

    return products