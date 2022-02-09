from sqlalchemy import Column, Integer, String, Date, DateTime
from app.configs.database import db
from dataclasses import dataclass


# dataclass vs namedTuples

# print(f"{__name__} DB -> {id(db)}")


@dataclass
class CallRecord(db.Model):
    # id: int
    # source: int
    # destination: str
    # start_time: str
    # end_time: str

    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True)
    source: int = Column(Integer, nullable=False)
    destination: str = Column(String, nullable=False)
    start_time: str = Column(Date)
    end_time: str = Column(Date)

    def __repr__(self):
        return f"<[{self.id}]{self.source} - {self.destination}>"

    def serializer(self):
        return {
            "id": self.id,
            "source": self.source,
            "destination": self.destination,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
