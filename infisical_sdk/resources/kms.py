from typing import Union

from infisical_sdk.api_types import (
    ECDSASigningAlgorithm,
    KmsKey,
    KmsKeyDecryptDataResponse,
    KmsKeyEncryptDataResponse,
    KmsKeySignDataResponse,
    KmsKeysOrderBy,
    KmsKeyVerifyDataResponse,
    ListKmsKeysResponse,
    OrderDirection,
    RSASigningAlgorithm,
    SingleKmsKeyResponse,
    SymmetricEncryption,
)
from infisical_sdk.infisical_requests import InfisicalRequests


class KMS:
    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def list_keys(
            self,
            project_id: str,
            offset: int = 0,
            limit: int = 100,
            order_by: KmsKeysOrderBy = KmsKeysOrderBy.NAME,
            order_direction: OrderDirection = OrderDirection.ASC,
            search: str = None) -> ListKmsKeysResponse:

        params = {
            "projectId": project_id,
            "search": search,
            "offset": offset,
            "limit": limit,
            "orderBy": order_by,
            "orderDirection": order_direction,
        }

        result = self.requests.get(
            path="/api/v1/kms/keys",
            params=params,
            model=ListKmsKeysResponse
        )

        return result.data

    def get_key_by_id(
            self,
            key_id: str) -> KmsKey:

        result = self.requests.get(
            path=f"/api/v1/kms/keys/{key_id}",
            model=SingleKmsKeyResponse
        )

        return result.data.key

    def get_key_by_name(
            self,
            key_name: str,
            project_id: str) -> KmsKey:

        params = {
            "projectId": project_id,
        }

        result = self.requests.get(
            path=f"/api/v1/kms/keys/key-name/{key_name}",
            params=params,
            model=SingleKmsKeyResponse
        )

        return result.data.key

    def create_key(
            self,
            name: str,
            project_id: str,
            encryption_algorithm: SymmetricEncryption,
            description: str = None) -> KmsKey:

        request_body = {
            "name": name,
            "projectId": project_id,
            "encryptionAlgorithm": encryption_algorithm,
            "description": description,
        }

        result = self.requests.post(
            path="/api/v1/kms/keys",
            json=request_body,
            model=SingleKmsKeyResponse
        )

        return result.data.key

    def update_key(
            self,
            key_id: str,
            name: str = None,
            is_disabled: bool = None,
            description: str = None) -> KmsKey:

        request_body = {
            "name": name,
            "isDisabled": is_disabled,
            "description": description,
        }

        result = self.requests.patch(
            path=f"/api/v1/kms/keys/{key_id}",
            json=request_body,
            model=SingleKmsKeyResponse
        )

        return result.data.key

    def delete_key(
            self,
            key_id: str) -> KmsKey:

        result = self.requests.delete(
            path=f"/api/v1/kms/keys/{key_id}",
            json={},
            model=SingleKmsKeyResponse
        )

        return result.data.key

    def encrypt_data(
            self,
            key_id: str,
            base64EncodedPlaintext: str) -> str:
        """
            Encrypt data with the specified KMS key.

            :param key_id: The ID of the key to decrypt the ciphertext with
            :type key_id: str
            :param base64EncodedPlaintext: The base64 encoded plaintext to encrypt
            :type plaintext: str


            :return: The encrypted base64 encoded plaintext (ciphertext)
            :rtype: str
        """

        request_body = {
            "plaintext": base64EncodedPlaintext
        }

        result = self.requests.post(
            path=f"/api/v1/kms/keys/{key_id}/encrypt",
            json=request_body,
            model=KmsKeyEncryptDataResponse
        )

        return result.data.ciphertext

    def decrypt_data(
            self,
            key_id: str,
            ciphertext: str) -> str:
        """
            Decrypt data with the specified KMS key.

            :param key_id: The ID of the key to decrypt the ciphertext with
            :type key_id: str
            :param ciphertext: The encrypted base64 plaintext to decrypt
            :type ciphertext: str


            :return: The base64 encoded plaintext
            :rtype: str
        """

        request_body = {
            "ciphertext": ciphertext
        }

        result = self.requests.post(
            path=f"/api/v1/kms/keys/{key_id}/decrypt",
            json=request_body,
            model=KmsKeyDecryptDataResponse
        )

        return result.data.plaintext

    def sign_data(
        self,
        key_id: str,
        base64EncodedPlaintext: str,
        signingAlgorithm: Union[ECDSASigningAlgorithm | RSASigningAlgorithm],
    ) -> str:
        """
        Sign the provided base64-encoded plaintext using the specified KMS key and signing algorithm.

        :param key_id: The ID of the key used for signing.
        :type key_id: str
        :param base64EncodedPlaintext: The base64-encoded plaintext to sign.
        :type base64EncodedPlaintext: str
        :param signingAlgorithm: The signing algorithm to use (RSA or ECDSA variants).
        :type signingAlgorithm: ECDSASigningAlgorithm | RSASigningAlgorithm

        :return: The base64-encoded signature.
        :rtype: str
        """
        request_body = {
            "data": base64EncodedPlaintext,
            "signingAlgorithm": signingAlgorithm.value,
        }

        result = self.requests.post(
            path=f"/api/v1/kms/keys/{key_id}/sign",
            json=request_body,
            model=KmsKeySignDataResponse,
        )

        return result.data.signature

    def verify_data(
        self,
        key_id: str,
        base64EncodedPlaintext: str,
        signingAlgorithm: Union[ECDSASigningAlgorithm | RSASigningAlgorithm],
        signature: str,
    ) -> bool:
        """
        Verify a signature for the given base64-encoded plaintext using the specified KMS key and signing algorithm.

        :param key_id: The ID of the key used to verify the signature.
        :type key_id: str
        :param base64EncodedPlaintext: The base64-encoded plaintext whose signature is being verified.
        :type base64EncodedPlaintext: str
        :param signingAlgorithm: The algorithm used to generate the signature.
        :type signingAlgorithm: ECDSASigningAlgorithm | RSASigningAlgorithm
        :param signature: The base64-encoded signature to verify.
        :type signature: str

        :return: True if the signature is valid, False otherwise.
        :rtype: bool
        """
        request_body = {
            "data": base64EncodedPlaintext,
            "signingAlgorithm": signingAlgorithm.value,
            "signature": signature,
        }

        result = self.requests.post(
            path=f"/api/v1/kms/keys/{key_id}/verify",
            json=request_body,
            model=KmsKeyVerifyDataResponse,
        )

        return result.data.signatureValid
