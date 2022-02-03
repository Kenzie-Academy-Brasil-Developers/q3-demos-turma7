from flask import jsonify, request
from http import HTTPStatus
from app.models.product_model import Product


def get_products():
    products = Product.select_all()

    return jsonify([Product.serializer(product) for product in products]), HTTPStatus.OK


def create_product():
    data = request.get_json()

    product = Product(**data)

    inserted_product = product.insert_into()

    # serialized_product = Product.serializer(inserted_product)

    return Product.serializer(inserted_product), HTTPStatus.OK
