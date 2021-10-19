from Selenium_HW_01.UI.locators.basic_locators import DashboardPageLocators
from Selenium_HW_01.UI.pages.base_page import BasePage


class DashboardPage(BasePage):

    def exit_system(self):
        self.clicking(DashboardPageLocators.ACCOUNT)
        self.find(DashboardPageLocators.EXIT)
        self.clicking(DashboardPageLocators.EXIT)
