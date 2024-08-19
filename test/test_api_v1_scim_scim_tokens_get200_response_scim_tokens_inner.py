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

from infisicalapi_client.models.api_v1_scim_scim_tokens_get200_response_scim_tokens_inner import ApiV1ScimScimTokensGet200ResponseScimTokensInner  # noqa: E501

class TestApiV1ScimScimTokensGet200ResponseScimTokensInner(unittest.TestCase):
    """ApiV1ScimScimTokensGet200ResponseScimTokensInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ScimScimTokensGet200ResponseScimTokensInner:
        """Test ApiV1ScimScimTokensGet200ResponseScimTokensInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ScimScimTokensGet200ResponseScimTokensInner`
        """
        model = ApiV1ScimScimTokensGet200ResponseScimTokensInner()  # noqa: E501
        if include_optional:
            return ApiV1ScimScimTokensGet200ResponseScimTokensInner(
                id = '',
                ttl_days = 1.337,
                description = '',
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1ScimScimTokensGet200ResponseScimTokensInner(
                id = '',
                description = '',
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1ScimScimTokensGet200ResponseScimTokensInner(self):
        """Test ApiV1ScimScimTokensGet200ResponseScimTokensInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()