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

from infisicalapi_client.models.api_v1_integration_auth_integration_auth_id_northflank_secret_groups_get200_response_secret_groups_inner import ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner  # noqa: E501

class TestApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner(unittest.TestCase):
    """ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner:
        """Test ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner`
        """
        model = ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner(
                name = '',
                group_id = ''
            )
        else:
            return ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner(
                name = '',
                group_id = '',
        )
        """

    def testApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner(self):
        """Test ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
