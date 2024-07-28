import logging

class AssertableResponse(object):

    def __init__(self, response):
        logging.info(f"Request: url: {response.url}, method: {response.request.method}, body: {response.request.body}")
        logging.info(f"Response: status_code: {response.status_code}, body: {response.text}")
        self._response = response

    def status_code(self, code):
        logging.info(f"Expected status code: {code}, got: {self._response.status_code}")
        return self._response.status_code == code

    def field(self, name):
        logging.info(f"Expected field: {name}, got: {self._response.json()[name]}")
        return self._response.json()[name]