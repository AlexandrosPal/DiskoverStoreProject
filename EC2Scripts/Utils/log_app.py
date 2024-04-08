import sys
from pathlib import Path
sys.path.append(f'{str(Path('.').absolute())}')

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
env = os.environ.get('env')

import logging
from functools import reduce

from .read_properties_file import config

def build_logger(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(f"logs/{env}-{name}.log")

    formatter = logging.Formatter('%(levelname)s %(filename)s %(name)s@%(asctime)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level=config.get('logging', 'log.level'))

    return logger

def build_log_message(message):
    return {'env': env, 'message': message}

def build_log_error(error):
    return {'env': env, 'error': error}


flow_logger = build_logger('flow')