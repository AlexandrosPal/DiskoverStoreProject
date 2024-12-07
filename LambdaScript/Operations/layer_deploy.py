import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")


from lambda_operations import deploy_lambda_layer, update_lambda_layers
from Utils import config
from Utils import flow_logger, build_log_message, build_log_error


lambda_arn = config.get('lambda', 'lambda.arn')

layer_arn = deploy_lambda_layer()
update_lambda_layers(lambda_arn, layer_arn)