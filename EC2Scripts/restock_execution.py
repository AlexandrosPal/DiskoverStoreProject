import sys
sys.path.append("/home/ec2-user/DiskoverProject")

from send_sns import send_sns
from restock_products import restock_products

try:
    restock_products()
    send_sns("arn:aws:sns:eu-central-1:419022735529:S3-Input", "restock-success")
except:
    send_sns("arn:aws:sns:eu-central-1:419022735529:S3-Input", "restock-fail")
