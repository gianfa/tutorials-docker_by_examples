from flask import Flask, request
import json

app = Flask(__name__)
PORT = 2100

@app.route("/")
def hello():
    return "Hello Worldo by Python!\nWe're in <b>proj2_serv2</b>"

@app.route("/calc/sum/", methods = ['GET'])
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return json.dumps(a+b)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(PORT), debug=True)