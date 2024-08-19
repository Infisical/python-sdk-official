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

from infisicalapi_client.models.api_v1_dynamic_secrets_name_delete_request import ApiV1DynamicSecretsNameDeleteRequest  # noqa: E501

class TestApiV1DynamicSecretsNameDeleteRequest(unittest.TestCase):
    """ApiV1DynamicSecretsNameDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1DynamicSecretsNameDeleteRequest:
        """Test ApiV1DynamicSecretsNameDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1DynamicSecretsNameDeleteRequest`
        """
        model = ApiV1DynamicSecretsNameDeleteRequest()  # noqa: E501
        if include_optional:
            return ApiV1DynamicSecretsNameDeleteRequest(
                project_slug = '0',
                path = '/',
                environment_slug = '0',
                is_forced = True
            )
        else:
            return ApiV1DynamicSecretsNameDeleteRequest(
                project_slug = '0',
                environment_slug = '0',
        )
        """

    def testApiV1DynamicSecretsNameDeleteRequest(self):
        """Test ApiV1DynamicSecretsNameDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
