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

from infisicalapi_client.models.api_v1_integration_post_request import ApiV1IntegrationPostRequest  # noqa: E501

class TestApiV1IntegrationPostRequest(unittest.TestCase):
    """ApiV1IntegrationPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IntegrationPostRequest:
        """Test ApiV1IntegrationPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IntegrationPostRequest`
        """
        model = ApiV1IntegrationPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1IntegrationPostRequest(
                integration_auth_id = '',
                app = '',
                is_active = True,
                app_id = '',
                secret_path = '/',
                source_environment = '',
                target_environment = '',
                target_environment_id = '',
                target_service = '',
                target_service_id = '',
                owner = '',
                url = '',
                path = '',
                region = '',
                scope = '',
                metadata = infisicalapi_client.models._api_v1_integration_post_request_metadata._api_v1_integration_post_request_metadata(
                    secret_prefix = '', 
                    secret_suffix = '', 
                    initial_sync_behavior = '', 
                    mapping_behavior = 'one-to-one', 
                    should_auto_redeploy = True, 
                    secret_gcp_label = infisicalapi_client.models._api_v1_integration_post_request_metadata_secret_gcp_label._api_v1_integration_post_request_metadata_secretGCPLabel(
                        label_name = '', 
                        label_value = '', ), 
                    secret_aws_tag = [
                        infisicalapi_client.models._api_v1_audit_log_streams__id__get_200_response_audit_log_stream_headers_inner._api_v1_audit_log_streams__id__get_200_response_auditLogStream_headers_inner(
                            key = '', 
                            value = '', )
                        ], 
                    kms_key_id = '', 
                    should_disable_delete = True, 
                    should_enable_delete = True, 
                    should_mask_secrets = True, 
                    should_protect_secrets = True, )
            )
        else:
            return ApiV1IntegrationPostRequest(
                integration_auth_id = '',
                source_environment = '',
        )
        """

    def testApiV1IntegrationPostRequest(self):
        """Test ApiV1IntegrationPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
