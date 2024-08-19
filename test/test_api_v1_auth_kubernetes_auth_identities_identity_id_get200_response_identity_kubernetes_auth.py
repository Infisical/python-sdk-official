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

from infisicalapi_client.models.api_v1_auth_kubernetes_auth_identities_identity_id_get200_response_identity_kubernetes_auth import ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth  # noqa: E501

class TestApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth(unittest.TestCase):
    """ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth:
        """Test ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth`
        """
        model = ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth()  # noqa: E501
        if include_optional:
            return ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth(
                id = '',
                access_token_ttl = 1.337,
                access_token_max_ttl = 1.337,
                access_token_num_uses_limit = 1.337,
                access_token_trusted_ips = None,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identity_id = '',
                kubernetes_host = '',
                allowed_namespaces = '',
                allowed_names = '',
                allowed_audience = '',
                ca_cert = '',
                token_reviewer_jwt = ''
            )
        else:
            return ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identity_id = '',
                kubernetes_host = '',
                allowed_namespaces = '',
                allowed_names = '',
                allowed_audience = '',
                ca_cert = '',
                token_reviewer_jwt = '',
        )
        """

    def testApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth(self):
        """Test ApiV1AuthKubernetesAuthIdentitiesIdentityIdGet200ResponseIdentityKubernetesAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
