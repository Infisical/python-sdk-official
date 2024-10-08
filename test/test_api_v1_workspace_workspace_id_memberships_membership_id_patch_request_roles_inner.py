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

from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner import ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner:
        """Test ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner`
        """
        model = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner(
                role = '',
                is_temporary = True,
                temporary_mode = 'relative',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner(
                role = '',
                is_temporary = True,
                temporary_mode = 'relative',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner(self):
        """Test ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
