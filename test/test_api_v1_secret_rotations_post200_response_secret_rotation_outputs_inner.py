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

from infisicalapi_client.models.api_v1_secret_rotations_post200_response_secret_rotation_outputs_inner import ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner  # noqa: E501

class TestApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner(unittest.TestCase):
    """ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner:
        """Test ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner`
        """
        model = ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner()  # noqa: E501
        if include_optional:
            return ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner(
                id = '',
                key = '',
                secret_id = '',
                rotation_id = ''
            )
        else:
            return ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner(
                id = '',
                key = '',
                secret_id = '',
                rotation_id = '',
        )
        """

    def testApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner(self):
        """Test ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
