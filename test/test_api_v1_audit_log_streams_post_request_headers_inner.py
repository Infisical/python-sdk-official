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

from infisicalapi_client.models.api_v1_audit_log_streams_post_request_headers_inner import ApiV1AuditLogStreamsPostRequestHeadersInner  # noqa: E501

class TestApiV1AuditLogStreamsPostRequestHeadersInner(unittest.TestCase):
    """ApiV1AuditLogStreamsPostRequestHeadersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuditLogStreamsPostRequestHeadersInner:
        """Test ApiV1AuditLogStreamsPostRequestHeadersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuditLogStreamsPostRequestHeadersInner`
        """
        model = ApiV1AuditLogStreamsPostRequestHeadersInner()  # noqa: E501
        if include_optional:
            return ApiV1AuditLogStreamsPostRequestHeadersInner(
                key = '0',
                value = '0'
            )
        else:
            return ApiV1AuditLogStreamsPostRequestHeadersInner(
                key = '0',
                value = '0',
        )
        """

    def testApiV1AuditLogStreamsPostRequestHeadersInner(self):
        """Test ApiV1AuditLogStreamsPostRequestHeadersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
