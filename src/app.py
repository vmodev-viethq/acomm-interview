from flask import Flask
from flask_restful import Api
from marshmallow import ValidationError

from config import Config


def create_app():
    app: Flask = Flask(__name__)
    configure_router(app)
    configure_error_handler(app)
    return app


def configure_router(app: Flask):
    from routers import api
    api.init_app(app)


def configure_error_handler(app: Flask):
    from error_handlers import register_validation_error
    app.register_error_handler(ValidationError, register_validation_error)


app = create_app()
