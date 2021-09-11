from pacienteServer import create_app
import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify , request
from .modelos import db, CuentaPagos
from faker import Faker
from datetime import datetime
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrar_pago')
def registrar_pago(*args):
    pass

@celery_app.task(name='voting_pago')
def voting_pago(*args):
    pass


faker = Faker()

app = Flask(__name__)

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    for i in range(100):
     c = CuentaPagos(nombre_paciente =faker.name(),valor_pago = faker.pricetag(),confirmacion_pago = False)
     db.session.add(c) 
     db.session.commit()
     id = c.id
     print(c.id)
     args = (id,datetime.now())
     registrar_pago.apply_async(args=args, queue = 'logs')
     voting_pago.apply_async(args=args, queue = 'logs')
     

     


# @app.route('/payment',methods=['POST'])
# def payment():
#     id = request.json["id_paciente"]
#     nombre_paciente = request.json["nombre_paciente"]
#     apellido_paciente = request.json["apellido_paciente"]
#     correo = request.json["correo"]
#     teléfono = request.json["teléfono"]
#     valor_pendiente = request.json["valor_pendiente"]
#     salida = boelano 

#     return jsonify(res)


# def filterPrice(dic,name):
#     for item in dic:
#         if item["name"]==name:
#             return item



# @app.route('/price/<string:product_name>',methods=['GET'])
# def ping2(product_name):
#     res = filterPrice(products,product_name)
#     return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True,port=4000)
