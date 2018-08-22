from api.v1.views import app_views
from models import storage
from flask import jsonify

@app_views.route('/status')
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats')
def stats():
    return jsonify(storage.count())
