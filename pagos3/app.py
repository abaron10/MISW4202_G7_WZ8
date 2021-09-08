import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify , request
from flask_cors import CORS
import time
app = Flask(__name__)
cors = CORS(app)


@app.route('/ping',methods=['POST'])
def ping():
 
    return "I AM ALIVE"

@app.route('/payment',methods=['POST'])
def payment():
    time.sleep(5000)
    return "payment ok"

if __name__ == '__main__':
    app.run(debug=True,port=4000)
