from pydantic import BaseModel


class CurrencySchema(BaseModel):
    name: str
    code: str
    rate: float

    class Config:
        from_attributes = True
