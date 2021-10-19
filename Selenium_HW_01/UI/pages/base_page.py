from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Selenium_HW_01.UI.locators.basic_locators import LoginPageLocators

LOGIN = "Disclers2@yandex.ru"
PASSWORD = "SwzsheYkXK+&-#7"
CLICK = 3


class BasePage(object):
    def __init__(self, driver):
        self.browser = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.browser, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def clicking(self, locator, timeout=None):
        for i in range(CLICK):
            try:
                button_is_clickable = self.find(locator, timeout=timeout)
                button_is_clickable.click()
                return
            except StaleElementReferenceException:
                if i == CLICK - 1:
                    raise
            except ElementClickInterceptedException:
                if i == CLICK - 1:
                    raise
            except ElementNotInteractableException:
                if i == CLICK - 1:
                    raise

    def login(self, timeout=None):
        self.clicking(LoginPageLocators.ENTER_BUTTON, timeout)
        email = self.find(LoginPageLocators.EMAIL_FIELD)
        email.send_keys(LOGIN)
        email_password = self.find(LoginPageLocators.PASSWORD_FIELD)
        email_password.send_keys(PASSWORD)
        self.clicking(LoginPageLocators.LOG_IN_BUTTON)

    def element_is_disappeared(self, locator):
        self.wait().until(EC.invisibility_of_element_located(locator))
