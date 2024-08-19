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

from infisicalapi_client.models.api_v1_identities_post200_response_identity import ApiV1IdentitiesPost200ResponseIdentity  # noqa: E501

class TestApiV1IdentitiesPost200ResponseIdentity(unittest.TestCase):
    """ApiV1IdentitiesPost200ResponseIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IdentitiesPost200ResponseIdentity:
        """Test ApiV1IdentitiesPost200ResponseIdentity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IdentitiesPost200ResponseIdentity`
        """
        model = ApiV1IdentitiesPost200ResponseIdentity()  # noqa: E501
        if include_optional:
            return ApiV1IdentitiesPost200ResponseIdentity(
                id = '',
                name = '',
                auth_method = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1IdentitiesPost200ResponseIdentity(
                id = '',
                name = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1IdentitiesPost200ResponseIdentity(self):
        """Test ApiV1IdentitiesPost200ResponseIdentity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
