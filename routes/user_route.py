from flask import Blueprint
from flask_restful import Api

from resources import UserResource
from resources import UserDetailResource

user_route = Blueprint("user_route", __name__)

api = Api(user_route)

api.add_resource(UserResource, "/users")
api.add_resource(UserDetailResource, "/users/<int:id>")