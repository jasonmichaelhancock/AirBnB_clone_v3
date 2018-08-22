#!/usr/bin/python3
'''
    API for HolbertonBnB
'''
from api.v1.views import app_views
from models import storage
from flask import Flask, make_response, jsonify

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardown(self):
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
