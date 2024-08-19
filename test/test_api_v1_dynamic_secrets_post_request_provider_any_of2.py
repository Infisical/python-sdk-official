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

from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of2 import ApiV1DynamicSecretsPostRequestProviderAnyOf2  # noqa: E501

class TestApiV1DynamicSecretsPostRequestProviderAnyOf2(unittest.TestCase):
    """ApiV1DynamicSecretsPostRequestProviderAnyOf2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1DynamicSecretsPostRequestProviderAnyOf2:
        """Test ApiV1DynamicSecretsPostRequestProviderAnyOf2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1DynamicSecretsPostRequestProviderAnyOf2`
        """
        model = ApiV1DynamicSecretsPostRequestProviderAnyOf2()  # noqa: E501
        if include_optional:
            return ApiV1DynamicSecretsPostRequestProviderAnyOf2(
                type = 'aws-iam',
                inputs = infisicalapi_client.models._api_v1_dynamic_secrets_post_request_provider_any_of_2_inputs._api_v1_dynamic_secrets_post_request_provider_anyOf_2_inputs(
                    access_key = '0', 
                    secret_access_key = '0', 
                    region = '0', 
                    aws_path = '', 
                    permission_boundary_policy_arn = '', 
                    policy_document = '', 
                    user_groups = '', 
                    policy_arns = '', )
            )
        else:
            return ApiV1DynamicSecretsPostRequestProviderAnyOf2(
                type = 'aws-iam',
                inputs = infisicalapi_client.models._api_v1_dynamic_secrets_post_request_provider_any_of_2_inputs._api_v1_dynamic_secrets_post_request_provider_anyOf_2_inputs(
                    access_key = '0', 
                    secret_access_key = '0', 
                    region = '0', 
                    aws_path = '', 
                    permission_boundary_policy_arn = '', 
                    policy_document = '', 
                    user_groups = '', 
                    policy_arns = '', ),
        )
        """

    def testApiV1DynamicSecretsPostRequestProviderAnyOf2(self):
        """Test ApiV1DynamicSecretsPostRequestProviderAnyOf2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
