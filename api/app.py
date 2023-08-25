from flask import Flask, jsonify
from api.endpoints import fortune, homeassistant, uptime, map_generation

try:
    from api import env
except ImportError:
    print("No env.py found!")
    exit(1)

app = Flask(__name__)


@app.route("/")
def hello_world():
    response = {
        "status": 0,
        "data": {
            "message": "Hello World! This is a simple API built with Flask by Fluffy. "
            "To check out more about how to use it, check the documentation at gay.leggy.dev/api. "
            "Code is open source and available at github.com/Fluffy-Bean/api."
        },
    }
    return jsonify(response)


app.register_blueprint(fortune.blueprint, url_prefix="/fortune")
app.register_blueprint(homeassistant.blueprint, url_prefix="/homeassistant")
app.register_blueprint(uptime.blueprint, url_prefix="/uptime")
app.register_blueprint(map_generation.blueprint, url_prefix="/map-generation")


if __name__ == "__main__":
    app.run()
