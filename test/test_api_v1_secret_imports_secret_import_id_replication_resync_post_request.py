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

from infisicalapi_client.models.api_v1_secret_imports_secret_import_id_replication_resync_post_request import ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest  # noqa: E501

class TestApiV1SecretImportsSecretImportIdReplicationResyncPostRequest(unittest.TestCase):
    """ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest:
        """Test ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest`
        """
        model = ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest(
                workspace_id = '',
                environment = '',
                path = '/'
            )
        else:
            return ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest(
                workspace_id = '',
                environment = '',
        )
        """

    def testApiV1SecretImportsSecretImportIdReplicationResyncPostRequest(self):
        """Test ApiV1SecretImportsSecretImportIdReplicationResyncPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()