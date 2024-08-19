# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request import ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest  # noqa: E501

class TestApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest(unittest.TestCase):
    """ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest:
        """Test ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest`
        """
        model = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest(
                description = '',
                num_uses_limit = 0,
                ttl = 0
            )
        else:
            return ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest(
        )
        """

    def testApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest(self):
        """Test ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
