#!/usr/bin/python3
'''
    API for HolbertonBnB
'''
from api.v1.views import app_views
from models import storage
from flask import Flask, make_response, jsonify
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown(exception):
    """Teardown and close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Return error status"""
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = int(getenv('HBNB_API_PORT', default=5000))
    app.run(host, int(port), threaded=True)
