import time

import pytest

from UI.locators.basic_locators import DashboardPageLocators, CreateCompanyPageLocators, ProfileInfoLocators
from base import BaseClass



class TestMyTarget(BaseClass):

    def test_login(self):
        self.base_page.login()
        assert "dashboard" in self.browser.current_url, "User did not login"

    def test_logout(self, dashboard):
        # self.base_page.login()
        dashboard.exit_system()
        assert "https://target.my.com/" == self.browser.current_url,  "User did not logout"

    @pytest.mark.UI
    def test_create_company(self, dashboard):
        dashboard.go_to_create_new_company
        time.sleep(5)
        # self.base_page.clicking(CreateCompanyPageLocators.REACH)
        # time.sleep(5)

    # @pytest.mark.parametrize(
    #     "locator, expected", [pytest.param(DashboardPageLocators.AUDIENCE, "segments"),
    #                           pytest.param(DashboardPageLocators.BILLING, "billing")
    #                           ]
    # )
    # def test_change_page(self, locator, expected):
    #     self.base_page.login()
    #     self.base_page.clicking(locator)
    #     assert expected in self.browser.current_url, "Page did not change"
    #
    # def test_change_info(self):
    #     self.base_page.login()
    #     self.base_page.clicking(DashboardPageLocators.PROFILE)
    #     self.profile_page.send_info(ProfileInfoLocators.MOBILE, "8800")
    #     self.profile_page.send_info(ProfileInfoLocators.FIO)
    #     self.base_page.clicking(ProfileInfoLocators.SAVE)
    #     self.base_page.browser.refresh()
    #     new_name = self.base_page.find(DashboardPageLocators.USER_NAME)
    #     assert self.profile_page.name.upper() == new_name.text, "User did not change profile info"
