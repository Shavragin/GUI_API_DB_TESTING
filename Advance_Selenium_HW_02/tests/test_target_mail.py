import pytest
from assertpy import soft_assertions, assert_that

from base import BaseClass


@pytest.mark.UI
class TestMyTarget(BaseClass):

    def test_create_campaign(self, dashboard, temp_dir):
        create_page = dashboard.go_to_create_new_campaign()
        create_page.fill_information(temp_dir)
        create_page.create_campaign()
        campaign_name_dashboard = dashboard.find_new_campaign()
        assert create_page.campaign == campaign_name_dashboard, "Campaign have not created"

    def test_create_segments(self, dashboard):
        segments = dashboard.go_to_segments()
        segments.create_segment()
        created = segments.name_created_segment()
        with soft_assertions():
            assert_that(created).contains(segments.campaign_name)
            segments.delete_segment_checkbox()

    def test_delete_segment(self, dashboard):
        segments = dashboard.go_to_segments()
        segments.create_segment()
        segments.delete_segment()
        assert segments.is_element_present(segments.locators.SEGMENT_IN_TABLE), "Segment did not deleted"

    def test_incorrect_email(self, credentials):
        self.login_page.incorrect_login_name(*credentials)
        assert "https://account.my.com/login" in self.browser.current_url, "Account logged in with incorrect email"

    def test_incorrect_password(self, credentials):
        self.login_page.incorrect_password(*credentials)
        assert "https://account.my.com/login" in self.browser.current_url, "Account logged in with incorrect password"
