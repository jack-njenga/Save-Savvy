#!/usr/bin/env python3
"""
THis is the items endpoint
"""
import json
from models.user import User
from models.item import Item
from models.uitem import UItem
from models.tools.create import Create_Item
from api.v1.endpoints import endpoints
from flask import abort, jsonify, make_response, request


@endpoints.route("/item", methods=["POST", "GET"], strict_slashes=False)
def new_item():
    """
    creates a new item
    """
    if request.method == "GET":
        return jsonify({"status": "GETTING"})
    data = request.get_json()
    print(data)
    if data:
        print(data)
        if isinstance(data, dict):
            keys = list(data.keys())
            item = str(data[keys[0]])

            url = f"https://www.jumia.co.ke/catalog/?q={item}"
            create = Create_Item(url)
            create.new()
            print("done")

            return make_response(jsonify({"status-save": "SUCCESS"}), 201)
        else:
            abort(400, "Not a JSON")
    else:
        abort(400, "Not or No JSON at all")


@endpoints.route("/item", methods=["PUT", "GET"], strict_slashes=False)
def get_item():
    """returns all the items of certain type"""
    data = request.get_json()
    if data:
        if isinstance(data, dict):
            keys = list(data.keys())
            item = str(data[keys[0]])

            my_uitem = UItem()

            uitem = my_uitem.get_uitems(item)
            # item_dicts = [item.to_dict() for item in items]

            return jsonify([uitem.to_dict()]), 200
        else:
            abort(400, "Not a JSON")
    else:
        abort(400, "Not or No JSON at all")
