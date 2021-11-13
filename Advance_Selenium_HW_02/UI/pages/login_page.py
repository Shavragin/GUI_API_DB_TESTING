import allure

from UI.locators.basic_locators import LoginPageLocators
from UI.pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://target.my.com/"

    def click_on_enter(self):
        self.logger.info("Click on enter button")
        self.clicking(LoginPageLocators.ENTER_BUTTON)

    def click_on_log_in_button(self):
        self.logger.info("Click on log in button")
        self.clicking(LoginPageLocators.LOG_IN_BUTTON)

    def filling_information(self, user, password):
        self.logger.info("Filling information")
        self.find(LoginPageLocators.EMAIL_FIELD).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step("Logging to Target")
    def login(self, user, password):
        self.click_on_enter()
        self.filling_information(user, password)
        self.click_on_log_in_button()

    @allure.step("Logging with incorrect login_name")
    def incorrect_login_name(self, user, password):
        self.click_on_enter()
        self.filling_information(f"{user}y", password)
        self.click_on_log_in_button()

    @allure.step("Logging with incorrect password")
    def incorrect_password(self, user, password):
        self.click_on_enter()
        self.filling_information(user, f"{password}1")
        self.click_on_log_in_button()
