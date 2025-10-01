from flask_restful import Resource
from flask import make_response, request
from models import User
from app.extension import db
from datetime import datetime

from schemas import UserDetailsResponseSchema, UpdateUserSchema

user_details_response_schema = UserDetailsResponseSchema()
update_user_schema = UpdateUserSchema()

class UserDetailResource(Resource):
    def get(self, id):
        user = User.query.get(id)
        
        if not user:
            return make_response({"error":"user not found"}, 404)
        
        result = user_details_response_schema.dump(user)
        
        return make_response({"user": result}, 200)
    
    def patch(self, id):
        user = User.query.get(id)
        if not user:
            return {"error": "User not found"}, 404
        
        data = request.get_json()
        errors = update_user_schema.validate(data, partial=True)
        
        if errors:
            return {"errors": errors}, 400
        
        user.username = data.get("username", user.username)
        user.password = data.get("password", user.password)
        user.gender = data.get("gender", user.gender)
        user.created_at = datetime.now()
        
        db.session.commit()
        return user_details_response_schema.dump(user), 200
    
    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return {"error": "User not found"}, 404
        
        db.session.delete(user)
        db.session.commit()
        
        return {"message": "User deleted"}, 204