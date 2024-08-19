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

from infisicalapi_client.models.api_v1_scim_users_get200_response_resources_inner_name import ApiV1ScimUsersGet200ResponseResourcesInnerName  # noqa: E501

class TestApiV1ScimUsersGet200ResponseResourcesInnerName(unittest.TestCase):
    """ApiV1ScimUsersGet200ResponseResourcesInnerName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ScimUsersGet200ResponseResourcesInnerName:
        """Test ApiV1ScimUsersGet200ResponseResourcesInnerName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ScimUsersGet200ResponseResourcesInnerName`
        """
        model = ApiV1ScimUsersGet200ResponseResourcesInnerName()  # noqa: E501
        if include_optional:
            return ApiV1ScimUsersGet200ResponseResourcesInnerName(
                family_name = '',
                given_name = ''
            )
        else:
            return ApiV1ScimUsersGet200ResponseResourcesInnerName(
                family_name = '',
                given_name = '',
        )
        """

    def testApiV1ScimUsersGet200ResponseResourcesInnerName(self):
        """Test ApiV1ScimUsersGet200ResponseResourcesInnerName"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
