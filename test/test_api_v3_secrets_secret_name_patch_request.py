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

from infisicalapi_client.models.api_v3_secrets_secret_name_patch_request import ApiV3SecretsSecretNamePatchRequest  # noqa: E501

class TestApiV3SecretsSecretNamePatchRequest(unittest.TestCase):
    """ApiV3SecretsSecretNamePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsSecretNamePatchRequest:
        """Test ApiV3SecretsSecretNamePatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsSecretNamePatchRequest`
        """
        model = ApiV3SecretsSecretNamePatchRequest()  # noqa: E501
        if include_optional:
            return ApiV3SecretsSecretNamePatchRequest(
                workspace_id = '',
                environment = '',
                secret_id = '',
                type = 'shared',
                secret_path = '/',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
                secret_comment_ciphertext = '',
                secret_comment_iv = '',
                secret_comment_tag = '',
                secret_reminder_repeat_days = 1,
                secret_reminder_note = '',
                tags = [
                    ''
                    ],
                skip_multiline_encoding = True,
                secret_name = '',
                secret_key_iv = '',
                secret_key_tag = '',
                secret_key_ciphertext = '',
                metadata = {
                    'key' : ''
                    }
            )
        else:
            return ApiV3SecretsSecretNamePatchRequest(
                workspace_id = '',
                environment = '',
                secret_value_ciphertext = '',
                secret_value_iv = '',
                secret_value_tag = '',
        )
        """

    def testApiV3SecretsSecretNamePatchRequest(self):
        """Test ApiV3SecretsSecretNamePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
