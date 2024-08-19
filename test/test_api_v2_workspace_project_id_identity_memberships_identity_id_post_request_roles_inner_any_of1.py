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

from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_post_request_roles_inner_any_of1 import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1  # noqa: E501

class TestApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1(unittest.TestCase):
    """ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1:
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1`
        """
        model = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1()  # noqa: E501
        if include_optional:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1(
                role = '',
                is_temporary = True,
                temporary_mode = 'relative',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1(
                role = '',
                is_temporary = True,
                temporary_mode = 'relative',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1(self):
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInnerAnyOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()