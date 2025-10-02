from app import db
from datetime import datetime
from .user_role import user_roles
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    ## an user can created many blog
    blogs = db.relationship("Blog", back_populates="author")
    
    ## an user can created many comments
    comments = db.relationship("Comment", back_populates="author")
    
    ## user has many roles
    roles = db.relationship("Role", secondary=user_roles, back_populates="users")