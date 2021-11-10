import pytest

from test_api.base_api import ApiBase
from utils.builder import create_name


@pytest.mark.API
class TestMyTarget(ApiBase):

    def test_create_segment(self):
        name = create_name()
        response = self.create_segment_base(name)
        assert response.json().get('name') == name, "Segment was not created"

    def test_delete_segment(self):
        name = create_name()
        segments_before = len(self.get_segment_list_base().json().get('items'))
        self.create_segment_base(name)
        self.delete_first_segment_base()
        segments_after = len(self.get_segment_list_base().json().get('items'))
        assert segments_before == segments_after, "Segment was not deleted"

    def test_create_campaign(self):
        name = create_name()
        create_id = self.create_campaign_base(name).json().get('id')
        get_id = self.get_created_campaign_base().json().get('id')
        assert create_id == get_id, "Campaign was not created"
        self.api_client.delete_campaign()
