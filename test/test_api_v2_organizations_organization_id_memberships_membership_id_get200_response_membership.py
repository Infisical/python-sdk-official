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

from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership  # noqa: E501

class TestApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership(unittest.TestCase):
    """ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership:
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership`
        """
        model = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership()  # noqa: E501
        if include_optional:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership(
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
                user = infisicalapi_client.models._api_v2_organizations__organization_id__memberships__membership_id__get_200_response_membership_user._api_v2_organizations__organizationId__memberships__membershipId__get_200_response_membership_user(
                    username = '', 
                    email = '', 
                    is_email_verified = True, 
                    first_name = '', 
                    last_name = '', 
                    id = '', 
                    public_key = '', )
            )
        else:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership(
                id = '',
                role = '',
                org_id = '',
                user = infisicalapi_client.models._api_v2_organizations__organization_id__memberships__membership_id__get_200_response_membership_user._api_v2_organizations__organizationId__memberships__membershipId__get_200_response_membership_user(
                    username = '', 
                    email = '', 
                    is_email_verified = True, 
                    first_name = '', 
                    last_name = '', 
                    id = '', 
                    public_key = '', ),
        )
        """

    def testApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership(self):
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
