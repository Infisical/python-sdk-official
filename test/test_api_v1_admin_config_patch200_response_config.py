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

from infisicalapi_client.models.api_v1_admin_config_patch200_response_config import ApiV1AdminConfigPatch200ResponseConfig  # noqa: E501

class TestApiV1AdminConfigPatch200ResponseConfig(unittest.TestCase):
    """ApiV1AdminConfigPatch200ResponseConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdminConfigPatch200ResponseConfig:
        """Test ApiV1AdminConfigPatch200ResponseConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdminConfigPatch200ResponseConfig`
        """
        model = ApiV1AdminConfigPatch200ResponseConfig()  # noqa: E501
        if include_optional:
            return ApiV1AdminConfigPatch200ResponseConfig(
                id = '',
                initialized = True,
                allow_sign_up = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                allowed_sign_up_domain = '',
                instance_id = '00000000-0000-0000-0000-000000000000',
                trust_saml_emails = True,
                trust_ldap_emails = True,
                trust_oidc_emails = True,
                default_auth_org_id = '',
                enabled_login_methods = [
                    ''
                    ],
                default_auth_org_slug = ''
            )
        else:
            return ApiV1AdminConfigPatch200ResponseConfig(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_auth_org_slug = '',
        )
        """

    def testApiV1AdminConfigPatch200ResponseConfig(self):
        """Test ApiV1AdminConfigPatch200ResponseConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
