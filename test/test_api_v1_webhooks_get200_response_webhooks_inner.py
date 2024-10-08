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

from infisicalapi_client.models.api_v1_webhooks_get200_response_webhooks_inner import ApiV1WebhooksGet200ResponseWebhooksInner  # noqa: E501

class TestApiV1WebhooksGet200ResponseWebhooksInner(unittest.TestCase):
    """ApiV1WebhooksGet200ResponseWebhooksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WebhooksGet200ResponseWebhooksInner:
        """Test ApiV1WebhooksGet200ResponseWebhooksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WebhooksGet200ResponseWebhooksInner`
        """
        model = ApiV1WebhooksGet200ResponseWebhooksInner()  # noqa: E501
        if include_optional:
            return ApiV1WebhooksGet200ResponseWebhooksInner(
                id = '',
                secret_path = '/',
                last_status = '',
                last_run_error_message = '',
                is_disabled = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                env_id = '',
                type = 'general',
                project_id = '',
                environment = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                    id = '', 
                    name = '', 
                    slug = '', ),
                url = ''
            )
        else:
            return ApiV1WebhooksGet200ResponseWebhooksInner(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                env_id = '',
                project_id = '',
                environment = infisicalapi_client.models._api_v1_secret_approvals_get_200_response_approvals_inner_environment._api_v1_secret_approvals_get_200_response_approvals_inner_environment(
                    id = '', 
                    name = '', 
                    slug = '', ),
                url = '',
        )
        """

    def testApiV1WebhooksGet200ResponseWebhooksInner(self):
        """Test ApiV1WebhooksGet200ResponseWebhooksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
