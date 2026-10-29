from typing import Optional, List, Union

from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.api_types import (
    AgentVaultProxy,
    AgentVaultSession,
    AgentVaultSessionScope,
    AgentVaultSessionStatus,
    AgentVaultTrafficPolicy,
    AgentVaultProxyWithTokenResponse,
    CreateAgentVaultSessionResponse,
    CreatedAgentVaultSession,
    ListAgentVaultProxiesResponse,
    ListAgentVaultSessionsResponse,
    SingleAgentVaultProxyResponse,
    SingleAgentVaultSessionResponse,
)


def _join_hosts(allowed_hosts: Optional[Union[str, List[str]]]) -> Optional[str]:
    """The API takes host patterns as one comma-separated string, and rejects an empty one."""
    if isinstance(allowed_hosts, list):
        return ",".join(allowed_hosts) or None
    return allowed_hosts


class AgentVaultProxies:
    """Manages Agent Vault proxies."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def list(
            self,
            search: Optional[str] = None,
            order_by: str = "createdAt",
            order_direction: str = "desc",
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultProxiesResponse:
        """List the organization's Agent Vault proxies.

        Args:
            search: Match proxies by name.
            order_by: What to sort proxies by: "name" or "createdAt". Defaults to "createdAt".
            order_direction: Which way to sort: "asc" or "desc". Defaults to "desc".
            limit: The maximum number of proxies to return (1-100). Defaults to 20.
            offset: How many proxies to skip. Defaults to 0.

        Returns:
            ListAgentVaultProxiesResponse containing proxies and totalCount. Settings fields are only set for admins.
        """
        params = {
            "search": search,
            "orderBy": order_by,
            "orderDirection": order_direction,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path="/api/v1/agent-vault/proxies",
            params=params,
            model=ListAgentVaultProxiesResponse
        )

        return result.data

    def create(
            self,
            name: str,
            traffic_policy: Union[AgentVaultTrafficPolicy, str] = AgentVaultTrafficPolicy.ANY_HOST,
            allowed_hosts: Optional[Union[str, List[str]]] = None,
            poll_interval: int = 60) -> AgentVaultProxyWithTokenResponse:
        """Register an Agent Vault proxy and issue its proxy token.

        Args:
            name: The name of the proxy (a slug, at most 64 characters).
            traffic_policy: Which hosts an agent may reach through this proxy. Defaults to "any-host".
            allowed_hosts: Hosts that stay reachable under the "bundle-hosts" traffic policy even though no access bundle covers them. A list or a comma-separated string.
            poll_interval: How often, in seconds, the proxy refreshes its sessions and settings (10-300). Defaults to 60.

        Returns:
            AgentVaultProxyWithTokenResponse containing the proxy and its proxyToken. The token is only returned once.
        """
        request_body = {
            "name": name,
            "trafficPolicy": traffic_policy.value if isinstance(traffic_policy, AgentVaultTrafficPolicy) else traffic_policy,
            "allowedHosts": _join_hosts(allowed_hosts),
            "pollInterval": poll_interval,
        }

        result = self.requests.post_once(
            path="/api/v1/agent-vault/proxies",
            json=request_body,
            model=AgentVaultProxyWithTokenResponse
        )

        return result.data

    def update(
            self,
            proxy_id: str,
            name: Optional[str] = None,
            traffic_policy: Optional[Union[AgentVaultTrafficPolicy, str]] = None,
            allowed_hosts: Optional[Union[str, List[str]]] = None,
            poll_interval: Optional[int] = None,
            clear_allowed_hosts: bool = False) -> AgentVaultProxy:
        """Update an Agent Vault proxy's name or settings. Only the values you pass are changed.

        Args:
            proxy_id: The ID of the proxy to update.
            name: The new name of the proxy.
            traffic_policy: Which hosts an agent may reach through this proxy.
            allowed_hosts: Hosts that stay reachable under the "bundle-hosts" traffic policy. A list or a comma-separated string.
            poll_interval: How often, in seconds, the proxy refreshes its sessions and settings (10-300).
            clear_allowed_hosts: Remove all allowed hosts. Can't be combined with allowed_hosts.

        Returns:
            The updated proxy.
        """
        if clear_allowed_hosts and allowed_hosts is not None:
            raise ValueError("Pass either allowed_hosts or clear_allowed_hosts, not both")
        if allowed_hosts == []:
            raise ValueError("allowed_hosts can't be empty. To remove every allowed host, pass clear_allowed_hosts=True")

        if isinstance(traffic_policy, AgentVaultTrafficPolicy):
            traffic_policy = traffic_policy.value

        request_body = {
            "name": name,
            "trafficPolicy": traffic_policy,
            "allowedHosts": _join_hosts(allowed_hosts),
            "pollInterval": poll_interval,
        }

        result = self.requests.patch(
            path=f"/api/v1/agent-vault/proxies/{proxy_id}",
            json=request_body,
            model=SingleAgentVaultProxyResponse,
            nullable_keys=["allowedHosts"] if clear_allowed_hosts else None
        )

        return result.data.proxy

    def delete(self, proxy_id: str) -> AgentVaultProxy:
        """Delete an Agent Vault proxy.

        Args:
            proxy_id: The ID of the proxy to delete.

        Returns:
            The deleted proxy. Only id and name are set.
        """
        result = self.requests.delete(
            path=f"/api/v1/agent-vault/proxies/{proxy_id}",
            model=SingleAgentVaultProxyResponse
        )

        return result.data.proxy

    def rotate_token(self, proxy_id: str) -> AgentVaultProxyWithTokenResponse:
        """Issue a new proxy token. The proxy's earlier tokens stop working and it gets a new certificate authority.

        Args:
            proxy_id: The ID of the proxy to rotate the token for.

        Returns:
            AgentVaultProxyWithTokenResponse containing the proxy and its new proxyToken. The token is only returned once.
        """
        result = self.requests.post_once(
            path=f"/api/v1/agent-vault/proxies/{proxy_id}/token-auth/proxy-token",
            model=AgentVaultProxyWithTokenResponse
        )

        return result.data

    def revoke(self, proxy_id: str) -> AgentVaultProxy:
        """Revoke an Agent Vault proxy's token. Rotate its token to bring it back.

        Args:
            proxy_id: The ID of the proxy to revoke.

        Returns:
            The revoked proxy.
        """
        result = self.requests.post(
            path=f"/api/v1/agent-vault/proxies/{proxy_id}/revoke",
            model=SingleAgentVaultProxyResponse
        )

        return result.data.proxy


class AgentVaultSessions:
    """Manages Agent Vault sessions."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def list(
            self,
            scope: Union[AgentVaultSessionScope, str] = AgentVaultSessionScope.MINE,
            statuses: Optional[List[Union[AgentVaultSessionStatus, str]]] = None,
            search: Optional[str] = None,
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultSessionsResponse:
        """List Agent Vault sessions.

        Args:
            scope: Whose sessions to list: your own ("mine") or everyone's ("all", administrators only). Defaults to "mine".
            statuses: Only return sessions with any of these statuses: "active", "revoked" or "expired".
            search: Match sessions by label, actor name, actor email or access bundle name.
            limit: The maximum number of sessions to return (1-100). Defaults to 20.
            offset: How many sessions to skip. Defaults to 0.

        Returns:
            ListAgentVaultSessionsResponse containing sessions and totalCount.
        """
        status = None
        if statuses:
            status = ",".join(s.value if isinstance(s, AgentVaultSessionStatus) else s for s in statuses)

        params = {
            "scope": scope.value if isinstance(scope, AgentVaultSessionScope) else scope,
            "status": status,
            "search": search,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path="/api/v1/agent-vault/sessions",
            params=params,
            model=ListAgentVaultSessionsResponse
        )

        return result.data

    def get(self, session_id: str) -> AgentVaultSession:
        """Get an Agent Vault session.

        Args:
            session_id: The ID of the session to retrieve.

        Returns:
            The session.
        """
        result = self.requests.get(
            path=f"/api/v1/agent-vault/sessions/{session_id}",
            model=SingleAgentVaultSessionResponse
        )

        return result.data.session

    def create(
            self,
            access_bundle: str,
            ttl: str = "7d",
            label: Optional[str] = None) -> CreatedAgentVaultSession:
        """Create an Agent Vault session with an access bundle you can reach.

        Args:
            access_bundle: The name of the access bundle the session carries.
            ttl: How long the session lasts: a duration such as "30m", "8h" or "7d" (at least 1m), or "never". Defaults to "7d".
            label: A short description of what the session is for, such as "nightly deploy". Up to 128 characters, without line breaks, tabs, or invisible characters.

        Returns:
            The created session, including its token. The token is only returned once.
        """
        request_body = {
            "accessBundles": [access_bundle],
            "ttl": ttl,
            "label": label,
        }

        result = self.requests.post_once(
            path="/api/v1/agent-vault/sessions",
            json=request_body,
            model=CreateAgentVaultSessionResponse
        )

        return result.data.session

    def update(self, session_id: str, label: Optional[str]) -> AgentVaultSession:
        """Update the label of an Agent Vault session. This also works after the session expires or is revoked.

        Args:
            session_id: The ID of the session to update.
            label: The new label for the session, up to 128 characters, without line breaks, tabs, or invisible characters. Pass None or an empty string to remove the label. You can't change the label once the session's owner is deleted.

        Returns:
            The updated session.
        """
        request_body = {
            "label": label,
        }

        result = self.requests.patch(
            path=f"/api/v1/agent-vault/sessions/{session_id}",
            json=request_body,
            model=SingleAgentVaultSessionResponse,
            nullable_keys=["label"]
        )

        return result.data.session

    def revoke(self, session_id: str) -> AgentVaultSession:
        """Revoke an Agent Vault session. Revoking an already revoked session is a no-op.

        Args:
            session_id: The ID of the session to revoke.

        Returns:
            The revoked session. Its accessBundles is None, because the response leaves the bundles out; call get for them.
        """
        result = self.requests.post(
            path=f"/api/v1/agent-vault/sessions/{session_id}/revoke",
            model=SingleAgentVaultSessionResponse
        )

        return result.data.session


class AgentVault:
    """Manages Infisical Agent Vault."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests
        self.proxies = AgentVaultProxies(requests)
        self.sessions = AgentVaultSessions(requests)
