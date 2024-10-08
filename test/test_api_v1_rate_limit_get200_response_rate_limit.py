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

from infisicalapi_client.models.api_v1_rate_limit_get200_response_rate_limit import ApiV1RateLimitGet200ResponseRateLimit  # noqa: E501

class TestApiV1RateLimitGet200ResponseRateLimit(unittest.TestCase):
    """ApiV1RateLimitGet200ResponseRateLimit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1RateLimitGet200ResponseRateLimit:
        """Test ApiV1RateLimitGet200ResponseRateLimit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1RateLimitGet200ResponseRateLimit`
        """
        model = ApiV1RateLimitGet200ResponseRateLimit()  # noqa: E501
        if include_optional:
            return ApiV1RateLimitGet200ResponseRateLimit(
                id = '',
                read_rate_limit = 1.337,
                write_rate_limit = 1.337,
                secrets_rate_limit = 1.337,
                auth_rate_limit = 1.337,
                invite_user_rate_limit = 1.337,
                mfa_rate_limit = 1.337,
                public_endpoint_limit = 1.337,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1RateLimitGet200ResponseRateLimit(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1RateLimitGet200ResponseRateLimit(self):
        """Test ApiV1RateLimitGet200ResponseRateLimit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
