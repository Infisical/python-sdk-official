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

from infisicalapi_client.models.api_v1_user_engagement_me_wish_post_request import ApiV1UserEngagementMeWishPostRequest  # noqa: E501

class TestApiV1UserEngagementMeWishPostRequest(unittest.TestCase):
    """ApiV1UserEngagementMeWishPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1UserEngagementMeWishPostRequest:
        """Test ApiV1UserEngagementMeWishPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1UserEngagementMeWishPostRequest`
        """
        model = ApiV1UserEngagementMeWishPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1UserEngagementMeWishPostRequest(
                text = '0'
            )
        else:
            return ApiV1UserEngagementMeWishPostRequest(
                text = '0',
        )
        """

    def testApiV1UserEngagementMeWishPostRequest(self):
        """Test ApiV1UserEngagementMeWishPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
