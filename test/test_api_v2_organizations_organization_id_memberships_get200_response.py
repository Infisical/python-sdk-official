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

from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_get200_response import ApiV2OrganizationsOrganizationIdMembershipsGet200Response  # noqa: E501

class TestApiV2OrganizationsOrganizationIdMembershipsGet200Response(unittest.TestCase):
    """ApiV2OrganizationsOrganizationIdMembershipsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2OrganizationsOrganizationIdMembershipsGet200Response:
        """Test ApiV2OrganizationsOrganizationIdMembershipsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2OrganizationsOrganizationIdMembershipsGet200Response`
        """
        model = ApiV2OrganizationsOrganizationIdMembershipsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV2OrganizationsOrganizationIdMembershipsGet200Response(
                users = [
                    infisicalapi_client.models._api_v2_organizations__organization_id__memberships_get_200_response_users_inner._api_v2_organizations__organizationId__memberships_get_200_response_users_inner(
                        id = '', 
                        role = '', 
                        status = 'invited', 
                        invite_email = '', 
                        user_id = '', 
                        org_id = '', 
                        role_id = '', 
                        project_favorites = [
                            ''
                            ], 
                        is_active = True, 
                        user = infisicalapi_client.models._api_v2_organizations__organization_id__memberships_get_200_response_users_inner_user._api_v2_organizations__organizationId__memberships_get_200_response_users_inner_user(
                            username = '', 
                            email = '', 
                            is_email_verified = True, 
                            first_name = '', 
                            last_name = '', 
                            id = '', 
                            public_key = '', ), )
                    ]
            )
        else:
            return ApiV2OrganizationsOrganizationIdMembershipsGet200Response(
                users = [
                    infisicalapi_client.models._api_v2_organizations__organization_id__memberships_get_200_response_users_inner._api_v2_organizations__organizationId__memberships_get_200_response_users_inner(
                        id = '', 
                        role = '', 
                        status = 'invited', 
                        invite_email = '', 
                        user_id = '', 
                        org_id = '', 
                        role_id = '', 
                        project_favorites = [
                            ''
                            ], 
                        is_active = True, 
                        user = infisicalapi_client.models._api_v2_organizations__organization_id__memberships_get_200_response_users_inner_user._api_v2_organizations__organizationId__memberships_get_200_response_users_inner_user(
                            username = '', 
                            email = '', 
                            is_email_verified = True, 
                            first_name = '', 
                            last_name = '', 
                            id = '', 
                            public_key = '', ), )
                    ],
        )
        """

    def testApiV2OrganizationsOrganizationIdMembershipsGet200Response(self):
        """Test ApiV2OrganizationsOrganizationIdMembershipsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
