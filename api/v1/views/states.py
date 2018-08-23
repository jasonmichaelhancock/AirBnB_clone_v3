#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage

@app_views.route('/states', methods=['GET'], strict_slashes=False)
'''
    Get list of all state objects.
'''
def get_states():
    states = []
    for key, obj in storage.all('State').items():
        states.append(obj.to_dict())
    return jsonify(states)

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
'''
Get a specified state object.
'''
def get_state(state_id):
    for key, obj in storage.all('State').items():
        if obj.id == state_id:
            return(obj.to_dict)
        else:
            abort(404)

@app.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
'''
Get list of a specified state object.
'''
def delete_state(state_id):
    for key, obj in storage.all('State').items():
        if obj.id == state_id:
            storage.remove(obj)
            return jsonify({})
        abort(404)

@app.route('/states', methods=['POST'], strict_slashes=False)
'''
Creates a State.
'''
def create_state():
    if not request.is_json:
        abort(400, description="Not a JSON")
    state_json = request.get_json
    if not 'name' in state_json:
        abort(400, description="Missing name")
    new_state = State()
    storage.new(new_state)
    for key, value in state_json.items():
        new_state.__dict__[key] = value
    storage.save()
    return jsonify(new_state)

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
'''
Updates a State object.
'''
def update_state(state_id):
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
    return jsonify(state.to_dict()), 200
