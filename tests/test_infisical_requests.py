from unittest import mock

import pytest

from infisical_sdk import InfisicalSDKClient
from infisical_sdk.infisical_requests import InfisicalRequests


def request_kwargs(api, method):
    with mock.patch.object(api.session, method) as send:
        send.return_value.headers = {}
        getattr(api, method)("/path", dict)
    return send.call_args.kwargs


@pytest.mark.parametrize("method", ["get", "post", "patch", "delete"])
def test_request_carries_default_timeout(method):
    api = InfisicalRequests(host="https://example.com")

    assert request_kwargs(api, method)["timeout"] == 30


def test_request_carries_configured_timeout():
    api = InfisicalRequests(host="https://example.com", timeout=5)

    assert request_kwargs(api, "get")["timeout"] == 5


def test_client_timeout_reaches_the_request():
    with InfisicalSDKClient(host="https://example.com", timeout=5) as client:
        assert request_kwargs(client.api, "get")["timeout"] == 5
