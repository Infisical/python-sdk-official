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

from infisicalapi_client.models.api_v1_scim_groups_post_request import ApiV1ScimGroupsPostRequest  # noqa: E501

class TestApiV1ScimGroupsPostRequest(unittest.TestCase):
    """ApiV1ScimGroupsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ScimGroupsPostRequest:
        """Test ApiV1ScimGroupsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ScimGroupsPostRequest`
        """
        model = ApiV1ScimGroupsPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1ScimGroupsPostRequest(
                schemas = [
                    ''
                    ],
                display_name = '',
                members = [
                    infisicalapi_client.models._api_v1_scim_users__org_membership_id__get_201_response_groups_inner._api_v1_scim_Users__orgMembershipId__get_201_response_groups_inner(
                        value = '', 
                        display = '', )
                    ]
            )
        else:
            return ApiV1ScimGroupsPostRequest(
                schemas = [
                    ''
                    ],
                display_name = '',
        )
        """

    def testApiV1ScimGroupsPostRequest(self):
        """Test ApiV1ScimGroupsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
