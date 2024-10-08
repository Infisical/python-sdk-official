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

from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_any_of import ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf:
        """Test ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf`
        """
        model = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf(
                role = '',
                is_temporary = True
            )
        else:
            return ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf(
                role = '',
        )
        """

    def testApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf(self):
        """Test ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInnerAnyOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
