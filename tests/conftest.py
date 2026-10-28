import json
from unittest import mock

import pytest
import requests

from infisical_sdk.infisical_requests import InfisicalRequests


@pytest.fixture(autouse=True)
def no_retry_delay():
    with mock.patch("infisical_sdk.infisical_requests.time.sleep"):
        yield


@pytest.fixture
def api():
    api = InfisicalRequests(host="https://infisical.example.com", token="token")
    api.session = mock.Mock()
    return api


@pytest.fixture
def json_response():
    def make(payload):
        response = requests.Response()
        response.status_code = 200
        response._content = json.dumps(payload).encode()
        return response
    return make
