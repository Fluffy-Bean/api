import requests
from flask import Blueprint, jsonify, request
from api.env import HASS_TOKEN, HASS_URL
from api.config import HASS_ALLOWED_DEVICES


blueprint = Blueprint("homeassistant", __name__)


@blueprint.route("/")
def status():
    device = request.args.get("device", "light.light")

    if device not in HASS_ALLOWED_DEVICES:
        response = {
            "status": 1,
            "data": {
                "message": "Device not found or is not allowed!",
            },
        }
        return jsonify(response), 404

    hass_data = requests.get(
        HASS_URL + "/api/states/" + device,
        headers={
            "Authorization": "Bearer " + HASS_TOKEN,
            "content-type": "application/json",
        },
    )

    if (
        hass_data.status_code == 200 or hass_data.status_code == 201
    ) and hass_data.json()["state"] is not None:
        response = {
            "status": 0,
            "data": {
                "state": hass_data.json()["state"],
                "attributes": hass_data.json()["attributes"],
            },
        }
        return jsonify(response)
    else:
        response = {
            "status": 1,
            "data": {
                "message": "Homeassistant returned a non-200 status code.",
                "error_code": hass_data.status_code,
            },
        }
        return jsonify(response), 500
