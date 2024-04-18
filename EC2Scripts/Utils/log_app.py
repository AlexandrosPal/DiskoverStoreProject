import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}")

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
env = os.environ.get('env')

import logging

from .read_properties_file import config

def build_logger(name):
    logger = logging.getLogger(name)
    handler = logging.FileHandler(f"logs/{env}-{name}.log")

    formatter = logging.Formatter('{levelname:^6s} {filename} {name}@{asctime}: {message}', style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level=config.get('logging', 'log.level'))

    return logger

def build_log_message(correlation_id, message):
    return {'correlation_id': str(correlation_id), 'env': env, 'message': message}

def build_log_error(correlation_id, error):
    return {'correlation_id': str(correlation_id), 'env': env, 'error': error}


flow_logger = build_logger('flow')