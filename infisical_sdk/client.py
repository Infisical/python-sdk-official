import base64
import json
from typing import List, Union
import os
import json
import base64
import datetime
from typing import Dict, Any

import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.exceptions import NoCredentialsError


import infisicalapi_client 
from infisicalapi_client.models.api_v1_auth_aws_auth_login_post_request import ApiV1AuthAwsAuthLoginPostRequest
from infisicalapi_client.models.api_v1_auth_token_auth_identities_identity_id_tokens_post200_response import ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response
from infisicalapi_client.models.api_v1_auth_universal_auth_login_post_request import ApiV1AuthUniversalAuthLoginPostRequest
from infisicalapi_client.models.api_v3_secrets_raw_get200_response import ApiV3SecretsRawGet200Response
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_delete_request import ApiV3SecretsRawSecretNameDeleteRequest
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_get200_response import ApiV3SecretsRawSecretNameGet200Response
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_patch_request import ApiV3SecretsRawSecretNamePatchRequest
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_post200_response import ApiV3SecretsRawSecretNamePost200Response
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_post_request import ApiV3SecretsRawSecretNamePostRequest

class InfisicalSDKClient:
    def __init__(self, host: str, token: str  = None):
        self.host = host
        self.token_type = None
        self.expires_in = None

        self._api_config = infisicalapi_client.Configuration(host=host, access_token=token)
        self._api_client = infisicalapi_client.ApiClient(self._api_config)
        self._api_instance = infisicalapi_client.DefaultApi(self._api_client)
        self.rest = self._api_instance

        self.auth = Auth(self)
        self.secrets = V3RawSecrets(self)

    def set_token(self, token: str):
        """
        Set the access token for future requests.
        """
        self._api_config.access_token = token

    def get_token(self):
        """
        Set the access token for future requests.
        """
        return self.token


class UniversalAuth:
    def __init__(self, client: InfisicalSDKClient):
        self.client = client

    def login(self, client_id: str, client_secret: str) -> ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response:
        """
        Login with Universal Auth.

        Args:
            client_id (str): Your Machine Identity Client ID.
            client_secret (str): Your Machine Identity Client Secret.

        Returns:
            Dict: A dictionary containing the access token and related information.
        """

        response = self.client._api_instance.api_v1_auth_universal_auth_login_post(ApiV1AuthUniversalAuthLoginPostRequest(
            client_id = client_id,
            client_secret = client_secret
        ))

        self.client.set_token(response.access_token)

        return response
    

class AWSAuth:
    def __init__(self, client: InfisicalSDKClient) -> None:
        self.client = client

    def login(self, identity_id: str) -> ApiV1AuthTokenAuthIdentitiesIdentityIdTokensPost200Response:
        """
        Login with AWS Authentication. 

        Args:
            identity_id (str): Your Machine Identity ID that has AWS Auth configured.

        Returns:
            Dict: A dictionary containing the access token and related information.
        """

        identity_id = identity_id or os.getenv("INFISICAL_AWS_IAM_AUTH_IDENTITY_ID")
        if not identity_id:
            raise ValueError("Identity ID must be provided or set in the environment variable INFISICAL_AWS_IAM_AUTH_IDENTITY_ID.")

        aws_region = self.get_aws_region()
        session = boto3.Session(region_name=aws_region)

        credentials = self._get_aws_credentials(session)

        iam_request_url = f"https://sts.{aws_region}.amazonaws.com/"
        iam_request_body = "Action=GetCallerIdentity&Version=2011-06-15"
        request_headers = self._prepare_aws_request(iam_request_url, iam_request_body, credentials, aws_region)

        login_request = ApiV1AuthAwsAuthLoginPostRequest(
            identityId=identity_id,
            iamRequestBody=base64.b64encode(iam_request_body.encode()).decode(),
            iamRequestHeaders=base64.b64encode(json.dumps(request_headers).encode()).decode(),
            iamHttpRequestMethod="POST"
        )

        response = self.client._api_instance.api_v1_auth_aws_auth_login_post(login_request)
        self.client.set_token(response.access_token)

        return response

    def _get_aws_credentials(self, session: boto3.Session) -> Any:
        try:
            credentials = session.get_credentials()
            if credentials is None:
                raise NoCredentialsError("AWS credentials not found.")
            return credentials.get_frozen_credentials()
        except NoCredentialsError as e:
            raise RuntimeError(f"AWS IAM Auth Login failed: {str(e)}")

    def _prepare_aws_request(self, url: str, body: str, credentials: Any, region: str) -> Dict[str, str]:
        current_time = datetime.datetime.now(datetime.timezone.utc)
        amz_date = current_time.strftime('%Y%m%dT%H%M%SZ')
        
        request = AWSRequest(method="POST", url=url, data=body)
        request.headers["X-Amz-Date"] = amz_date
        request.headers["Host"] = f"sts.{region}.amazonaws.com"
        request.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
        request.headers["Content-Length"] = str(len(body))

        signer = SigV4Auth(credentials, "sts", region)
        signer.add_auth(request)
        
        return {k: v for k, v in request.headers.items() if k.lower() != "content-length"}

    @staticmethod
    def get_aws_region() -> str:
        region = os.getenv("AWS_REGION") # Typically found in lambda runtime environment
        if region:
            return region

        try:
            return AWSAuth._get_aws_ec2_identity_document_region()
        except Exception as e:
            raise Exception("Failed to retrieve AWS region") from e

    @staticmethod
    def _get_aws_ec2_identity_document_region(timeout: int = 5000) -> str:
        session = requests.Session()
        token_response = session.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=timeout / 1000
        )
        token_response.raise_for_status()
        metadata_token = token_response.text

        identity_response = session.get(
            "http://169.254.169.254/latest/dynamic/instance-identity/document",
            headers={"X-aws-ec2-metadata-token": metadata_token, "Accept": "application/json"},
            timeout=timeout / 1000
        )

        identity_response.raise_for_status()
        return identity_response.json().get("region")


class Auth:
    def __init__(self, client):
        self.client = client
        self.aws_auth = AWSAuth(client)
        self.universal_auth = UniversalAuth(client)

class V3RawSecrets:
    def __init__(self, client: InfisicalSDKClient) -> None:
        self.client = client

    def list_secrets(self, project_id: str, environment_slug: str, secret_path: str, expand_secret_references: bool = True, recursive: bool = False, include_imports : bool = True, tag_filters: List[str] = []) -> ApiV3SecretsRawGet200Response:
        return self.client._api_instance.api_v3_secrets_raw_get(
            workspace_id=project_id, 
            environment=environment_slug, 
            secret_path=secret_path, 
            expand_secret_references=str(expand_secret_references).lower(), 
            recursive=str(recursive).lower(), 
            tag_slugs=",".join(tag_filters), 
            include_imports=str(include_imports).lower())

    def create_secret_by_name(self, secret_name: str, project_id: str, secret_path: str, environment_slug: str, secret_value: str = None, secret_comment: str = None, skip_multiline_encoding: bool = False, secret_reminder_repeat_days: Union[float, int] = None, secret_reminder_note: str = None) -> ApiV3SecretsRawSecretNamePost200Response:
        secret_request = ApiV3SecretsRawSecretNamePostRequest(
            workspaceId = project_id,
            environment = environment_slug,
            secretPath= secret_path,
            secretValue = secret_value,
            secretComment = secret_comment,
            tagIds = None,
            skipMultilineEncoding = skip_multiline_encoding,
            type = "shared",
            secretReminderRepeatDays = secret_reminder_repeat_days,
            secretReminderNote = secret_reminder_note
        )

        return self.client._api_instance.api_v3_secrets_raw_secret_name_post(secret_name, secret_request)
         

    def update_secret_by_name(self, current_secret_name: str, project_id: str, secret_path: str, environment_slug: str, secret_value: str = None, secret_comment: str = None, skip_multiline_encoding: bool = False, secret_reminder_repeat_days: Union[float, int] = None, secret_reminder_note: str = None, new_secret_name: str = None) -> ApiV3SecretsRawSecretNamePost200Response:
        secret_request = ApiV3SecretsRawSecretNamePatchRequest(
            workspaceId = project_id,
            environment = environment_slug,
            secretPath= secret_path,
            secretValue = secret_value,
            secretComment = secret_comment,
            new_secret_name=new_secret_name,
            tagIds = None,
            skipMultilineEncoding = skip_multiline_encoding,
            type = "shared",
            secretReminderRepeatDays = secret_reminder_repeat_days,
            secretReminderNote = secret_reminder_note
        )

        return self.client._api_instance.api_v3_secrets_raw_secret_name_patch(current_secret_name, secret_request) 

    def delete_secret_by_name(self, secret_name: str, project_id: str, secret_path: str, environment_slug: str) -> ApiV3SecretsRawSecretNamePost200Response:
        secret_delete_request = ApiV3SecretsRawSecretNameDeleteRequest(
            workspaceId = project_id,
            environment = environment_slug,
            secretPath= secret_path,
            type = "shared",
        )

        return self.client._api_instance.api_v3_secrets_raw_secret_name_delete(secret_name, secret_delete_request)

    def get_secret_by_name(self, secret_name: str, project_id: str, environment_slug: str, secret_path: str, expand_secret_references: bool = True, include_imports : bool = True, version: str = None) -> ApiV3SecretsRawSecretNameGet200Response:
        return self.client._api_instance.api_v3_secrets_raw_secret_name_get(
            secret_name=secret_name,
            workspace_id=project_id, 
            environment=environment_slug, 
            secret_path=secret_path,
            version=version, 
            type="shared",
            expand_secret_references=str(expand_secret_references).lower(), 
            include_imports=str(include_imports).lower()
        )
