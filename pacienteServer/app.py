import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify , request
app = Flask(__name__)
from faker import Faker
import random
import requests
import json


data_factory = Faker()
MONITOR_URL = "http://127.0.0.1:5000/"


@app.route('/payment',methods=['POST'])
def run_experiment():
    lis = []
    for iteration in range(1,5):
        lis.append(payment(iteration,
                data_factory.name().split(" ")[0],
                data_factory.name().split(" ")[1],
                data_factory.email(),
                "+57 " + str(random.randint(1000000, 9000000)),
                random.randint(100000, 900000),
                False))
    return jsonify(lis)



def payment(id,name,lastname,email,phone_number,billing,exit_granted):

    patient = {"id": id,
                "name": name, 
                "lastname": lastname, 
                "email":email,
                "phone_number":phone_number,
                "billing":billing,
                "exit_granted":exit_granted}

    r = requests.post(url = MONITOR_URL + "/send_payment", data=patient)
    return json.loads(r.content)
    

if __name__ == '__main__':
    app.run(debug=True,port=4000)
