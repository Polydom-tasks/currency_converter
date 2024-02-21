from sqlalchemy import Column, Integer, String, Numeric, DateTime
from db import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String(3), nullable=False, unique=True)
    rate = Column(Numeric(precision=10, scale=2))
    updated_at = Column(DateTime)

    def __repr__(self):
        return f"<Currency(name='{self.name}', code='{self.code}', rate={self.rate})>"
