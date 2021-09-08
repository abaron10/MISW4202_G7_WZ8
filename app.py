import sys
# sys.path.insert(0,"../../")
from flask import Flask, jsonify
from  products import products
app = Flask(__name__)


@app.route('/ping',methods=['GET'])
def ping():
    res = filterPrice(products)
    return jsonify(res)


def filterPrice(dic,name):
    for item in dic:
        if item["name"]==name:
            return item



@app.route('/price/<string:product_name>',methods=['GET'])
def ping2(product_name):
    res = filterPrice(products,product_name)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True,port=4000)
