from flask import Blueprint
from flask_restful import Api

from resources import UserResource

user_route = Blueprint("user_route", __name__)

api = Api(user_route)

api.add_resource(UserResource, "/users")