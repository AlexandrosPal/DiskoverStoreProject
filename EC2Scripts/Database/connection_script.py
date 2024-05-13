from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os

# Get password from enviroment
load_dotenv(find_dotenv())
db_password = os.environ.get("MONGODB_PWD")


# Connect to the MongoDB instance
connection_string = f"mongodb+srv://admin:{db_password}@main.oukdars.mongodb.net/?retryWrites=true&w=majority"
client: MongoClient = MongoClient(connection_string)