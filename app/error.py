from flask_jwt_extended.exceptions import JWTExtendedException
from flask import jsonify

def error_handlers(app):
    
    @app.errorhandler(JWTExtendedException)
    def jwt_errors(error):
        return jsonify({"error": str(error)}), 401