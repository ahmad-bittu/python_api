from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'username': 'ahmad', 'password': 'ahmadpass'},
    {'username': 'faizan', 'password': 'fazzypass'},
    {'username': 'asad', 'password': 'asadpass'},
]


@app.route('/users')
def get_incomes():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_income():
    users.append(request.get_json())
    return '', 204
