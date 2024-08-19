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

from infisicalapi_client.models.api_v1_pki_certificates_serial_number_revoke_post_request import ApiV1PkiCertificatesSerialNumberRevokePostRequest  # noqa: E501

class TestApiV1PkiCertificatesSerialNumberRevokePostRequest(unittest.TestCase):
    """ApiV1PkiCertificatesSerialNumberRevokePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PkiCertificatesSerialNumberRevokePostRequest:
        """Test ApiV1PkiCertificatesSerialNumberRevokePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PkiCertificatesSerialNumberRevokePostRequest`
        """
        model = ApiV1PkiCertificatesSerialNumberRevokePostRequest()  # noqa: E501
        if include_optional:
            return ApiV1PkiCertificatesSerialNumberRevokePostRequest(
                revocation_reason = 'UNSPECIFIED'
            )
        else:
            return ApiV1PkiCertificatesSerialNumberRevokePostRequest(
                revocation_reason = 'UNSPECIFIED',
        )
        """

    def testApiV1PkiCertificatesSerialNumberRevokePostRequest(self):
        """Test ApiV1PkiCertificatesSerialNumberRevokePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
