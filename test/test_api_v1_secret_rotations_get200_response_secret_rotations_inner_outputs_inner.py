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

from infisicalapi_client.models.api_v1_secret_rotations_get200_response_secret_rotations_inner_outputs_inner import ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner  # noqa: E501

class TestApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner(unittest.TestCase):
    """ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner:
        """Test ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner`
        """
        model = ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner()  # noqa: E501
        if include_optional:
            return ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner(
                key = '',
                secret = infisicalapi_client.models._api_v1_secret_rotations_get_200_response_secret_rotations_inner_outputs_inner_secret._api_v1_secret_rotations_get_200_response_secretRotations_inner_outputs_inner_secret(
                    secret_key = '', 
                    id = '', 
                    version = 1.337, )
            )
        else:
            return ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner(
                key = '',
                secret = infisicalapi_client.models._api_v1_secret_rotations_get_200_response_secret_rotations_inner_outputs_inner_secret._api_v1_secret_rotations_get_200_response_secretRotations_inner_outputs_inner_secret(
                    secret_key = '', 
                    id = '', 
                    version = 1.337, ),
        )
        """

    def testApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner(self):
        """Test ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
