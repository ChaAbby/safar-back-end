from app import db
from app.models.places import Places
from flask import request, Blueprint, make_response, jsonify
from werkzeug.datastructures import Authorization
from datetime import datetime
import os
import requests
import math

places_bp = Blueprint("places", __name__, url_prefix="/places")

@places_bp.route("/<place_id>", methods=["GET","PUT", "DELETE"])
def get_single_place(place_id):

    place = Places.query.get(place_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or place == None:
        return jsonify(None), 404
    elif request.method == "GET":
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
        new_place = Places(
                        lat=request_body["lat"],
                        lng=request_body["lng"],
                        total=request_body["lat"] + request_body["lng"],
                        name=request_body["name"],
                        google_place_id = request_body["google_place_id"])
        db.session.add(new_place)
        db.session.commit()

        return {"place": new_place.to_json()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400

# ==================== Tags ==============================

from app import db
from app.models.tags import Tags
from flask import request, Blueprint, make_response, jsonify


tags_bp = Blueprint("tags", __name__, url_prefix="/tags")

@tags_bp.route("/<tag_id>", methods=["GET", "DELETE"])
def get_single_tag(tag_id):

    tag = Tags.query.get(tag_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or tag == None:
        return jsonify(None), 404
    # This portion is the GET request for only one tag
    elif request.method == "GET":
        return {"tag": tag.to_json_tags()}, 200
    # elif request.method == "PUT":
    #     # This portion is the PUT request for only one tag
    #     request_body = request.get_json()
    #     tag.type = request_body["type"]
    #     db.session.commit()
        # return {"tag": tag.to_json_tags()}, 200
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
        tags_response.append(tag.to_json_tags())
    return jsonify(tags_response), 200




@tags_bp.route("", methods=["POST"])
# Creates new tags in the database
def tags():
    try:
        request_body = request.get_json()
        string_type = ""
        count = 0
        for type in request_body["type"]:
            count += 1
            if count == 1:
                string_type += f'{type}'
            else:
                string_type += f' {type}'
        new_tag = Tags(
                        type= string_type)
        db.session.add(new_tag)
        db.session.commit()

        return {"tag": new_tag.to_json_tags()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400


# ================== Itinerary ===========================

from app import db
from app.models.itinerary import Itinerary
from flask import request, Blueprint, make_response, jsonify

itinerary_bp = Blueprint("itinerary", __name__, url_prefix="/itinerary")

@itinerary_bp.route("/<itinerary_id>", methods=["GET", "DELETE"])
def get_single_itinerary(itinerary_id):

    itinerary = Itinerary.query.get(itinerary_id)
    # With the GET, POST and DELETE request if there is nothing we output this
    if request == None or itinerary == None:
        return jsonify(None), 404
    # This portion is the GET request for only one itinerary
    elif request.method == "GET":
        return {"itinerary": itinerary.to_json_itin()}, 200
    # elif request.method == "PUT":
    #     # This portion is the PUT request for only one itinerary
    #     request_body = request.get_json()
    #     itinerary.itinerary_name = request_body["itinerary_name"]
    #     db.session.commit()
    # return {"itinerary": itinerary.to_json_itin()}, 200
    elif request.method == "DELETE":
        db.session.delete(itinerary)
        db.session.commit()
        return {
            "details": f"Itinerary {itinerary.itinerary_id} \"{itinerary.itinerary_name}\" successfully deleted"
            }, 200

@itinerary_bp.route("", methods=["GET"])
def itinerary_index():
    itinerary = Itinerary.query.all()
    itinerary_response = []
    for single_itinerary in itinerary:
        itinerary_response.append(single_itinerary.to_json_itin())
    return jsonify(itinerary_response), 200


@itinerary_bp.route("", methods=["POST"])
# Creates new itinerary in the database
def itinerary():
    try:
        request_body = request.get_json()
        new_itinerary = Itinerary(
                        itinerary_name=request_body["itinerary_name"])
        db.session.add(new_itinerary)
        db.session.commit()

        return {"itinerary": new_itinerary.to_json_itin()}, 201
    except KeyError:
        return {
            "details": "Invalid data"}, 400

# ====
@itinerary_bp.route("<itinerary_id>/places", methods=["POST"])
def post_places_ids_to_itineary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    request_body = request.get_json()

    # origin_total = -74.68747

    # places_list = []
    # for place_id in request_body["place_ids"]:
    #     place = Places.query.get(place_id)
    #     places_list.append(place.total)
    
    # places_list.sort(key=lambda x: abs(origin_total-x))

    # final_ds = []
    # for total in places_list:
    #     for place_id in request_body["place_ids"]:
    #         place = Places.query.get(place_id)
    #         if total == place.total:
    #             final_ds.append(place)

    # for location in final_ds:
    #     place = Places.query.get(location["place_id"])
    #     itinerary.places.append(place)
    #     place.itinerary_id = itinerary_id
    # db.session.commit()



    
    for place_id in request_body["place_ids"]:
        place = Places.query.get(place_id)
        itinerary.places.append(place)
        place.itinerary_id = itinerary_id
    db.session.commit()
    return make_response({"id": itinerary.itinerary_id, "place_ids": request_body["place_ids"]}, 200)

@itinerary_bp.route("<itinerary_id>/places", methods=["GET"])
def getting_places_of_one_itinerary(itinerary_id):
    itinerary = Itinerary.query.get(itinerary_id)
    if itinerary == None:
        return jsonify(None), 404
    else:
        places_from_itinerary = itinerary.places

        places_response = []
        for place in places_from_itinerary:
            places_response.append(place.to_json())
            # def distance(place):
            #     return math.sqrt((place.lat-origin.lat)**2+(place.lon-origin.lon)**2 )
            # sorted_places = sort(itinerary.places, key=lambda distance() )

        return {"itinerary_id":itinerary.itinerary_id,"itinerary_name": itinerary.itinerary_name, "places": places_response}, 200

        # 2 route
            # attach itin id - save places array
            # Sort places array by distance function
        # math.sqrt((place.lat-origin.lat)**2+(place.lon-origin.lon)**2 )
            # for place in places:
                # if place.origin == True:
@itinerary_bp.route("itinerary_with_places", methods=["POST"])
def itinerary_with_places():
    try:
        request_body = request.get_json()
        print("****************", request_body)
        new_itinerary = Itinerary(
                        itinerary_name=request_body["itinerary_name"])
        for place_id in request_body["place_ids"]:
            place = Places.query.get(place_id)
            new_itinerary.places.append(place)
            place.itinerary_id = new_itinerary.itinerary_id
        db.session.add(new_itinerary)
        db.session.commit()
        return {"itinerary": new_itinerary.to_json_itin()}, 201
    except KeyError as error:
        return {
            "details":f"Invalid data. Missing key {error}"}, 400

