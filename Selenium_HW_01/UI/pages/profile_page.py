from Selenium_HW_01.UI.pages.base_page import BasePage
import random

class ProfilePage(BasePage):

    def send_info(self, locator, info="TestUser"):
        field = self.find(locator)
        field.clear()
        field.send_keys(info + str(random.randint(0, 100)))