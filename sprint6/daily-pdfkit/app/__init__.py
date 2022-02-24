from flask import Flask
from dotenv import load_dotenv
from app import configs, routes

load_dotenv()

def create_app() -> Flask:
    app = Flask(__name__)

    def get_styles(path: str):
        with app.open_resource(path) as f:
            return f.read().decode("utf-8")

    app.jinja_env.globals["get_styles"] = get_styles

    configs.init_app(app)
    routes.init_app(app)

    return app
