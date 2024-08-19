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

from infisicalapi_client.models.api_v1_auth_kubernetes_auth_identities_identity_id_patch_request import ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest  # noqa: E501

class TestApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest(unittest.TestCase):
    """ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest:
        """Test ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest`
        """
        model = ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest(
                kubernetes_host = '0',
                ca_cert = '',
                token_reviewer_jwt = '0',
                allowed_namespaces = '',
                allowed_names = '',
                allowed_audience = '',
                access_token_trusted_ips = [
                    infisicalapi_client.models._api_v1_auth_token_auth_identities__identity_id__post_request_access_token_trusted_ips_inner._api_v1_auth_token_auth_identities__identityId__post_request_accessTokenTrustedIps_inner(
                        ip_address = '', )
                    ],
                access_token_ttl = 0,
                access_token_num_uses_limit = 0,
                access_token_max_ttl = 56
            )
        else:
            return ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest(
        )
        """

    def testApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest(self):
        """Test ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
