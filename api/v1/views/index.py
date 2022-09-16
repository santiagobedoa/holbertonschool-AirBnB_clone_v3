#!/usr/bin/python3
"""Module for app_views /status route"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of /status route"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Returns the number of each objects by type"""
    objects = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    objects = {k: storage.count(v) for k, v in objects.items()}
    return jsonify(objects)
