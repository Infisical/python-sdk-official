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

from infisicalapi_client.models.api_v3_secrets_get200_response_imports_inner_secrets_inner import ApiV3SecretsGet200ResponseImportsInnerSecretsInner  # noqa: E501

class TestApiV3SecretsGet200ResponseImportsInnerSecretsInner(unittest.TestCase):
    """ApiV3SecretsGet200ResponseImportsInnerSecretsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsGet200ResponseImportsInnerSecretsInner:
        """Test ApiV3SecretsGet200ResponseImportsInnerSecretsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsGet200ResponseImportsInnerSecretsInner`
        """
        model = ApiV3SecretsGet200ResponseImportsInnerSecretsInner()  # noqa: E501
        if include_optional:
            return ApiV3SecretsGet200ResponseImportsInnerSecretsInner(
                id = '',
                version = 1.337,
                type = 'shared',
                secret_key_ciphertext = '',
                secret_key_iv = '',
                secret_key_tag = '',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
                secret_comment_ciphertext = '',
                secret_comment_iv = '',
                secret_comment_tag = '',
                secret_reminder_note = '',
                secret_reminder_repeat_days = 1.337,
                skip_multiline_encoding = True,
                algorithm = 'aes-256-gcm',
                key_encoding = 'utf8',
                metadata = None,
                user_id = '',
                folder_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                workspace = '',
                environment = ''
            )
        else:
            return ApiV3SecretsGet200ResponseImportsInnerSecretsInner(
                id = '',
                secret_key_ciphertext = '',
                secret_key_iv = '',
                secret_key_tag = '',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
                folder_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                workspace = '',
                environment = '',
        )
        """

    def testApiV3SecretsGet200ResponseImportsInnerSecretsInner(self):
        """Test ApiV3SecretsGet200ResponseImportsInnerSecretsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
