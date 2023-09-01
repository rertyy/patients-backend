from flask import Flask
from flask_cors import CORS

from .router import router_bp
from .db import connect


def create_app():
    app = Flask(__name__)
    app.register_blueprint(router_bp)
    CORS(app)

    return app
