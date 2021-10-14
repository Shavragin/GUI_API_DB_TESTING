from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_HW_01.UI.locators.basic_locators import LoginPageLocators

LOGIN = "Disclers2@yandex.ru"
PASSWORD = "SwzsheYkXK+&-#7"
CLICK = 3


class BasePage(object):
    def __init__(self, driver):
        self.browser = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.browser, timeout=timeout)

    def find(self, locator):
        return self.wait().until(EC.presence_of_element_located(locator))

    def click(self, locator):
        for i in range(CLICK):
            try:
                elem_is_located = self.find(locator)
                button_is_clickable = self.wait().until(EC.element_to_be_clickable(locator))
                return
            except StaleElementReferenceException:
                if i == CLICK - 1:
                    raise


    def login(self):
        button = self.wait(LoginPageLocators.ENTER_BUTTON, 5)
        button.click()
        email = self.find(LoginPageLocators.EMAIL_FIELD)
        email.send_keys(LOGIN)
        email_password = self.find(LoginPageLocators.PASSWORD_FIELD)
        email_password.send_keys(PASSWORD)
        log_in = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in.click()
