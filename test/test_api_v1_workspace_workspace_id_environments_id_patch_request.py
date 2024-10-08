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

from infisicalapi_client.models.api_v1_workspace_workspace_id_environments_id_patch_request import ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest:
        """Test ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest`
        """
        model = ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest(
                slug = '',
                name = '',
                position = 1.337
            )
        else:
            return ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest(
        )
        """

    def testApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest(self):
        """Test ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
