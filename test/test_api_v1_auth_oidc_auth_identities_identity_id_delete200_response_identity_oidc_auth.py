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

from infisicalapi_client.models.api_v1_auth_oidc_auth_identities_identity_id_delete200_response_identity_oidc_auth import ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth  # noqa: E501

class TestApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth(unittest.TestCase):
    """ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth:
        """Test ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth`
        """
        model = ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth()  # noqa: E501
        if include_optional:
            return ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth(
                id = '',
                access_token_ttl = 1.337,
                access_token_max_ttl = 1.337,
                access_token_num_uses_limit = 1.337,
                access_token_trusted_ips = None,
                identity_id = '',
                oidc_discovery_url = '',
                bound_issuer = '',
                bound_audiences = '',
                bound_claims = None,
                bound_subject = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth(
                id = '',
                identity_id = '',
                oidc_discovery_url = '',
                bound_issuer = '',
                bound_audiences = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth(self):
        """Test ApiV1AuthOidcAuthIdentitiesIdentityIdDelete200ResponseIdentityOidcAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
