import dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from app.data import patients_data


def reset_data():
    uri = dotenv.get_key(".env", "DBCONN")
    client = MongoClient(uri, server_api=ServerApi("1"))
    coll = client["patientDB"]["patientCollection"]
    coll.delete_many({})
    coll.insert_many(patients_data)
    print("reset data success")


if __name__ == "__main__":
    reset_data()
