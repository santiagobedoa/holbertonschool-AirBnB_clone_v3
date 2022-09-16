#!/usr/bin/python3
"""Module fro State endpoints"""
from flask import jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", strict_slashes=False,
                methods=['GET'], defaults={"state_id": None})
@app_views.route("/state/<state_id>", methods=['GET'])
def get_state(state_id):
    """GET /state API route"""
    if state_id is None:
        states = [v.to_dict() for v in storage.all("State").values()]
        return jsonify(states)
    state = storage.get(State, state_id)
    if not state:
        return make_response(jsonify({"error": "Not found"}), 404)
    return jsonify(state.to_dict())

@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """DELETE /state API route"""
    state = storage.get(State, state_id)
    if not state:
         return make_response(jsonify({"error": "Not found"}), 404)
    storage.delete(state)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route("/states", strict_slashes=False, methods=["POST"])
def post_state():
    """POST /state API route"""
    data = request.get_json(force=True, silent=True)
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    if "name" not in data:
        return make_response(jsonify({"error": "Missing name"}), 400)
    s = State(**data)
    s.save()
    return make_response(jsonify(s.to_dict()), 201)

@app_views.route("/states/<state_id>", methods=["PUT"])
def put_state(state_id):
    """PUT /state API route"""
    state = storage.get(State, state_id)
    if not state:
        return make_response(jsonify({"error": "Not found"}), 404)
    data = request.get_json(force=True, silent=True)
    if not data:
        return make_response(jsonify({"error": "Not a JSON"}), 400)
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)
