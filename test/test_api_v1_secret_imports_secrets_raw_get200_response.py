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

from infisicalapi_client.models.api_v1_secret_imports_secrets_raw_get200_response import ApiV1SecretImportsSecretsRawGet200Response  # noqa: E501

class TestApiV1SecretImportsSecretsRawGet200Response(unittest.TestCase):
    """ApiV1SecretImportsSecretsRawGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretImportsSecretsRawGet200Response:
        """Test ApiV1SecretImportsSecretsRawGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretImportsSecretsRawGet200Response`
        """
        model = ApiV1SecretImportsSecretsRawGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretImportsSecretsRawGet200Response(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_imports_secrets_raw_get_200_response_secrets_inner._api_v1_secret_imports_secrets_raw_get_200_response_secrets_inner(
                        secret_path = '', 
                        environment = '', 
                        environment_info = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                            id = '', 
                            name = '', 
                            slug = '', ), 
                        folder_id = '', 
                        secrets = [
                            infisicalapi_client.models._api_v1_secret__secret_id__secret_versions_get_200_response_secret_versions_inner._api_v1_secret__secretId__secret_versions_get_200_response_secretVersions_inner(
                                id = '', 
                                _id = '', 
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
                                metadata = null, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ]
            )
        else:
            return ApiV1SecretImportsSecretsRawGet200Response(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_imports_secrets_raw_get_200_response_secrets_inner._api_v1_secret_imports_secrets_raw_get_200_response_secrets_inner(
                        secret_path = '', 
                        environment = '', 
                        environment_info = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                            id = '', 
                            name = '', 
                            slug = '', ), 
                        folder_id = '', 
                        secrets = [
                            infisicalapi_client.models._api_v1_secret__secret_id__secret_versions_get_200_response_secret_versions_inner._api_v1_secret__secretId__secret_versions_get_200_response_secretVersions_inner(
                                id = '', 
                                _id = '', 
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
                                metadata = null, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
        )
        """

    def testApiV1SecretImportsSecretsRawGet200Response(self):
        """Test ApiV1SecretImportsSecretsRawGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
