import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path=r"D:\source\Mail_ru\2021-2-QA-AUTO-PYTHON-VKGROUP-D-Kolesnik\Selenium_HW_01\driver\chromedriver")
    driver.maximize_window()
    yield driver
    driver.close()