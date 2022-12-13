from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/ping')
def retornarPong():
    query = {'ping':'pong'}
    return jsonify(query)

app.run(host = '0.0.0.0')