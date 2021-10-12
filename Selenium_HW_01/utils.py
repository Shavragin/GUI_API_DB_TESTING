import pytest
from selenium import webdriver

class BaseClass():
    browser = None

    def setup(self, browser):
        self.browser = browser