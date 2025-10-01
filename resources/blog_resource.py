from flask_restful import Resource
from flask import make_response, request, jsonify
from models import Blog
from app.extension import db
from datetime import datetime

from schemas import CreateBlogSchema, BlogResponseSchema,BlogDetailsResponseSchema 

blog_response_schema = BlogResponseSchema(many=True)
blog_details_response_schema = BlogDetailsResponseSchema()
create_blog_schema = CreateBlogSchema()

class BlogResource(Resource):
    def get(self):
        blogs = Blog.query.all()
        if not blogs:
            return make_response({"error": "Blog not found"}, 404)
        
        result = blog_response_schema.dump(blogs)
        return make_response({"blogs": result}, 200)
    
    def post(self):
        blog = request.get_json()
        errors = create_blog_schema.validate(blog)

        if errors:
            return jsonify(errors), 400
        
        new_blog = Blog(
            title = blog["title"],
            description = blog["description"],
            created_date = datetime.now(),
            user_id = 1
        )
        
        try:
            db.session.add(new_blog)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return make_response({"error": str(e)}, 500)
        
        result = blog_details_response_schema.dump(new_blog)
        
        return make_response(result, 201)
