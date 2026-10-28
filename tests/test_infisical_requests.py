import pytest
import requests


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
