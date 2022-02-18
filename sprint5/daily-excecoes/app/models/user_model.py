from . import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


@dataclass
class UserModel(db.Model):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)

    name: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False, unique=True)
