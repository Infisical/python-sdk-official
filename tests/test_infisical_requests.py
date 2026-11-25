import pytest
import requests

from infisical_sdk.infisical_requests import APIError


def test_patch_leaves_out_none_values(api, json_response):
    api.session.patch.return_value = json_response({})
    api.patch(path="/api/v1/example", model=dict, json={"name": "edge", "description": None})
    assert api.session.patch.call_args.kwargs["json"] == {"name": "edge"}


def test_patch_sends_null_for_nullable_keys(api, json_response):
    api.session.patch.return_value = json_response({})
    api.patch(path="/api/v1/example", model=dict, json={"label": None, "description": None}, nullable_keys=["label"])
    assert api.session.patch.call_args.kwargs["json"] == {"label": None}


def test_patch_keeps_false_zero_and_empty_string(api, json_response):
    api.session.patch.return_value = json_response({})
    api.patch(path="/api/v1/example", model=dict, json={"enabled": False, "count": 0, "note": ""})
    assert api.session.patch.call_args.kwargs["json"] == {"enabled": False, "count": 0, "note": ""}


def test_put_leaves_out_none_values(api, json_response):
    api.session.put.return_value = json_response({})
    api.put(path="/api/v1/example", model=dict, json={"scope": "selected", "groupIds": None})
    assert api.session.put.call_args.kwargs["json"] == {"scope": "selected"}


def test_put_retries_a_read_timeout(api, json_response):
    api.session.put.side_effect = [requests.exceptions.ReadTimeout(), json_response({"ok": True})]
    assert api.put(path="/api/v1/example", model=dict).data == {"ok": True}
    assert api.session.put.call_count == 2


def test_post_retries_a_read_timeout(api, json_response):
    api.session.post.side_effect = [requests.exceptions.ReadTimeout(), json_response({"ok": True})]
    assert api.post(path="/api/v1/example", model=dict).data == {"ok": True}
    assert api.session.post.call_count == 2


def test_post_once_retries_when_the_connection_never_opened(api, json_response):
    api.session.post.side_effect = [requests.exceptions.ConnectTimeout(), json_response({"ok": True})]
    assert api.post_once(path="/api/v1/example", model=dict).data == {"ok": True}
    assert api.session.post.call_count == 2


@pytest.mark.parametrize("error", [
    requests.exceptions.ReadTimeout,
    requests.exceptions.ConnectionError,
    requests.exceptions.ChunkedEncodingError,
])
def test_post_once_does_not_retry_once_the_request_may_have_reached_the_server(api, error):
    api.session.post.side_effect = error()
    with pytest.raises(error):
        api.post_once(path="/api/v1/example", model=dict)
    assert api.session.post.call_count == 1


@pytest.mark.parametrize("status", [502, 503, 504])
def test_get_retries_a_gateway_error(api, json_response, status):
    api.session.get.side_effect = [json_response({"message": "unavailable"}, status), json_response({"ok": True})]
    assert api.get(path="/api/v3/secrets/raw", model=dict).data == {"ok": True}
    assert api.session.get.call_count == 2


def test_get_raises_the_503_once_every_retry_got_one(api, json_response):
    api.session.get.side_effect = lambda *args, **kwargs: json_response({"message": "unavailable"}, 503)
    with pytest.raises(APIError) as error:
        api.get(path="/api/v3/secrets/raw", model=dict)
    assert error.value.status_code == 503
    # 1 initial + 4 retries
    assert api.session.get.call_count == 5


@pytest.mark.parametrize("status", [400, 401, 403, 404, 429, 500])
def test_get_does_not_retry_other_error_statuses(api, json_response, status):
    api.session.get.return_value = json_response({"message": "no"}, status)
    with pytest.raises(APIError):
        api.get(path="/api/v3/secrets/raw", model=dict)
    assert api.session.get.call_count == 1


def test_post_does_not_retry_a_503_since_the_server_may_have_acted_on_it(api, json_response):
    api.session.post.return_value = json_response({"message": "unavailable"}, 503)
    with pytest.raises(APIError):
        api.post(path="/api/v1/example", model=dict)
    assert api.session.post.call_count == 1
