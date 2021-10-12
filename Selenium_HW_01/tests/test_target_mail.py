import pytest
from selenium import webdriver
from Selenium_HW_01.utils import BaseClass


@pytest.mark.UI
# class TestMyTarget(BaseClass):

def test1(browser):
    browser.get("https://target.my.com/")



