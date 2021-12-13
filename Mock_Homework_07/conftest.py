import logging
import os
import shutil
import sys

import allure
import pytest
import requests

import settings
from client.client_mock import SocketClient


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = "C://test"
    else:
        base_dir = "/tmp/test"

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_dir = base_dir

    from mock import mock_server
    mock_server.run_mock()


@pytest.fixture(scope="session")
def temp_dir(request):
    test_dir = os.path.abspath(os.path.join(request.config.base_dir,
                                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture
def logger(temp_dir):
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


def pytest_unconfigure():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


@pytest.fixture(scope="session")
def socket_client():
    return SocketClient()
