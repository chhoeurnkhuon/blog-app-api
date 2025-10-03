from flask import Blueprint
from flask_restful import Api

from resources import CommentResource, CommentDetailsResource

comment_route = Blueprint("CommentResource", __name__)

api = Api(comment_route)

api.add_resource(CommentResource, "/comments")
api.add_resource(CommentDetailsResource, "/comments/<int:id>")