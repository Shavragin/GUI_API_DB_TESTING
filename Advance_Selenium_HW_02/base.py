import os

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from UI.pages.base_page import BasePage
from UI.pages.login_page import LoginPage


class BaseClass():
    browser = None

    @pytest.fixture(autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.browser = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue("base_page")
        self.login_page: LoginPage = request.getfixturevalue("login_page")

    @pytest.fixture(autouse=True)
    def ui_report(self, request, temp_dir, driver):
        failed_tests_count = request.session.testsfailed
        yield
        if failed_tests_count < request.session.testsfailed:
            screenshot = os.path.join(temp_dir, "failure.png")
            driver.get_screenshot_as_file(screenshot)
            allure.attach.file(screenshot, "failure.png", attachment_type=allure.attachment_type.PNG)

            browser_log = os.path.join(temp_dir, "browser.log")
            with open(browser_log, "w") as f:
                for i in driver.get_log("browser"):
                    f.write(f"{i['level']} - {i['source']} - {i['message']}")

            with open(browser_log, "r") as f:
                allure.attach(f.read(), "browser.log", attachment_type=allure.attachment_type.TEXT)
