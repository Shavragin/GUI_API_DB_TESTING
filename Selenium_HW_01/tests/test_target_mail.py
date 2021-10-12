import pytest
from selenium import webdriver
from Selenium_HW_01.utils import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium_HW_01.UI.locators import LoginPageLocators
import time


@pytest.mark.UI
# class TestMyTarget(BaseClass):

def test1(browser):
    browser.get("https://target.my.com/")
    button = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((LoginPageLocators.ENTER_BUTTON))
    )
    button.click()
    email_field = browser.find_element(*LoginPageLocators.EMAIL_FIELD)
    email_field.send_keys("Privet")
    time.sleep(10)




