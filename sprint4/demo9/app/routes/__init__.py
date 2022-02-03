from flask import Blueprint, Flask

# from app.routes.user_route import user_route
# from app.routes.product_route import product_route

from app.routes.user_route import bp as bp_user
from app.routes.product_route import bp as bp_product
from app.routes.order_route import bp as bp_order

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    # user_route(app)
    # product_route(app)

    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_product)
    bp_api.register_blueprint(bp_order)

    app.register_blueprint(bp_api)
