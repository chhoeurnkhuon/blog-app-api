from flask_restful import Resource
from flask import make_response, request
from models import Blog
from app import db, current_user_id
from datetime import datetime
from app import role_required

from schemas import CreateBlogSchema, BlogResponseSchema,BlogDetailsResponseSchema ,BlogUpdateSchema

class BlogService:
    def __init__(self):
        self.blog_response_schema = BlogResponseSchema(many=True)
        self.blog_details_response_schema = BlogDetailsResponseSchema()
        self.create_blog_schema = CreateBlogSchema()
        self.update_blog_schema = BlogUpdateSchema()
    
    def get_all_blog(self):
        blogs = Blog.query.all()
        
        result = self.blog_response_schema.dump(blogs)
        return make_response({"message": result}, 200)
        
    def create_blog(self, data):
        
        errors = self.create_blog_schema.validate(data)
        if errors:
            return make_response({"error": str(errors)}, 400)
        
        new_blog = Blog(
            title = data["title"],
            description = data["description"],
            created_date = datetime.now(),
            user_id = current_user_id()
        )
        
        try:
            db.session.add(new_blog)
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        result = self.blog_details_response_schema.dump(new_blog)
        return make_response({"message": result}, 201)
        
    def get_blog_by_id(self, id):
        blog = Blog.query.get(id)
        if not blog:
            return make_response({"message": blog})
        
        result = self.blog_details_response_schema.dump(blog)
        return make_response({"message": result}, 200)
    
    def update_blog_by_id(self, id, data):
        blog = Blog.query.get(id)
        if not blog:
            return make_response({"error": "Blog not found"}, 404)
        
        errors = self.update_blog_schema.validate(data, partial=True)
        
        if errors:
            return {"error": errors}, 400
        
        blog.title = data.get("title", blog.title)
        blog.description = data.get("description", blog.description)
        
        try:
            db.session.commit()
            db.session.refresh(blog)
            
            return self.blog_details_response_schema.dump(blog), 200
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
    def delete_blog_by_id(self, id):
        blog = Blog.query.get(id)
        if not blog:
            return make_response({"error": "Blog not found"}, 404)
        
        try:
            db.session.delete(blog)
            db.session.commit()
        except Exception as e:
            return make_response({"message": str(e)})
        
        return make_response({"message": "Blog has been deleted"}, 204)