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

from infisicalapi_client.models.api_v3_secrets_move_post_request import ApiV3SecretsMovePostRequest  # noqa: E501

class TestApiV3SecretsMovePostRequest(unittest.TestCase):
    """ApiV3SecretsMovePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsMovePostRequest:
        """Test ApiV3SecretsMovePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsMovePostRequest`
        """
        model = ApiV3SecretsMovePostRequest()  # noqa: E501
        if include_optional:
            return ApiV3SecretsMovePostRequest(
                project_slug = '',
                source_environment = '',
                source_secret_path = '/',
                destination_environment = '',
                destination_secret_path = '/',
                secret_ids = [
                    ''
                    ],
                should_overwrite = True
            )
        else:
            return ApiV3SecretsMovePostRequest(
                project_slug = '',
                source_environment = '',
                destination_environment = '',
                secret_ids = [
                    ''
                    ],
        )
        """

    def testApiV3SecretsMovePostRequest(self):
        """Test ApiV3SecretsMovePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
