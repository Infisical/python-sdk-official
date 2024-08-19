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

from infisicalapi_client.models.api_v3_secrets_raw_get200_response_imports_inner_secrets_inner import ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner  # noqa: E501

class TestApiV3SecretsRawGet200ResponseImportsInnerSecretsInner(unittest.TestCase):
    """ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner:
        """Test ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner`
        """
        model = ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner()  # noqa: E501
        if include_optional:
            return ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner(
                id = '',
                id = '',
                workspace = '',
                environment = '',
                version = 1.337,
                type = '',
                secret_key = '',
                secret_value = '',
                secret_comment = '',
                secret_reminder_note = '',
                secret_reminder_repeat_days = 1.337,
                skip_multiline_encoding = True,
                metadata = None
            )
        else:
            return ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner(
                id = '',
                id = '',
                workspace = '',
                environment = '',
                version = 1.337,
                type = '',
                secret_key = '',
                secret_value = '',
                secret_comment = '',
        )
        """

    def testApiV3SecretsRawGet200ResponseImportsInnerSecretsInner(self):
        """Test ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
