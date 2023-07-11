from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'username': 'ahmad', 'password': 'ahmadpass'},
    {'username': 'faizan', 'password': 'fazzypass'},
    {'username': 'asad', 'password': 'asadpass'},
]
admins = [
    {'name': 'ahmad', 'key': 'ahahahhaha'},
    {'name': 'faizan', 'key': 'aaaaaaaahhhhhh'},
    {'name': 'asad', 'key': 'hhhhhhhhhhaaaaaaaa'},
]


@app.route('/users')
def getUsers():
    return jsonify(users)


@app.route('/admins')
def getAdmins():
    return jsonify(admins)


@app.route('/users', methods=['POST'])
def addUsers():
    users.append(request.get_json())
    return '', 204


@app.route('/admins', methods=['POST'])
def addAdmins():
    admins.append(request.get_json())
    return '', 204


app.run(host='0.0.0.0', port=8080)
