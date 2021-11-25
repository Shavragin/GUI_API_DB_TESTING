import allure

from UI.locators.basic_locators import DashboardPageLocators
from UI.pages.base_page import BasePage
from UI.pages.create_campaign_page import CreateCampaignPage
from UI.pages.segments_page import SegmentsPage


class DashboardPage(BasePage):
    url = "https://target.my.com/dashboard"
    locator = DashboardPageLocators()

    def go_to_create_new_campaign(self):
        self.clicking(DashboardPageLocators.CREATE_CAMPAIGN)
        return CreateCampaignPage(self.browser)

    def find_new_campaign(self):
        campaign = self.find(self.locator.CREATED_CAMPAIGN)
        return campaign.get_attribute("title")

    @allure.step("Going to segments")
    def go_to_segments(self):
        self.clicking(DashboardPageLocators.SEGMENTS)
        return SegmentsPage(self.browser)
