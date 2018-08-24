#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities_state():
    '''
    Get cities by state objects.
    '''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    city = state.cities
    cities_in_state = [cities.to_dict() for cities in city]
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    '''
    Get a specified city object.
    '''
    for key, obj in storage.all('City').items():
        if obj.id == city_id:
            return(obj.to_dict)
    abort(404)


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(city_id):
    '''
    Delete a specified city object.
    '''
    for key, obj in storage.all('City').items():
        if obj.id == city_id:
            storage.delete(obj)
            return jsonify({})
    abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city():
    '''
    Creates a City object.
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_city = City()
    storage.new(new_city)
    for key, value in update.items():
        new_city.__dict__[key] = value
    storage.save()
    return jsonify(new_city.to_dict)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    '''
    Updates a City object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    city = storage.get('City', city_id)
    if state is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, val)
    storage.save()
    return jsonify(city.to_dict())
