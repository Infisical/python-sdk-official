import base64
import json
from typing import List, Union
import os
import datetime
from typing import Dict, Any

import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.exceptions import NoCredentialsError

from .infisical_requests import InfisicalRequests
from .api_types import ListSecretsResponse, MachineIdentityLoginResponse
from .api_types import SingleSecretResponse, BaseSecret
from .api_types import (
    BaseKey,
    ListKeysResponse,
    SingleKeyResponse,
    EncryptDataResponse,
    DecryptDataResponse,
)


class InfisicalSDKClient:
    def __init__(self, host: str, token: str = None):
        self.host = host
        self.access_token = token

        self.api = InfisicalRequests(host=host, token=token)

        self.auth = Auth(self)
        self.secrets = V3RawSecrets(self)
        self.keys = V1Keys(self)

    def set_token(self, token: str):
        """
        Set the access token for future requests.
        """
        self.api.set_token(token)
        self.access_token = token

    def get_token(self):
        """
        Set the access token for future requests.
        """
        return self.access_token


class UniversalAuth:
    def __init__(self, client: InfisicalSDKClient):
        self.client = client

    def login(self, client_id: str, client_secret: str) -> MachineIdentityLoginResponse:
        """
        Login with Universal Auth.

        Args:
            client_id (str): Your Machine Identity Client ID.
            client_secret (str): Your Machine Identity Client Secret.

        Returns:
            Dict: A dictionary containing the access token and related information.
        """

        requestBody = {
            "clientId": client_id,
            "clientSecret": client_secret
        }

        result = self.client.api.post(
          path="/api/v1/auth/universal-auth/login",
          json=requestBody,
          model=MachineIdentityLoginResponse
        )

        self.client.set_token(result.data.accessToken)

        return result.data


class AWSAuth:
    def __init__(self, client: InfisicalSDKClient) -> None:
        self.client = client

    def login(self, identity_id: str) -> MachineIdentityLoginResponse:
        """
        Login with AWS Authentication.

        Args:
            identity_id (str): Your Machine Identity ID that has AWS Auth configured.

        Returns:
            Dict: A dictionary containing the access token and related information.
        """

        identity_id = identity_id or os.getenv("INFISICAL_AWS_IAM_AUTH_IDENTITY_ID")
        if not identity_id:
            raise ValueError(
              "Identity ID must be provided or set in the environment variable" +
              "INFISICAL_AWS_IAM_AUTH_IDENTITY_ID."
            )

        aws_region = self.get_aws_region()
        session = boto3.Session(region_name=aws_region)

        credentials = self._get_aws_credentials(session)

        iam_request_url = f"https://sts.{aws_region}.amazonaws.com/"
        iam_request_body = "Action=GetCallerIdentity&Version=2011-06-15"

        request_headers = self._prepare_aws_request(
          iam_request_url,
          iam_request_body,
          credentials,
          aws_region
        )

        requestBody = {
          "identityId": identity_id,
          "iamRequestBody": base64.b64encode(iam_request_body.encode()).decode(),
          "iamRequestHeaders": base64.b64encode(json.dumps(request_headers).encode()).decode(),
          "iamHttpRequestMethod": "POST"
        }

        result = self.client.api.post(
          path="/api/v1/auth/aws-auth/login",
          json=requestBody,
          model=MachineIdentityLoginResponse
        )

        self.client.set_token(result.data.accessToken)

        return result.data

    def _get_aws_credentials(self, session: boto3.Session) -> Any:
        try:
            credentials = session.get_credentials()
            if credentials is None:
                raise NoCredentialsError("AWS credentials not found.")
            return credentials.get_frozen_credentials()
        except NoCredentialsError as e:
            raise RuntimeError(f"AWS IAM Auth Login failed: {str(e)}")

    def _prepare_aws_request(
      self,
      url: str,
      body: str,
      credentials: Any,
      region: str) -> Dict[str, str]:

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
        region = os.getenv("AWS_REGION")  # Typically found in lambda runtime environment
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

    def list_secrets(
            self,
            project_id: str,
            environment_slug: str,
            secret_path: str,
            expand_secret_references: bool = True,
            recursive: bool = False,
            include_imports: bool = True,
            tag_filters: List[str] = []) -> ListSecretsResponse:

        params = {
            "workspaceId": project_id,
            "environment": environment_slug,
            "secretPath": secret_path,
            "expandSecretReferences": str(expand_secret_references).lower(),
            "recursive": str(recursive).lower(),
            "include_imports": str(include_imports).lower(),
        }

        if tag_filters:
            params["tagSlugs"] = ",".join(tag_filters)

        result = self.client.api.get(
            path="/api/v3/secrets/raw",
            params=params,
            model=ListSecretsResponse
        )

        return result.data

    def get_secret_by_name(
            self,
            secret_name: str,
            project_id: str,
            environment_slug: str,
            secret_path: str,
            expand_secret_references: bool = True,
            include_imports: bool = True,
            version: str = None) -> BaseSecret:

        params = {
          "workspaceId": project_id,
          "environment": environment_slug,
          "secretPath": secret_path,
          "expandSecretReferences": str(expand_secret_references).lower(),
          "include_imports": str(include_imports).lower(),
          "version": version
        }

        result = self.client.api.get(
            path=f"/api/v3/secrets/raw/{secret_name}",
            params=params,
            model=SingleSecretResponse
        )

        return result.data.secret

    def create_secret_by_name(
            self,
            secret_name: str,
            project_id: str,
            secret_path: str,
            environment_slug: str,
            secret_value: str = None,
            secret_comment: str = None,
            skip_multiline_encoding: bool = False,
            secret_reminder_repeat_days: Union[float, int] = None,
            secret_reminder_note: str = None) -> BaseSecret:

        requestBody = {
          "workspaceId": project_id,
          "environment": environment_slug,
          "secretPath": secret_path,
          "secretValue": secret_value,
          "secretComment": secret_comment,
          "tagIds": None,
          "skipMultilineEncoding": skip_multiline_encoding,
          "type": "shared",
          "secretReminderRepeatDays": secret_reminder_repeat_days,
          "secretReminderNote": secret_reminder_note
        }
        result = self.client.api.post(
            path=f"/api/v3/secrets/raw/{secret_name}",
            json=requestBody,
            model=SingleSecretResponse
        )

        return result.data.secret

    def update_secret_by_name(
            self,
            current_secret_name: str,
            project_id: str,
            secret_path: str,
            environment_slug: str,
            secret_value: str = None,
            secret_comment: str = None,
            skip_multiline_encoding: bool = False,
            secret_reminder_repeat_days: Union[float, int] = None,
            secret_reminder_note: str = None,
            new_secret_name: str = None) -> BaseSecret:

        requestBody = {
          "workspaceId": project_id,
          "environment": environment_slug,
          "secretPath": secret_path,
          "secretValue": secret_value,
          "secretComment": secret_comment,
          "new_secret_name": new_secret_name,
          "tagIds": None,
          "skipMultilineEncoding": skip_multiline_encoding,
          "type": "shared",
          "secretReminderRepeatDays": secret_reminder_repeat_days,
          "secretReminderNote": secret_reminder_note
        }

        result = self.client.api.patch(
            path=f"/api/v3/secrets/raw/{current_secret_name}",
            json=requestBody,
            model=SingleSecretResponse
        )
        return result.data.secret

    def delete_secret_by_name(
            self,
            secret_name: str,
            project_id: str,
            secret_path: str,
            environment_slug: str) -> BaseSecret:

        requestBody = {
          "workspaceId": project_id,
          "environment": environment_slug,
          "secretPath": secret_path,
          "type": "shared",
        }

        result = self.client.api.delete(
            path=f"/api/v3/secrets/raw/{secret_name}",
            json=requestBody,
            model=SingleSecretResponse
        )

        return result.data.secret

class V1Keys:
    def __init__(self, client: InfisicalSDKClient):
        """
        Initializes the KeysAPI class.

        Args:
            client: An instance of the API client.
        """
        self.client = client

    def list_keys(
        self,
        project_id: str,
        offset: int = 0,
        limit: int = 100,
        order_by: str = "name",
        order_direction: str = "asc",
        search: str = None,
    ) -> ListKeysResponse:
        """
        List KMS keys for a given project.

        Args:
            project_id: The project ID to list keys from.
            offset: The offset to start from.
            limit: The number of keys to return.
            order_by: The column to order keys by.
            order_direction: The direction to order keys (asc/desc).
            search: A text string to filter key names.

        Returns:
            A dictionary containing the list of keys and the total count.
        """
        params = {
            "projectId": project_id,
            "offset": offset,
            "limit": limit,
            "orderBy": order_by,
            "orderDirection": order_direction,
        }
        if search:
            params["search"] = search

        response = self.client.api.get(
            path="/api/v1/kms/keys", model=ListKeysResponse, params=params
        )
        return response.data

    def create_key(
        self,
        name: str,
        project_id: str,
        description: str = None,
        encryption_algorithm: str = "aes-256-gcm",
    ) -> BaseKey:
        """
        Create a new KMS key.

        Args:
            name: The name of the key.
            project_id: The project ID to create the key in.
            description: An optional description of the key.
            encryption_algorithm: The encryption algorithm to use.

        Returns:
            A dictionary containing the created key details.
        """
        body = {
            "name": name,
            "projectId": project_id,
            "description": description,
            "encryptionAlgorithm": encryption_algorithm,
        }
        response = self.client.api.post(
            path="/api/v1/kms/keys", model=SingleKeyResponse, json=body
        )
        return response.data.key

    def update_key(
        self,
        key_id: str,
        name: str = None,
        description: str = None,
        is_disabled: bool = None,
    ) -> BaseKey:
        """
        Update a KMS key.

        Args:
            key_id: The ID of the key to update.
            name: The updated name of the key.
            description: The updated description of the key.
            is_disabled: Flag to enable or disable the key.

        Returns:
            A dictionary containing the updated key details.
        """
        body = {}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if is_disabled is not None:
            body["isDisabled"] = is_disabled

        response = self.client.api.patch(
            path=f"/api/v1/kms/keys/{key_id}", model=SingleKeyResponse, json=body
        )
        return response.data.key

    def delete_key(self, key_id: str) -> BaseKey:
        """
        Delete a KMS key.

        Args:
            key_id: The ID of the key to delete.

        Returns:
            A dictionary containing the details of the deleted key.
        """
        response = self.client.api.delete(
            path=f"/api/v1/kms/keys/{key_id}", model=SingleKeyResponse
        )
        return response.data.key

    def encrypt_data(self, key_id: str, plaintext: str) -> EncryptDataResponse:
        """
        Encrypt data using a KMS key.

        Args:
            key_id: The ID of the key to encrypt the data with.
            plaintext: The plaintext to be encrypted (base64 encoded).

        Returns:
            A dictionary containing the ciphertext.
        """
        body = {"plaintext": plaintext}
        response = self.client.api.post(
            path=f"/api/v1/kms/keys/{key_id}/encrypt",
            model=EncryptDataResponse,
            json=body,
        )
        return response.data

    def decrypt_data(self, key_id: str, ciphertext: str) -> DecryptDataResponse:
        """
        Decrypt data using a KMS key.

        Args:
            key_id: The ID of the key to decrypt the data with.
            ciphertext: The ciphertext to be decrypted (base64 encoded).

        Returns:
            A dictionary containing the plaintext.
        """
        body = {"ciphertext": ciphertext}
        response = self.client.api.post(
            path=f"/api/v1/kms/keys/{key_id}/decrypt",
            model=DecryptDataResponse,
            json=body,
        )
        return response.data
