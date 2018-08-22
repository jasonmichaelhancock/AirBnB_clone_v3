#!/usr/bin/python3
'''
    API for HolbertonBnB
'''
from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

@app.errorhandler(404)
'''
Handler for 404 errors that returns a JSON-formatted 404 status code response.
'''
def page_not_found():
return make_response(jsonify({'error': 'Not Found'}), 404)
