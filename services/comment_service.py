from flask_restful import Resource
from flask import make_response, request
from models import Comment
from schemas import CommentResponseSchema, CreateCommentSchema, CommentDetailsResponse, UpdateCommentSchema
from datetime import datetime
from app import db, current_user_id, role_required

class CommentService:
    
    def __init__(self):
        self.create_comment_schema = CreateCommentSchema()
        self.comment_response_schema = CommentResponseSchema(many=True)
        self.comment_details_response_schema = CommentDetailsResponse()
        self.update_comment_schema = UpdateCommentSchema()
    
    def get_all_comment(self):
        
        comments = Comment.query.all()
        if not comments:
            return make_response({"message": "Comment not found"}, 200)
        result = self.comment_response_schema.dump(comments)
        return make_response({"comments": result}, 200)
    
    def create_comment(self, data, user_id, blog_id):
        
        errors = self.create_comment_schema.validate(data)
        
        if errors:
            return make_response({"error": "Something is required"}, 400)
        
        new_comment = Comment(
            content = data["content"],
            created_at = datetime.now(),
            user_id = user_id,
            blog_id = blog_id
        )
        
        try:
            db.session.add(new_comment)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        ## cannot use (many=True) for one reponse
        result = self.comment_details_response_schema.dump(new_comment)
        return make_response({"comment": result}, 200)
        
    def get_comment_by_id(self, id):
        comment = Comment.query.get(id)
        if not comment:
            return make_response({"message": "Comment not found"}, 200)
        result = self.comment_details_response_schema.dump(comment)
        return make_response({"comment": result}, 200)
    
    def update_comment_by_id(self, id, data):
        comment = Comment.query.get(id)
        if not comment:
            return make_response({"message": "Comment not found"}, 404)
        
        ## partial refer too ignore some data request only for patch
        errors = self.update_comment_schema.validate(data, partial=True)
        if errors:
            return make_response({"error": errors}, 400)
        
        comment.content = data.get("content", comment.content)
        
        try:
            db.session.commit()
            db.session.refresh(comment)
            
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        result = self.comment_details_response_schema.dump(comment)
        return make_response({"comment": result}, 200)
        
    def delete_comment_by_id(self, id):
        comment = Comment.query.get(id)
        if not comment:
            return make_response({"error": "Comment not found"}, 404)
        try:
            db.session.delete(comment)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"message": str(e)}, 500)
        
        return make_response({"message": "Comment has been deleted"}, 204)