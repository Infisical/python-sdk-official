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

from infisicalapi_client.models.api_v1_pki_ca_ca_id_csr_get200_response import ApiV1PkiCaCaIdCsrGet200Response  # noqa: E501

class TestApiV1PkiCaCaIdCsrGet200Response(unittest.TestCase):
    """ApiV1PkiCaCaIdCsrGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PkiCaCaIdCsrGet200Response:
        """Test ApiV1PkiCaCaIdCsrGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PkiCaCaIdCsrGet200Response`
        """
        model = ApiV1PkiCaCaIdCsrGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1PkiCaCaIdCsrGet200Response(
                csr = ''
            )
        else:
            return ApiV1PkiCaCaIdCsrGet200Response(
                csr = '',
        )
        """

    def testApiV1PkiCaCaIdCsrGet200Response(self):
        """Test ApiV1PkiCaCaIdCsrGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
