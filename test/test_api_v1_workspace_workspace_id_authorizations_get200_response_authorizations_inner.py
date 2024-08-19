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

from infisicalapi_client.models.api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner import ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner:
        """Test ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner`
        """
        model = ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner(
                id = '',
                project_id = '',
                integration = '',
                team_id = '',
                url = '',
                namespace = '',
                account_id = '',
                metadata = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner(
                id = '',
                project_id = '',
                integration = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner(self):
        """Test ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
