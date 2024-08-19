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

from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post200_response_privilege import ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege  # noqa: E501

class TestApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege(unittest.TestCase):
    """ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege:
        """Test ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege`
        """
        model = ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege()  # noqa: E501
        if include_optional:
            return ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege(
                id = '',
                slug = '',
                project_membership_id = '',
                is_temporary = True,
                temporary_mode = '',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                temporary_access_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                permissions = [
                    infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner(
                        subject = null, 
                        action = null, 
                        conditions = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner_conditions._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner_conditions(
                            environment = '', 
                            secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner_conditions_secretPath(
                                __glob = '0', ), ), )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege(
                id = '',
                slug = '',
                project_membership_id = '',
                permissions = [
                    infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner(
                        subject = null, 
                        action = null, 
                        conditions = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner_conditions._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner_conditions(
                            environment = '', 
                            secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_200_response_role_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_200_response_role_permissions_inner_conditions_secretPath(
                                __glob = '0', ), ), )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege(self):
        """Test ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
