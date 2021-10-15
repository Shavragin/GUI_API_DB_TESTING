import pytest
from Selenium_HW_01.base import BaseClass
from Selenium_HW_01.UI.locators.basic_locators import LoginPageLocators
from Selenium_HW_01.UI.locators.basic_locators import DashboardPageLocators
import time

@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self):
        self.base_page.login()
        assert "dashboard" in self.browser.current_url

    def test_logout(self):
        self.base_page.login()
        self.base_page.clicking(DashboardPageLocators.ACCOUNT)
        self.base_page.clicking(DashboardPageLocators.EXIT)
        time.sleep(5)

    @pytest.mark.parametrize(
        "link, expected", [pytest.param(DashboardPageLocators.AUDIENCE, "segments"),
                           pytest.param(DashboardPageLocators.BILLING, "billing")
        ]
    )
    def test_change_page(self, link, expected):
        self.base_page.login()
        self.base_page.clicking(link)
        assert expected in self.browser.current_url





