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

from infisicalapi_client.models.api_v1_integration_auth_integration_options_get200_response import ApiV1IntegrationAuthIntegrationOptionsGet200Response  # noqa: E501

class TestApiV1IntegrationAuthIntegrationOptionsGet200Response(unittest.TestCase):
    """ApiV1IntegrationAuthIntegrationOptionsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationAuthIntegrationOptionsGet200Response:
        """Test ApiV1IntegrationAuthIntegrationOptionsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationAuthIntegrationOptionsGet200Response`
        """
        model = ApiV1IntegrationAuthIntegrationOptionsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationAuthIntegrationOptionsGet200Response(
                integration_options = [
                    infisicalapi_client.models._api_v1_integration_auth_integration_options_get_200_response_integration_options_inner._api_v1_integration_auth_integration_options_get_200_response_integrationOptions_inner(
                        name = '', 
                        slug = '', 
                        client_slug = '', 
                        image = '', 
                        is_available = True, 
                        type = '', 
                        client_id = '', 
                        docs_link = '', )
                    ]
            )
        else:
            return ApiV1IntegrationAuthIntegrationOptionsGet200Response(
                integration_options = [
                    infisicalapi_client.models._api_v1_integration_auth_integration_options_get_200_response_integration_options_inner._api_v1_integration_auth_integration_options_get_200_response_integrationOptions_inner(
                        name = '', 
                        slug = '', 
                        client_slug = '', 
                        image = '', 
                        is_available = True, 
                        type = '', 
                        client_id = '', 
                        docs_link = '', )
                    ],
        )
        """

    def testApiV1IntegrationAuthIntegrationOptionsGet200Response(self):
        """Test ApiV1IntegrationAuthIntegrationOptionsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()