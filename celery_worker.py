from celery import Celery

celery = Celery("order_worker",
                broker="pyamqp://guest:guest@localhost:5672//",
                backend="rpc://")
celery.conf.task_routes={
    "app.tasks.*":{"queue":"orders"}
}
