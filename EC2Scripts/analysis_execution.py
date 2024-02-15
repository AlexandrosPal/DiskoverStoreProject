import sys
sys.path.append("/home/ec2-user/DiskoverProject")

from generate_plots import generate_plots
from fill_report import fill_report
from upload_to_s3 import upload_file
from empty_bucket import empty_bucket
from send_sns import send_sns

try:
    generate_plots()
    fileName = fill_report('live')
    empty_bucket('diskoveranalytics.live')
    upload_file(f'/home/ec2-user/DiskoverProject/assets/{fileName}', 'diskoveranalytics.live')

    fileName = fill_report('archive')
    upload_file(f'/home/ec2-user/DiskoverProject/assets/{fileName}', 'diskover-archive')
    send_sns("arn:aws:sns:eu-central-1:419022735529:S3-Input", "analysis-success")

except:
    send_sns("arn:aws:sns:eu-central-1:419022735529:S3-Input", "analysis-fail")
