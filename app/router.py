from flask import jsonify, json

from flask import Blueprint, make_response
from .db import collection
from flask_cors import cross_origin
from .util import parse_json
from .data import patients_data

router_bp = Blueprint("router_bp", __name__)

db = collection()


@router_bp.route("/")
@cross_origin()
def hello_world():  # put application's code here
    response = make_response("Hello World", 200)
    return response


@router_bp.route("/health")
@cross_origin()
def healthcheck():  # put application's code here
    response = make_response("200 OK", 200)
    return response


@router_bp.route("/patients")
@cross_origin()
def get_patients():
    return jsonify(patients_data)
    # cursor = db.find()
    # result = list(cursor)
    # return parse_json(result)


@router_bp.route("/patients/<int:patient_id>")
@cross_origin()
def get_patients_by_id(patient_id: int):
    document = db.find_one({"id": patient_id})
    if document:
        result = parse_json(document)
        return make_response(result, 200)
    return make_response("Patient not found", 404)


@router_bp.route("/patients/<int:patient_id>/records")
@cross_origin()
def get_patients_record_by_id(patient_id: int):
    document = db.find_one({"id": patient_id})
    result = document.get("records")
    if not result:
        return make_response("Patient or records not found", 404)
    result_json = parse_json(result)
    return make_response(result_json, 200)
