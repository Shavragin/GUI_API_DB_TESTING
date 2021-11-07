import json
import os
from urllib.parse import urljoin

import requests
from requests.cookies import cookiejar_from_dict


class CookieDoNotSetException(Exception):
    pass


base_dir = os.path.abspath(os.path.join((__file__), os.path.pardir))
temp_dir = os.path.join(base_dir, 'photoeditorsdk-export.png')


class ApiClient:

    def __init__(self, url, username, password):
        self.url = url
        self.session = requests.Session()
        self.username = username
        self.password = password
        self.target_url = 'https://target.my.com/'

        self.mc_cookie = None
        self.ssdc_cookie = None
        self.csrf_token = None

    def post_headers_auth(self):
        return {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /'
                              'Chrome/93.0.4577.82 YaBrowser/21.9.2.169 Yowser/2.5 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://account.my.com/'
                }

    def post_headers_target(self):
        return {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /'
                              'Chrome/93.0.4577.82 YaBrowser/21.9.2.169 Yowser/2.5 Safari/537.36',
                # 'Content-Type': 'application/json',
                'Host': 'target.my.com'
                }

    def login(self):
        headers = self.post_headers_auth()

        payload = {
            'email': self.username,
            'password': self.password,
            'continue': 'https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com%2Fprofile%2Fuserinfo%2F',
            'nosavelogin': 0
        }

        response = self.session.request('POST', self.url, headers=headers, data=payload,
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

        data = json.dumps({
            'name': f'{segment_name}',
            'pass_condition': 1,
            'logicType': 'or',
            "relations": [{"object_type": "remarketing_player",
                           "params": {"type": "positive", "left": 365, "right": 0}}],
        })

        response = self.session.post(urljoin(self.target_url, location), headers=headers, data=data)
        return response

    def delete_segment(self, segment_name):
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        response = self.create_segment(segment_name)
        id = response.json().get('id')
        location = f'api/v2/remarketing/segments/{id}.json'

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

    def create_campaign(self, name: str, temp_dir):
        location = '/api/v2/campaigns.json'
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token

        id = self.post_image(temp_dir)

        campaign_objective = self.session.request('GET', urljoin(self.target_url,
                                                                 '/api/v2/campaign_objective/reach/urls.json?_=1636300089249'),
                                                  headers=headers)

        primary_id = campaign_objective.json().get('items')[0].get('id')

        data = {
            "name": name,
            "read_only": False,
            "conversion_funnel_id": None,
            "objective": "reach",
            "targetings": {"split_audience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "sex": ["male", "female"],
                           "age": {
                               "age_list": [0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                                            30, 31, 32, 33,
                                            34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                                            53, 54, 55,
                                            56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                                            75]}},
            "autobidding_mode": "max_shows",
            "uniq_shows_period": "day",
            "budget_limit_day": "100",
            "budget_limit": "100",
            "mixing": "recommended",
            "enable_utm": True,
            "price": "21",
            "max_price": "0",
            "package_id": 960,
            "banners": [
                {"urls": {"primary": {"id": f'{primary_id}'}}, "textblocks": {},
                 "content": {"image_240x400": {"id": f'{id}'}},
                 "name": ""}]
        }

        response_create = self.session.request('POST', urljoin(self.target_url, location), headers=headers, json=data)
        self.id_campaign = response_create.json().get('id')
        return response_create

    def delete_campaign(self):
        location = f'/api/v2/campaigns/{self.id_campaign}.json'
        headers = self.post_headers_target()
        headers['X-CSRFToken'] = self.csrf_token
        return self.session.request('DELETE', urljoin(self.target_url, location), headers=headers)
