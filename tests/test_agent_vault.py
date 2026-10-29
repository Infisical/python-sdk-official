import pytest
import requests

from infisical_sdk.resources.agent_vault import AgentVault

PROXY = {"id": "a2b5e0d1-6f3e-4c55-9a43-3f0c1f0a2b7e", "name": "edge-proxy"}
SESSION = {
    "id": "6f1c2a9e-3b7d-4e8a-9c41-2d5f7b8e0a13",
    "label": None,
    "status": "active",
    "createdAt": "2026-10-27T00:00:00.000Z",
    "accessBundles": [],
}


@pytest.fixture
def agent_vault(api):
    return AgentVault(api)


def test_proxies_update_sends_null_to_clear_allowed_hosts(api, agent_vault, json_response):
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.update(PROXY["id"], clear_allowed_hosts=True)
    assert api.session.patch.call_args.kwargs["json"] == {"allowedHosts": None}


def test_proxies_update_leaves_out_values_you_do_not_pass(api, agent_vault, json_response):
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.update(PROXY["id"], name="edge-proxy")
    assert api.session.patch.call_args.kwargs["json"] == {"name": "edge-proxy"}


def test_proxies_update_rejects_allowed_hosts_with_clear_allowed_hosts(api, agent_vault):
    with pytest.raises(ValueError):
        agent_vault.proxies.update(PROXY["id"], allowed_hosts=["pypi.org"], clear_allowed_hosts=True)
    api.session.patch.assert_not_called()


@pytest.mark.parametrize("label", ["nightly deploy", None])
def test_sessions_update_always_sends_the_label(api, agent_vault, json_response, label):
    api.session.patch.return_value = json_response({"session": dict(SESSION, label=label)})
    assert agent_vault.sessions.update(SESSION["id"], label).label == label
    assert api.session.patch.call_args.kwargs["json"] == {"label": label}


@pytest.mark.parametrize("create", [
    lambda agent_vault: agent_vault.sessions.create(access_bundle="release"),
    lambda agent_vault: agent_vault.proxies.create(name="edge-proxy"),
], ids=["sessions.create", "proxies.create"])
def test_creates_are_not_retried_once_the_request_may_have_reached_the_server(api, agent_vault, create):
    api.session.post.side_effect = requests.exceptions.ReadTimeout()
    with pytest.raises(requests.exceptions.ReadTimeout):
        create(agent_vault)
    assert api.session.post.call_count == 1


def test_proxies_create_leaves_out_an_empty_allowed_hosts_list(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"proxy": PROXY, "proxyToken": "token"})
    agent_vault.proxies.create(name="edge-proxy", allowed_hosts=[])
    assert "allowedHosts" not in api.session.post.call_args.kwargs["json"]


def test_proxies_update_rejects_an_empty_allowed_hosts_list(api, agent_vault):
    with pytest.raises(ValueError, match="clear_allowed_hosts"):
        agent_vault.proxies.update(PROXY["id"], allowed_hosts=[])
    api.session.patch.assert_not_called()


def test_proxies_rotate_token_is_not_retried_once_the_request_may_have_reached_the_server(api, agent_vault):
    api.session.post.side_effect = requests.exceptions.ReadTimeout()
    with pytest.raises(requests.exceptions.ReadTimeout):
        agent_vault.proxies.rotate_token(PROXY["id"])
    assert api.session.post.call_count == 1


def test_sessions_revoke_leaves_access_bundles_unset_when_the_response_omits_them(api, agent_vault, json_response):
    revoked = {key: value for key, value in SESSION.items() if key != "accessBundles"}
    api.session.post.return_value = json_response({"session": dict(revoked, status="revoked")})
    assert agent_vault.sessions.revoke(SESSION["id"]).accessBundles is None


def test_sessions_get_keeps_an_empty_access_bundles_list(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"session": SESSION})
    assert agent_vault.sessions.get(SESSION["id"]).accessBundles == []
