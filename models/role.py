from app import db
from .user_role import user_roles
from sqlalchemy.orm import relationship

class Role(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    role_name = db.Column(db.String(25), nullable=False, unique=True)
    
    ## a role can apply to many user
    users = db.relationship("User", secondary=user_roles, back_populates="roles")