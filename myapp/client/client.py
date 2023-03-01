import datetime
import json

import requests

from myapp.settings import CLIENT_ID, CLIENT_SECRET, TEACHBASE_URL


class TeachbaseClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = None
        self.token_expired_in = 0

    def get_token(self):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(f'{self.base_url}/oauth/token', params)

        if response.status_code != 200:
            return response.status_code

        self.access_token = json.loads(response.text)['access_token']
        time_now = datetime.datetime.timestamp(datetime.datetime.now())
        self.token_expired_in = time_now + json.loads(response.text)['expires_in']

    def check_token_is_alive(self):
        if datetime.datetime.timestamp(datetime.datetime.now()) >= self.token_expired_in:
            self.get_token()

    def get_all_courses(self):
        self.check_token_is_alive()
        params = {
            'access_token': self.access_token
        }
        response = requests.get(f'{self.base_url}/endpoint/v1/courses', params)

        if response.status_code != 200:
            return response.status_code
        return response.json()

    def get_one_course(self, course_id):
        self.check_token_is_alive()
        params = {
            'access_token': self.access_token
        }
        response = requests.get(f'{self.base_url}/endpoint/v1/courses/{course_id}', params)

        if response.status_code != 200:
            return response.status_code
        return response.json()


teachbase = TeachbaseClient(CLIENT_ID, CLIENT_SECRET, TEACHBASE_URL)
