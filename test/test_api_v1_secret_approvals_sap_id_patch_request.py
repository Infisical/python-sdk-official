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

from infisicalapi_client.models.api_v1_secret_approvals_sap_id_patch_request import ApiV1SecretApprovalsSapIdPatchRequest  # noqa: E501

class TestApiV1SecretApprovalsSapIdPatchRequest(unittest.TestCase):
    """ApiV1SecretApprovalsSapIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalsSapIdPatchRequest:
        """Test ApiV1SecretApprovalsSapIdPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalsSapIdPatchRequest`
        """
        model = ApiV1SecretApprovalsSapIdPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalsSapIdPatchRequest(
                name = '',
                approvers = [
                    ''
                    ],
                approvals = 1,
                secret_path = '',
                enforcement_level = 'hard'
            )
        else:
            return ApiV1SecretApprovalsSapIdPatchRequest(
                approvers = [
                    ''
                    ],
        )
        """

    def testApiV1SecretApprovalsSapIdPatchRequest(self):
        """Test ApiV1SecretApprovalsSapIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
