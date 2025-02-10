from flask import Flask
from flask_cors import CORS
from app.routes.comic_route import comic_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(comic_bp, url_prefix='/api/comic')
    return app
