from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MONGOdb")
mongo_client = MongoClient(api_key)
db = mongo_client['Portfolio']
projects = db['Projects']
Contact = db['Contact']
