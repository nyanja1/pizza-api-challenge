from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizzas_bp = Blueprint('pizzas', __name__)

@pizzas_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])