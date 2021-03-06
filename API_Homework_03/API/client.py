import json
import os
from urllib.parse import urljoin

import requests

from utils.data import data_create_campaign, data_create_segment


class EmptySegmentListException(Exception):
    pass


base_dir = os.path.abspath(os.path.join((__file__), "../.."))
temp_dir = os.path.join(base_dir, 'test_api', 'photoeditorsdk-export.png')


class ApiClient:

    def __init__(self, url, username, password):
        self.login_url = url
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.target_url = 'https://target.my.com/'
        self.csrf_token = None

    def post_headers_auth(self):
        return {
            'Referer': 'https://account.my.com/'
        }

    def post_headers_target(self):
        return {
            'Host': 'target.my.com'
        }

    def login(self):
        headers = self.post_headers_auth()

        payload = {
            'email': self.username,
            'password': self.password,
            'continue': 'https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F',
        }

        self.session.request('POST', self.login_url, headers=headers, data=payload,
                             allow_redirects=True)

        return self.session.get(self.target_url, headers=headers, allow_redirects=True)

    def get_csrf_token(self):
        headers = self.post_headers_auth()
        self.session.request('GET', f'{self.target_url}csrf', headers=headers, allow_redirects=True)
        self.csrf_token = self.session.cookies.get('csrftoken')

    def create_segment(self, segment_name):
        location = 'api/v2/remarketing/segments.json?fields=name,pass_condition,created,id'

        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token

        data = json.dumps(data_create_segment(segment_name))

        return self.session.post(urljoin(self.target_url, location), headers=headers, data=data)

    def delete_segment(self, id):
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        try:
            # id = self.get_first_segment()
            location = f'api/v2/remarketing/segments/{id}.json'
        except EmptySegmentListException as e:
            print(e)
        else:
            return self.session.delete(urljoin(self.target_url, location), headers=headers)

    def post_image(self, dir):
        location_content = 'api/v2/content/static.json'
        location_media = 'api/v2/mediateka.json'

        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token

        with open(dir, 'rb') as d:
            file = {'file': d,
                    'data': '{"width": 240, "height": 400}',
                    }

            upload = self.session.request('POST', urljoin(self.target_url, location_content), headers=headers,
                                          files=file)
        id = upload.json().get('id')

        data = json.dumps({
            'description': 'photoeditorsdk-export.png',
            'content': {'id': f'{id}'}
        })

        self.session.request('POST', urljoin(self.target_url, location_media), headers=headers, data=data)

        return id

    def create_campaign(self, name: str):
        location = '/api/v2/campaigns.json'
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token

        id = self.post_image(temp_dir)

        primary_id = self.make_campaign_url()

        data = data_create_campaign(name, primary_id, id)

        response_create_campaign = self.session.request('POST', urljoin(self.target_url, location), headers=headers,
                                                        json=data)
        return response_create_campaign

    def get_created_campaign(self, id):
        location = f'api/v2/campaigns/{id}.json'
        headers = self.post_headers_target()
        return self.session.request('GET', urljoin(self.target_url, location), headers=headers)

    def get_active_campaigns(self):
        location = f'api/v2/campaigns.json?fields=id&_status__in=active'
        headers = self.post_headers_target()
        return self.session.request('GET', urljoin(self.target_url, location), headers=headers).json().get('items')

    def delete_campaign(self, id=None):
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        if id is None:
            try:
                finded_id = self.get_active_campaigns()[0].get('id')
            except IndexError:
                raise EmptySegmentListException('There are not active campaigns')

            location = f'/api/v2/campaigns/{finded_id}.json'
            return self.session.request('DELETE', urljoin(self.target_url, location), headers=headers)
        else:
            location = f'/api/v2/campaigns/{id}.json'
            return self.session.request('DELETE', urljoin(self.target_url, location), headers=headers)

    def get_first_segment(self):
        response = self.get_segments_list()
        try:
            id = response.json().get('items')[0]['id']
        except IndexError:
            raise EmptySegmentListException('There are not segments')
        else:
            return id

    def get_segments_list(self):
        location = 'api/v2/remarketing/segments.json?fields=id&limit=500'
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        return self.session.request('GET', urljoin(self.target_url, location), headers=headers)

    def make_campaign_url(self):
        headers = self.post_headers_target()
        return self.session.request('GET', urljoin(self.target_url, "api/v1/urls/?url=https.github.com"),
                                    headers=headers).json()['id']

    def check_segments(self, segment_id, segment_list):
        if any(item.get('id') == segment_id for item in segment_list):
            return True
        return False
