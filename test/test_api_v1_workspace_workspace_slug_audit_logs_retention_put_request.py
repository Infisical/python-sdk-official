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

from infisicalapi_client.models.api_v1_workspace_workspace_slug_audit_logs_retention_put_request import ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest  # noqa: E501

class TestApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest:
        """Test ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest`
        """
        model = ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest(
                audit_logs_retention_days = 0
            )
        else:
            return ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest(
                audit_logs_retention_days = 0,
        )
        """

    def testApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest(self):
        """Test ApiV1WorkspaceWorkspaceSlugAuditLogsRetentionPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
