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

from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner_reviewers_inner import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner  # noqa: E501

class TestApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner(unittest.TestCase):
    """ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner:
        """Test ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner`
        """
        model = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner()  # noqa: E501
        if include_optional:
            return ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner(
                member = '',
                status = ''
            )
        else:
            return ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner(
                member = '',
                status = '',
        )
        """

    def testApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner(self):
        """Test ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
