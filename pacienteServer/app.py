import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify , request
app = Flask(__name__)



@app.route('/payment',methods=['POST'])
def payment():
    id = request.json["id_paciente"]
    nombre_paciente = request.json["nombre_paciente"]
    apellido_paciente = request.json["apellido_paciente"]
    correo = request.json["correo"]
    teléfono = request.json["teléfono"]
    valor_pendiente = request.json["valor_pendiente"]
    salida = boelano 

    return jsonify(res)


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
