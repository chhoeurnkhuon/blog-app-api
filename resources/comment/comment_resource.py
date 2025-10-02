from flask_restful import Resource
from flask import make_response, request
from models import Comment
from schemas import CommentResponseSchema
from flask_jwt_extended import jwt_required

comment_response_schema = CommentResponseSchema(many=True)

class CommentResource(Resource):
    
    def get(self):
        comments = Comment.query.all()
        
        if not comments:
            return make_response({"error": "Comment not found"}, 404)
        
        result = comment_response_schema.dump(comments)
        return make_response({"Comments": result}, 200)
        
        