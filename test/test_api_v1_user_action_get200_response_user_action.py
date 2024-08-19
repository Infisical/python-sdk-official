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

from infisicalapi_client.models.api_v1_user_action_get200_response_user_action import ApiV1UserActionGet200ResponseUserAction  # noqa: E501

class TestApiV1UserActionGet200ResponseUserAction(unittest.TestCase):
    """ApiV1UserActionGet200ResponseUserAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1UserActionGet200ResponseUserAction:
        """Test ApiV1UserActionGet200ResponseUserAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1UserActionGet200ResponseUserAction`
        """
        model = ApiV1UserActionGet200ResponseUserAction()  # noqa: E501
        if include_optional:
            return ApiV1UserActionGet200ResponseUserAction(
                id = '',
                action = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_id = ''
            )
        else:
            return ApiV1UserActionGet200ResponseUserAction(
                id = '',
                action = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_id = '',
        )
        """

    def testApiV1UserActionGet200ResponseUserAction(self):
        """Test ApiV1UserActionGet200ResponseUserAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()