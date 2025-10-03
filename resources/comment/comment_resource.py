from flask_restful import Resource
from flask import make_response, request
from models import Comment
from schemas import CommentResponseSchema, CreateCommentSchema, CommentDetailsResponse
from flask_jwt_extended import jwt_required
from datetime import datetime
from app import db

comment_details_response = CommentDetailsResponse()
comment_response_schema = CommentResponseSchema(many=True)
create_comment_schema = CreateCommentSchema()


class CommentResource(Resource):
    
    def get(self):
        comments = Comment.query.all()
        
        if not comments:
            return make_response({"error": "Comment not found"}, 404)
        
        result = comment_response_schema.dump(comments)
        return make_response({"Comments": result}, 200)
    
    @jwt_required()
    def post(self):
        
        ## (force=True) used to ignore request data if not support applicaion/json
        data = request.get_json(force=True)
        errors = create_comment_schema.validate(data)
        
        if errors:
            return make_response({"error": "Something is required"}, 400)
        
        new_comment = Comment(
            content = data["content"],
            created_at = datetime.now(),
            user_id = 1,
            blog_id = 1
        )
        
        try:
            db.session.add(new_comment)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        ## cannot use (many=True) for one reponse
        result = comment_details_response.dump(new_comment)
        
        return make_response({"comments": result}, 200)
        