#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import City
from models import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_city_state(state_id):
    '''
        Get cities in a specified state object.
    '''
    cities = []
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    for key, obj in storage.all('City').items():
        if obj.state_id == state_id:
            cities.append(obj.to_dict())
            return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city_id(city_id):
    '''
        Get city matching specified id
    '''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    cities = []
    for key, obj in storage.all('City').items():
        if obj.id == city_id:
            cities.append(obj.to_dict())
    return jsonify(cities)


@app_views.route('/cities/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    '''
    Delete a specified city object.
    '''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    delcity = "City." + city_id
    cities = storage.all('City')
    for key, obj in cities.items():
        if key == delcity:
            storage.delete(obj)
            storage.save()
            return jsonify({})


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city():
    '''
    Creates a City object.
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    name = update.get("name")
    if name is None:
        abort(400, "Missing name")
    check_state = storage.get('State', state_id)
    if check_state is None:
        abort(404)
    new_city = City()
    new_city.state_id = state_id
    new_city.name = name
    new_city.save()
    return jsonify(new_city.to_dict()), 200


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
