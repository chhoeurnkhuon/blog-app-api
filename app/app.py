from flask import Flask;

from routes import user_route   

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

app.register_blueprint(user_route)