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

from infisicalapi_client.models.api_v1_invite_org_verify_post_request import ApiV1InviteOrgVerifyPostRequest  # noqa: E501

class TestApiV1InviteOrgVerifyPostRequest(unittest.TestCase):
    """ApiV1InviteOrgVerifyPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1InviteOrgVerifyPostRequest:
        """Test ApiV1InviteOrgVerifyPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1InviteOrgVerifyPostRequest`
        """
        model = ApiV1InviteOrgVerifyPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1InviteOrgVerifyPostRequest(
                email = '',
                organization_id = '',
                code = ''
            )
        else:
            return ApiV1InviteOrgVerifyPostRequest(
                email = '',
                organization_id = '',
                code = '',
        )
        """

    def testApiV1InviteOrgVerifyPostRequest(self):
        """Test ApiV1InviteOrgVerifyPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
