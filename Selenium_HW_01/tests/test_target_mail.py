import pytest

from Selenium_HW_01.UI.locators.basic_locators import DashboardPageLocators, ProfileInfoLocators
from Selenium_HW_01.base import BaseClass


@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self, credentials):
        self.base_page.login(*credentials)
        assert "dashboard" in self.browser.current_url, "User did not login"

    def test_logout(self, credentials):
        self.base_page.login(*credentials)
        self.dashboard_page.exit_system()
        assert "https://target.my.com/" == self.browser.current_url, "User did not logout"

    @pytest.mark.parametrize(
        "locator, expected", [pytest.param(DashboardPageLocators.AUDIENCE, "segments"),
                              pytest.param(DashboardPageLocators.BILLING, "billing")
                              ]
    )
    def test_change_page(self, locator, expected, credentials):
        self.base_page.login(*credentials)
        self.base_page.clicking(locator)
        assert expected in self.browser.current_url, "Page did not change"

    def test_change_info(self, credentials):
        self.base_page.login(*credentials)
        self.base_page.clicking(DashboardPageLocators.PROFILE)
        self.profile_page.send_info(ProfileInfoLocators.MOBILE, "8800")
        self.profile_page.send_info(ProfileInfoLocators.FIO)
        self.base_page.clicking(ProfileInfoLocators.SAVE)
        self.base_page.browser.refresh()
        new_name = self.base_page.find(DashboardPageLocators.USER_NAME)
        assert self.profile_page.name.upper() == new_name.text, "User did not change profile info"
