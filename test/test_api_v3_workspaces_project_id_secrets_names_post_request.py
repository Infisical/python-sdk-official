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

from infisicalapi_client.models.api_v3_workspaces_project_id_secrets_names_post_request import ApiV3WorkspacesProjectIdSecretsNamesPostRequest  # noqa: E501

class TestApiV3WorkspacesProjectIdSecretsNamesPostRequest(unittest.TestCase):
    """ApiV3WorkspacesProjectIdSecretsNamesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3WorkspacesProjectIdSecretsNamesPostRequest:
        """Test ApiV3WorkspacesProjectIdSecretsNamesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3WorkspacesProjectIdSecretsNamesPostRequest`
        """
        model = ApiV3WorkspacesProjectIdSecretsNamesPostRequest()  # noqa: E501
        if include_optional:
            return ApiV3WorkspacesProjectIdSecretsNamesPostRequest(
                secrets_to_update = [
                    infisicalapi_client.models._api_v3_workspaces__project_id__secrets_names_post_request_secrets_to_update_inner._api_v3_workspaces__projectId__secrets_names_post_request_secretsToUpdate_inner(
                        secret_name = '', 
                        secret_id = '', )
                    ]
            )
        else:
            return ApiV3WorkspacesProjectIdSecretsNamesPostRequest(
                secrets_to_update = [
                    infisicalapi_client.models._api_v3_workspaces__project_id__secrets_names_post_request_secrets_to_update_inner._api_v3_workspaces__projectId__secrets_names_post_request_secretsToUpdate_inner(
                        secret_name = '', 
                        secret_id = '', )
                    ],
        )
        """

    def testApiV3WorkspacesProjectIdSecretsNamesPostRequest(self):
        """Test ApiV3WorkspacesProjectIdSecretsNamesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()