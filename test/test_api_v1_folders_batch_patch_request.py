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

from infisicalapi_client.models.api_v1_folders_batch_patch_request import ApiV1FoldersBatchPatchRequest  # noqa: E501

class TestApiV1FoldersBatchPatchRequest(unittest.TestCase):
    """ApiV1FoldersBatchPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1FoldersBatchPatchRequest:
        """Test ApiV1FoldersBatchPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1FoldersBatchPatchRequest`
        """
        model = ApiV1FoldersBatchPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1FoldersBatchPatchRequest(
                project_slug = '',
                folders = [
                    infisicalapi_client.models._api_v1_folders_batch_patch_request_folders_inner._api_v1_folders_batch_patch_request_folders_inner(
                        id = '', 
                        environment = '', 
                        name = '', 
                        path = '/', )
                    ]
            )
        else:
            return ApiV1FoldersBatchPatchRequest(
                project_slug = '',
                folders = [
                    infisicalapi_client.models._api_v1_folders_batch_patch_request_folders_inner._api_v1_folders_batch_patch_request_folders_inner(
                        id = '', 
                        environment = '', 
                        name = '', 
                        path = '/', )
                    ],
        )
        """

    def testApiV1FoldersBatchPatchRequest(self):
        """Test ApiV1FoldersBatchPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
