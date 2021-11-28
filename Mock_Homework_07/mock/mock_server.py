from flask import Flask, jsonify, request

import json

from werkzeug.serving import WSGIRequestHandler

from settings import MOCK_HOST, MOCK_PORT

app = Flask(__name__)

is_login_data = {}

@app.route('/', methods = ['GET'])
def get_login_data():
    return is_login_data

@app.route('/get_login_status/<nickname>', methods=['GET'])
def get_status(nickname):
    if status := is_login_data.get(nickname):
        data = {
            nickname: status
        }
        return jsonify(data), 200
    else:
        return jsonify('Account does not exist, please create account and login in'), 404


@app.route('/post_new_user_status', methods=['POST'])
def post_new_login_status():
    nickname = json.loads(request.data)['name']

    if nickname in is_login_data:
        return jsonify('Account already exist, use put method to change status of exist user'), 404
    else:
        is_login_data[nickname] = 'True'
        return jsonify({nickname: is_login_data[nickname]}), 201


@app.route('/change_status_user', methods=['PUT'])
def change_login_status():
    nickname = json.loads(request.data)['name']
    status = json.loads(request.data)['status']
    if nickname in is_login_data:
        is_login_data[nickname] = status
        data = {
            nickname: status
        }
        return jsonify(f'Status was changed, current status is {data}'), 200
    else:
        return jsonify('User was not created, please use post request to create new user'), 404


@app.route('/delete_user/<nickname>', methods=['DELETE'])
def delete_nickname(nickname):
    # nickname = json.loads(request.data)['name']
    if nickname in is_login_data:
        is_login_data.pop(nickname)
        return jsonify(is_login_data), 200
    else:
        return jsonify("User is not is login list"), 400


WSGIRequestHandler.protocol_version = "HTTP/1.1"
app.run(MOCK_HOST, MOCK_PORT)
# is_login_data['sfsdfsd'] = 'True'
# print(delete_nickname('sfsdfsd'))
