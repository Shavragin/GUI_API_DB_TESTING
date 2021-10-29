from UI.pages.base_page import BasePage
from UI.locators.basic_locators import SegmentPageLocators

class SegmentsPage(BasePage):
    url = "https://target.my.com/segments/segments_list"
    locators = SegmentPageLocators()

    def create_segment(self):
        self.clicking(self.locators.CREATE_SEGMENT_MAIN)
        self.find(self.locators.CHECKBOX).click()
        self.clicking(self.locators.ADD_SEGMENT)
        self.clicking(self.locators.CREATE_SEGMENT_FINAL)