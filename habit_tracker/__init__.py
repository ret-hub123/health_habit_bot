from .config import Config
from flask import Flask

from .build_model import db, migrate

from .routes.habit import habit
from .routes.user import user


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(habit)
    app.register_blueprint(user)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    return app

