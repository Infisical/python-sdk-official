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

from infisicalapi_client.models.api_v1_sso_oidc_config_patch_request import ApiV1SsoOidcConfigPatchRequest  # noqa: E501

class TestApiV1SsoOidcConfigPatchRequest(unittest.TestCase):
    """ApiV1SsoOidcConfigPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SsoOidcConfigPatchRequest:
        """Test ApiV1SsoOidcConfigPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SsoOidcConfigPatchRequest`
        """
        model = ApiV1SsoOidcConfigPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1SsoOidcConfigPatchRequest(
                allowed_email_domains = '',
                discovery_url = '',
                configuration_type = 'custom',
                issuer = '',
                authorization_endpoint = '',
                jwks_uri = '',
                token_endpoint = '',
                userinfo_endpoint = '',
                client_id = '',
                client_secret = '',
                is_active = True,
                org_slug = ''
            )
        else:
            return ApiV1SsoOidcConfigPatchRequest(
                org_slug = '',
        )
        """

    def testApiV1SsoOidcConfigPatchRequest(self):
        """Test ApiV1SsoOidcConfigPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
