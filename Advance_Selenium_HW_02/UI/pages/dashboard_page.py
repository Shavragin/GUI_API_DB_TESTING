import allure

from UI.locators.basic_locators import DashboardPageLocators
from UI.pages.base_page import BasePage
from UI.pages.create_company_page import CreateCompanyPage
from UI.pages.segments_page import SegmentsPage


class DashboardPage(BasePage):
    url = "https://target.my.com/dashboard"
    locator = DashboardPageLocators()

    def go_to_create_new_company(self):
        self.clicking(DashboardPageLocators.CREATE_COMPANY)
        return CreateCompanyPage(self.browser)

    def find_new_company(self):
        company = self.find(self.locator.CREATED_COMPANY)
        return company.get_attribute("title")

    @allure.step("Going to segments")
    def go_to_segments(self):
        self.clicking(DashboardPageLocators.SEGMENTS)
        return SegmentsPage(self.browser)
