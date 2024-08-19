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

from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response import ApiV1AccessApprovalsRequestsGet200Response  # noqa: E501

class TestApiV1AccessApprovalsRequestsGet200Response(unittest.TestCase):
    """ApiV1AccessApprovalsRequestsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AccessApprovalsRequestsGet200Response:
        """Test ApiV1AccessApprovalsRequestsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AccessApprovalsRequestsGet200Response`
        """
        model = ApiV1AccessApprovalsRequestsGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1AccessApprovalsRequestsGet200Response(
                requests = [
                    infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner._api_v1_access_approvals_requests_get_200_response_requests_inner(
                        id = '', 
                        policy_id = '', 
                        privilege_id = '', 
                        requested_by = '', 
                        is_temporary = True, 
                        temporary_range = '', 
                        permissions = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        environment_name = '', 
                        is_approved = True, 
                        privilege = infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_privilege._api_v1_access_approvals_requests_get_200_response_requests_inner_privilege(
                            membership_id = '', 
                            is_temporary = True, 
                            temporary_mode = '', 
                            temporary_range = '', 
                            temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            permissions = null, ), 
                        policy = infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_policy._api_v1_access_approvals_requests_get_200_response_requests_inner_policy(
                            id = '', 
                            name = '', 
                            approvals = 1.337, 
                            approvers = [
                                ''
                                ], 
                            secret_path = '', 
                            env_id = '', 
                            enforcement_level = '', ), 
                        reviewers = [
                            infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_reviewers_inner._api_v1_access_approvals_requests_get_200_response_requests_inner_reviewers_inner(
                                member = '', 
                                status = '', )
                            ], )
                    ]
            )
        else:
            return ApiV1AccessApprovalsRequestsGet200Response(
                requests = [
                    infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner._api_v1_access_approvals_requests_get_200_response_requests_inner(
                        id = '', 
                        policy_id = '', 
                        privilege_id = '', 
                        requested_by = '', 
                        is_temporary = True, 
                        temporary_range = '', 
                        permissions = null, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        environment_name = '', 
                        is_approved = True, 
                        privilege = infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_privilege._api_v1_access_approvals_requests_get_200_response_requests_inner_privilege(
                            membership_id = '', 
                            is_temporary = True, 
                            temporary_mode = '', 
                            temporary_range = '', 
                            temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            permissions = null, ), 
                        policy = infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_policy._api_v1_access_approvals_requests_get_200_response_requests_inner_policy(
                            id = '', 
                            name = '', 
                            approvals = 1.337, 
                            approvers = [
                                ''
                                ], 
                            secret_path = '', 
                            env_id = '', 
                            enforcement_level = '', ), 
                        reviewers = [
                            infisicalapi_client.models._api_v1_access_approvals_requests_get_200_response_requests_inner_reviewers_inner._api_v1_access_approvals_requests_get_200_response_requests_inner_reviewers_inner(
                                member = '', 
                                status = '', )
                            ], )
                    ],
        )
        """

    def testApiV1AccessApprovalsRequestsGet200Response(self):
        """Test ApiV1AccessApprovalsRequestsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
