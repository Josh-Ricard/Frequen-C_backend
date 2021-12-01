import json

from flask import Flask
from werkzeug.exceptions import HTTPException

from frequen_c_backend.blueprints import blueprints
from frequen_c_backend.config import Config

__version__ = "0.1.0"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    register_blueprints(app)
    register_error_handler(app)
    return app


def register_blueprints(app: Flask):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def register_error_handler(app: Flask):
    @app.errorhandler(HTTPException)  # type: ignore
    def handle_exception(exception: HTTPException):
        response = exception.get_response()
        if response.content_type != "application/json":
            response.data = json.dumps(  # type: ignore
                {
                    "code": exception.code,
                    "name": exception.name,
                    "description": exception.description,
                }
            )
            response.content_type = "application/json"
        return response
