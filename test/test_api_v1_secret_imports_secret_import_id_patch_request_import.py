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

from infisicalapi_client.models.api_v1_secret_imports_secret_import_id_patch_request_import import ApiV1SecretImportsSecretImportIdPatchRequestImport  # noqa: E501

class TestApiV1SecretImportsSecretImportIdPatchRequestImport(unittest.TestCase):
    """ApiV1SecretImportsSecretImportIdPatchRequestImport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretImportsSecretImportIdPatchRequestImport:
        """Test ApiV1SecretImportsSecretImportIdPatchRequestImport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretImportsSecretImportIdPatchRequestImport`
        """
        model = ApiV1SecretImportsSecretImportIdPatchRequestImport()  # noqa: E501
        if include_optional:
            return ApiV1SecretImportsSecretImportIdPatchRequestImport(
                environment = '',
                path = '',
                position = 1.337
            )
        else:
            return ApiV1SecretImportsSecretImportIdPatchRequestImport(
        )
        """

    def testApiV1SecretImportsSecretImportIdPatchRequestImport(self):
        """Test ApiV1SecretImportsSecretImportIdPatchRequestImport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
