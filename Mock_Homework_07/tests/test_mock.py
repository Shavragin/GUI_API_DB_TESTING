import json

from tests.base import Base
from tests.builder import fake_name


class TestMock(Base):

    def test_add_user(self):
        name = fake_name()
        resp = self.socket_client.client_post(name)
        assert resp.json()[name] == 'True'

    def test_change_status_user(self):
        name = fake_name()
        self.socket_client.client_post(name)
        resp = self.socket_client.client_put(name, 'False')
        assert resp.json()[name] == 'False'

    def test_get_user(self):
        name = fake_name()
        self.socket_client.client_post(name)
        data = self.socket_client.client_get(name)
        assert json.loads(data[-1])[name] == 'True'

    def test_delete_user(self):
        name = fake_name()
        self.socket_client.client_post(name)
        data = self.socket_client.client_delete(name)
        assert json.loads(data[-1]).get(name) is None

    def test_add_existed_name(self):
        name = fake_name()
        self.socket_client.client_post(name)
        resp = self.socket_client.client_post(name)
        assert 'Account already exist' in resp.json()['error']
        assert resp.status_code == 404

    def test_get_not_existed_name(self):
        data = self.socket_client.client_get(fake_name())
        assert 'Account does not exist' in json.loads(data[-1]).get('error')

    def test_change_status_on_not_existed_name(self):
        name = fake_name()
        resp = self.socket_client.client_put(name, 'False')
        assert 'User was not created' in resp.json()['error']

    def test_delete_not_existed_user(self):
        name = fake_name()
        data = self.socket_client.client_delete(name)
        assert 'User is not is login list' in json.loads(data[-1]).get('error')
