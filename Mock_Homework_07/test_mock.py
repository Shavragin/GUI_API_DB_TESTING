import pytest
import requests

import json

from client.client_mock import SocketClient

class TestMock(SocketClient):

    def test_post_user(self):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': 'Anton'})
        resp = requests.post('http://127.0.0.1:1234/post_new_user_status', headers=headers, data=data)

        # data = self.socket_client_post("Anton")
        # assert resp.json()['Anton'] == 'True'

    def test_put(self):
        name = 'Anton'
        status = 'False'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': 'Anton', 'status': 'False'})
        resp = requests.put('http://127.0.0.1:1234/change_status_user', headers=headers, data=data)
        # self.socket_client_put(name, status)



    # def test_get(self):
    #     name = 'Anton'
    #     data = self.socket_client_get(name)
    #     assert json.loads(data[-1])[name] == 'True'

    def test_delete(self):
        name = "Anton"
        data = self.socket_client_delete(name)
        # data = json.dumps({'name': 'Anton'})
        # resp = requests.delete(f'http://127.0.0.1:1234/delete_user/{name}', headers={'Content-Type': 'application/json'})
        assert json.loads(data[-1]).get(name) is None

