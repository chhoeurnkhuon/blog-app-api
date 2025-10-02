from flask_restful import Resource
from flask import make_response, request, jsonify
from models import User, Role
from app import db
from datetime import datetime
import bcrypt

from schemas import UserResponseSchema, UserDetailsResponseSchema, CreateUserSchema, UpdateUserSchema

user_response_schema = UserResponseSchema(many=True)
user_details_response_schema = UserDetailsResponseSchema()
create_user_schema = CreateUserSchema()
update_user_schema = UpdateUserSchema()

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        result = user_response_schema.dump(users)
        return make_response({"user": result}, 200)

    def post(self):
        data = request.get_json()
        errors = create_user_schema.validate(data)
        
        if errors: 
            return jsonify(errors), 400
        
        existing_user = User.query.filter_by(username = data["username"]).first()
        if existing_user:
            return make_response({"error": "User alreay exist"}, 409)
        
        role = Role.query.filter_by(role_name=data["role_name"]).first()
        if not role:
            return make_response({"error": "Role not found"}, 400)
        
        new_user =  User(
            username = data["username"],
            password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            gender = data["gender"],
            created_at = datetime.now()
        )
        
        new_user.roles.append(role)
        
        try:
           db.session.add(new_user)
           db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
            
        result = user_details_response_schema.dump(new_user)
        
        return make_response(result, 201)
