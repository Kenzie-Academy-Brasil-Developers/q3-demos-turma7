from flask import Flask
from app import routes


def create_app():
    app = Flask(__name__)

    # Inicialização das rotas
    routes.init_app(app)

    return app
