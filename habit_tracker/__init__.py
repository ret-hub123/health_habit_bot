from .config import Config

from flask import Flask
from .build_model import db
from .routes import habit


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(habit)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

