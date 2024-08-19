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

from infisicalapi_client.models.api_v1_scim_groups_group_id_patch_request_operations_inner import ApiV1ScimGroupsGroupIdPatchRequestOperationsInner  # noqa: E501

class TestApiV1ScimGroupsGroupIdPatchRequestOperationsInner(unittest.TestCase):
    """ApiV1ScimGroupsGroupIdPatchRequestOperationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1ScimGroupsGroupIdPatchRequestOperationsInner:
        """Test ApiV1ScimGroupsGroupIdPatchRequestOperationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1ScimGroupsGroupIdPatchRequestOperationsInner`
        """
        model = ApiV1ScimGroupsGroupIdPatchRequestOperationsInner()  # noqa: E501
        if include_optional:
            return ApiV1ScimGroupsGroupIdPatchRequestOperationsInner(
                op = 'add',
                value = [
                    infisicalapi_client.models._api_v1_scim_groups__group_id__patch_request_operations_inner_any_of_2_value_inner._api_v1_scim_Groups__groupId__patch_request_Operations_inner_anyOf_2_value_inner(
                        value = '', 
                        display = '', )
                    ],
                path = ''
            )
        else:
            return ApiV1ScimGroupsGroupIdPatchRequestOperationsInner(
                op = 'add',
                value = [
                    infisicalapi_client.models._api_v1_scim_groups__group_id__patch_request_operations_inner_any_of_2_value_inner._api_v1_scim_Groups__groupId__patch_request_Operations_inner_anyOf_2_value_inner(
                        value = '', 
                        display = '', )
                    ],
                path = '',
        )
        """

    def testApiV1ScimGroupsGroupIdPatchRequestOperationsInner(self):
        """Test ApiV1ScimGroupsGroupIdPatchRequestOperationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
