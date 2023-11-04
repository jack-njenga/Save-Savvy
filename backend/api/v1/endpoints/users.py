#!/usr/bin/env python3
"""user endpoint"""

from models.user import User
from api.v1.endpoints import endpoints
from flask import abort, jsonify, make_response, request

@endpoints.route("/users", methods=["POST"], strict_slashes=False)
def post_user():
    """
    Posts a new user(creation of a new user)
    """
    data = request.get_json()

    if data:
        if isinstance(data, dict):
            # check the data requirements
            new_user = User(**data)
            new_user.save()
            return make_response(jsonify({"status-save": "SUCCESS"}), 201)
        else:
            abort(400, "Not a JSON")
    else:
        abort(400, "Not or No JSON at all")

@endpoints.route("/user", methods=["PUT"], strict_slashes=False)
def get_user():
    """
    Gets a user data
    """
    data = request.get_json()
    user = {}

    if data:
        if isinstance(data, dict):
            for key, val in data.items():
                if key in ["email", "password"]:
                    user[key] = val
        if len(list(user.keys())) == 2:
            userData = User.get(user["email"], user["password"])
            return make_response(jsonify(userData))
        else:
            abort(400, "No email | No password")
    else:
        abort(400, "Not a JSON")