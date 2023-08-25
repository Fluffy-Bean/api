import subprocess
from flask import Blueprint, jsonify


blueprint = Blueprint("fortune", __name__)


@blueprint.route("/")
def fortune():
    try:
        response = {
            "status": 0,
            "data": {
                "message": (
                    subprocess.run(["fortune"], stdout=subprocess.PIPE)
                    .stdout.decode("utf-8")
                    .strip()
                )
            },
        }
        return jsonify(response)
    except FileNotFoundError:
        response = {
            "status": 1,
            "data": {
                "message": "fortune command not found. Please bother Fluffy to install it."
            },
        }
        return jsonify(response), 500
