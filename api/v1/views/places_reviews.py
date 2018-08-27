#!/usr/bin/python3
'''
Page for outes related to State class.
'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models import State
from models import Review


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_states():
    '''
    Get list of all review objects.
    '''
    review = []
    for key, obj in storage.all('Review').items():
        reviews.append(obj.to_dict())
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    '''
    Get a specified review object.
    '''
    for key, obj in storage.all('Review').items():
        if obj.id == review_id:
            return jsonify((obj.to_dict()))
    abort(404)


@app_views.route('/reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    '''
    Delete a specified review object.
    '''
    delreview = "Review." + review_id
    reviews = storage.all('Reviews')
    for key, obj in reviews.items():
        if key == delreview:
            storage.delete(obj)
            storage.save()
            return jsonify({})
    abort(404)


@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def create_reviews():
    '''
    Creates a Review.
    '''
    if not request.is_json:
        abort(400, "Not a JSON")
    update = request.get_json()
    if 'name' not in update.keys():
        abort(400, "Missing name")
    new_review = Review()
    storage.new(new_review)
    for key, value in update.items():
        new_review.__dict__[key] = value
    storage.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    '''
    Updates a Review object.
    '''
    if not request.is_json:
        abort(400, description="Not a JSON")
    review = storage.get('Review', review_id)
    if review is None:
        abort(404)
    update = request.get_json()
    for key, value in update.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(review, key, val)
    storage.save()
    return jsonify(review.to_dict())
