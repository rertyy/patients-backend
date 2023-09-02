from flask import jsonify, json, request

from flask import Blueprint, make_response
from .db import collection
from flask_cors import cross_origin
from .util import parse_json, string_to_json
from .data import patients_data

router_bp = Blueprint("router_bp", __name__)

db = collection()
# reset_data()


@router_bp.route("/", methods=["GET"])
@cross_origin()
def hello_world():  # put application's code here
    json_msg = {"Message": "Hello World"}
    response = make_response(jsonify(json_msg), 200)
    # return "Hello World"
    return response


@router_bp.route("/health", methods=["GET"])
@cross_origin()
def healthcheck():  # put application's code here
    json_msg = {"Message": "200 OK"}
    response = make_response(json_msg, 200)
    return response


@router_bp.route("/patients", methods=["GET"])
@cross_origin()
def get_patients():
    # return jsonify(patients_data)
    cursor = db.find()
    result = list(cursor)
    return parse_json(result)


@router_bp.route("/patients/<int:patient_id>", methods=["GET"])
@cross_origin()
def get_patients_by_id(patient_id: int):
    document = db.find_one({"id": patient_id})
    if document:
        result = parse_json(document)
        return make_response(result, 200)
    return make_response(string_to_json("Patient not found"), 404)


@router_bp.route("/patients/<int:patient_id>/notes", methods=["POST"])
@cross_origin()
def update_patient_notes(patient_id: int):
    text = request.json.get("patientNotes")
    # print("id:", patient_id, "text", text)
    result = db.update_one({"id": patient_id}, {"$set": {"notes": text}})
    print("ack:", result.acknowledged)
    print("match:", result.matched_count)
    print("modify", result.modified_count)

    if result.acknowledged != 1:
        return make_response(string_to_json("Error: DB query error"), 500)
    elif result.matched_count != 1:
        return make_response(string_to_json("Error: patient ID not found"), 404)
    elif result.modified_count != 1:
        return make_response(string_to_json("Error: Document not updated"), 404)
    elif result.modified_count == 1:
        return make_response(string_to_json("Update successful"), 201)


@router_bp.route("/patients/<int:patient_id>/records", methods=["GET"])
@cross_origin()
def get_patients_record_by_id(patient_id: int):
    document = db.find_one({"id": patient_id})
    result = document.get("records")
    if not result:
        return make_response(string_to_json("Patient or records not found"), 404)
    result_json = parse_json(result)
    return make_response(result_json, 200)
