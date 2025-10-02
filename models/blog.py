from app import db
from datetime import datetime

class Blog(db.Model):
    __tablename__ = "blogs"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(25))
    description = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    ## user created many blogs
    author = db.relationship("User", back_populates="blogs")
    
    ## comments are many but on only a blog
    comments = db.relationship("Comment", back_populates="blog")