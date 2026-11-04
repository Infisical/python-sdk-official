from typing import Any, Dict, Optional, List, Union

from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.api_types import (
    AgentVaultAccessBundle,
    AgentVaultDelegation,
    AgentVaultDelegationScope,
    AgentVaultMemberType,
    AgentVaultProxy,
    AgentVaultSession,
    AgentVaultSessionScope,
    AgentVaultSessionStatus,
    AgentVaultTrafficPolicy,
    AgentVaultGrantChangeResponse,
    AgentVaultProxyWithTokenResponse,
    CreateAgentVaultSessionResponse,
    CreatedAgentVaultSession,
    ListAgentVaultAccessBundlesResponse,
    ListAgentVaultDelegationsResponse,
    ListAgentVaultGranteesResponse,
    ListAgentVaultMembersResponse,
    ListAgentVaultProxiesResponse,
    ListAgentVaultSessionsResponse,
    SingleAgentVaultAccessBundleResponse,
    SingleAgentVaultDelegationResponse,
    SingleAgentVaultProxyResponse,
    SingleAgentVaultSessionResponse,
)


def _join_hosts(allowed_hosts: Optional[Union[str, List[str]]]) -> Optional[str]:
    """The API takes host patterns as one comma-separated string and rejects an empty one, so empty values become None."""
    if isinstance(allowed_hosts, list):
        allowed_hosts = ",".join(allowed_hosts)
    if allowed_hosts is not None and not allowed_hosts.strip():
        return None
    return allowed_hosts


def _query_bool(value: Optional[bool]) -> Optional[str]:
    """The API reads a query boolean only as "true" or "false", and requests would send True as "True"."""
    if value is None:
        return None
    return "true" if value else "false"


def _wire_traffic_policy(traffic_policy: Optional[Union[AgentVaultTrafficPolicy, str]]) -> Optional[str]:
    """Infisical stores service-hosts under its old name, bundle-hosts, and still accepts that name, while a version
    from before the rename accepts only bundle-hosts. So either name goes out as bundle-hosts, which every version takes."""
    if isinstance(traffic_policy, AgentVaultTrafficPolicy):
        traffic_policy = traffic_policy.value
    return "bundle-hosts" if traffic_policy == AgentVaultTrafficPolicy.SERVICE_HOSTS.value else traffic_policy


def _with_services(session: AgentVaultSession) -> AgentVaultSession:
    """A session from an Infisical version without inline services has none, so it gets an empty list rather than None."""
    if session.services is None:
        session.services = []
    return session


def _check_one_user(on_behalf_of_user_email: Optional[str], on_behalf_of_user_id: Optional[str]) -> None:
    """The API names a user by email address or by ID, not both."""
    if on_behalf_of_user_email is not None and on_behalf_of_user_id is not None:
        raise ValueError("Pass either on_behalf_of_user_email or on_behalf_of_user_id, not both")


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
            search: Match proxies by name or description.
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
            poll_interval: int = 60,
            description: Optional[str] = None) -> AgentVaultProxyWithTokenResponse:
        """Register an Agent Vault proxy and issue its proxy token.

        Args:
            name: The name of the proxy (a slug, at most 64 characters).
            traffic_policy: Which hosts an agent may reach through this proxy: AgentVaultTrafficPolicy.ANY_HOST ("any-host"), or AgentVaultTrafficPolicy.SERVICE_HOSTS ("service-hosts") for only the hosts that the session's services cover. Defaults to "any-host". The old name of SERVICE_HOSTS, BUNDLE_HOSTS ("bundle-hosts"), works the same.
            allowed_hosts: Hosts that stay reachable under the "service-hosts" traffic policy even though none of the session's services cover them. A list or a comma-separated string.
            poll_interval: How often, in seconds, the proxy refreshes its sessions and settings (10-300). Defaults to 60.
            description: What the proxy is for, up to 256 characters, without line breaks or other control characters.

        Returns:
            AgentVaultProxyWithTokenResponse containing the proxy and its proxyToken. The token is only returned once.
        """
        request_body = {
            "name": name,
            "trafficPolicy": _wire_traffic_policy(traffic_policy),
            "allowedHosts": _join_hosts(allowed_hosts),
            "pollInterval": poll_interval,
            "description": description,
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
            description: Optional[str] = None) -> AgentVaultProxy:
        """Update an Agent Vault proxy's name, description or settings. Only the values you pass are changed.

        Args:
            proxy_id: The ID of the proxy to update.
            name: The new name of the proxy.
            traffic_policy: Which hosts an agent may reach through this proxy: AgentVaultTrafficPolicy.ANY_HOST ("any-host"), or AgentVaultTrafficPolicy.SERVICE_HOSTS ("service-hosts") for only the hosts that the session's services cover. The old name of SERVICE_HOSTS, BUNDLE_HOSTS ("bundle-hosts"), works the same.
            allowed_hosts: Hosts that stay reachable under the "service-hosts" traffic policy. A list or a comma-separated string. Pass an empty list or string to remove every allowed host.
            poll_interval: How often, in seconds, the proxy refreshes its sessions and settings (10-300).
            description: The new description, up to 256 characters, without line breaks or other control characters. Pass an empty string to remove the description.

        Returns:
            The updated proxy.
        """
        hosts = _join_hosts(allowed_hosts)
        # An empty value removes every allowed host, which the API takes as null.
        remove_hosts = allowed_hosts is not None and hosts is None

        request_body = {
            "name": name,
            "trafficPolicy": _wire_traffic_policy(traffic_policy),
            "allowedHosts": hosts,
            "pollInterval": poll_interval,
            "description": description,
        }

        result = self.requests.patch(
            path=f"/api/v1/agent-vault/proxies/{proxy_id}",
            json=request_body,
            model=SingleAgentVaultProxyResponse,
            nullable_keys=["allowedHosts"] if remove_hosts else None
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
            search: Match sessions by label, actor name, actor email, the name or email of the user a session was started on behalf of, or access bundle name.
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

        for session in result.data.sessions:
            _with_services(session)
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

        return _with_services(result.data.session)

    def create(
            self,
            access_bundle: Optional[str] = None,
            ttl: Optional[str] = None,
            label: Optional[str] = None,
            on_behalf_of_user_email: Optional[str] = None,
            on_behalf_of_user_id: Optional[str] = None,
            services: Optional[List[Dict[str, Any]]] = None) -> CreatedAgentVaultSession:
        """Create an Agent Vault session with an access bundle you can reach, services of its own, or both, for yourself or, as a machine identity with a delegation, on behalf of a user.

        Only Agent Vault admins can send services with a session. On behalf of a user, that's your machine identity:
        the user doesn't need the Admin role, and the services don't use the user's personal values.

        To start a session on behalf of a user, you must be a machine identity whose delegation covers the user. The proxy
        then uses the user's personal values, and the session can use only an access bundle that both the user and your
        machine identity can use. The session still belongs to your machine identity, so the user can't see it unless
        they're an Agent Vault admin.

        Args:
            access_bundle: The name of the access bundle the session carries. Pass access_bundle, services, or both.
            ttl: How long the session lasts: a duration such as "30m", "8h" or "7d" (at least 1m), or "never". Defaults to "7d", or to "1h" for a session on behalf of a user.
            label: A short description of what the session is for, such as "nightly deploy". Up to 128 characters, without line breaks, tabs, or invisible characters.
            on_behalf_of_user_email: The email address of the user to start the session on behalf of. Can't be combined with on_behalf_of_user_id.
            on_behalf_of_user_id: The ID of the user to start the session on behalf of. Can't be combined with on_behalf_of_user_email.
            services: Services the session carries itself, instead of or beside its access bundle's: up to 20 dicts with the API's field names, such as {"type": "http", "hostPattern": "api.github.com", "credential": {"type": "bearer", "value": token}}. Only Agent Vault admins can send them. Each has the same fields as a service in an access bundle, except that its name is optional, its values can't use variables, and it can't use OAuth or member-provided values.

        Returns:
            The created session, including its token. The token is only returned once. Its services leave out their tokens, passwords and values.
        """
        _check_one_user(on_behalf_of_user_email, on_behalf_of_user_id)

        on_behalf_of = None
        if on_behalf_of_user_email is not None:
            on_behalf_of = {"userEmail": on_behalf_of_user_email}
        elif on_behalf_of_user_id is not None:
            on_behalf_of = {"userId": on_behalf_of_user_id}

        request_body = {
            # Left out without an access bundle, for a session that carries only services of its own.
            "accessBundles": [access_bundle] if access_bundle is not None else None,
            "services": services,
            "ttl": ttl,
            "label": label,
            "onBehalfOf": on_behalf_of,
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
            label: The new label for the session, up to 128 characters, without line breaks, tabs, or invisible characters. Pass None or an empty string to remove the label. You can't change the label once the session's owner, or the user it was started on behalf of, is deleted.

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

        return _with_services(result.data.session)

    def revoke(self, session_id: str) -> AgentVaultSession:
        """Revoke an Agent Vault session. Revoking an already revoked session is a no-op.

        Args:
            session_id: The ID of the session to revoke.

        Returns:
            The revoked session. Its accessBundles and services are None, because the response leaves them out; call get for them.
        """
        result = self.requests.post(
            path=f"/api/v1/agent-vault/sessions/{session_id}/revoke",
            model=SingleAgentVaultSessionResponse
        )

        return result.data.session


class AgentVaultAccessBundles:
    """Manages Agent Vault access bundles and who they're granted to. Every method except list and get requires the Admin role in Agent Vault."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def list(
            self,
            search: Optional[str] = None,
            requires_setup: Optional[bool] = None,
            granted: Optional[bool] = None,
            on_behalf_of_user_email: Optional[str] = None,
            on_behalf_of_user_id: Optional[str] = None,
            order_by: str = "createdAt",
            order_direction: str = "desc",
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultAccessBundlesResponse:
        """List the Agent Vault access bundles you can reach. Admins reach every access bundle.

        Args:
            search: Match access bundles by name or description.
            requires_setup: True lists only the access bundles with services that still need your personal values, and False lists the rest. Defaults to both.
            granted: True lists only the access bundles granted to you, directly or through a group, and False lists the ones you reach only as an admin. Defaults to both. Can't be combined with on_behalf_of_user_email or on_behalf_of_user_id.
            on_behalf_of_user_email: As a machine identity whose delegation covers the user with this email address, list the access bundles that a session on the user's behalf could use: those both the user and your machine identity can use. requires_setup and servicesRequiringSetup then refer to the user's personal values. Can't be combined with on_behalf_of_user_id.
            on_behalf_of_user_id: Like on_behalf_of_user_email, naming the user by ID instead.
            order_by: What to sort access bundles by: "name", "serviceCount" or "createdAt". Defaults to "createdAt".
            order_direction: Which way to sort: "asc" or "desc". Defaults to "desc".
            limit: The maximum number of access bundles to return (1-100). Defaults to 20.
            offset: How many access bundles to skip. Defaults to 0.

        Returns:
            ListAgentVaultAccessBundlesResponse containing accessBundles and totalCount.
        """
        _check_one_user(on_behalf_of_user_email, on_behalf_of_user_id)

        params = {
            "search": search,
            "requiresSetup": _query_bool(requires_setup),
            "granted": _query_bool(granted),
            "onBehalfOfUserEmail": on_behalf_of_user_email,
            "onBehalfOfUserId": on_behalf_of_user_id,
            "orderBy": order_by,
            "orderDirection": order_direction,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path="/api/v1/agent-vault/access-bundles",
            params=params,
            model=ListAgentVaultAccessBundlesResponse
        )

        return result.data

    def get(self, access_bundle_id: str) -> AgentVaultAccessBundle:
        """Get an Agent Vault access bundle you can reach, with its services.

        Args:
            access_bundle_id: The ID of the access bundle.

        Returns:
            The access bundle, with its services in services. A service's variableReferences is only set for admins.
        """
        result = self.requests.get(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}",
            model=SingleAgentVaultAccessBundleResponse
        )

        return result.data.accessBundle

    def create(self, name: str, description: Optional[str] = None) -> AgentVaultAccessBundle:
        """Create an Agent Vault access bundle. It's granted to you, unless you're in Agent Vault only through a group.

        Args:
            name: The name of the access bundle (a slug, at most 64 characters).
            description: What the access bundle is for, up to 256 characters, without line breaks or other control characters.

        Returns:
            The created access bundle.
        """
        request_body = {
            "name": name,
            "description": description,
        }

        result = self.requests.post_once(
            path="/api/v1/agent-vault/access-bundles",
            json=request_body,
            model=SingleAgentVaultAccessBundleResponse
        )

        return result.data.accessBundle

    def update(
            self,
            access_bundle_id: str,
            name: Optional[str] = None,
            description: Optional[str] = None) -> AgentVaultAccessBundle:
        """Update an Agent Vault access bundle's name or description. Only the values you pass are changed.

        Args:
            access_bundle_id: The ID of the access bundle to update.
            name: The new name of the access bundle (a slug, at most 64 characters).
            description: The new description, up to 256 characters, without line breaks or other control characters. Pass an empty string to remove the description.

        Returns:
            The updated access bundle.
        """
        request_body = {
            "name": name,
            "description": description,
        }

        result = self.requests.patch(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}",
            json=request_body,
            model=SingleAgentVaultAccessBundleResponse
        )

        return result.data.accessBundle

    def delete(self, access_bundle_id: str) -> AgentVaultAccessBundle:
        """Delete an Agent Vault access bundle.

        Args:
            access_bundle_id: The ID of the access bundle to delete.

        Returns:
            The deleted access bundle.
        """
        result = self.requests.delete(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}",
            model=SingleAgentVaultAccessBundleResponse
        )

        return result.data.accessBundle

    def list_grantees(
            self,
            access_bundle_id: str,
            search: Optional[str] = None,
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultGranteesResponse:
        """List the users, machine identities and groups that an Agent Vault access bundle is granted to.

        Args:
            access_bundle_id: The ID of the access bundle.
            search: Match grantees by name, username or email address.
            limit: The maximum number of grantees to return (1-100). Defaults to 20.
            offset: How many grantees to skip. Defaults to 0.

        Returns:
            ListAgentVaultGranteesResponse containing the grantees in members, and totalCount.
        """
        params = {
            "search": search,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}/members",
            params=params,
            model=ListAgentVaultGranteesResponse
        )

        return result.data

    def list_available_grantees(
            self,
            access_bundle_id: str,
            search: Optional[str] = None,
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultMembersResponse:
        """List the Agent Vault members that an access bundle isn't granted to yet, so you can grant it to them.

        Args:
            access_bundle_id: The ID of the access bundle.
            search: Match members by name, username or email address.
            limit: The maximum number of members to return (1-100). Defaults to 20.
            offset: How many members to skip. Defaults to 0.

        Returns:
            ListAgentVaultMembersResponse containing members and totalCount.
        """
        params = {
            "search": search,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}/members/available",
            params=params,
            model=ListAgentVaultMembersResponse
        )

        return result.data

    def grant(
            self,
            access_bundle_id: str,
            user_ids: Optional[List[str]] = None,
            machine_identity_ids: Optional[List[str]] = None,
            group_ids: Optional[List[str]] = None) -> AgentVaultGrantChangeResponse:
        """Grant an Agent Vault access bundle to users, machine identities or groups. Each must be a member of Agent Vault. Name at least one, and at most 100 in total.

        Args:
            access_bundle_id: The ID of the access bundle.
            user_ids: The IDs of the users to grant the access bundle to.
            machine_identity_ids: The IDs of the machine identities to grant the access bundle to.
            group_ids: The IDs of the groups to grant the access bundle to.

        Returns:
            AgentVaultGrantChangeResponse with the new grants in members, and the grantees that already had the access bundle in skipped.
        """
        request_body = {
            "userIds": user_ids,
            "machineIdentityIds": machine_identity_ids,
            "groupIds": group_ids,
        }

        result = self.requests.post(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}/members",
            json=request_body,
            model=AgentVaultGrantChangeResponse
        )

        return result.data

    def revoke(
            self,
            access_bundle_id: str,
            user_ids: Optional[List[str]] = None,
            machine_identity_ids: Optional[List[str]] = None,
            group_ids: Optional[List[str]] = None) -> AgentVaultGrantChangeResponse:
        """Revoke an Agent Vault access bundle from users, machine identities or groups. Name at least one, and at most 100 in total.

        Args:
            access_bundle_id: The ID of the access bundle.
            user_ids: The IDs of the users to revoke the access bundle from.
            machine_identity_ids: The IDs of the machine identities to revoke the access bundle from.
            group_ids: The IDs of the groups to revoke the access bundle from.

        Returns:
            AgentVaultGrantChangeResponse with the revoked grants in members, and the grantees that didn't have the access bundle in skipped.
        """
        request_body = {
            "userIds": user_ids,
            "machineIdentityIds": machine_identity_ids,
            "groupIds": group_ids,
        }

        result = self.requests.delete(
            path=f"/api/v1/agent-vault/access-bundles/{access_bundle_id}/members",
            json=request_body,
            model=AgentVaultGrantChangeResponse
        )

        return result.data


class AgentVaultDelegations:
    """Manages Agent Vault delegations, which let machine identities create sessions on behalf of users. Every method requires the Admin role in Agent Vault, except that a machine identity can get its own delegation."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def list(
            self,
            machine_identity_ids: Optional[List[str]] = None,
            limit: int = 100,
            offset: int = 0) -> ListAgentVaultDelegationsResponse:
        """List the machine identities that can create Agent Vault sessions on behalf of users.

        Args:
            machine_identity_ids: Only return the delegations of these machine identities, up to 100.
            limit: The maximum number of delegations to return (1-100). Defaults to 100.
            offset: How many delegations to skip. Defaults to 0.

        Returns:
            ListAgentVaultDelegationsResponse containing delegations and totalCount. missingAccessBundles isn't set on these delegations; call get for it.
        """
        params = {
            "machineIdentityIds": ",".join(machine_identity_ids) if machine_identity_ids else None,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path="/api/v1/agent-vault/delegations",
            params=params,
            model=ListAgentVaultDelegationsResponse
        )

        return result.data

    def get(self, machine_identity_id: str) -> AgentVaultDelegation:
        """Get which users a machine identity can create Agent Vault sessions on behalf of. Raises an APIError with status 404 if the machine identity has no delegation.

        Args:
            machine_identity_id: The ID of the machine identity.

        Returns:
            The delegation. missingAccessBundles lists the access bundles that the users it covers can use and the machine identity can't, so the machine identity can't create sessions over them. They're empty when a machine identity that isn't an admin gets its own delegation.
        """
        result = self.requests.get(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}",
            model=SingleAgentVaultDelegationResponse
        )

        return result.data.delegation

    def set(
            self,
            machine_identity_id: str,
            scope: Union[AgentVaultDelegationScope, str],
            user_ids: Optional[List[str]] = None,
            group_ids: Optional[List[str]] = None) -> AgentVaultDelegation:
        """Set which users a machine identity can create Agent Vault sessions on behalf of, replacing any delegation it has.

        Args:
            machine_identity_id: The ID of the machine identity. It must be a member of Agent Vault.
            scope: AgentVaultDelegationScope.ALL_MEMBERS ("all-members") for every Agent Vault member, admins included, or AgentVaultDelegationScope.SELECTED ("selected") for only the users and groups you name.
            user_ids: With the "selected" scope, the users the machine identity can act on behalf of, up to 100. Each must be a member of Agent Vault. For a user who's in Agent Vault only through a group, name the group instead.
            group_ids: With the "selected" scope, the groups whose members the machine identity can act on behalf of, up to 100. Each must be a member of Agent Vault.

        Returns:
            The saved delegation, with missingAccessBundles.
        """
        request_body = {
            "scope": scope.value if isinstance(scope, AgentVaultDelegationScope) else scope,
            "userIds": user_ids,
            "groupIds": group_ids,
        }

        result = self.requests.put(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}",
            json=request_body,
            model=SingleAgentVaultDelegationResponse
        )

        return result.data.delegation

    def delete(self, machine_identity_id: str) -> AgentVaultDelegation:
        """Stop a machine identity from creating Agent Vault sessions on behalf of users. The sessions it already created on their behalf stop working.

        Args:
            machine_identity_id: The ID of the machine identity.

        Returns:
            The deleted delegation. missingAccessBundles isn't set.
        """
        result = self.requests.delete(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}",
            model=SingleAgentVaultDelegationResponse
        )

        return result.data.delegation

    def add_subjects(
            self,
            machine_identity_id: str,
            user_ids: Optional[List[str]] = None,
            group_ids: Optional[List[str]] = None) -> AgentVaultDelegation:
        """Add users and groups to a machine identity's delegation, keeping the ones it already names. If the machine identity has no delegation, this creates one with the "selected" scope. A delegation to all members can't take users or groups.

        Args:
            machine_identity_id: The ID of the machine identity.
            user_ids: The users to add, up to 100. Each must be a member of Agent Vault. Users the delegation already names are skipped.
            group_ids: The groups to add, up to 100. Each must be a member of Agent Vault. Groups the delegation already names are skipped.

        Returns:
            The delegation after the change, with missingAccessBundles.
        """
        request_body = {
            "userIds": user_ids,
            "groupIds": group_ids,
        }

        result = self.requests.post(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}/subjects",
            json=request_body,
            model=SingleAgentVaultDelegationResponse
        )

        return result.data.delegation

    def remove_subjects(
            self,
            machine_identity_id: str,
            user_ids: Optional[List[str]] = None,
            group_ids: Optional[List[str]] = None) -> Optional[AgentVaultDelegation]:
        """Take users and groups out of a machine identity's delegation. The sessions it created on behalf of the users you take out stop working, and taking out the last user or group removes the delegation.

        Args:
            machine_identity_id: The ID of the machine identity.
            user_ids: The users to take out, up to 100. Users the delegation doesn't name are skipped.
            group_ids: The groups to take out, up to 100. Groups the delegation doesn't name are skipped.

        Returns:
            The delegation after the change, with missingAccessBundles, or None if it no longer names anyone.
        """
        request_body = {
            "userIds": user_ids,
            "groupIds": group_ids,
        }

        result = self.requests.delete(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}/subjects",
            json=request_body,
            model=SingleAgentVaultDelegationResponse
        )

        return result.data.delegation

    def list_available_subjects(
            self,
            machine_identity_id: str,
            actor_type: Optional[Union[AgentVaultMemberType, str]] = None,
            search: Optional[str] = None,
            limit: int = 20,
            offset: int = 0) -> ListAgentVaultMembersResponse:
        """List the Agent Vault users and groups that can still be added to a machine identity's delegation.

        Args:
            machine_identity_id: The ID of the machine identity. It must be a member of Agent Vault.
            actor_type: List only users (AgentVaultMemberType.USER) or only groups (AgentVaultMemberType.GROUP). Defaults to both.
            search: Match users by name, username or email address, and groups by name.
            limit: The maximum number of users and groups to return (1-100). Defaults to 20.
            offset: How many users and groups to skip. Defaults to 0.

        Returns:
            ListAgentVaultMembersResponse containing the users and groups in members, and totalCount.
        """
        params = {
            "actorType": actor_type.value if isinstance(actor_type, AgentVaultMemberType) else actor_type,
            "search": search,
            "limit": limit,
            "offset": offset,
        }

        result = self.requests.get(
            path=f"/api/v1/agent-vault/delegations/{machine_identity_id}/subjects/available",
            params=params,
            model=ListAgentVaultMembersResponse
        )

        return result.data


class AgentVault:
    """Manages Infisical Agent Vault."""

    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests
        self.proxies = AgentVaultProxies(requests)
        self.sessions = AgentVaultSessions(requests)
        self.access_bundles = AgentVaultAccessBundles(requests)
        self.delegations = AgentVaultDelegations(requests)
