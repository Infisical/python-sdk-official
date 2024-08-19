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

from infisicalapi_client.models.api_v1_dynamic_secrets_name_get200_response import ApiV1DynamicSecretsNameGet200Response  # noqa: E501

class TestApiV1DynamicSecretsNameGet200Response(unittest.TestCase):
    """ApiV1DynamicSecretsNameGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1DynamicSecretsNameGet200Response:
        """Test ApiV1DynamicSecretsNameGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1DynamicSecretsNameGet200Response`
        """
        model = ApiV1DynamicSecretsNameGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1DynamicSecretsNameGet200Response(
                dynamic_secret = infisicalapi_client.models._api_v1_dynamic_secrets__name__get_200_response_dynamic_secret._api_v1_dynamic_secrets__name__get_200_response_dynamicSecret(
                    id = '', 
                    name = '', 
                    version = 1.337, 
                    type = '', 
                    default_ttl = '', 
                    max_ttl = '', 
                    folder_id = '', 
                    status = '', 
                    status_details = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    inputs = null, )
            )
        else:
            return ApiV1DynamicSecretsNameGet200Response(
                dynamic_secret = infisicalapi_client.models._api_v1_dynamic_secrets__name__get_200_response_dynamic_secret._api_v1_dynamic_secrets__name__get_200_response_dynamicSecret(
                    id = '', 
                    name = '', 
                    version = 1.337, 
                    type = '', 
                    default_ttl = '', 
                    max_ttl = '', 
                    folder_id = '', 
                    status = '', 
                    status_details = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    inputs = null, ),
        )
        """

    def testApiV1DynamicSecretsNameGet200Response(self):
        """Test ApiV1DynamicSecretsNameGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()