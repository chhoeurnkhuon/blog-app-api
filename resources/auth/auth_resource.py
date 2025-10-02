from flask_restful import Resource
from flask import make_response, request
from flask_jwt_extended import create_access_token
import bcrypt

from schemas import LoginRequestSchema
from models import User

login_request_schema = LoginRequestSchema()

class AuthResource(Resource):
    
    def post(self):
        data = request.get_json()
        
        errors = login_request_schema.validate(data)
        if errors: 
            return make_response({"error": "Something is wrong"}, 400)
        
        username = data["username"]
        password = data["password"]
        
        user = User.query.filter_by(username = username).first()
        if not user:
            return make_response({"error": "Invalid username or password"}, 401)
        
        if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return make_response({"error": "Invalid username or password"}, 401)
        
        access_token = create_access_token(identity=user.id)

        return make_response({"access_token": access_token}, 200)
        
        