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

from infisicalapi_client.models.api_v3_secrets_backfill_secret_references_post_request import ApiV3SecretsBackfillSecretReferencesPostRequest  # noqa: E501

class TestApiV3SecretsBackfillSecretReferencesPostRequest(unittest.TestCase):
    """ApiV3SecretsBackfillSecretReferencesPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsBackfillSecretReferencesPostRequest:
        """Test ApiV3SecretsBackfillSecretReferencesPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsBackfillSecretReferencesPostRequest`
        """
        model = ApiV3SecretsBackfillSecretReferencesPostRequest()  # noqa: E501
        if include_optional:
            return ApiV3SecretsBackfillSecretReferencesPostRequest(
                project_id = '0'
            )
        else:
            return ApiV3SecretsBackfillSecretReferencesPostRequest(
                project_id = '0',
        )
        """

    def testApiV3SecretsBackfillSecretReferencesPostRequest(self):
        """Test ApiV3SecretsBackfillSecretReferencesPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
