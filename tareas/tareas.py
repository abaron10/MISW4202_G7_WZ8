from celery import Celery
from celery.signals import task_postrun
from flask import request
import requests
from flask_cors import CORS


celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrar_pago')
def registrar_pago(idCuentaPago,fecha):
    with open('log_pagos.txt', 'a+') as file:
        file.write('Pago Id -{}- enviado: {}\n' .format(idCuentaPago,fecha))

@celery_app.task(name='voting_pago')
def voting_pago(idCuentaPago,fecha):
        print ("llamar a servicio")
        API_ENDPOINT = "http://127.0.0.1:5010"
        print(API_ENDPOINT + "/send_payment")
        r = requests.post(url = API_ENDPOINT + "/send_payment")
        with open('log_pagos_respuesta.txt', 'a+') as file:
            file.write(str(r.content.decode('UTF-8')) + 'Pago Id -{}- enviado: {}\n' .format(idCuentaPago,fecha))

# @task_postrun.conenct()
# def acknowledge(*args, **kwargs):
#     print("exito")