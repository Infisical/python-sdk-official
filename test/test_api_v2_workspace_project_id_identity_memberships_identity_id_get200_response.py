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

from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_get200_response import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response  # noqa: E501

class TestApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response(unittest.TestCase):
    """ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response:
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response`
        """
        model = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response()  # noqa: E501
        if include_optional:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response(
                identity_membership = infisicalapi_client.models._api_v1_identities__identity_id__identity_memberships_get_200_response_identity_memberships_inner._api_v1_identities__identityId__identity_memberships_get_200_response_identityMemberships_inner(
                    id = '', 
                    identity_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    roles = [
                        infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_roles_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner_roles_inner(
                            id = '', 
                            role = '', 
                            custom_role_id = '', 
                            custom_role_name = '', 
                            custom_role_slug = '', 
                            is_temporary = True, 
                            temporary_mode = '', 
                            temporary_range = '', 
                            temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    identity = infisicalapi_client.models._api_v1_identities_get_200_response_identities_inner_identity._api_v1_identities_get_200_response_identities_inner_identity(
                        name = '', 
                        id = '', 
                        auth_method = '', ), 
                    project = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_project._api_v1_workspace__workspaceId__users_get_200_response_users_inner_project(
                        name = '', 
                        id = '', ), )
            )
        else:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response(
                identity_membership = infisicalapi_client.models._api_v1_identities__identity_id__identity_memberships_get_200_response_identity_memberships_inner._api_v1_identities__identityId__identity_memberships_get_200_response_identityMemberships_inner(
                    id = '', 
                    identity_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    roles = [
                        infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_roles_inner._api_v1_workspace__workspaceId__users_get_200_response_users_inner_roles_inner(
                            id = '', 
                            role = '', 
                            custom_role_id = '', 
                            custom_role_name = '', 
                            custom_role_slug = '', 
                            is_temporary = True, 
                            temporary_mode = '', 
                            temporary_range = '', 
                            temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    identity = infisicalapi_client.models._api_v1_identities_get_200_response_identities_inner_identity._api_v1_identities_get_200_response_identities_inner_identity(
                        name = '', 
                        id = '', 
                        auth_method = '', ), 
                    project = infisicalapi_client.models._api_v1_workspace__workspace_id__users_get_200_response_users_inner_project._api_v1_workspace__workspaceId__users_get_200_response_users_inner_project(
                        name = '', 
                        id = '', ), ),
        )
        """

    def testApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response(self):
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
