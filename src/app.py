from flask import Flask, request, jsonify
from src.usecases.signup import SignUp


def create_app():
    app = Flask(__name__)

    @app.route("/api/users", methods=['POST'])
    def signup():
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        signup_usecase = SignUp(user_repo, hash_service)
