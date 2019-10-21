from flask import Flask, request
import json
from examp_funx import *

app = Flask(__name__)
PORT = 5001

@app.route("/")
def hello():
    return "Hello World!"

# Working example
@app.route("/db", methods = ['GET'])
def dbio():
    TABLE_NAME = 'YOUR_TABLE_NAME'
    df = retrieve_table_from_db(TABLE_NAME)
    return df[:50].to_string()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(PORT), debug=True)