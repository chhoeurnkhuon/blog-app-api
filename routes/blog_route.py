from flask import Blueprint, request
from services import BlogService
from flask import make_response, jsonify
from app import role_required

blog_service = BlogService()
blog_route = Blueprint("blogs", __name__)

@blog_route.route("/blogs", methods=["GET"])
def get_all_blogs():
    return blog_service.get_all_blog()

@blog_route.route("/blogs", methods=["POST"])
@role_required("ADMIN")
def create_blog():
    data = request.get_json()
    return blog_service.create_blog(data)

@blog_route.route("/blogs/<int:id>", methods=["GET"])
@role_required("ADMIN")
def get_blog_by_id(id):
    return blog_service.get_blog_by_id(id)

@blog_route.route("/blogs/<int:id>", methods=["PATCH"])
@role_required("ADMIN")
def update_blog_by_id(id):
    data = request.get_json(force=True)
    return blog_service.update_blog_by_id(id, data)

@blog_route.route("/blogs/<int:id>", methods=["DELETE"])
@role_required("ADMIN")
def delete_by_id(id):
    return blog_service.delete_blog_by_id(id)