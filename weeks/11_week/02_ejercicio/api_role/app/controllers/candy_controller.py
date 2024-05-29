from flask import Blueprint, request, jsonify
from models.candy_model import Candy
from views.candy_view import render_candy_list, render_candy_detail
from utils.decorators import jwt_required, roles_required


#candy store
#marca, peso, sabor, origen
#brand, weight, taste, origin

candy_bp = Blueprint("candy", __name__)


@candy_bp.route("/candys", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_candys():
    candys = Candy.get_all()
    return jsonify(render_candy_list(candys))


@candy_bp.route("/candys/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_candy(id):
    candy = Candy.get_by_id(id)
    if candy:
        return jsonify(render_candy_detail(candy))
    return jsonify({"error": "candy no encontrado"}), 404


@candy_bp.route("/candys", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_candy():
    data = request.json
    brand = data.get("brand")
    weight = data.get("weight")
    taste = data.get("taste")
    origin = data.get("origin")

    if not brand or not weight or not taste or not origin is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    candy = Candy(brand=brand, weight=weight, taste=taste, origin=origin)
    candy.save()

    return jsonify(render_candy_detail(candy)), 201


@candy_bp.route("/candys/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_candy(id):
    candy = Candy.get_by_id(id)

    if not candy:
        return jsonify({"error": "candy no encontrado"}), 404

    data = request.json
    brand = data.get("brand")
    weight = data.get("weight")
    taste = data.get("taste")
    origin = data.get("origin")

    candy.update(brand=brand, weight=weight, taste=taste, origin=origin)

    return jsonify(render_candy_detail(candy))


@candy_bp.route("/candys/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_candy(id):
    candy = Candy.get_by_id(id)

    if not candy:
        return jsonify({"error": "candy no encontrado"}), 404

    candy.delete()

    return "", 204
