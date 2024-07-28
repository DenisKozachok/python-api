import json
import os

import allure
import requests

from src.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self._base_url = os.environ['BASE_URL']

    @allure.step("POST request to {url}")
    def _post(self, url, body):
        return requests.post("{}{}".format(self._base_url, url), data=json.dumps(body),
                             headers={'content-type': 'application/json'})

    @allure.step("GET request to {url}")
    def _get(self, url):
        return requests.get("{}{}".format(self._base_url, url),
                             headers={'content-type': 'application/json'})

    @allure.step("GET request to {url}/{id}")
    def _get_by_id(self, url, id):
        return requests.get("{}{}/{}".format(self._base_url, url, id),
                             headers={'content-type': 'application/json'})

class UserApiService(ApiService):

    def __init__(self):
        super().__init__()

    @allure.step("Create user with params: {user}")
    def create_user(self, user):
        return AssertableResponse(self._post("/users", user))

    @allure.step("Get users")
    def get_users(self):
        return AssertableResponse(self._get("/users"))

    @allure.step("Get user by {id}")
    def get_user_by_id(self, id):
        return AssertableResponse(self._get_by_id("/users", id))
