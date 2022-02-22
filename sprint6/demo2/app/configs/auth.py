from flask_httpauth import HTTPTokenAuth
from app.models.user_model import User
import os

auth = HTTPTokenAuth()
# equivale auth = HTTPTokenAuth(scheme='Bearer')


# @auth.verify_token
# def verify_token(api_key: str):
#     user = User.query.filter_by(api_key=api_key).first()

#     return user

"""
    Outra abordagem, supondo que o serviço será usado internamente
    nao precisando de usuarios ou logins
"""


@auth.verify_token
def verify_token(api_key: str):

    return api_key == os.getenv("API_KEY")
