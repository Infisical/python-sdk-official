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

from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_delete200_response import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response  # noqa: E501

class TestApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response(unittest.TestCase):
    """ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response:
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response`
        """
        model = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response()  # noqa: E501
        if include_optional:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response(
                membership = infisicalapi_client.models._api_v1_organization__organization_id__permissions_get_200_response_membership._api_v1_organization__organizationId__permissions_get_200_response_membership(
                    id = '', 
                    role = '', 
                    status = 'invited', 
                    invite_email = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', 
                    org_id = '', 
                    role_id = '', 
                    project_favorites = [
                        ''
                        ], 
                    is_active = True, )
            )
        else:
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response(
                membership = infisicalapi_client.models._api_v1_organization__organization_id__permissions_get_200_response_membership._api_v1_organization__organizationId__permissions_get_200_response_membership(
                    id = '', 
                    role = '', 
                    status = 'invited', 
                    invite_email = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_id = '', 
                    org_id = '', 
                    role_id = '', 
                    project_favorites = [
                        ''
                        ], 
                    is_active = True, ),
        )
        """

    def testApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response(self):
        """Test ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
