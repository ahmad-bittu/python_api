from flask import Flask

app = Flask(__skyways__)


@app.route('/')
def hello_world():
    return 'Hello World'
