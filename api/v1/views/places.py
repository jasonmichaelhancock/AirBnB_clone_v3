#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import City
from models import Place


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_place_city(city_id):
    '''
        Get places in a specified City object.
    '''
    places = []
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    for key, obj in storage.all('Place').items():
        if obj.city_id == city_id:
            places.append(obj.to_dict())
            return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    '''
        Get a specified Place object.
    '''
    for key, obj in storage.all('Place').items():
        if obj.id == place_id:
            return jsonify(obj.to_dict())
    abort(404)


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    '''
    Delete a specified Place object.
    '''
    delplace = "Place." + place_id
    places = storage.all('Place')
    for key, obj in places.items():
        if key == delplace:
            storage.delete(obj)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/places', methods=['POST'], strict_slashes=False)
def create_place():
    '''
    Creates a Place object.
    '''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'user_id' not in update.keys():
        abort(400, "Missing usser_id")
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_place = Place()
    storage.new(new_place)
    for key, value in update.items():
        new_user.__dict__[key] = value
    storage.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    '''
    Updates a Place object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict())
