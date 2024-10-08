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

from infisicalapi_client.models.api_v1_scim_users_org_membership_id_put200_response import ApiV1ScimUsersOrgMembershipIdPut200Response  # noqa: E501

class TestApiV1ScimUsersOrgMembershipIdPut200Response(unittest.TestCase):
    """ApiV1ScimUsersOrgMembershipIdPut200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ScimUsersOrgMembershipIdPut200Response:
        """Test ApiV1ScimUsersOrgMembershipIdPut200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ScimUsersOrgMembershipIdPut200Response`
        """
        model = ApiV1ScimUsersOrgMembershipIdPut200Response()  # noqa: E501
        if include_optional:
            return ApiV1ScimUsersOrgMembershipIdPut200Response(
                schemas = [
                    ''
                    ],
                id = '',
                user_name = '',
                name = infisicalapi_client.models._api_v1_scim_users_get_200_response_resources_inner_name._api_v1_scim_Users_get_200_response_Resources_inner_name(
                    family_name = '', 
                    given_name = '', ),
                emails = [
                    infisicalapi_client.models._api_v1_scim_users_post_request_emails_inner._api_v1_scim_Users_post_request_emails_inner(
                        primary = True, 
                        value = '', 
                        type = '', )
                    ],
                display_name = '',
                active = True,
                groups = [
                    infisicalapi_client.models._api_v1_scim_users__org_membership_id__get_201_response_groups_inner._api_v1_scim_Users__orgMembershipId__get_201_response_groups_inner(
                        value = '', 
                        display = '', )
                    ]
            )
        else:
            return ApiV1ScimUsersOrgMembershipIdPut200Response(
                schemas = [
                    ''
                    ],
                id = '',
                user_name = '',
                name = infisicalapi_client.models._api_v1_scim_users_get_200_response_resources_inner_name._api_v1_scim_Users_get_200_response_Resources_inner_name(
                    family_name = '', 
                    given_name = '', ),
                emails = [
                    infisicalapi_client.models._api_v1_scim_users_post_request_emails_inner._api_v1_scim_Users_post_request_emails_inner(
                        primary = True, 
                        value = '', 
                        type = '', )
                    ],
                display_name = '',
                active = True,
                groups = [
                    infisicalapi_client.models._api_v1_scim_users__org_membership_id__get_201_response_groups_inner._api_v1_scim_Users__orgMembershipId__get_201_response_groups_inner(
                        value = '', 
                        display = '', )
                    ],
        )
        """

    def testApiV1ScimUsersOrgMembershipIdPut200Response(self):
        """Test ApiV1ScimUsersOrgMembershipIdPut200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
