import random

from Selenium_HW_01.UI.pages.base_page import BasePage


class ProfilePage(BasePage):

    def send_info(self, locator, info="TestUser"):
        field = self.find(locator)
        field.clear()
        self.name = info + str(random.randint(0, 100))
        field.send_keys(self.name)
