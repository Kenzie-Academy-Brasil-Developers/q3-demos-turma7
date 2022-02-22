from dataclasses import dataclass
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class User(db.Model):
    user_id: str
    email: str
    api_key: str

    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(64), unique=True, nullable=False)
    # unsafe_password = Column(String, nullable=False)
    password_hash = Column(String)
    api_key = Column(String)

    @property
    def password(self):
        raise AttributeError("Password is not accessible")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    """
        user -> Objeto da classe User
        # Attribute error
        print(user.password)

        user.password = '1234'
    """

    """
        {
            'email': 'alguma_coisa@mail.com',
            'password': '1234'
        }
    """
