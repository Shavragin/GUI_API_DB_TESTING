import pytest
from Selenium_HW_01.utils import BaseClass
from Selenium_HW_01.UI.locators import MainPageLocators

@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self):
        self.login()
        self.wait(MainPageLocators.TITLE, 5)
        title = self.find(MainPageLocators.TITLE)
        assert "С чего начать" in title.text




