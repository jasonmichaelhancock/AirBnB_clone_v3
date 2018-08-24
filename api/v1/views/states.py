#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    '''
    Get list of all state objects.
    '''
    states = []
    for key, obj in storage.all('State').items():
        states.append(obj.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    '''
    Get a specified state object.
    '''
    for key, obj in storage.all('State').items():
        if obj.id == state_id:
            return jsonify((obj.to_dict()))
    abort(404)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    '''
    Delete a specified state object.
    '''
    states = storage.all('State')
    for key, obj in states.items():
        if key == delstate:
            print(key, obj)
            storage.delete(obj)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    '''
    Creates a State.
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_state = State()
    storage.new(new_state)
    for key, value in update.items():
        new_state.__dict__[key] = value
    storage.save()
    return jsonify(new_state.to_dict)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    '''
    Updates a State object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, val)
    storage.save()
    return jsonify(state.to_dict())
