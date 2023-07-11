from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'username': 'ahmad', 'password': 'ahmadpass'}
]


@app.route('/users')
def get_incomes():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_income():
    users.append(request.get_json())
    return '', 204
