import pytest

from test_api.base_api import ApiBase


@pytest.mark.API
class TestMyTarget(ApiBase):

    def test_create_segment(self):
        response = self.create_segment_base()
        assert response.json().get('error') is None, "Segment was not created"

    def test_delete_segment(self):
        response = self.delete_segment_base()
        assert response.status_code == 204, "Segment was not deleted"

    def test_create_campaign(self, temp_dir):
        response = self.create_campaign_base()
        assert response.status_code == 200, "Campaign was not created"
        resp = self.delete_campaign_base()
        assert resp.status_code == 204,  "Campaign was not deleted"
