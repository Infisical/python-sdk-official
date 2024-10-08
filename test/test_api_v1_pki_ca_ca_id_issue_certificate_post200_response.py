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

from infisicalapi_client.models.api_v1_pki_ca_ca_id_issue_certificate_post200_response import ApiV1PkiCaCaIdIssueCertificatePost200Response  # noqa: E501

class TestApiV1PkiCaCaIdIssueCertificatePost200Response(unittest.TestCase):
    """ApiV1PkiCaCaIdIssueCertificatePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PkiCaCaIdIssueCertificatePost200Response:
        """Test ApiV1PkiCaCaIdIssueCertificatePost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PkiCaCaIdIssueCertificatePost200Response`
        """
        model = ApiV1PkiCaCaIdIssueCertificatePost200Response()  # noqa: E501
        if include_optional:
            return ApiV1PkiCaCaIdIssueCertificatePost200Response(
                certificate = '',
                issuing_ca_certificate = '',
                certificate_chain = '',
                private_key = '',
                serial_number = ''
            )
        else:
            return ApiV1PkiCaCaIdIssueCertificatePost200Response(
                certificate = '',
                issuing_ca_certificate = '',
                certificate_chain = '',
                private_key = '',
                serial_number = '',
        )
        """

    def testApiV1PkiCaCaIdIssueCertificatePost200Response(self):
        """Test ApiV1PkiCaCaIdIssueCertificatePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
