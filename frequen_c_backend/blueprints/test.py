from flask import Blueprint

test_blueprint = Blueprint("test", __name__, url_prefix="/")


@test_blueprint.get("")
def index():
    return {"message": "Hello World!"}
