from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from dataclasses import dataclass
from sqlalchemy.orm import relationship, validates
from app.configs.database import db
from app.exc.user_exception import InvalidBirthDateFormat, InvalidEmail
from datetime import datetime as dt


@dataclass
class User(db.Model):
    user_id: int
    email: str
    birthdate: str
    children: int
    married: bool
    account_balance: float
    orders: str

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    email = Column(String(64), unique=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    children = Column(Integer, nullable=False)
    married = Column(Boolean, nullable=False)
    account_balance = Column(Float(2))
    # created_at

    orders = relationship("Order", back_populates="customer", uselist=True)

    @validates("email")
    def validate_email(self, _, email_to_be_tested):
        if "@" not in email_to_be_tested:
            raise InvalidEmail

        return email_to_be_tested

    @validates("birthdate")
    def validate_birthdate(self, _, date_to_be_tested):
        try:
            b_date = dt.strptime(date_to_be_tested, "%Y/%m/%d")
        except ValueError:
            raise InvalidBirthDateFormat

        # TODO: Verificar se o usuario tem mais de 25anos
        """
            - capturar a data atual (ano mes e dia atual)
            - comparar com birthdate
            - é possivel utilizar operadores aritmeticos em objetos datetime
        """

        return date_to_be_tested
