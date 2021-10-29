import time
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from UI.locators.basic_locators import LoginPageLocators


CLICK = 3
TIMEOUT = 10

class PageNotLoadedException(Exception):
    pass

class BasePage(object):
    url = "https://target.my.com/"

    def __init__(self, driver):
        self.browser = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.browser, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def is_opened(self, timeout=TIMEOUT):
        current_time = time.time()
        while time.time() - current_time < timeout:
            if self.browser.current_url == self.url:
                return True

        raise PageNotLoadedException(f"{self.url} did not open in {timeout} for {self.__class__.__name__}"
                                     f"current url {self.browser.current_url}")

    def clicking(self, locator, timeout=None):
        for i in range(CLICK):
            try:
                self.find(locator)
                self.wait(timeout=timeout).until(EC.element_to_be_clickable(locator)).click()
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


    def login(self, user, password, timeout=None):
        self.clicking(LoginPageLocators.ENTER_BUTTON, timeout)
        self.find(LoginPageLocators.EMAIL_FIELD).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.clicking(LoginPageLocators.LOG_IN_BUTTON)

    def incorrect_login(self, user, password, timeout=None):
        self.clicking(LoginPageLocators.ENTER_BUTTON, timeout)
        self.find(LoginPageLocators.EMAIL_FIELD).send_keys(f"{user}y")
        self.find(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.clicking(LoginPageLocators.LOG_IN_BUTTON)

    def incorrect_password(self, user, password, timeout=None):
        self.clicking(LoginPageLocators.ENTER_BUTTON, timeout)
        self.find(LoginPageLocators.EMAIL_FIELD).send_keys(f"{user}")
        self.find(LoginPageLocators.PASSWORD_FIELD).send_keys(f"{password}1")
        self.clicking(LoginPageLocators.LOG_IN_BUTTON)


    def element_is_disappeared(self, locator):
        self.wait().until(EC.invisibility_of_element_located(locator))

    def scroll_to(self, element):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)
