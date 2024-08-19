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

from infisicalapi_client.models.api_v2_workspace_post_request import ApiV2WorkspacePostRequest  # noqa: E501

class TestApiV2WorkspacePostRequest(unittest.TestCase):
    """ApiV2WorkspacePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2WorkspacePostRequest:
        """Test ApiV2WorkspacePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2WorkspacePostRequest`
        """
        model = ApiV2WorkspacePostRequest()  # noqa: E501
        if include_optional:
            return ApiV2WorkspacePostRequest(
                project_name = '',
                slug = '01234',
                kms_key_id = ''
            )
        else:
            return ApiV2WorkspacePostRequest(
                project_name = '',
        )
        """

    def testApiV2WorkspacePostRequest(self):
        """Test ApiV2WorkspacePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
