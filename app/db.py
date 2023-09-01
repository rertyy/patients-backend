from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


def connect():
    uri = os.environ['DBCONN']

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        print("Attempting to ping")
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Unable to connect to MongoDB: {e}")
    return client['patientDB']

def collection():
    db = connect()
    return db["patientCollection"]
