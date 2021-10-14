import pytest
from Selenium_HW_01.base import BaseClass
from Selenium_HW_01.UI.locators.basic_locators import MainPageLocators

@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self):
        self.login()
        self.wait(MainPageLocators.TITLE)
        title = self.find(MainPageLocators.TITLE)
        assert "С чего начать" in title.text




