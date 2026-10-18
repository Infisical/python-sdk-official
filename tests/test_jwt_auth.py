import json

import pytest
import responses

from infisical_sdk import InfisicalSDKClient
from infisical_sdk.api_types import MachineIdentityLoginResponse
from infisical_sdk.infisical_requests import APIError

HOST = "https://example.com"
LOGIN = {
    "accessToken": "new-access-token",
    "expiresIn": 7200,
    "accessTokenMaxTTL": 86400,
    "tokenType": "Bearer",
}


@pytest.mark.parametrize("initial_token", [None, "existing-token"])
@pytest.mark.parametrize("organization_slug", [None, "example-org"])
@responses.activate
def test_jwt_login_sets_token_for_later_requests(initial_token, organization_slug):
    responses.post(HOST + "/api/v1/auth/jwt-auth/login", json=LOGIN)
    responses.get(HOST + "/probe", json={"ok": True})
    with InfisicalSDKClient(host=HOST, token=initial_token, cache_ttl=None) as client:
        options = {} if organization_slug is None else {"organization_slug": organization_slug}
        result = client.auth.jwt_auth.login(
            identity_id="identity-example", jwt="test.jwt.value", **options
        )
        assert isinstance(result, MachineIdentityLoginResponse)
        assert result.to_dict() == LOGIN
        assert client.get_token() == LOGIN["accessToken"]
        client.api.get(path="/probe", model=dict)
    expected = {"identityId": "identity-example", "jwt": "test.jwt.value"}
    if organization_slug is not None:
        expected["organizationSlug"] = organization_slug
    assert json.loads(responses.calls[0].request.body) == expected
    assert responses.calls[1].request.headers["Authorization"] == "Bearer new-access-token"


@pytest.mark.parametrize("initial_token", [None, "existing-token"])
@pytest.mark.parametrize("status", [401, 403])
@responses.activate
def test_jwt_login_failure_preserves_current_token(initial_token, status):
    responses.post(
        HOST + "/api/v1/auth/jwt-auth/login",
        json={"message": "Login rejected"}, status=status,
    )
    with InfisicalSDKClient(host=HOST, token=initial_token, cache_ttl=None) as client:
        with pytest.raises(APIError) as error:
            client.auth.jwt_auth.login(identity_id="identity-example", jwt="test.jwt.value")
        assert error.value.status_code == status
        assert client.get_token() == initial_token
        expected_header = "Bearer existing-token" if initial_token else None
        assert client.api.session.headers.get("Authorization") == expected_header
    assert len(responses.calls) == 1


@pytest.mark.parametrize("initial_token", [None, "existing-token"])
@responses.activate
def test_oidc_login_keeps_its_own_endpoint(initial_token):
    responses.post(HOST + "/api/v1/auth/oidc-auth/login", json=LOGIN)
    with InfisicalSDKClient(host=HOST, token=initial_token, cache_ttl=None) as client:
        result = client.auth.oidc_auth.login(identity_id="identity-example", jwt="test.jwt.value")
        assert result.accessToken == LOGIN["accessToken"]
        assert client.get_token() == LOGIN["accessToken"]
    assert len(responses.calls) == 1
