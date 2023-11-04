#!/usr/bin/env python3
"""
...
"""
import sys
sys.path.extend([".", "../", "../../", "../../../", "../../../../"])

# from models import *
from os import getenv
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from api.v1.endpoints import endpoints


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(endpoints)


if __name__ == "__main__":
    host = getenv("API_HOST", "127.0.0.1")
    port = int(getenv("API_PORT", 5005)
)
    app.run(debug=True, host="0.0.0.0", port=port, threaded=True)
