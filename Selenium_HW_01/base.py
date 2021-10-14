import pytest
from _pytest.fixtures import FixtureRequest
from Selenium_HW_01.UI.pages.base_page import BasePage

class BaseClass():
    browser = None

    @pytest.fixture(autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.browser = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue("base_page")


