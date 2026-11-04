import pytest
import requests

from infisical_sdk.api_types import (
    AgentVaultDelegationScope,
    AgentVaultInlineService,
    AgentVaultMemberType,
    AgentVaultSessionActor,
    AgentVaultTrafficPolicy,
)
from infisical_sdk.infisical_requests import APIError
from infisical_sdk.resources.agent_vault import AgentVault

PROXY = {"id": "a2b5e0d1-6f3e-4c55-9a43-3f0c1f0a2b7e", "name": "edge-proxy"}
SESSION = {
    "id": "6f1c2a9e-3b7d-4e8a-9c41-2d5f7b8e0a13",
    "label": None,
    "status": "active",
    "createdAt": "2026-10-27T00:00:00.000Z",
    "accessBundles": [],
    "services": [],
}
ON_BEHALF_OF = {
    "type": "user",
    "id": "0d9a7c3e-5b1f-4e2a-8c6d-7f4b2e1a9c50",
    "username": "jsmith@example.com",
    "email": "jsmith@example.com",
    "firstName": "Jane",
    "lastName": "Smith",
}
BUNDLE = {
    "id": "5e2d8c1a-7b3f-4a9e-8d6c-1f0b2a3c4d5e",
    "name": "release",
    "description": None,
    "createdAt": "2026-10-27T00:00:00.000Z",
    "updatedAt": "2026-10-27T00:00:00.000Z",
}
INLINE_SERVICE_INPUT = {
    "type": "http",
    "name": "github",
    "hostPattern": "api.github.com",
    "allowedMethods": ["GET"],
    "credential": {"type": "bearer", "value": "github-token"},
    "customHeaders": [{"name": "X-Team", "value": "platform"}],
}
INLINE_SERVICE = {
    "id": "8e2f4a6c-1b3d-4e5f-9a7b-2c4d6e8f0a1b",
    "name": "github",
    "type": "http",
    "serverUrl": None,
    "transport": None,
    "hostPattern": "api.github.com",
    "allowedMethods": ["GET"],
    "allowedPathPrefixes": None,
    "credential": {"type": "bearer", "headerName": "Authorization", "headerPrefix": "Bearer"},
    "customHeaders": [{"name": "X-Team", "prefix": ""}],
    "substitutions": [],
}
MACHINE_IDENTITY_ID = "9c4b2a1d-3e5f-4a6b-8c7d-2e1f0a9b8c7d"
GROUP_ID = "7b1e4f2a-9c3d-4a6b-8e5f-1d2c3b4a5e6f"
SERVICE_ID = "3a5c7e9b-2d4f-4a6c-8e1b-5d7f9a2c4e6b"
DELEGATION = {
    "machineIdentity": {"id": MACHINE_IDENTITY_ID, "name": "slack-bot"},
    "scope": "selected",
    "users": [
        dict({key: ON_BEHALF_OF[key] for key in ("id", "username", "email", "firstName", "lastName")},
             addedAt="2026-10-27T00:00:00.000Z", missingAccessBundles=[{"id": BUNDLE["id"], "name": "release"}]),
    ],
    "groups": [{"id": GROUP_ID, "name": "Engineering", "addedAt": "2026-10-27T00:00:00.000Z", "missingAccessBundles": []}],
    "createdAt": "2026-10-27T00:00:00.000Z",
    "updatedAt": "2026-10-27T00:00:00.000Z",
    "missingAccessBundles": [{"id": BUNDLE["id"], "name": "release"}],
}


@pytest.fixture
def agent_vault(api):
    return AgentVault(api)


@pytest.mark.parametrize("allowed_hosts", [[], "", "  "], ids=["empty list", "empty string", "blank string"])
def test_proxies_update_sends_null_for_empty_allowed_hosts(api, agent_vault, json_response, allowed_hosts):
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.update(PROXY["id"], allowed_hosts=allowed_hosts)
    assert api.session.patch.call_args.kwargs["json"] == {"allowedHosts": None}


def test_proxies_update_leaves_out_values_you_do_not_pass(api, agent_vault, json_response):
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.update(PROXY["id"], name="edge-proxy")
    assert api.session.patch.call_args.kwargs["json"] == {"name": "edge-proxy"}


def test_proxies_create_sends_and_reads_the_description(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"proxy": dict(PROXY, description="Edge traffic"), "proxyToken": "token"})
    created = agent_vault.proxies.create(name="edge-proxy", description="Edge traffic")
    assert api.session.post.call_args.kwargs["json"]["description"] == "Edge traffic"
    assert created.proxy.description == "Edge traffic"


@pytest.mark.parametrize("kwargs, body", [
    ({"description": ""}, {"description": ""}),
    ({"description": "", "allowed_hosts": []}, {"description": "", "allowedHosts": None}),
], ids=["description", "description and allowed hosts"])
def test_proxies_update_sends_an_empty_description_to_remove_it(api, agent_vault, json_response, kwargs, body):
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.update(PROXY["id"], **kwargs)
    assert api.session.patch.call_args.kwargs["json"] == body


@pytest.mark.parametrize("label", ["nightly deploy", None])
def test_sessions_update_always_sends_the_label(api, agent_vault, json_response, label):
    api.session.patch.return_value = json_response({"session": dict(SESSION, label=label)})
    assert agent_vault.sessions.update(SESSION["id"], label).label == label
    assert api.session.patch.call_args.kwargs["json"] == {"label": label}


@pytest.mark.parametrize("create", [
    lambda agent_vault: agent_vault.sessions.create(access_bundle="release"),
    lambda agent_vault: agent_vault.proxies.create(name="edge-proxy"),
    lambda agent_vault: agent_vault.access_bundles.create(name="release"),
], ids=["sessions.create", "proxies.create", "access_bundles.create"])
def test_creates_are_not_retried_once_the_request_may_have_reached_the_server(api, agent_vault, create):
    api.session.post.side_effect = requests.exceptions.ReadTimeout()
    with pytest.raises(requests.exceptions.ReadTimeout):
        create(agent_vault)
    assert api.session.post.call_count == 1


@pytest.mark.parametrize("allowed_hosts", [[], ""], ids=["empty list", "empty string"])
def test_proxies_create_leaves_out_empty_allowed_hosts(api, agent_vault, json_response, allowed_hosts):
    api.session.post.return_value = json_response({"proxy": PROXY, "proxyToken": "token"})
    agent_vault.proxies.create(name="edge-proxy", allowed_hosts=allowed_hosts)
    assert "allowedHosts" not in api.session.post.call_args.kwargs["json"]


def test_proxies_rotate_token_is_not_retried_once_the_request_may_have_reached_the_server(api, agent_vault):
    api.session.post.side_effect = requests.exceptions.ReadTimeout()
    with pytest.raises(requests.exceptions.ReadTimeout):
        agent_vault.proxies.rotate_token(PROXY["id"])
    assert api.session.post.call_count == 1


def test_sessions_revoke_leaves_access_bundles_and_services_unset_when_the_response_omits_them(api, agent_vault, json_response):
    revoked = {key: value for key, value in SESSION.items() if key not in ("accessBundles", "services")}
    api.session.post.return_value = json_response({"session": dict(revoked, status="revoked")})
    session = agent_vault.sessions.revoke(SESSION["id"])
    assert (session.accessBundles, session.services) == (None, None)


def test_sessions_get_keeps_an_empty_access_bundles_list(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"session": SESSION})
    assert agent_vault.sessions.get(SESSION["id"]).accessBundles == []


def test_sessions_create_leaves_out_ttl_so_the_server_picks_the_default(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token")})
    agent_vault.sessions.create(access_bundle="release")
    assert api.session.post.call_args.kwargs["json"] == {"accessBundles": ["release"]}


@pytest.mark.parametrize("kwargs, on_behalf_of", [
    ({"on_behalf_of_user_email": ON_BEHALF_OF["email"]}, {"userEmail": ON_BEHALF_OF["email"]}),
    ({"on_behalf_of_user_id": ON_BEHALF_OF["id"]}, {"userId": ON_BEHALF_OF["id"]}),
    ({"on_behalf_of_user_email": ""}, {"userEmail": ""}),
], ids=["email", "id", "empty email"])
def test_sessions_create_names_the_user_it_acts_for(api, agent_vault, json_response, kwargs, on_behalf_of):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token")})
    agent_vault.sessions.create(access_bundle="release", **kwargs)
    assert api.session.post.call_args.kwargs["json"] == {"accessBundles": ["release"], "onBehalfOf": on_behalf_of}


def test_sessions_create_still_takes_the_access_bundle_first(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token")})
    agent_vault.sessions.create("release", "1h")
    assert api.session.post.call_args.kwargs["json"] == {"accessBundles": ["release"], "ttl": "1h"}


def test_sessions_create_rejects_both_a_user_email_and_a_user_id(api, agent_vault):
    with pytest.raises(ValueError, match="not both"):
        agent_vault.sessions.create(
            access_bundle="release",
            on_behalf_of_user_email=ON_BEHALF_OF["email"],
            on_behalf_of_user_id=ON_BEHALF_OF["id"],
        )
    api.session.post.assert_not_called()


@pytest.mark.parametrize("on_behalf_of", [ON_BEHALF_OF, dict(ON_BEHALF_OF, id=None), None],
                         ids=["user", "deleted user", "own session"])
def test_sessions_get_reads_the_user_a_session_acts_for(api, agent_vault, json_response, on_behalf_of):
    api.session.get.return_value = json_response({"session": dict(SESSION, onBehalfOf=on_behalf_of)})
    expected = AgentVaultSessionActor(**on_behalf_of) if on_behalf_of else None
    assert agent_vault.sessions.get(SESSION["id"]).onBehalfOf == expected


def test_access_bundles_list_sends_booleans_the_way_the_api_reads_them(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"accessBundles": [], "totalCount": 0})
    agent_vault.access_bundles.list(requires_setup=True, granted=False)
    params = api.session.get.call_args.kwargs["params"]
    assert (params["requiresSetup"], params["granted"]) == ("true", "false")


def test_access_bundles_list_names_the_user_a_session_would_act_for(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"accessBundles": [], "totalCount": 0})
    agent_vault.access_bundles.list(on_behalf_of_user_email=ON_BEHALF_OF["email"])
    params = api.session.get.call_args.kwargs["params"]
    assert (params["onBehalfOfUserEmail"], params["onBehalfOfUserId"]) == (ON_BEHALF_OF["email"], None)


def test_access_bundles_list_rejects_both_a_user_email_and_a_user_id(api, agent_vault):
    with pytest.raises(ValueError, match="not both"):
        agent_vault.access_bundles.list(on_behalf_of_user_email=ON_BEHALF_OF["email"], on_behalf_of_user_id=ON_BEHALF_OF["id"])
    api.session.get.assert_not_called()


def test_access_bundles_list_reads_the_services_requiring_setup(api, agent_vault, json_response):
    listed = dict(BUNDLE, serviceCount=1, memberCount=2, hostPatterns=["api.github.com"],
                  servicesRequiringSetup=[{"id": SERVICE_ID, "name": "github"}])
    api.session.get.return_value = json_response({"accessBundles": [listed], "totalCount": 1})
    bundle = agent_vault.access_bundles.list().accessBundles[0]
    assert [(service.id, service.name) for service in bundle.servicesRequiringSetup] == [(SERVICE_ID, "github")]
    assert bundle.services is None


def test_access_bundles_get_reads_services_and_keeps_their_nested_settings(api, agent_vault, json_response):
    service = {
        "id": SERVICE_ID, "accessBundleId": BUNDLE["id"], "name": "github", "type": "http",
        "hostPattern": "api.github.com", "credential": {"type": "bearer", "memberProvidedFields": []},
        "customHeaders": [], "substitutions": [], "personalValues": None,
        "createdAt": BUNDLE["createdAt"], "updatedAt": BUNDLE["updatedAt"],
    }
    api.session.get.return_value = json_response({"accessBundle": dict(BUNDLE, services=[service])})
    [read] = agent_vault.access_bundles.get(BUNDLE["id"]).services
    assert (read.name, read.credential["type"], read.variableReferences) == ("github", "bearer", None)


def test_access_bundles_update_sends_an_empty_description_to_remove_it(api, agent_vault, json_response):
    api.session.patch.return_value = json_response({"accessBundle": BUNDLE})
    agent_vault.access_bundles.update(BUNDLE["id"], description="")
    assert api.session.patch.call_args.kwargs["json"] == {"description": ""}


def test_access_bundles_grant_and_revoke_send_only_the_grantees_you_name(api, agent_vault, json_response):
    change = {"members": [{"type": "user", "id": ON_BEHALF_OF["id"]}], "skipped": []}
    api.session.post.return_value = json_response(change)
    api.session.delete.return_value = json_response(change)
    agent_vault.access_bundles.grant(BUNDLE["id"], machine_identity_ids=[MACHINE_IDENTITY_ID])
    revoked = agent_vault.access_bundles.revoke(BUNDLE["id"], user_ids=[ON_BEHALF_OF["id"]])
    assert api.session.post.call_args.kwargs["json"] == {"machineIdentityIds": [MACHINE_IDENTITY_ID]}
    assert api.session.delete.call_args.kwargs["json"] == {"userIds": [ON_BEHALF_OF["id"]]}
    assert [(member.type, member.id) for member in revoked.members] == [("user", ON_BEHALF_OF["id"])]


def test_delegations_set_puts_the_scope_value(api, agent_vault, json_response):
    api.session.put.return_value = json_response({"delegation": DELEGATION})
    agent_vault.delegations.set(MACHINE_IDENTITY_ID, AgentVaultDelegationScope.SELECTED, group_ids=[GROUP_ID])
    assert api.session.put.call_args.kwargs["json"] == {"scope": "selected", "groupIds": [GROUP_ID]}


def test_delegations_get_reads_users_groups_and_missing_access_bundles(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"delegation": DELEGATION})
    delegation = agent_vault.delegations.get(MACHINE_IDENTITY_ID)
    assert delegation.machineIdentity.name == "slack-bot"
    assert [bundle.name for bundle in delegation.users[0].missingAccessBundles] == ["release"]
    assert (delegation.groups[0].name, delegation.groups[0].missingAccessBundles) == ("Engineering", [])


def test_delegations_list_joins_the_machine_identity_ids(api, agent_vault, json_response):
    other_machine_identity_id = "2f6e8a4c-1b3d-4c5e-9f7a-6b8c0d2e4f1a"
    listed = {key: value for key, value in DELEGATION.items() if key != "missingAccessBundles"}
    api.session.get.return_value = json_response({"delegations": [listed], "totalCount": 1})
    delegations = agent_vault.delegations.list(machine_identity_ids=[MACHINE_IDENTITY_ID, other_machine_identity_id])
    expected = f"{MACHINE_IDENTITY_ID},{other_machine_identity_id}"
    assert api.session.get.call_args.kwargs["params"]["machineIdentityIds"] == expected
    assert delegations.delegations[0].missingAccessBundles is None


def test_delegations_remove_subjects_returns_none_once_the_last_one_is_gone(api, agent_vault, json_response):
    api.session.delete.return_value = json_response({"delegation": None})
    assert agent_vault.delegations.remove_subjects(MACHINE_IDENTITY_ID, user_ids=[ON_BEHALF_OF["id"]]) is None
    assert api.session.delete.call_args.kwargs["json"] == {"userIds": [ON_BEHALF_OF["id"]]}


def test_delegations_list_available_subjects_sends_the_actor_type_value(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"members": [], "totalCount": 0})
    agent_vault.delegations.list_available_subjects(MACHINE_IDENTITY_ID, actor_type=AgentVaultMemberType.GROUP)
    assert api.session.get.call_args.kwargs["params"]["actorType"] == "group"


@pytest.mark.parametrize("traffic_policy", [
    AgentVaultTrafficPolicy.SERVICE_HOSTS, AgentVaultTrafficPolicy.BUNDLE_HOSTS, "service-hosts", "bundle-hosts",
], ids=["SERVICE_HOSTS", "BUNDLE_HOSTS", "service-hosts", "bundle-hosts"])
def test_proxies_send_either_name_of_service_hosts_as_bundle_hosts_which_every_version_takes(
        api, agent_vault, json_response, traffic_policy):
    api.session.post.return_value = json_response({"proxy": PROXY, "proxyToken": "token"})
    api.session.patch.return_value = json_response({"proxy": PROXY})
    agent_vault.proxies.create(name="edge-proxy", traffic_policy=traffic_policy)
    agent_vault.proxies.update(PROXY["id"], traffic_policy=traffic_policy)
    assert api.session.post.call_args.kwargs["json"]["trafficPolicy"] == "bundle-hosts"
    assert api.session.patch.call_args.kwargs["json"] == {"trafficPolicy": "bundle-hosts"}


@pytest.mark.parametrize("kwargs", [{}, {"traffic_policy": AgentVaultTrafficPolicy.ANY_HOST}, {"traffic_policy": "any-host"}],
                         ids=["default", "ANY_HOST", "any-host"])
def test_proxies_create_sends_any_host_as_it_is(api, agent_vault, json_response, kwargs):
    api.session.post.return_value = json_response({"proxy": PROXY, "proxyToken": "token"})
    agent_vault.proxies.create(name="edge-proxy", **kwargs)
    assert api.session.post.call_args.kwargs["json"]["trafficPolicy"] == "any-host"


@pytest.mark.parametrize("reported", ["service-hosts", "bundle-hosts"], ids=["current version", "version before the rename"])
@pytest.mark.parametrize("verb, payload, call", [
    ("get", lambda proxy: {"proxies": [proxy], "totalCount": 1}, lambda agent_vault: agent_vault.proxies.list().proxies[0]),
    ("post", lambda proxy: {"proxy": proxy, "proxyToken": "token"},
     lambda agent_vault: agent_vault.proxies.create(name="edge-proxy").proxy),
    ("patch", lambda proxy: {"proxy": proxy}, lambda agent_vault: agent_vault.proxies.update(PROXY["id"], poll_interval=30)),
    ("post", lambda proxy: {"proxy": proxy, "proxyToken": "token"},
     lambda agent_vault: agent_vault.proxies.rotate_token(PROXY["id"]).proxy),
    ("post", lambda proxy: {"proxy": proxy}, lambda agent_vault: agent_vault.proxies.revoke(PROXY["id"])),
], ids=["list", "create", "update", "rotate_token", "revoke"])
def test_proxies_report_either_name_as_service_hosts(api, agent_vault, json_response, reported, verb, payload, call):
    getattr(api.session, verb).return_value = json_response(payload(dict(PROXY, trafficPolicy=reported)))
    proxy = call(agent_vault)
    assert proxy.trafficPolicy == "service-hosts"
    assert proxy.trafficPolicy == AgentVaultTrafficPolicy.SERVICE_HOSTS
    assert proxy.trafficPolicy == AgentVaultTrafficPolicy.BUNDLE_HOSTS


def test_proxies_list_leaves_the_traffic_policy_unset_for_a_member(api, agent_vault, json_response):
    api.session.get.return_value = json_response({"proxies": [PROXY], "totalCount": 1})
    assert agent_vault.proxies.list().proxies[0].trafficPolicy is None


def test_traffic_policy_old_name_is_the_same_member():
    assert AgentVaultTrafficPolicy.BUNDLE_HOSTS is AgentVaultTrafficPolicy.SERVICE_HOSTS
    assert AgentVaultTrafficPolicy("bundle-hosts") is AgentVaultTrafficPolicy.SERVICE_HOSTS
    assert AgentVaultTrafficPolicy("service-hosts") is AgentVaultTrafficPolicy.SERVICE_HOSTS
    assert list(AgentVaultTrafficPolicy) == [AgentVaultTrafficPolicy.ANY_HOST, AgentVaultTrafficPolicy.SERVICE_HOSTS]
    with pytest.raises(ValueError):
        AgentVaultTrafficPolicy("all-hosts")


def test_sessions_create_sends_services_without_an_access_bundle(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token", services=[INLINE_SERVICE])})
    agent_vault.sessions.create(services=[INLINE_SERVICE_INPUT])
    assert api.session.post.call_args.kwargs["json"] == {"services": [INLINE_SERVICE_INPUT]}


def test_sessions_create_sends_an_access_bundle_and_services_together(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token", services=[INLINE_SERVICE])})
    agent_vault.sessions.create(access_bundle="release", services=[INLINE_SERVICE_INPUT])
    assert api.session.post.call_args.kwargs["json"] == {"accessBundles": ["release"], "services": [INLINE_SERVICE_INPUT]}


def test_sessions_create_sends_an_empty_access_bundle_name_so_the_server_rejects_it(api, agent_vault, json_response):
    api.session.post.return_value = json_response({"session": dict(SESSION, token="token")})
    agent_vault.sessions.create(access_bundle="")
    assert api.session.post.call_args.kwargs["json"] == {"accessBundles": [""]}


def test_sessions_read_services_as_the_api_sends_them(api, agent_vault, json_response):
    session = dict(SESSION, services=[INLINE_SERVICE])
    api.session.post.return_value = json_response({"session": dict(session, token="token")})
    api.session.get.side_effect = [
        json_response({"session": session}),
        json_response({"sessions": [session], "totalCount": 1}),
    ]
    expected = [AgentVaultInlineService(**INLINE_SERVICE)]
    assert agent_vault.sessions.create(services=[INLINE_SERVICE_INPUT]).services == expected
    assert agent_vault.sessions.get(SESSION["id"]).services == expected
    assert agent_vault.sessions.list().sessions[0].services == expected


def test_sessions_from_an_infisical_version_without_inline_services_have_an_empty_list_of_them(
        api, agent_vault, json_response):
    older = {key: value for key, value in SESSION.items() if key != "services"}
    api.session.post.return_value = json_response({"session": dict(older, token="token")})
    api.session.patch.return_value = json_response({"session": older})
    api.session.get.side_effect = [
        json_response({"session": older}),
        json_response({"sessions": [older], "totalCount": 1}),
    ]
    assert agent_vault.sessions.create(access_bundle="release").services == []
    assert agent_vault.sessions.update(SESSION["id"], None).services == []
    assert agent_vault.sessions.get(SESSION["id"]).services == []
    assert agent_vault.sessions.list().sessions[0].services == []


@pytest.mark.parametrize("status_code, payload, explanation", [
    (422, {
        "reqId": "req-1",
        "statusCode": 422,
        "message": [{
            "code": "too_big",
            "maximum": 20,
            "path": ["services"],
            "message": "A session can have at most 20 services. Add the others to an access bundle and name it in accessBundles.",
        }],
        "error": "ValidationFailure",
    }, "at most 20 services"),
    (403, {
        "statusCode": 403,
        "message": "Only an Agent Vault admin can send services with a session. Name an access bundle instead.",
        "error": "PermissionDenied",
    }, "Only an Agent Vault admin can send services with a session"),
], ids=["validation error", "refusal"])
def test_sessions_create_keeps_the_servers_explanation_when_it_refuses_services(
        api, agent_vault, json_response, status_code, payload, explanation):
    api.session.post.return_value = json_response(payload, status_code)
    with pytest.raises(APIError) as raised:
        agent_vault.sessions.create(services=[INLINE_SERVICE_INPUT])
    assert raised.value.status_code == status_code
    assert explanation in str(raised.value)
    assert api.session.post.call_count == 1


def test_access_bundles_get_reads_the_tools_an_mcp_service_allows(api, agent_vault, json_response):
    service = {
        "id": SERVICE_ID, "accessBundleId": BUNDLE["id"], "name": "linear", "type": "mcp",
        "serverUrl": "https://mcp.linear.app/mcp", "transport": "streamable-http", "hostPattern": "mcp.linear.app",
        "allowedMethods": None, "allowedPathPrefixes": None, "allowedTools": ["list_issues"],
        "credential": {"type": "bearer", "memberProvidedFields": []}, "customHeaders": [], "substitutions": [],
        "createdAt": BUNDLE["createdAt"], "updatedAt": BUNDLE["updatedAt"],
    }
    api.session.get.return_value = json_response({"accessBundle": dict(BUNDLE, services=[service])})
    assert agent_vault.access_bundles.get(BUNDLE["id"]).services[0].allowedTools == ["list_issues"]


def test_access_bundles_list_grantees_reads_a_pending_organization_membership(api, agent_vault, json_response):
    grantee = dict({key: ON_BEHALF_OF[key] for key in ("type", "id", "username", "email", "firstName", "lastName")},
                   isOrgMembershipPending=True, grantedAt="2026-10-27T00:00:00.000Z")
    api.session.get.return_value = json_response({"members": [grantee], "totalCount": 1})
    assert agent_vault.access_bundles.list_grantees(BUNDLE["id"]).members[0].isOrgMembershipPending is True
