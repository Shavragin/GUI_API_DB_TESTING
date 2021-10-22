from UI.locators.basic_locators import DashboardPageLocators
from UI.pages.base_page import BasePage
from UI.pages.Create_company_page import CreateCompanyPage


class DashboardPage(BasePage):
    url = "https://target.my.com/dashboard"

    def exit_system(self):
        self.clicking(DashboardPageLocators.ACCOUNT)
        self.find(DashboardPageLocators.EXIT)
        self.clicking(DashboardPageLocators.EXIT)

    def go_to_create_new_company(self):
        self.clicking(DashboardPageLocators.CREATE_COMPANY)
        # return CreateCompanyPage(self.browser)

