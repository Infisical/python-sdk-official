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

from infisicalapi_client.models.api_v1_auth_azure_auth_identities_identity_id_post_request import ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest  # noqa: E501

class TestApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest(unittest.TestCase):
    """ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest:
        """Test ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest`
        """
        model = ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest(
                tenant_id = '',
                resource = '',
                allowed_service_principal_ids = '',
                access_token_trusted_ips = [
                    infisicalapi_client.models._api_v1_auth_token_auth_identities__identity_id__post_request_access_token_trusted_ips_inner._api_v1_auth_token_auth_identities__identityId__post_request_accessTokenTrustedIps_inner(
                        ip_address = '', )
                    ],
                access_token_ttl = 1,
                access_token_max_ttl = 56,
                access_token_num_uses_limit = 0
            )
        else:
            return ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest(
                tenant_id = '',
                resource = '',
        )
        """

    def testApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest(self):
        """Test ApiV1AuthAzureAuthIdentitiesIdentityIdPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()