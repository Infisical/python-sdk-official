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

from infisicalapi_client.models.api_v3_secrets_raw_secret_name_post200_response import ApiV3SecretsRawSecretNamePost200Response  # noqa: E501

class TestApiV3SecretsRawSecretNamePost200Response(unittest.TestCase):
    """ApiV3SecretsRawSecretNamePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsRawSecretNamePost200Response:
        """Test ApiV3SecretsRawSecretNamePost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsRawSecretNamePost200Response`
        """
        model = ApiV3SecretsRawSecretNamePost200Response()  # noqa: E501
        if include_optional:
            return ApiV3SecretsRawSecretNamePost200Response(
                secret = infisicalapi_client.models._api_v1_secret__secret_id__secret_versions_get_200_response_secret_versions_inner._api_v1_secret__secretId__secret_versions_get_200_response_secretVersions_inner(
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
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                approval = infisicalapi_client.models._api_v1_secret_approval_requests__id__merge_post_200_response_approval._api_v1_secret_approval_requests__id__merge_post_200_response_approval(
                    id = '', 
                    policy_id = '', 
                    has_merged = True, 
                    status = 'open', 
                    conflicts = null, 
                    slug = '', 
                    folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_replicated = True, 
                    committer_user_id = '', 
                    status_changed_by_user_id = '', 
                    bypass_reason = '', )
            )
        else:
            return ApiV3SecretsRawSecretNamePost200Response(
                secret = infisicalapi_client.models._api_v1_secret__secret_id__secret_versions_get_200_response_secret_versions_inner._api_v1_secret__secretId__secret_versions_get_200_response_secretVersions_inner(
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
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                approval = infisicalapi_client.models._api_v1_secret_approval_requests__id__merge_post_200_response_approval._api_v1_secret_approval_requests__id__merge_post_200_response_approval(
                    id = '', 
                    policy_id = '', 
                    has_merged = True, 
                    status = 'open', 
                    conflicts = null, 
                    slug = '', 
                    folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_replicated = True, 
                    committer_user_id = '', 
                    status_changed_by_user_id = '', 
                    bypass_reason = '', ),
        )
        """

    def testApiV3SecretsRawSecretNamePost200Response(self):
        """Test ApiV3SecretsRawSecretNamePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
