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

from infisicalapi_client.models.api_v1_identities_get200_response_identities_inner import ApiV1IdentitiesGet200ResponseIdentitiesInner  # noqa: E501

class TestApiV1IdentitiesGet200ResponseIdentitiesInner(unittest.TestCase):
    """ApiV1IdentitiesGet200ResponseIdentitiesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1IdentitiesGet200ResponseIdentitiesInner:
        """Test ApiV1IdentitiesGet200ResponseIdentitiesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1IdentitiesGet200ResponseIdentitiesInner`
        """
        model = ApiV1IdentitiesGet200ResponseIdentitiesInner()  # noqa: E501
        if include_optional:
            return ApiV1IdentitiesGet200ResponseIdentitiesInner(
                id = '',
                role = '',
                role_id = '',
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identity_id = '',
                custom_role = infisicalapi_client.models._api_v1_organization__organization_id__groups_get_200_response_groups_inner_custom_role._api_v1_organization__organizationId__groups_get_200_response_groups_inner_customRole(
                    id = '', 
                    name = '', 
                    slug = '', 
                    permissions = null, 
                    description = '', ),
                identity = infisicalapi_client.models._api_v1_identities_get_200_response_identities_inner_identity._api_v1_identities_get_200_response_identities_inner_identity(
                    name = '', 
                    id = '', 
                    auth_method = '', )
            )
        else:
            return ApiV1IdentitiesGet200ResponseIdentitiesInner(
                id = '',
                role = '',
                org_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identity_id = '',
                identity = infisicalapi_client.models._api_v1_identities_get_200_response_identities_inner_identity._api_v1_identities_get_200_response_identities_inner_identity(
                    name = '', 
                    id = '', 
                    auth_method = '', ),
        )
        """

    def testApiV1IdentitiesGet200ResponseIdentitiesInner(self):
        """Test ApiV1IdentitiesGet200ResponseIdentitiesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
