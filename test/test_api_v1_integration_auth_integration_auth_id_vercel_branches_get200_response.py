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

from infisicalapi_client.models.api_v1_integration_auth_integration_auth_id_vercel_branches_get200_response import ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response  # noqa: E501

class TestApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response(unittest.TestCase):
    """ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response:
        """Test ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response`
        """
        model = ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response(
                branches = [
                    ''
                    ]
            )
        else:
            return ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response(
                branches = [
                    ''
                    ],
        )
        """

    def testApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response(self):
        """Test ApiV1IntegrationAuthIntegrationAuthIdVercelBranchesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
