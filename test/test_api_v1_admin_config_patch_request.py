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

from infisicalapi_client.models.api_v1_admin_config_patch_request import ApiV1AdminConfigPatchRequest  # noqa: E501

class TestApiV1AdminConfigPatchRequest(unittest.TestCase):
    """ApiV1AdminConfigPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdminConfigPatchRequest:
        """Test ApiV1AdminConfigPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdminConfigPatchRequest`
        """
        model = ApiV1AdminConfigPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1AdminConfigPatchRequest(
                allow_sign_up = True,
                allowed_sign_up_domain = '',
                trust_saml_emails = True,
                trust_ldap_emails = True,
                trust_oidc_emails = True,
                default_auth_org_id = '',
                enabled_login_methods = [
                    'email'
                    ]
            )
        else:
            return ApiV1AdminConfigPatchRequest(
        )
        """

    def testApiV1AdminConfigPatchRequest(self):
        """Test ApiV1AdminConfigPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
