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

from infisicalapi_client.models.api_v3_secrets_batch_raw_post_request import ApiV3SecretsBatchRawPostRequest  # noqa: E501

class TestApiV3SecretsBatchRawPostRequest(unittest.TestCase):
    """ApiV3SecretsBatchRawPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsBatchRawPostRequest:
        """Test ApiV3SecretsBatchRawPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsBatchRawPostRequest`
        """
        model = ApiV3SecretsBatchRawPostRequest()  # noqa: E501
        if include_optional:
            return ApiV3SecretsBatchRawPostRequest(
                project_slug = '',
                workspace_id = '',
                environment = '',
                secret_path = '/',
                secrets = [
                    infisicalapi_client.models._api_v3_secrets_batch_raw_post_request_secrets_inner._api_v3_secrets_batch_raw_post_request_secrets_inner(
                        secret_key = '', 
                        secret_value = '', 
                        secret_comment = '', 
                        skip_multiline_encoding = True, 
                        metadata = {
                            'key' : ''
                            }, 
                        tag_ids = [
                            ''
                            ], )
                    ]
            )
        else:
            return ApiV3SecretsBatchRawPostRequest(
                environment = '',
                secrets = [
                    infisicalapi_client.models._api_v3_secrets_batch_raw_post_request_secrets_inner._api_v3_secrets_batch_raw_post_request_secrets_inner(
                        secret_key = '', 
                        secret_value = '', 
                        secret_comment = '', 
                        skip_multiline_encoding = True, 
                        metadata = {
                            'key' : ''
                            }, 
                        tag_ids = [
                            ''
                            ], )
                    ],
        )
        """

    def testApiV3SecretsBatchRawPostRequest(self):
        """Test ApiV3SecretsBatchRawPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
