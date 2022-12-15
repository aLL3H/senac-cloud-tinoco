from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def testeAPI():
    return 'API está online'

app.run()

