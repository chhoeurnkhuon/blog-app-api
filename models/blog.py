from app.extension import db
from sqlalchemy.sql import func
from sqlalchemy import DateTime

class Blog(db.Model):
    __tablename__ = "blogs"
    
    id = db.Column(db.Integer, primary_key=True,)
    title = db.Column(db.String(25))
    description = db.Column(db.String(255))
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    author = db.relationship("User", back_populates="blogs")