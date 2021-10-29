import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from UI.pages.base_page import BasePage
from UI.pages.dashboard_page import DashboardPage
from UI.pages.profile_page import ProfilePage
import sys, os, shutil

dir_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
credential= os.path.join(dir_path, "UI", "credentials", "credentials.txt")

def pytest_addoption(parser):
    parser.addoption("--url", default="https://target.my.com/")
    parser.addoption("--browser", default="chrome")
    # parser.addoption("selenoid", action="store_true")


@pytest.fixture
def config(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    # selenide = request.config.getoption("--selenide")

    return {"url": url, "browser": browser}


@pytest.fixture
def driver(config, temp_dir):
    url = config["url"]
    driver = get_driver(config, download_dir=temp_dir)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


def get_driver(config, download_dir=None):
    browser_name = config["browser"]

    if browser_name == "chrome":
        options = Options()
        if download_dir is not None:
            options.add_experimental_option("prefs", {"download.default_directory": download_dir})

        manager = ChromeDriverManager(version="latest")
        browser = webdriver.Chrome(executable_path=manager.install(), options=options)
        return browser


    elif browser_name == "firefox":
        manager = GeckoDriverManager(version="latest")
        browser = webdriver.Firefox(executable_path=manager.install())


    else:
        raise RuntimeError(f"{browser_name} is not supported")

    return browser

def pytest_configure(config):
    if sys.platform.startswith("win"):
        base_path = "C://test"
    else:
        base_path = "/tmp/test"

    if not hasattr(config, "workerinput"):
        if os.path.exists(base_path):
            shutil.rmtree(base_path)

        os.makedirs(base_path)

    config.base_temp_dir = base_path


@pytest.fixture
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir,
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))

    os.makedirs(test_dir)
    return test_dir

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver=driver)


@pytest.fixture
def dashboard(driver, credentials):
    base_page = BasePage(driver)
    base_page.login(*credentials)
    return DashboardPage(driver)


@pytest.fixture(scope="session")
def credentials():
    with open(credential) as c:
        user = c.readline().strip()
        password = c.readline().strip()
    return user, password