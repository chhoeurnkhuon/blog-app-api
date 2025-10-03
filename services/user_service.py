from flask_restful import Resource
from flask import make_response, request, jsonify
from models import User, Role
from app import db, role_required
from datetime import datetime
import bcrypt

from schemas import UserResponseSchema, UserDetailsResponseSchema, CreateUserSchema, UpdateUserSchema

class UserService:
    def __init__(self):
        self.user_response_schema = UserResponseSchema(many=True)
        self.user_details_response_schema = UserDetailsResponseSchema()
        self.create_user_schema = CreateUserSchema()
        self.update_user_schema = UpdateUserSchema()
        
    def get_all_users(self):
        users = User.query.all()
        if not users:
            return make_response({"message": "User not found"}, 404)
        
        result = self.user_response_schema.dump(users)
        return make_response({"users": result}, 200)
    
    def create_new_user(self, data):
        errors = self.create_user_schema.validate(data, partial=True)
        if errors:
            return make_response({"message": "Something is wrong"})
        
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
            
        result = self.user_details_response_schema.dump(new_user)
        
        return make_response(result, 201)
    
    def get_user_by_id(self, id):
        user = User.query.get(id)
        
        if not user:
            return make_response({"message": "User not found"}, 404)
        
        result = self.user_details_response_schema.dump(user)
        return make_response({"user": result}, 200)
    
    def update_user_by_id(self, id, data):
        user = User.query.get(id)
        if not user:
            return make_response({"message": "User not found"}, 404)
        
        errors = self.update_user_schema.validate(data, partial=True)
        
        if errors:
            return {"errors": errors}, 400
        
        user.username = data.get("username", user.username)
        user.password = data.get("password", user.password)
        user.gender = data.get("gender", user.gender)
        
        db.session.commit()
        result = self.user_details_response_schema.dump(user)
        return make_response({"user": result}, 201)
    
    def delete_user_by_id(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"message": "User not found"}, 404)
        
        db.session.delete(user)
        db.session.commit()
        
        return make_response({"message": "User has been deleted"}, 204)