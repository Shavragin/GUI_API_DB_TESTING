import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.login()

    def create_segment_base(self, name):
        return self.api_client.create_segment(name)

    def delete_first_segment_base(self):
        return self.api_client.delete_first_segment()

    def create_campaign_base(self, name):
        return self.api_client.create_campaign(name)

    def get_segment_base(self):
        return self.api_client.get_first_segment()

    def get_segment_list_base(self):
        return self.api_client.get_segments_list()

    def get_created_campaign_base(self):
        return self.api_client.get_created_campaign()
