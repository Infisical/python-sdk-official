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

from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_post200_response_identity_membership import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership  # noqa: E501

class TestApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership(unittest.TestCase):
    """ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership:
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership`
        """
        model = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership()  # noqa: E501
        if include_optional:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership(
                id = '',
                project_id = '',
                identity_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership(
                id = '',
                project_id = '',
                identity_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership(self):
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200ResponseIdentityMembership"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()