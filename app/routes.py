from app import db
from app.models.places import Places
from flask import request, Blueprint, make_response, jsonify
from werkzeug.datastructures import Authorization
from datetime import datetime
import os
import requests

places_bp = Blueprint("places", __name__, url_prefix="/places")

@places_bp.route("/<place_id>", methods=["GET","PUT", "DELETE"])
def get_single_place(place_id):

    place = Places.query.get(place_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or place == None:
        return jsonify(None), 404
    # This portion is the GET request for only one place
    elif request.method == "GET":
        return {"place": place.to_json()}, 200
    elif request.method == "PUT":
        # This portion is the PUT request for only one place
        request_body = request.get_json()
        place.name = request_body["name"]
        place.lat = request_body["lat"]
        place.lng = request_body["lng"]
        db.session.commit()
        return {"place": place.to_json()}, 200
    elif request.method == "DELETE":
        db.session.delete(place)
        db.session.commit()
        return {
            "details": f"Place {place.place_id} \"{place.name}\" successfully deleted"
            }, 200

@places_bp.route("", methods=["GET"])
def places_index():
    places = Places.query.all()
    places_response = []
    for place in places:
        places_response.append(place.to_json())
    return jsonify(places_response), 200


@places_bp.route("", methods=["POST"])
# Creates new places in the database
def places():
    try:
        request_body = request.get_json()
        new_place = Places(place_id=request_body["place_id"],
                        lat=request_body["lat"],
                        lng=request_body["lng"],
                        name=request_body["name"])
        db.session.add(new_place)
        db.session.commit()

        return {"place": new_place.to_json()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400

# ==================== Tasks ==============================

from app import db
from app.models.tags import Tags
from flask import request, Blueprint, make_response, jsonify


tags_bp = Blueprint("tags", __name__, url_prefix="/tags")

@places_bp.route("/<tag_id>", methods=["GET","PUT", "DELETE"])
def get_single_tag(tag_id):

    tag = Tags.query.get(tag_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or tag == None:
        return jsonify(None), 404
    # This portion is the GET request for only one tag
    elif request.method == "GET":
        return {"tag": tag.to_json()}, 200
    elif request.method == "PUT":
        # This portion is the PUT request for only one tag
        request_body = request.get_json()
        tag.type = request_body["type"]
        db.session.commit()
        return {"tag": tag.to_json()}, 200
    elif request.method == "DELETE":
        db.session.delete(tag)
        db.session.commit()
        return {
            "details": f"Tag {tag.tag_id} \"{tag.type}\" successfully deleted"
            }, 200

@tags_bp.route("", methods=["GET"])
def tags_index():
    tags = Tags.query.all()
    tags_response = []
    for tag in tags:
        tags_response.append(tag.to_json())
    return jsonify(tags_response), 200


@tags_bp.route("", methods=["POST"])
# Creates new tags in the database
def tags():
    try:
        request_body = request.get_json()
        new_tag = Tags(place_id=request_body["tag_id"],
                        lat=request_body["type"])
        db.session.add(new_tag)
        db.session.commit()

        return {"tag": new_tag.to_json()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400


# ================== Itinerary ===========================

from app import db
from app.models.itinerary import Itinerary
from flask import request, Blueprint, make_response, jsonify

itinerary_bp = Blueprint("itinerary", __name__, url_prefix="/itinerary")

@itinerary_bp.route("/<itinerary_id>", methods=["GET","PUT", "DELETE"])
def get_single_itinerary(itinerary_id):

    itinerary = Itinerary.query.get(itinerary_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or itinerary == None:
        return jsonify(None), 404
    # This portion is the GET request for only one itinerary
    elif request.method == "GET":
        return {"itinerary": itinerary.to_json()}, 200
    elif request.method == "PUT":
        # This portion is the PUT request for only one itinerary
        request_body = request.get_json()
        itinerary.itinerary_name = request_body["itinerary_name"]
        itinerary.location = request_body["location"]
        db.session.commit()
        return {"itinerary": itinerary.to_json()}, 200
    elif request.method == "DELETE":
        db.session.delete(itinerary)
        db.session.commit()
        return {
            "details": f"Itinerary {itinerary.itinerary_id} \"{itinerary.itinerary_name}\" successfully deleted"
            }, 200

@places_bp.route("", methods=["GET"])
def places_index():
    itinerary = Itinerary.query.all()
    itinerary_response = []
    for single_itinerary in itinerary:
        itinerary_response.append(single_itinerary.to_json())
    return jsonify(itinerary_response), 200


@itinerary_bp.route("", methods=["POST"])
# Creates new itinerary in the database
def itinerary():
    try:
        request_body = request.get_json()
        new_itinerary = Itinerary(itinerary_id=request_body["itinerary_id"],
                        itinerary_name=request_body["itinerary_name"],
                        lng=request_body["lng"],
                        location=request_body["location"])
        db.session.add(new_itinerary)
        db.session.commit()

        return {"itinerary": new_itinerary.to_json()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400