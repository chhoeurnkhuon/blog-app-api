from flask_restful import Resource
from flask import make_response, request, jsonify
from models import User
from app.extension import db
from schemas.user_schema import UserSchema
from schemas.users_schema import UsersSchema

user_schema = UserSchema()
users_schema = UsersSchema(many=True)

class UserResource(Resource):
    def get(self):
        users = User.query.all()
        result = users_schema.dump(users)
        return make_response({"user": result}, 200)

    def post(self):
        data = request.get_json()
        errors = user_schema.validate(data)
        
        if errors: 
            return jsonify(errors), 400
        
        new_user =  User(**data)
        
        try:
           db.session.add(new_user)
           db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
            
        result = user_schema.dump(new_user)
        
        return make_response(result, 201)
