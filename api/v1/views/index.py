#!/usr/bin/python3
"""Module for app_views /status route"""
from crypt import methods
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of /status route"""
    return jsonify({"status": "OK"})
