from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/greetings/")
def hello():
    return "Hello Worlda!"

@app.route("/calc/sum/", methods = ['GET'])
def calc():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return json.dumps(a+b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)