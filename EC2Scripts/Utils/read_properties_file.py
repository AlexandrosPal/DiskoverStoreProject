import sys
from pathlib import Path
sys.path.append(f"{str(Path('.').absolute())}/EC2Scripts/Properties")

import configparser
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
env = os.environ.get('env')
config = configparser.RawConfigParser()

base_path = f"{str(Path('.').absolute())}/EC2Scripts/Properties"
config.read(f"{base_path}/{env}-config.properties")