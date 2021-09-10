import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify , request
from flask_cors import CORS
import time
import json
from database import cur , conn
app = Flask(__name__)
cors = CORS(app)



@app.route('/ping',methods=['POST'])
def ping():
    return "I AM ALIVE"

@app.route('/payment',methods=['POST'])
def payment():
    time.sleep(2)
    cur.execute('''INSERT INTO payments (id, name , lastname , email , phone_number , billing , exit_granted)
#                 VALUES (?, ?, ?, ?, ?, ?, ?)''', (request.form["id"],request.form["name"],request.form["lastname"],request.form["email"],request.form["phone_number"],request.form["billing"],True))
    patient = {"id":  request.form["id"],
                "name":  request.form["name"],
                "lastname":  request.form["lastname"],
                "email": request.form["email"],
                "phone_number":  request.form["phone_number"],
                "billing": request.form["billing"],
                "exit_granted":  True
    }
    cur.close()
    return patient

if __name__ == '__main__':
    app.run(debug=True,port=4000)
