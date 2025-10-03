from flask_restful import Resource
from flask import make_response, request 
from models import Comment
from app import db
from flask_jwt_extended import jwt_required

from schemas import CommentDetailsResponse, UpdateCommentSchema

comment_details_response_schema = CommentDetailsResponse()
update_comment_schema = UpdateCommentSchema()

class CommentDetailsResource(Resource):
    def get(self, id):
        data = Comment.query.get(id)
        if not data:
            return make_response({"error": "Comment not found"}, 404)
        
        result = comment_details_response_schema.dump(data)
        return make_response({"comment": result}, 200)
    
    @jwt_required()
    def patch(self, id):
        comment = Comment.query.get(id)
        if not comment:
            return make_response({"error": "comment not found"}, 404)
        
        ## (force=True) ignore data type for "application/json" if not support
        try:
            data = request.get_json(force=True)
        except Exception as e:
            return make_response({"error": str(e)}, 400)
        
        ## partial refer too ignore some data request only for patch
        errors = update_comment_schema.validate(data, partial=True)
        if errors:
            return make_response({"error": errors}, 400)
        
        
        comment.content = data.get("content", comment.content)
        comment.user_id = 1
        comment.blog_id = 1
        
        try:
            db.session.commit()
            db.session.refresh(comment)
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        return comment_details_response_schema.dump(comment), 200
    
    @jwt_required()
    def delete(self, id):
        comment = Comment.query.get(id)
        if not comment:
            return make_response({"error": "Comment not found"}, 404)
        
        db.session.delete(comment)
        db.session.commit()
        
        return make_response({"msg": "Comment has been deleted"}, 204)