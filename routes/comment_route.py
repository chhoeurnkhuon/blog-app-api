from flask import Blueprint, make_response, request
from app import db, current_user_id, role_required
from models import Comment

from services import CommentService

comment_route = Blueprint("comments", __name__)
comment_service = CommentService()

@comment_route.route("/comments", methods=["GET"])
def get_all_comments():
    return comment_service.get_all_comment()

@comment_route.route("/blogs/<int:blog_id>/comments", methods=["POST"])
@role_required("ADMIN", "USER")
def create_comment(blog_id):
    
    ## (force=True) used to ignore request data if not support applicaion/json
    data = request.get_json(force=True)
    user_id = current_user_id()
    return comment_service.create_comment(data, user_id, blog_id)

@comment_route.route("/comments/<int:id>")
def get_comment_by_id(id):
    return comment_service.get_comment_by_id(id)

@comment_route.route("/comments/<int:id>", methods=["PATCH"])
@role_required("ADMIN", "USER")
def update_comment_by_id(id):
    
    ## (force=True) ignore data type for "application/json" if not support
    data = request.get_json(force=True)
    return comment_service.update_comment_by_id(id, data)

@comment_route.route("/comments/<int:id>", methods=["DELETE"])
@role_required("ADMIN", "USER")
def delete_comment_by_id(id):
    
    return comment_service.delete_comment_by_id(id)
    