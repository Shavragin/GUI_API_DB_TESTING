import pytest

from test_api.base_api import ApiBase
from utils.builder import create_name


# @pytest.mark.API
class TestMyTarget(ApiBase):
    @pytest.mark.API
    def test_create_segment(self):
        name = create_name()
        response = self.create_segment_base(name)
        print(response.json())
        assert response.json().get('name') == name, "Segment was not created"

    def test_delete_segment(self):

        response = self.delete_segment_base()
        assert response.status_code == 204, "Segment was not deleted"

    def test_create_campaign(self):
        response = self.create_campaign_base()
        assert response.status_code == 200, "Campaign was not created"
        self.api_client.delete_campaign()
