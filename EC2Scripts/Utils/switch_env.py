from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
os.environ['env'] = 'prod'