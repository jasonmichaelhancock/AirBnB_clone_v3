#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import State
from models import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    '''
    Get list of all user objects.
    '''
    users = []
    print("Hello")
    for key, obj in storage.all('User').items():
        users.append(obj.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''
        Get a specified state object.
    '''
    for key, obj in storage.all('User').items():
        if obj.id == user_id:
            return jsonify((obj.to_dict()))
    abort(404)

@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''
    Delete a specified state object.
    '''
    userkey = "User." + user_id
    users = storage.all('User')
    for key, val in users.items():
        if key == userkey:
            storage.delete(val)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''
    Creates a User
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_user = User()
    storage.new(new_user)
    for key, value in update.items():
        new_user.__dict__[key] = value
    storage.save()
    return jsonify(new_user.to_dict)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    '''
    Updates a User object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, val)
    storage.save()
    return jsonify(state.to_dict())
