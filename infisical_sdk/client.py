from .infisical_requests import InfisicalRequests

from infisical_sdk.resources import Auth
from infisical_sdk.resources import V3RawSecrets
from infisical_sdk.resources import KMS
from infisical_sdk.resources import V2Folders
from infisical_sdk.resources import DynamicSecrets

from infisical_sdk.util import SecretsCache

class InfisicalSDKClient:
    def __init__(self, host: str, token: str = None, cache_ttl: int = 60, timeout: float = 30):
        """
        Initialize the Infisical SDK client.

        :param str host: The host URL for your Infisical instance. Will default to `https://app.infisical.com` if not specified.
        :param str token: The authentication token for the client. If not specified, you can use the `auth` methods to authenticate.
        :param int cache_ttl: The time to live for the secrets cache. This is the number of seconds that secrets fetched from the API will be cached for. Set to `None` to disable caching. Defaults to `60` seconds.
        :param float timeout: The number of seconds to wait for each HTTP request. Set to `None` to disable the timeout. Defaults to `30` seconds.
        """
        
        self.host = host
        self.access_token = token

        self.api = InfisicalRequests(host=host, token=token, timeout=timeout)
        self.cache = SecretsCache(cache_ttl)
        self.auth = Auth(self.api, self.set_token)
        self.secrets = V3RawSecrets(self.api, self.cache)
        self.kms = KMS(self.api)
        self.folders = V2Folders(self.api)
        self.dynamic_secrets = DynamicSecrets(self.api)

    def set_token(self, token: str):
        """
        Set the access token for future requests.
        """
        self.api.set_token(token)
        self.access_token = token

    def get_token(self):
        """
        Get the access token for future requests.
        """
        return self.access_token

    def close(self):
        """
        Close the client and release resources.
        
        This stops the background cache cleanup thread. You don't need to call
        this if you're using the client as a context manager (with statement),
        as cleanup happens automatically when exiting the context.
        """
        if self.cache:
            self.cache.close()

    # These are automatically called if using the client as a context manager (on start)
    # Example:
    # with InfisicalSDKClient(...) as client:
    # ...  
    def __enter__(self) -> "InfisicalSDKClient":
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Ensure cleanup when exiting context."""
        self.close()