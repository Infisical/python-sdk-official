from typing import Callable, Optional

from infisical_sdk.api_types import MachineIdentityLoginResponse
from infisical_sdk.infisical_requests import InfisicalRequests


class JwtAuth:
    def __init__(self, requests: InfisicalRequests, setToken: Callable[[str], None]):
        self.requests = requests
        self.setToken = setToken

    def login(
        self,
        identity_id: str,
        jwt: str,
        organization_slug: Optional[str] = None,
    ) -> MachineIdentityLoginResponse:
        """Log in a Machine Identity configured with JWT Auth.

        Args:
            identity_id: Your Machine Identity ID.
            jwt: The JWT accepted by the identity's JWT Auth configuration.
            organization_slug: Optional organization slug for the login request.

        Returns:
            The access token and related information. The client's token is
            updated only after a successful login.
        """
        result = self.requests.post(
            path="/api/v1/auth/jwt-auth/login",
            json={
                "identityId": identity_id,
                "jwt": jwt,
                "organizationSlug": organization_slug,
            },
            model=MachineIdentityLoginResponse,
        )
        self.setToken(result.data.accessToken)
        return result.data
