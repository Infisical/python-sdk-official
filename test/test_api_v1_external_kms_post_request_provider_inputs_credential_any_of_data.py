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

from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential_any_of_data import ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData  # noqa: E501

class TestApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData(unittest.TestCase):
    """ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData:
        """Test ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData`
        """
        model = ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData()  # noqa: E501
        if include_optional:
            return ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData(
                access_key = '0',
                secret_key = '0'
            )
        else:
            return ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData(
                access_key = '0',
                secret_key = '0',
        )
        """

    def testApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData(self):
        """Test ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOfData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()