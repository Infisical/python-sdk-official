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

from infisicalapi_client.models.api_v1_auth_gcp_auth_identities_identity_id_get200_response import ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response  # noqa: E501

class TestApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response(unittest.TestCase):
    """ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response:
        """Test ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response`
        """
        model = ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response(
                identity_gcp_auth = infisicalapi_client.models._api_v1_auth_gcp_auth_identities__identity_id__get_200_response_identity_gcp_auth._api_v1_auth_gcp_auth_identities__identityId__get_200_response_identityGcpAuth(
                    id = '', 
                    access_token_ttl = 1.337, 
                    access_token_max_ttl = 1.337, 
                    access_token_num_uses_limit = 1.337, 
                    access_token_trusted_ips = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identity_id = '', 
                    type = '', 
                    allowed_service_accounts = '', 
                    allowed_projects = '', 
                    allowed_zones = '', )
            )
        else:
            return ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response(
                identity_gcp_auth = infisicalapi_client.models._api_v1_auth_gcp_auth_identities__identity_id__get_200_response_identity_gcp_auth._api_v1_auth_gcp_auth_identities__identityId__get_200_response_identityGcpAuth(
                    id = '', 
                    access_token_ttl = 1.337, 
                    access_token_max_ttl = 1.337, 
                    access_token_num_uses_limit = 1.337, 
                    access_token_trusted_ips = null, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identity_id = '', 
                    type = '', 
                    allowed_service_accounts = '', 
                    allowed_projects = '', 
                    allowed_zones = '', ),
        )
        """

    def testApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response(self):
        """Test ApiV1AuthGcpAuthIdentitiesIdentityIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
