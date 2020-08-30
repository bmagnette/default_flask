import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from core.api.hello import hello_world_router
from core.extensions import mail, db


def create_app() -> Flask:
    dir_path = os.path.dirname(os.path.realpath(__file__))

    project_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    load_dotenv(dotenv_path=project_path + '/.env')

    app = Flask("Insiders", template_folder=os.path.join(dir_path, 'templates'))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ[
        'SQLALCHEMY_DATABASE_URI']  # '{}://{}:{}@{}/{}'.format(os.environ['DB_TYPE'], os.environ['DB_USER'], os.environ['DB_USER'], os.environ['DB_HOST'], os.environ['DB_NAME'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = False

    app.register_blueprint(hello_world_router)

    register_extensions(app)
    # register_models(app)

    return app


def register_extensions(app: Flask) -> None:
    mail.init_app(app)
    db.init_app(app)
    Migrate(app, db)


def register_models(app: Flask) -> None:
    with app.app_context():
        db.create_all()
