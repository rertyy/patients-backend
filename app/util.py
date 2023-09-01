from bson import json_util
from flask import json

def parse_json(data):
    return json.loads(json_util.dumps(data))


