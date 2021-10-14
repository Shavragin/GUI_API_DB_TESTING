import pytest
from _pytest.fixtures import FixtureRequest


class BaseClass():

    @pytest.fixture(autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.browser = driver
        self.config = config
