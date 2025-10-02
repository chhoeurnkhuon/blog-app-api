from flask import Blueprint
from flask_restful import Api

from resources import CommentResource

comment_route = Blueprint("CommentResource", __name__)

api = Api(comment_route)

api.add_resource(CommentResource, "/comments")