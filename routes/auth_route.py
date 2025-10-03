from flask import Blueprint, make_response, request
from models import User

from services import AuthService

auth_route = Blueprint("auths", __name__)
auth_service = AuthService()

@auth_route.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    
    return auth_service.login(data)