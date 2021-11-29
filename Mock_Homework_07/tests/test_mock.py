import json

import requests

from base import Base


class TestMock(Base):

    def test_post_user(self):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': 'Anton'})
        resp = requests.post('http://127.0.0.1:1234/post_new_user_status', headers=headers, data=data)

    def test_put(self):
        name = 'Anton'
        status = 'False'
        headers = {'Content-Type': 'application/json'}
        data = json.dumps({'name': 'Anton', 'status': 'False'})
        resp = requests.put('http://127.0.0.1:1234/change_status_user', headers=headers, data=data)

    def test_get(self):
        name = 'Anton'
        data = self.socket_client.client_get(name)
        assert json.loads(data[-1])[name] == 'True'

    def test_delete(self):
        name = "Anton"
        data = self.socket_client.client_delete(name)
        assert json.loads(data[-1]).get(name) is None
