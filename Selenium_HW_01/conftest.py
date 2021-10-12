import pytest
from selenium import webdriver
import sys, os

path = os.path.abspath("...")
path2 = sys.path.append(os.path.join(sys.path[0], "/driver"))
print(path)


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path="D:/source/Mail_ru/2021-2-QA-AUTO-PYTHON-VKGROUP-D-Kolesnik/Selenium_HW_01/driver/chromedriver")
    yield driver
    driver.close()