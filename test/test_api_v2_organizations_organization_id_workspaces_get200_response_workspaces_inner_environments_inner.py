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

from infisicalapi_client.models.api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_environments_inner import ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner  # noqa: E501

class TestApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner(unittest.TestCase):
    """ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner:
        """Test ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner`
        """
        model = ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner()  # noqa: E501
        if include_optional:
            return ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner(
                name = '',
                slug = ''
            )
        else:
            return ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner(
                name = '',
                slug = '',
        )
        """

    def testApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner(self):
        """Test ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()