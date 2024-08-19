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

from infisicalapi_client.models.api_v1_organization_organization_id_roles_get200_response_data_roles_inner import ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner  # noqa: E501

class TestApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner(unittest.TestCase):
    """ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner:
        """Test ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner`
        """
        model = ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner()  # noqa: E501
        if include_optional:
            return ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner(
                id = '',
                name = '',
                description = '',
                slug = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                org_id = '',
                permissions = None
            )
        else:
            return ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner(
                id = '',
                name = '',
                slug = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                org_id = '',
        )
        """

    def testApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner(self):
        """Test ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
