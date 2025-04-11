from .infisical_requests import InfisicalRequests

from infisical_sdk.resources import Auth
from infisical_sdk.resources import V3RawSecrets
from infisical_sdk.resources import KMS

from infisical_sdk.util import SecretsCache

class InfisicalSDKClient:
    def __init__(self, host: str, token: str = None, cache_ttl: int = 60, verifySSL: bool = True):
        """
        Initialize the Infisical SDK client.

        :param str host: The host URL for your Infisical instance. Will default to `https://app.infisical.com` if not specified.
        :param str token: The authentication token for the client. If not specified, you can use the `auth` methods to authenticate.
        :param int cache_ttl: The time to live for the secrets cache. This is the number of seconds that secrets fetched from the API will be cached for. Set to `None` to disable caching. Defaults to `60` seconds.
        """
        
        self.host = host
        self.access_token = token
        self.verifySSL = verifySSL

        self.api = InfisicalRequests(host=host, token=token, verifySSL=verifySSL)
        self.cache = SecretsCache(cache_ttl)
        self.auth = Auth(self.api, self.set_token)
        self.secrets = V3RawSecrets(self.api, self.cache)
        self.kms = KMS(self.api)

    def set_token(self, token: str):
        """
        Set the access token for future requests.
        """
        self.api.set_token(token)
        self.access_token = token

    def get_token(self):
        """
        Set the access token for future requests.
        """
        return self.access_token

