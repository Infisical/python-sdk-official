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

from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_rollback_post200_response import ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response  # noqa: E501

class TestApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response(unittest.TestCase):
    """ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response:
        """Test ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response`
        """
        model = ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response(
                secret_snapshot = infisicalapi_client.models._api_v1_workspace__workspace_id__secret_snapshots_get_200_response_secret_snapshots_inner._api_v1_workspace__workspaceId__secret_snapshots_get_200_response_secretSnapshots_inner(
                    id = '', 
                    env_id = '', 
                    folder_id = '', 
                    parent_folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response(
                secret_snapshot = infisicalapi_client.models._api_v1_workspace__workspace_id__secret_snapshots_get_200_response_secret_snapshots_inner._api_v1_workspace__workspaceId__secret_snapshots_get_200_response_secretSnapshots_inner(
                    id = '', 
                    env_id = '', 
                    folder_id = '', 
                    parent_folder_id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response(self):
        """Test ApiV1SecretSnapshotSecretSnapshotIdRollbackPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
