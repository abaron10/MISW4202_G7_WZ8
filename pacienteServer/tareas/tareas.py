from celery import Celery
from celery.signals import task_postrun
from flask import request

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name="registrar_pago")
def send_payment(paciente):


@task_postrun.conenct()
def acknowledge(*args, **kwargs):
    print("exito")