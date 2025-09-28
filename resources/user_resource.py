from flask_restful import Resource
from flask import make_response

class UserResource(Resource):
    def get(self):

        return make_response({"user": {"name": "test user"}}, 200)

    def post(self):
        return make_response({}, 201)
