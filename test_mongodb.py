import os
from dotenv import load_dotenv
import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
uri = os.getenv('MONGO_DB_URL')
ca = certifi.where()

print(f"Connecting to: {uri.split('@')[-1] if uri else 'None'}")

client = MongoClient(uri, server_api=ServerApi("1"), tlsCAFile=ca)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Connection Failed: {e}")