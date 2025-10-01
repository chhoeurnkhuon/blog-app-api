from flask import Blueprint
from flask_restful import Api

from resources import BlogResource, BlogDetailResource

blog_route = Blueprint("blog_route", __name__)

api = Api(blog_route)

api.add_resource(BlogResource, "/blogs")
api.add_resource(BlogDetailResource, "/blogs/<int:id>")
