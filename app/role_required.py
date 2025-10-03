from functools import wraps
from flask import make_response
from .get_user import current_user_id
from models import User
from flask_jwt_extended import jwt_required

def role_required(*required_roles):
    def decorator(fn):
        
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            user_id = current_user_id()
            user = User.query.get(user_id)
            
            if not user:
                return make_response({"error": "User not found"}, 404)
            
            print("user", user)
            
            user_roles = [role.role_name for role in user.roles]
            
            if not any(role in user_roles for role in required_roles):
                return make_response({"error": "Insufficient role"}, 403)
            
            return fn(*args, **kwargs)
        return wrapper
    return decorator