import pytest
from Selenium_HW_01.base import BaseClass
from Selenium_HW_01.UI.locators.basic_locators import MainPageLocators

@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_login(self):
        self.base_page.login()
        self.base_page.wait(MainPageLocators.TITLE)
        title = self.base_page.find(MainPageLocators.TITLE)
        assert "С чего начать" in title.text




