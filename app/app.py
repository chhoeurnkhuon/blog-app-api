from flask import Flask
from dotenv import load_dotenv
import os
import logging

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .extension import db
    from flask_migrate import Migrate

    db.init_app(app)
    Migrate(app, db)

    from models import User
    from routes import user_route, blog_route
    
    app.register_blueprint(user_route)
    app.register_blueprint(blog_route)

    @app.route("/")
    def home():
        return "Hello World"

    return app
