import time

import pytest

from UI.locators.basic_locators import DashboardPageLocators, CreateCompanyPageLocators, ProfileInfoLocators
from base import BaseClass



class TestMyTarget(BaseClass):


    def test_create_company(self, dashboard, temp_dir):
        create_page = dashboard.go_to_create_new_company()
        company_name_create = create_page.fill_information(temp_dir)
        create_page.create_company()
        company_name_dashboard = dashboard.find_new_company()
        assert company_name_create == company_name_dashboard

    def test_incorrect_email(self, credentials):
        self.base_page.incorrect_login(*credentials)
        assert "https://account.my.com/login" in self.browser.current_url


    def test_incorrect_password(self, credentials):
        self.base_page.incorrect_password(*credentials)
        assert "https://account.my.com/login" in self.browser.current_url

    @pytest.mark.UI
    def test_create_segments(self, dashboard):
        segments = dashboard.go_to_segments()
        segments.create_segment()
        time.sleep(5)




