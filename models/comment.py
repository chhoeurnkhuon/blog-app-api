from app import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = "comments"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"), nullable=False)
    
    ## many comments can has one or many author
    author = db.relationship("User", back_populates="comments")
    
    ## a blog has many comments
    blog = db.relationship("Blog", back_populates="comments") 