from flask import Blueprint, request
from app import role_required

from services import UserService

user_service = UserService()
user_route = Blueprint("users", __name__)

@user_route.route("/users", methods=["GET"])
@role_required("ADMIN", "USER")
def get_all_users():
    return user_service.get_all_users()

@user_route.route("/users", methods=["POST"])
def create_new_user():
    data = request.get_json()
    return user_service.create_new_user(data)

@user_route.route("/users/<int:id>", methods=["GET"])
@role_required("ADMIN", "USER")
def get_user_by_id(id):
    return user_service.get_user_by_id(id)

@user_route.route("/users/<int:id>", methods=["PATCH"])
@role_required("ADMIN", "USER")
def update_user_by_id(id):
    data = request.get_json()
    return user_service.update_user_by_id(id, data)

@user_route.route("/users/<int:id>", methods=["DELETE"])
@role_required("ADMIN")
def delete_user_by_id(id):
    return user_service.delete_user_by_id(id)