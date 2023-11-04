#!/usr/bin/env python3
"""
Default status
"""
from api.v1.endpoints import endpoints
from flask import jsonify

@endpoints.route("/", strict_slashes=False, methods=["GET"])
@endpoints.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """
    Returns the status
    """
    status = {"status": "SUCCESS"}

    return jsonify(status)
