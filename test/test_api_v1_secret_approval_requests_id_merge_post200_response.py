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

from infisicalapi_client.models.api_v1_secret_approval_requests_id_merge_post200_response import ApiV1SecretApprovalRequestsIdMergePost200Response  # noqa: E501

class TestApiV1SecretApprovalRequestsIdMergePost200Response(unittest.TestCase):
    """ApiV1SecretApprovalRequestsIdMergePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretApprovalRequestsIdMergePost200Response:
        """Test ApiV1SecretApprovalRequestsIdMergePost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretApprovalRequestsIdMergePost200Response`
        """
        model = ApiV1SecretApprovalRequestsIdMergePost200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretApprovalRequestsIdMergePost200Response(
                approval = infisicalapi_client.models._api_v1_secret_approval_requests__id__merge_post_200_response_approval._api_v1_secret_approval_requests__id__merge_post_200_response_approval(
                    id = '', 
                    policy_id = '', 
                    has_merged = True, 
                    status = 'open', 
                    conflicts = null, 
                    slug = '', 
                    folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_replicated = True, 
                    committer_user_id = '', 
                    status_changed_by_user_id = '', 
                    bypass_reason = '', )
            )
        else:
            return ApiV1SecretApprovalRequestsIdMergePost200Response(
                approval = infisicalapi_client.models._api_v1_secret_approval_requests__id__merge_post_200_response_approval._api_v1_secret_approval_requests__id__merge_post_200_response_approval(
                    id = '', 
                    policy_id = '', 
                    has_merged = True, 
                    status = 'open', 
                    conflicts = null, 
                    slug = '', 
                    folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_replicated = True, 
                    committer_user_id = '', 
                    status_changed_by_user_id = '', 
                    bypass_reason = '', ),
        )
        """

    def testApiV1SecretApprovalRequestsIdMergePost200Response(self):
        """Test ApiV1SecretApprovalRequestsIdMergePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
