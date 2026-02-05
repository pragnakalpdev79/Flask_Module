from flask import Flask
from app.extensions import db, migrate, jwt, ma
from app.routes.book_routes import book_bp
from app.routes.auth_routes import auth_bp
from app.routes.users import usersbp
from config import DevConfig
import click


def create_app(config_class=DevConfig):
    app = Flask(__name__)
    if config_class:
        app.config.from_object(config_class)
    #app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(book_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(usersbp)
    return app
