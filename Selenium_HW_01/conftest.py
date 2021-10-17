import pytest
from selenium import webdriver
from Selenium_HW_01.UI.pages.base_page import BasePage
from Selenium_HW_01.UI.pages.dashboard_page import DashboardPage
from Selenium_HW_01.UI.pages.profile_page import ProfilePage

def pytest_addoption(parser):
    parser.addoption("--url", default = "https://target.my.com/")

@pytest.fixture
def config(request):
    url = request.config.getoption("--url")

    return {"url": url}

@pytest.fixture
def driver(config):
    url = config["url"]
    driver = webdriver.Chrome(executable_path=r"D:\Mail_ru_HOMEWORKS\2021-2-QA-AUTO-PYTHON-VKGROUP-D-Kolesnik\Selenium_HW_01\driver\chromedriver")
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver=driver)