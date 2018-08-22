#!/usr/bin/python3
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

@app_views.route('/api/v1/states', methods=['GET'])
'''
    Get list of all state objects.
'''
def get_states():
    states = []
    for key, obj in storage.all('State').items():
        states.append(obj.to_dict())
    return jsonify(states)

@app_views.route('/api/v1/states/<state_id>', methods=['GET'])
'''
Get list of a specified state object.
'''
def get_state(state_id):
    for key, obj in storage.all('State').items():
        if obj.id == state_id:
            return(obj.to_dict)
        else:
            abort(404)

@app.route('/api/v1/states/<state_id>', methods=['DELETE'])
'''
Get list of a specified state object.                                                                        
'''
def delete_state(state_id):
    for key, obj in storage.all('State').items():
        if obj.id == state_id:
            storage.remove(obj)
            return jsonify({})
        abort(404)

@app.route('/api/v1/states', methods=['POST'])
def create_state():
    if not request.json:
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


if __name__ == '__main__':
