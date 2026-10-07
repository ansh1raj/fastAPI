from pydantic import BaseModel

class CreateProductSchema(BaseModel):
    name: str
    category: str
    price: int = 0
    stock: int = 0

