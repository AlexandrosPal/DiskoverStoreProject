import sys
sys.path.append("/home/ec2-user/DiskoverProject")

from generate_plots import generate_plots
from fill_report import fill_report
from upload_to_s3 import upload_file
from empty_bucket import empty_bucket


generate_plots()
fileName = fill_report()
empty_bucket('diskoveranalytics.live')
upload_file(f'assets/{fileName}', 'diskoveranalytics.live')
upload_file(f'assets/{fileName}', 'diskover-archive')