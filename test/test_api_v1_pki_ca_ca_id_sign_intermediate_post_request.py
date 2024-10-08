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

from infisicalapi_client.models.api_v1_pki_ca_ca_id_sign_intermediate_post_request import ApiV1PkiCaCaIdSignIntermediatePostRequest  # noqa: E501

class TestApiV1PkiCaCaIdSignIntermediatePostRequest(unittest.TestCase):
    """ApiV1PkiCaCaIdSignIntermediatePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PkiCaCaIdSignIntermediatePostRequest:
        """Test ApiV1PkiCaCaIdSignIntermediatePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PkiCaCaIdSignIntermediatePostRequest`
        """
        model = ApiV1PkiCaCaIdSignIntermediatePostRequest()  # noqa: E501
        if include_optional:
            return ApiV1PkiCaCaIdSignIntermediatePostRequest(
                csr = '0',
                not_before = '',
                not_after = '',
                max_path_length = -1
            )
        else:
            return ApiV1PkiCaCaIdSignIntermediatePostRequest(
                csr = '0',
                not_after = '',
        )
        """

    def testApiV1PkiCaCaIdSignIntermediatePostRequest(self):
        """Test ApiV1PkiCaCaIdSignIntermediatePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
