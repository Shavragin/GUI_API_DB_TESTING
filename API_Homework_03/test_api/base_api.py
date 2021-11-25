import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.login()
            self.api_client.get_csrf_token()
