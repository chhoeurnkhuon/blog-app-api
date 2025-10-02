from flask_restful import Resource
from flask import make_response, request
from models import Blog
from app import db
from flask_jwt_extended import jwt_required

from schemas import BlogDetailsResponseSchema
from schemas import BlogUpdateSchema

blog_details_response_schema = BlogDetailsResponseSchema()
blog_update_schema = BlogUpdateSchema()

class BlogDetailResource(Resource):
    
    def get(self, id):
        blog = Blog.query.get(id)
        if not blog:
            return make_response({"error": "Blog not found"}, 404)
        
        result = blog_details_response_schema.dump(blog)
        
        return make_response({"blog": result}, 200)
    
    @jwt_required()
    def patch(self, id):
        blog = Blog.query.get(id)
        if not blog:
            return make_response({"error": "Blog not found"}, 404)
        
        data = request.get_json()
        errors = blog_update_schema.validate(data, partial=True)
        
        if errors:
            return {"error": errors}, 400
        
        blog.title = data.get("title", blog.title)
        blog.description = data.get("description", blog.description)
        
        db.session.commit()
        db.session.refresh(blog)
        return blog_details_response_schema.dump(blog)
    
    @jwt_required()
    def delete(self, id):
        blog = Blog.query.get(id)
        if not blog:
            return ({"error": "Blog not found"}, 404)
        
        db.session.delete(blog)
        db.session.commit()

        return {"message": "Blog has been deleted"}, 204
        