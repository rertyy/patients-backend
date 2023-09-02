from bson import json_util
from flask import json, jsonify


def parse_json(data):
    return json.loads(json_util.dumps(data))


def string_to_json(msg: str):
    return jsonify({"Message": msg})
