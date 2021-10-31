import random

import allure
from selenium.common.exceptions import TimeoutException

from UI.locators.basic_locators import SegmentPageLocators
from UI.pages.base_page import BasePage


class SegmentsPage(BasePage):
    url = "https://target.my.com/segments/segments_list"
    locators = SegmentPageLocators()

    @allure.step("Creating segment")
    def create_segment(self):
        self.add_new_segment()
        self.picking_segment_type()
        self.filling_company_name()
        self.clicking(self.locators.CREATE_SEGMENT_FINAL)

    def add_new_segment(self):
        self.logger.info("Adding new segment")
        self.logger.info("Trying to find main create button")
        try:
            self.clicking(self.locators.CREATE_SEGMENT_MAIN, timeout=1)
        except TimeoutException:
            self.logger.info(" Clicking on extra create button")
            self.clicking(self.locators.CREATE_SEGMENT_IF_EXIST)

    def filling_company_name(self):
        self.logger.info("Filling new company")
        new_company_field = self.find(self.locators.SEGMENT_NAME)
        self.company_name = f"Company{random.randint(0, 1000)}"
        new_company_field.send_keys(self.company_name)

    def picking_segment_type(self):
        self.logger.info("Picking segment type")
        self.find(self.locators.CHECKBOX).click()
        self.clicking(self.locators.ADD_SEGMENT)

    def name_created_segment(self):
        return self.find(self.locators.SEGMENT_IN_TABLE).get_attribute("title")

    @allure.step("Deleting segment")
    def delete_segment(self):
        self.logger.info("Deleting segment")
        self.clicking(self.locators.REMOVE_CELL)
        self.clicking(self.locators.CONFIRM_DELETE)

    @allure.step("Deleting segment via checkbox")
    def delete_segment_checkbox(self):
        self.logger.info("Deleting segment via checkbox")
        self.clicking(self.locators.CHECKBOX_SEGMENTS)
        self.clicking(self.locators.ACTION_BUTTON)
        self.clicking(self.locators.DELETE_ACTION)

    def segment_on_page(self):
        element = self.find(self.locators.SEGMENT_IN_TABLE)
        if element is None:
            return False
        return True
