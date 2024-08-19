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

from infisicalapi_client.models.api_v1_secret_approvals_get200_response_approvals_inner_environment import ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment  # noqa: E501

class TestApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment(unittest.TestCase):
    """ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment:
        """Test ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment`
        """
        model = ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment(
                id = '',
                name = '',
                slug = ''
            )
        else:
            return ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment(
                id = '',
                name = '',
                slug = '',
        )
        """

    def testApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment(self):
        """Test ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
