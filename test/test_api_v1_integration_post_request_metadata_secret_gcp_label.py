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

from infisicalapi_client.models.api_v1_integration_post_request_metadata_secret_gcp_label import ApiV1IntegrationPostRequestMetadataSecretGCPLabel  # noqa: E501

class TestApiV1IntegrationPostRequestMetadataSecretGCPLabel(unittest.TestCase):
    """ApiV1IntegrationPostRequestMetadataSecretGCPLabel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationPostRequestMetadataSecretGCPLabel:
        """Test ApiV1IntegrationPostRequestMetadataSecretGCPLabel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationPostRequestMetadataSecretGCPLabel`
        """
        model = ApiV1IntegrationPostRequestMetadataSecretGCPLabel()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationPostRequestMetadataSecretGCPLabel(
                label_name = '',
                label_value = ''
            )
        else:
            return ApiV1IntegrationPostRequestMetadataSecretGCPLabel(
                label_name = '',
                label_value = '',
        )
        """

    def testApiV1IntegrationPostRequestMetadataSecretGCPLabel(self):
        """Test ApiV1IntegrationPostRequestMetadataSecretGCPLabel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
