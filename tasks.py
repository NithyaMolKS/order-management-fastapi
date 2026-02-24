from app.celery_worker import celery
from app.database import SessionLocal
from app.models import Order
import time

@celery.task(name="app.tasks.process_order")
def process_order(order_id:int):
    db=SessionLocal()
    order = db.query(Order).filter(order_id=Order.id).first()
    if not order:
        return "order not found"
    print("processing")
    time.sleep(10)
    order.status="COMPLETED"
    db.commit()
    db.close(0)

