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

from infisicalapi_client.models.api_v1_bot_project_id_get200_response import ApiV1BotProjectIdGet200Response  # noqa: E501

class TestApiV1BotProjectIdGet200Response(unittest.TestCase):
    """ApiV1BotProjectIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1BotProjectIdGet200Response:
        """Test ApiV1BotProjectIdGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1BotProjectIdGet200Response`
        """
        model = ApiV1BotProjectIdGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1BotProjectIdGet200Response(
                bot = infisicalapi_client.models._api_v1_bot__project_id__get_200_response_bot._api_v1_bot__projectId__get_200_response_bot(
                    id = '', 
                    name = '', 
                    is_active = True, 
                    public_key = '', 
                    encrypted_project_key = '', 
                    encrypted_project_key_nonce = '', 
                    project_id = '', 
                    sender_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ApiV1BotProjectIdGet200Response(
                bot = infisicalapi_client.models._api_v1_bot__project_id__get_200_response_bot._api_v1_bot__projectId__get_200_response_bot(
                    id = '', 
                    name = '', 
                    is_active = True, 
                    public_key = '', 
                    encrypted_project_key = '', 
                    encrypted_project_key_nonce = '', 
                    project_id = '', 
                    sender_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testApiV1BotProjectIdGet200Response(self):
        """Test ApiV1BotProjectIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
