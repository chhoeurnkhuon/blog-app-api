from flask import Flask
from dotenv import load_dotenv
import os
import logging
from flask_jwt_extended import JWTManager

from .error import error_handlers

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    ## allow jwt
    app.config['JWT_VERIFY_SUB'] = False
    
    ## allow exception handler
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    jwt = JWTManager(app)

    from .extension import db
    from flask_migrate import Migrate

    db.init_app(app)
    Migrate(app, db)
    
    from routes import user_route, blog_route, comment_route, auth_route
    
    app.register_blueprint(user_route)
    app.register_blueprint(blog_route)
    app.register_blueprint(comment_route)
    app.register_blueprint(auth_route)
    
    error_handlers(app)

    return app
