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

from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential import ApiV1ExternalKmsPostRequestProviderInputsCredential  # noqa: E501

class TestApiV1ExternalKmsPostRequestProviderInputsCredential(unittest.TestCase):
    """ApiV1ExternalKmsPostRequestProviderInputsCredential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ExternalKmsPostRequestProviderInputsCredential:
        """Test ApiV1ExternalKmsPostRequestProviderInputsCredential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ExternalKmsPostRequestProviderInputsCredential`
        """
        model = ApiV1ExternalKmsPostRequestProviderInputsCredential()  # noqa: E501
        if include_optional:
            return ApiV1ExternalKmsPostRequestProviderInputsCredential(
                type = 'access-key',
                data = infisicalapi_client.models._api_v1_external_kms_post_request_provider_inputs_credential_any_of_1_data._api_v1_external_kms_post_request_provider_inputs_credential_anyOf_1_data(
                    assume_role_arn = '0', 
                    external_id = '0', )
            )
        else:
            return ApiV1ExternalKmsPostRequestProviderInputsCredential(
                type = 'access-key',
                data = infisicalapi_client.models._api_v1_external_kms_post_request_provider_inputs_credential_any_of_1_data._api_v1_external_kms_post_request_provider_inputs_credential_anyOf_1_data(
                    assume_role_arn = '0', 
                    external_id = '0', ),
        )
        """

    def testApiV1ExternalKmsPostRequestProviderInputsCredential(self):
        """Test ApiV1ExternalKmsPostRequestProviderInputsCredential"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
