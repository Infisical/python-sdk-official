from unittest import mock

import pytest
import requests

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


def send_attempts(api, method, error):
    with mock.patch.object(api.session, method, side_effect=error) as send:
        with mock.patch("infisical_sdk.infisical_requests.time.sleep"):
            with pytest.raises(type(error)):
                getattr(api, method)("/path", dict)
    return send.call_count


@pytest.mark.parametrize("method", ["post", "patch", "delete"])
def test_read_timeout_is_not_replayed_on_writes(method):
    api = InfisicalRequests(host="https://example.com")

    assert send_attempts(api, method, requests.exceptions.ReadTimeout()) == 1


def test_read_timeout_is_retried_on_reads():
    api = InfisicalRequests(host="https://example.com")

    assert send_attempts(api, "get", requests.exceptions.ReadTimeout()) > 1


@pytest.mark.parametrize("method", ["post", "patch", "delete"])
def test_connect_timeout_is_still_retried_on_writes(method):
    api = InfisicalRequests(host="https://example.com")

    assert send_attempts(api, method, requests.exceptions.ConnectTimeout()) > 1
