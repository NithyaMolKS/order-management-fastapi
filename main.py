from fastapi import FastAPI,Depends
from sqlalchemy.orm import session
import schemas
from app import crud
from app.database import Base,engine,SessionLocal
from tasks import process_order

app=FastAPI(title="Order Managmenet service")

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/orders")
def get_orders(db:session=Depends(get_db)):
    return crud.get_orders(db)



@app.get("/")
def home():
    return {"message":"Order Management Service Running"}

@app.post("/orders", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db:session=Depends(get_db)):
    new_order =  crud.create_order(db, order)
    process_order.delay(new_order.id)
    return new_order


