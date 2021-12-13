import json
import threading

from flask import Flask, jsonify, request

from settings import MOCK_HOST, MOCK_PORT

app = Flask(__name__)

is_login_data = {}


@app.route('/', methods=['GET'])
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
        return jsonify({'error': 'Account does not exist, please create account and login in'}), 404


@app.route('/post_new_user_status', methods=['POST'])
def post_new_login_status():
    nickname = json.loads(request.data)['name']

    if nickname in is_login_data:
        return jsonify({'error':'Account already exist, use put method to change status of exist user'}), 404
    else:
        is_login_data[nickname] = 'True'
        return jsonify({nickname: is_login_data[nickname]}), 201


@app.route('/change_status_user', methods=['PUT'])
def change_login_status():
    nickname = json.loads(request.data)['name']
    status = json.loads(request.data)['status']
    if nickname in is_login_data:
        is_login_data[nickname] = status

        return jsonify({nickname: is_login_data[nickname]}), 200
    else:
        return jsonify({'error':'User was not created, please use post request to create new user'}), 404


@app.route('/delete_user/<nickname>', methods=['DELETE'])
def delete_nickname(nickname):
    if nickname in is_login_data:
        is_login_data.pop(nickname)
        return jsonify(is_login_data), 200
    else:
        return jsonify({'error': 'User is not is login list'}), 400


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify('If you say so...terminating'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })
    server.start()
    return server
