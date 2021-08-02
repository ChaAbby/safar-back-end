# from flask import Blueprint
# from flask import request

# hello_world_bp = Blueprint("hello_world", __name__)

# @blueprint_name.route("/endpoint/path/here", methods=["GET"])
# def endpoint_name():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body

# # from flask import Blueprint

# # hello_world_bp = Blueprint("hello_world", __name__)


# # @hello_world_bp.route("/hello-world", methods=["GET"])
# # def say_hello_world():
# #     my_beautiful_response_body = "Hello, World!"
# #     return my_beautiful_response_body


from app import db
from app.models.locations import Locations
from flask import request, Blueprint, make_response

locations_bp = Blueprint("locations", __name__, url_prefix="/locations")


@locations_bp.route("", methods=["POST"])
def handle_locations():
    request_body = request.get_json()
    new_location = Locations(title=request_body["Lat"],
                    description=request_body["Lon"])

    db.session.add(new_location)
    db.session.commit()

    return make_response(f"Location {new_location} successfully created", 201)

