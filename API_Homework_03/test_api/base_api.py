import os

import pytest


base_dir = os.path.abspath(os.path.join((__file__), os.path.pardir))
temp_dir = os.path.join(base_dir, 'photoeditorsdk-export.png')


class ApiBase():
    authorize = True

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.login()

    def create_segment_base(self,name):
        return self.api_client.create_segment(name)

    def delete_segment_base(self):
        return self.api_client.delete_segment()

    def create_campaign_base(self):
        return self.api_client.create_campaign(temp_dir)

