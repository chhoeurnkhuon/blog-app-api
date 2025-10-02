from flask_jwt_extended.exceptions import JWTExtendedException
from flask import jsonify
import logging

def error_handlers(app):
    
    @app.errorhandler(JWTExtendedException)
    def jwt_errors(error):
        return jsonify({"error": str(error)}), 401
    
    @app.errorhandler(Exception)
    def internal_server_error(error):
        logging.error(f"Internal Server Error: {error}")
        return jsonify({
            "error": "Internal Server Error",
        }), 500