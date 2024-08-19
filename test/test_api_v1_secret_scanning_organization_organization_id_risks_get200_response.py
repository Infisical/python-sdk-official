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

from infisicalapi_client.models.api_v1_secret_scanning_organization_organization_id_risks_get200_response import ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response  # noqa: E501

class TestApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response(unittest.TestCase):
    """ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response:
        """Test ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response`
        """
        model = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response(
                risks = [
                    infisicalapi_client.models._api_v1_secret_scanning_organization__organization_id__risks_get_200_response_risks_inner._api_v1_secret_scanning_organization__organizationId__risks_get_200_response_risks_inner(
                        id = '', 
                        description = '', 
                        start_line = '', 
                        end_line = '', 
                        start_column = '', 
                        end_column = '', 
                        file = '', 
                        symlink_file = '', 
                        commit = '', 
                        entropy = '', 
                        author = '', 
                        email = '', 
                        date = '', 
                        message = '', 
                        tags = [
                            ''
                            ], 
                        rule_id = '', 
                        fingerprint = '', 
                        finger_print_without_commit_id = '', 
                        is_false_positive = True, 
                        is_resolved = True, 
                        risk_owner = '', 
                        installation_id = '', 
                        repository_id = '', 
                        repository_link = '', 
                        repository_full_name = '', 
                        pusher_name = '', 
                        pusher_email = '', 
                        status = '', 
                        org_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response(
                risks = [
                    infisicalapi_client.models._api_v1_secret_scanning_organization__organization_id__risks_get_200_response_risks_inner._api_v1_secret_scanning_organization__organizationId__risks_get_200_response_risks_inner(
                        id = '', 
                        description = '', 
                        start_line = '', 
                        end_line = '', 
                        start_column = '', 
                        end_column = '', 
                        file = '', 
                        symlink_file = '', 
                        commit = '', 
                        entropy = '', 
                        author = '', 
                        email = '', 
                        date = '', 
                        message = '', 
                        tags = [
                            ''
                            ], 
                        rule_id = '', 
                        fingerprint = '', 
                        finger_print_without_commit_id = '', 
                        is_false_positive = True, 
                        is_resolved = True, 
                        risk_owner = '', 
                        installation_id = '', 
                        repository_id = '', 
                        repository_link = '', 
                        repository_full_name = '', 
                        pusher_name = '', 
                        pusher_email = '', 
                        status = '', 
                        org_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response(self):
        """Test ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
