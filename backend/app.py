from datetime import datetime, timedelta
import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt
import jwt
from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///studysphere.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-me")

    CORS(app, origins=os.getenv("CORS_ORIGINS", "http://localhost:3000"))
    db.init_app(app)

    with app.app_context():
        from models import User, Project, Task, Note  # noqa: F401

        db.create_all()

    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok", "timestamp": datetime.utcnow().isoformat()})

    @app.route("/api/auth/register", methods=["POST"])
    def register():
        from models import User

        data = request.get_json() or {}
        email = data.get("email")
        password = data.get("password")
        name = data.get("name")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({"message": "User already exists"}), 409

        user = User(
            email=email,
            name=name or email.split("@")[0],
            password_hash=bcrypt.hash(password),
        )
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201

    @app.route("/api/auth/login", methods=["POST"])
    def login():
        from models import User

        data = request.get_json() or {}
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.verify(password, user.password_hash):
            return jsonify({"message": "Invalid credentials"}), 401

        token = jwt.encode(
            {
                "sub": user.id,
                "exp": datetime.utcnow() + timedelta(hours=12),
            },
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )

        return jsonify(
            {
                "access_token": token,
                "user": {"id": user.id, "email": user.email, "name": user.name},
            }
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

