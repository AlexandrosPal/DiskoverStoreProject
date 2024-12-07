import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
env = os.environ.get('env')

from lambda_operations import deploy_lambda, deploy_lambda_layer, update_lambda_layers
from Utils import config
from Utils import copy_file, save_zipfile, delete_files, get_file_in_binary, save_file
from Utils import flow_logger, build_log_message, build_log_error


lambda_arn = config.get('lambda', 'lambda.arn')
lambda_file_name = 'lambda_function.py'
env_file_name = '.env'
env_file_content = f'env={env}'
env_file_directory = f"{str(Path('.').absolute())}/LambdaScript/Deployment"
path_to_lambda_code = f"{str(Path('.').absolute())}/LambdaScript/Deployment"
path_to_lambda_code_with_file = f"{str(Path('.').absolute())}/LambdaScript/Deployment/lambda_function.py"
func_name = config.get('lambda', 'lambda.arn')
zip_name = 'lambda_function.zip'

save_file(env_file_name, env_file_content, env_file_directory)
copy_file('lambda_function', path_to_lambda_code_with_file)
save_zipfile(zip_name=zip_name, file_names=[lambda_file_name, env_file_name], file_dir=path_to_lambda_code)
delete_files([lambda_file_name])

zip_file = get_file_in_binary(zip_name)
deploy_lambda(func_name, zip_file)