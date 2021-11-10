import logging
import os
import shutil
import sys

import allure
import pytest

from API.client import ApiClient

dir_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
credential = os.path.join(dir_path, "test_api/credentials", "credentials.txt")


def pytest_addoption(parser):
    parser.addoption("--url", default="https://auth-ac.my.com/auth")


@pytest.fixture(scope="session")
def config(request):
    url = request.config.getoption("--url")

    return {"url": url}


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


@pytest.fixture(scope="session")
def credentials():
    with open(credential) as c:
        user = c.readline().strip()
        password = c.readline().strip()
    return user, password


@pytest.fixture
def logger(temp_dir, config):
    log_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    log_file = os.path.join(temp_dir, "test.log")
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, "w")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, "r") as f:
        allure.attach(f.read(), "test.log", attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope="session")
def api_client(config, credentials):
    return ApiClient(config['url'], *credentials)
