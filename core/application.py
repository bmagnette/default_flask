import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from core.api.hello import stack_router
from core.extensions import mail, db
from flask_restplus import Api, Resource

from core.models.stack import Stack


def create_app() -> Flask:
    dir_path = os.path.dirname(os.path.realpath(__file__))

    project_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    load_dotenv(dotenv_path=project_path + '/.env')

    app = Flask("Cacib", template_folder=os.path.join(dir_path, 'templates'))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = False

    app.register_blueprint(stack_router)
    register_extensions(app)
    register_models(app)
    api = Api(app=app,
              version="1.0",
              title="Test CACIB ",
              description="RPN Calculator ")
    name_space = api.namespace('names', description='Manage names')

    return app


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    Migrate(app, db)


def register_models(app: Flask) -> None:
    with app.app_context():
        db.create_all()
