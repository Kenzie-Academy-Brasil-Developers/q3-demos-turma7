from app.models.order_model import Order
from flask import jsonify, request
from http import HTTPStatus
from sqlalchemy.orm import Query

# from werkzeug.exceptions import NotFound
import werkzeug.exceptions

from app.models.product_model import Product
from app.models.order_product_model import OrderProduct
from app.configs.database import db


def get_order_by_id(order_id: int):
    order: Order = Order.query.get(order_id)

    if not order:
        return {"error": f"order id {order_id} not found"}, HTTPStatus.NOT_FOUND

    return jsonify(order), HTTPStatus.OK


def get_order_products(order_id: int):
    order: Order = Order.query.get(order_id)

    if not order:
        return {"error": f"order id {order_id} not found"}, HTTPStatus.NOT_FOUND

    return jsonify(order.products), HTTPStatus.OK


def add_item(order_id: int):
    data = request.get_json()

    try:
        product_id = data["product_id"]
        sale_value = data["sale_value"]

        order = Order.query.get_or_404(
            order_id, description=f"order id {order_id} not found"
        )
        product = Product.query.get_or_404(
            product_id, description=f"product id {product_id} not found"
        )
        # poderia ser product_id=product_id
        item = OrderProduct(product_id=product.product_id, sale_value=sale_value)

        order.products.append(item)

        db.session.commit()

        return jsonify(order.products), HTTPStatus.OK

    except KeyError as e:
        return {"error": f"missing key {e.args[0]}"}, HTTPStatus.BAD_REQUEST
    except werkzeug.exceptions.NotFound as e:
        return {"error": f"{e.description}"}, e.code


def get_order_products_query(order_id: int):
    base_query: Query = (
        db.session.query(Product.product_id, Product.name, OrderProduct.sale_value)
        .select_from(Order)
        .join(OrderProduct)
        .join(Product)
        .filter(Order.id == order_id)
    )

    # marshmallow -> flask-marshmallow
    column_names = [q["name"] for q in base_query.column_descriptions]
    serialized_data = [dict(zip(column_names, row)) for row in base_query.all()]

    return jsonify(serialized_data), HTTPStatus.OK
