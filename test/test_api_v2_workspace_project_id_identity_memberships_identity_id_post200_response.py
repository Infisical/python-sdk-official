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

from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_post200_response import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response  # noqa: E501

class TestApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response(unittest.TestCase):
    """ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response:
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response`
        """
        model = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response()  # noqa: E501
        if include_optional:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response(
                identity_membership = infisicalapi_client.models._api_v2_workspace__project_id__identity_memberships__identity_id__post_200_response_identity_membership._api_v2_workspace__projectId__identity_memberships__identityId__post_200_response_identityMembership(
                    id = '', 
                    project_id = '', 
                    identity_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response(
                identity_membership = infisicalapi_client.models._api_v2_workspace__project_id__identity_memberships__identity_id__post_200_response_identity_membership._api_v2_workspace__projectId__identity_memberships__identityId__post_200_response_identityMembership(
                    id = '', 
                    project_id = '', 
                    identity_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response(self):
        """Test ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
