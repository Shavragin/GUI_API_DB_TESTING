import pytest
from selenium import webdriver
from Selenium_HW_01.UI.pages.base_page import BasePage

# @pytest.fixture
# def base_page(driver):
#     return BasePage(driver=driver)

# @pytest.fixture
# def driver(config):
#     url = config["url"]
#     driver = webdriver.Chrome(executable_path=r"D:\source\Mail_ru\2021-2-QA-AUTO-PYTHON-VKGROUP-D-Kolesnik\Selenium_HW_01\driver\chromedriver")
#     driver.maximize_window()
#     driver.get(url)
#     yield driver
#     driver.close()