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

from infisicalapi_client.models.api_v3_auth_login2_post_request import ApiV3AuthLogin2PostRequest  # noqa: E501

class TestApiV3AuthLogin2PostRequest(unittest.TestCase):
    """ApiV3AuthLogin2PostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3AuthLogin2PostRequest:
        """Test ApiV3AuthLogin2PostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3AuthLogin2PostRequest`
        """
        model = ApiV3AuthLogin2PostRequest()  # noqa: E501
        if include_optional:
            return ApiV3AuthLogin2PostRequest(
                email = '',
                provider_auth_token = '',
                client_proof = '',
                captcha_token = '',
                password = ''
            )
        else:
            return ApiV3AuthLogin2PostRequest(
                email = '',
                client_proof = '',
        )
        """

    def testApiV3AuthLogin2PostRequest(self):
        """Test ApiV3AuthLogin2PostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
