from app.extension import db
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    blogs = db.relationship("Blog", back_populates="author")