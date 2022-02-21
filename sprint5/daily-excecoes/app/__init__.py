from app import routes
from app.configs import database, migration
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)

    return app
