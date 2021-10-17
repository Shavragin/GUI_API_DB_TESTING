import pytest
from Selenium_HW_01.base import BaseClass
from Selenium_HW_01.UI.locators.basic_locators import LoginPageLocators, DashboardPageLocators, ProfileInfoLocators


@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self):
        self.base_page.login()
        assert "dashboard" in self.browser.current_url


    def test_logout(self):
        self.base_page.login()
        self.dashboard_page.exit_system()
        enter_button = self.base_page.find(LoginPageLocators.ENTER_BUTTON)
        assert "Войти" in enter_button.text

    @pytest.mark.parametrize(
        "locator, expected", [pytest.param(DashboardPageLocators.AUDIENCE, "segments"),
                           pytest.param(DashboardPageLocators.BILLING, "billing")
        ]
    )
    def test_change_page(self, locator, expected):
        self.base_page.login()
        self.base_page.clicking(locator)
        assert expected in self.browser.current_url


    def test_change_info(self):
        self.base_page.login()
        self.base_page.clicking(DashboardPageLocators.PROFILE)
        self.profile_page.send_info(ProfileInfoLocators.FIO)
        self.profile_page.send_info(ProfileInfoLocators.MOBILE, "8800")
        self.base_page.clicking(ProfileInfoLocators.SAVE)







