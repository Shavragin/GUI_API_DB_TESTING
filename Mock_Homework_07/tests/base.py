import pytest


class Base:

    @pytest.fixture(autouse=True)
    def setup(self, logger, socket_client):
        self.socket_client = socket_client
        self.logger = logger
