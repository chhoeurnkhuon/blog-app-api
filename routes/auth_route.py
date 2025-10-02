from flask import Blueprint
from flask_restful import Api

from resources import AuthResource

auth_route = Blueprint("auth_route", __name__)

api = Api(auth_route)

api.add_resource(AuthResource, "/auth/login")