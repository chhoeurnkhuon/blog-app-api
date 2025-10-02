from flask_restful import Resource
from flask import make_response, request
from models import Comment
from schemas import CommentResponseSchema
from schemas import CreateCommentSchema
from flask_jwt_extended import jwt_required
from datetime import datetime

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
        data = request.get_json()
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
        
        result = comment_response_schema.dump(new_comment)
        
        return make_response({"comments": result}, 200)
        