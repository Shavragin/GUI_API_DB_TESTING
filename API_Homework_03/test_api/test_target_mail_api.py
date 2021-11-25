import pytest

from test_api.base_api import ApiBase
from utils.builder import create_name


@pytest.mark.API
class TestMyTarget(ApiBase):

    def test_create_segment(self):
        name = create_name()
        response = self.api_client.create_segment(name)
        assert response.json().get('name') == name, "Segment was not created"

    def test_delete_segment(self):
        name = create_name()
        id = self.api_client.create_segment(name).json()['id']
        self.api_client.delete_segment(id)
        segments_list = self.api_client.get_segments_list().json()['items']

        assert self.api_client.check_segments(id, segments_list) is False, "Segment was not deleted"

    def test_create_campaign(self):
        name = create_name()
        create_id = self.api_client.create_campaign(name).json().get('id')
        get_id = self.api_client.get_created_campaign(create_id).json().get('id')
        assert create_id == get_id, "Campaign was not created"
        self.api_client.delete_campaign(id=create_id)
