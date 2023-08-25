import datetime
from flask import Blueprint, jsonify


blueprint = Blueprint("uptime", __name__)
time_started = datetime.datetime.now()


@blueprint.route("/")
def uptime():
    time_now = datetime.datetime.now()
    response = {"status": 0, "data": {"message": str(time_now - time_started)}}

    return jsonify(response)
