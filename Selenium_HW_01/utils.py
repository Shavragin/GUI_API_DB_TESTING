import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_HW_01.UI.locators import LoginPageLocators

LOGIN = "Disclers2@yandex.ru"
PASSWORD = "SwzsheYkXK+&-#7"

class BaseClass():

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.browser = driver

    def find(self, locator):
        return self.browser.find_element(*locator)

    def wait(self, locator, time):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located((locator)))

    def login(self):
        self.browser.get("https://target.my.com/")
        button = self.wait(LoginPageLocators.ENTER_BUTTON, 5)
        button.click()
        email = self.find(LoginPageLocators.EMAIL_FIELD)
        email.send_keys(LOGIN)
        email_password = self.find(LoginPageLocators.PASSWORD_FIELD)
        email_password.send_keys(PASSWORD)
        log_in = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in.click()