import pytest
from selenium import webdriver


# dir_path = os.path.abspath(os.path.dirname(__file__))
# driver_path = os.path.join(dir_path, "driver", "chromedriver.exe")
# print(driver_path)


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path=r"D:/Mail_ru_HOMEWORKS/2021-2-QA-AUTO-PYTHON-VKGROUP-D-Kolesnik/Selenium_HW_01/driver/chromedriver")
    yield driver
    driver.close()