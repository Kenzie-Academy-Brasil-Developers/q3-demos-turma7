from flask import Flask

# from app.routes.user_route import user_route
# from app.routes.product_route import product_route

from app.routes.user_route import bp as bp_user
from app.routes.product_route import bp as bp_product


def init_app(app: Flask):
    # user_route(app)
    # product_route(app)

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_product)
