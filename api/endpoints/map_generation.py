import os
from py_map_generation import GenerateMap
from flask import Blueprint, request, send_file
from api.config import MAP_SAVE_PATH, MAP_NAME, MAP_SIZE, MAP_MAX_SIZE


blueprint = Blueprint("map-generation", __name__)


@blueprint.route("/")
def generate_map():
    seed = request.args.get("seed", 69, type=int)
    size = min(request.args.get("size", MAP_SIZE, type=int), MAP_MAX_SIZE)
    map_name = MAP_NAME % (seed, size)

    if not os.path.exists(os.path.join(MAP_SAVE_PATH, map_name)):
        map_generation = GenerateMap((size, size), seed)
        map_generation.generate_map()
        map_generation.make_map(map_name, MAP_SAVE_PATH)

    return send_file(os.path.join(MAP_SAVE_PATH, map_name), mimetype="image/png")
