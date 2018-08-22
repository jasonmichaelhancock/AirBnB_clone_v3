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
   '''Returns number of each type of object.'''
   stats = {
       'test': 'test',
       'amenities': storage.count('Amenity'),
       'cities': storage.count('Cities'),
       'places': storage.count('Places'),
       'reviews': storage.count('Reviews'),
       'states': storage.count('State'),
       'users': storage.count('Users')
   }
   return jsonify(stats)
'''
@app_views.route('/stats')
def stats():
    StatesCount= {}
    for obj, val in models.classes.items():
#        count= storage.count(obj)
        StatesCount['test'] = 'test'
        print(obj + ":" + "count")
    return jsonify(StatesCount)
'''
