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

from infisicalapi_client.models.api_v1_external_kms_post200_response_external_kms import ApiV1ExternalKmsPost200ResponseExternalKms  # noqa: E501

class TestApiV1ExternalKmsPost200ResponseExternalKms(unittest.TestCase):
    """ApiV1ExternalKmsPost200ResponseExternalKms unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ExternalKmsPost200ResponseExternalKms:
        """Test ApiV1ExternalKmsPost200ResponseExternalKms
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ExternalKmsPost200ResponseExternalKms`
        """
        model = ApiV1ExternalKmsPost200ResponseExternalKms()  # noqa: E501
        if include_optional:
            return ApiV1ExternalKmsPost200ResponseExternalKms(
                id = '',
                description = '',
                is_disabled = True,
                is_reserved = True,
                org_id = '',
                slug = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                external = infisicalapi_client.models._api_v1_external_kms_post_200_response_external_kms_external._api_v1_external_kms_post_200_response_externalKms_external(
                    id = '', 
                    status = '', 
                    status_details = '', 
                    provider = '', )
            )
        else:
            return ApiV1ExternalKmsPost200ResponseExternalKms(
                id = '',
                org_id = '',
                slug = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                external = infisicalapi_client.models._api_v1_external_kms_post_200_response_external_kms_external._api_v1_external_kms_post_200_response_externalKms_external(
                    id = '', 
                    status = '', 
                    status_details = '', 
                    provider = '', ),
        )
        """

    def testApiV1ExternalKmsPost200ResponseExternalKms(self):
        """Test ApiV1ExternalKmsPost200ResponseExternalKms"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
