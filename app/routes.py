from flask import Blueprint, jsonify, request
from .services import get_items, add_item, get_item_by_id

api = Blueprint('api', __name__)

@api.route('/items', methods=['GET'])
def get_items_route():
    return jsonify(get_items())

@api.route('/items', methods=['POST'])
def add_item_route():
    item = request.json
    return jsonify(add_item(item)), 201

@api.route('/items/<int:item_id>', methods=['GET'])
def get_item_route(item_id):
    item, status = get_item_by_id(item_id)
    return jsonify(item), status
