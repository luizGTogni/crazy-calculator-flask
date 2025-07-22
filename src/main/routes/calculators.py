from flask import Blueprint, jsonify, request

calc_route_blueprint = Blueprint("calc_routes", __name__)

@calc_route_blueprint.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request)
    return jsonify({ "success": True }), 200