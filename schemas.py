from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name:str
    item: str
    quantity:int


class OrderResponse(OrderCreate):
    id:int
    status:str

    class config:
        from_attributues= True



