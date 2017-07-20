import json

from flask import Blueprint


# create the blueprint
bp = Blueprint("shippable", __name__)

@bp.route("/", methods=["GET"])
def index():
    return json.dumps(dict(response="hello world!"))

@bp.route("/ping", methods=["GET"])
def ping():
    return json.dumps(dict(ping="pong!"))