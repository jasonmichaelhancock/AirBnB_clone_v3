from api.v1.views import app_views
from models import storage
from flask import jsonify
from os import getenv
import models

@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def stats():
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('Cities'),
        'places': storage.count('Places'),
        'reviews': storage.count('Reviews'),
        'states': storage.count('States'),
        'users': storage.count('Users')
    }
