import logging
import time

import allure
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CLICK = 3
TIMEOUT = 10


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    url = "https://target.my.com/"

    def __init__(self, driver):
        self.browser = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.browser, timeout=timeout)

    @allure.step("Searching for {locator}")
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def is_opened(self, timeout=TIMEOUT):
        current_time = time.time()
        while time.time() - current_time < timeout:
            if self.browser.current_url == self.url:
                return True

        raise PageNotLoadedException(f"{self.url} did not open in {timeout} for {self.__class__.__name__}"
                                     f"current url {self.browser.current_url}")

    @allure.step("Clicking on {locator}")
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

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def element_is_disappeared(self, locator):
        self.wait().until(EC.invisibility_of_element_located(locator))

    @allure.step("Scrolling to {element}")
    def scroll_to(self, element):
        self.browser.execute_script('arguments[0].scrollIntoView(true);', element)
