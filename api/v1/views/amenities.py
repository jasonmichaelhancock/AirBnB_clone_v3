#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import State
from models import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    '''
    Get list of all Amenity objects.
    '''
    amenities = []
    for key, obj in storage.all('Amenity').items():
        amenities.append(obj.to_dict())
    return jsonify(amenities)


@app_views.route('/amenites/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    '''
    Get a specified Amenity object.
    '''
    for key, obj in storage.all('Amenity').items():
        if obj.id == amenity_id:
            return jsonify((obj.to_dict()))
    abort(404)


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    '''
    Delete a specified Amenity object.
    '''
    delamenity = "Amenity." + amenity_id
    amenities = storage.all('Amenity')
    for key, obj in amenities.items():
        if key == delamenity:
            storage.delete(obj)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''
    Creates an Amenity object.
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_amenity = Amenity()
    storage.new(new_amenity)
    for key, value in update.items():
        new_amenity.__dict__[key] = value
    storage.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    '''
    Updates an Amenity object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    amenity = storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, val)
    storage.save()
    return jsonify(amenity.to_dict())
