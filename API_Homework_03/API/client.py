import json
import os
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict

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

        response = self.session.request('POST', self.login_url, headers=headers, data=payload,
                                        allow_redirects=True)

        response_cookies = response.history[0]
        set_cookie = response_cookies.headers.get('Set-Cookie').split(';')
        csrf_cookie = self.session.get(f'{self.target_url}csrf', headers=headers, allow_redirects=True).headers.get(
            'set-cookie').split(";")
        self.csrf_token = [c for c in csrf_cookie if 'csrf' in c][0].split('=')[-1]
        self.mc_cookie = [m for m in set_cookie if 'mc' in m][0].split('=')[-1]
        self.ssdc_cookie = [s for s in set_cookie if 'sdc' in s][0].split(',')[1].split('=')[-1]
        self.session.cookies = cookiejar_from_dict({
            'mc': self.mc_cookie,
            'ssdc': self.ssdc_cookie,
            'csrftoken': self.csrf_token
        })

        return self.session.get(self.target_url, headers=headers, allow_redirects=True)

    def create_segment(self, segment_name):
        location = 'api/v2/remarketing/segments.json?fields=name,pass_condition,created,id'

        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token

        data = json.dumps(data_create_segment(segment_name))

        return self.session.post(urljoin(self.target_url, location), headers=headers, data=data)

    def delete_first_segment(self):
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        try:
            id = self.get_first_segment()
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
        self.campaign_id = response_create_campaign.json().get('id')
        return response_create_campaign

    def get_created_campaign(self):
        location = f'api/v2/campaigns/{self.campaign_id}.json'
        headers = self.post_headers_target()
        return self.session.request('GET', urljoin(self.target_url, location), headers=headers)


    def delete_campaign(self):
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        location = f'/api/v2/campaigns/{self.campaign_id}.json'
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
        location = 'https://target.my.com/api/v2/remarketing/segments.json?fields=id'
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        return self.session.request('GET', urljoin(self.target_url, location), headers=headers)

    def make_campaign_url(self):
        headers = self.post_headers_target()
        return self.session.request('GET', urljoin(self.target_url, "api/v1/urls/?url=https.github.com"),
                                    headers=headers).json()['id']
