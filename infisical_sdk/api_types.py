import json
from dataclasses import dataclass, field, fields
from enum import Enum
from typing import Any, Dict, List, Optional, Union


class ApprovalStatus(str, Enum):
    """Enum for approval status"""
    OPEN = "open"
    APPROVED = "approved"
    REJECTED = "rejected"


class BaseModel:
    """Base class for all models"""
    def to_dict(self) -> Dict:
        """Convert model to dictionary"""
        result = {}
        for key, value in self.__dict__.items():
            if value is not None:  # Skip None values
                if isinstance(value, BaseModel):
                    result[key] = value.to_dict()
                elif isinstance(value, list):
                    result[key] = [
                        item.to_dict() if isinstance(item, BaseModel) else item
                        for item in value
                    ]
                elif isinstance(value, Enum):
                    result[key] = value.value
                else:
                    result[key] = value
        return result

    @classmethod
    def from_dict(cls, data: Dict) -> 'BaseModel':
        """Create model from dictionary"""
        # Get only the fields that exist in the dataclass
        valid_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered_data)

    def to_json(self) -> str:
        """Convert model to JSON string"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> 'BaseModel':
        """Create model from JSON string"""
        data = json.loads(json_str)
        return cls.from_dict(data)


@dataclass(frozen=True)
class SecretTag(BaseModel):
    """Model for secret tags"""
    id: str
    slug: str
    name: str
    color: Optional[str] = None


@dataclass
class BaseSecret(BaseModel):
    """Infisical Secret"""
    id: str
    _id: str
    workspace: str
    environment: str
    version: int
    type: str
    secretKey: str
    secretValue: str
    secretComment: str
    createdAt: str
    updatedAt: str
    secretMetadata: Optional[Dict[str, Any]] = None
    secretValueHidden: Optional[bool] = False
    secretReminderNote: Optional[str] = None
    secretReminderRepeatDays: Optional[int] = None
    skipMultilineEncoding: Optional[bool] = False
    metadata: Optional[Any] = None
    secretPath: Optional[str] = None
    tags: List[SecretTag] = field(default_factory=list)


@dataclass
class Import(BaseModel):
    """Model for imports section"""
    secretPath: str
    environment: str
    folderId: Optional[str] = None
    secrets: List[BaseSecret] = field(default_factory=list)


@dataclass
class ListSecretsResponse(BaseModel):
    """Complete response model for secrets API"""
    secrets: List[BaseSecret]
    imports: List[Import] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListSecretsResponse':
        """Create model from dictionary with camelCase keys, handling nested objects"""
        return cls(
            secrets=[BaseSecret.from_dict(secret) for secret in data['secrets']],
            imports=[Import.from_dict(imp) for imp in data.get('imports', [])]
        )


@dataclass
class SingleSecretResponse(BaseModel):
    """Response model for get secret API"""
    secret: BaseSecret

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleSecretResponse':
        return cls(
            secret=BaseSecret.from_dict(data['secret']),
        )


@dataclass
class MachineIdentityLoginResponse(BaseModel):
    """Response model for machine identity login API"""
    accessToken: str
    expiresIn: int
    accessTokenMaxTTL: int
    tokenType: str


class SymmetricEncryption(str, Enum):
    AES_GCM_256 = "aes-256-gcm"
    AES_GCM_128 = "aes-128-gcm"


class AsymmetricEncryption(str, Enum):
    RSA_4096 = "rsa-4096"
    ECC_NIST_P256 = "ecc-nist-p256"


class RSASigningAlgorithm(str, Enum):
    RSASSA_PSS_SHA_256 = "RSASSA_PSS_SHA_256"
    RSASSA_PSS_SHA_384 = "RSASSA_PSS_SHA_384"
    RSASSA_PSS_SHA_512 = "RSASSA_PSS_SHA_512"
    RSASSA_PKCS1_V1_5_SHA_256 = "RSASSA_PKCS1_V1_5_SHA_256"
    RSASSA_PKCS1_V1_5_SHA_384 = "RSASSA_PKCS1_V1_5_SHA_384"
    RSASSA_PKCS1_V1_5_SHA_512 = "RSASSA_PKCS1_V1_5_SHA_512"


class ECDSASigningAlgorithm(str, Enum):
    ECDSA_SHA_256 = "ECDSA_SHA_256"
    ECDSA_SHA_384 = "ECDSA_SHA_384"
    ECDSA_SHA_512 = "ECDSA_SHA_512"


class OrderDirection(str, Enum):
    ASC = "asc"
    DESC = "desc"


class KmsKeysOrderBy(str, Enum):
    NAME = "name"


@dataclass
class KmsKey(BaseModel):
    """Infisical KMS Key"""
    id: str
    description: str
    isDisabled: bool
    orgId: str
    name: str
    createdAt: str
    updatedAt: str
    projectId: str
    version: int
    encryptionAlgorithm: SymmetricEncryption


@dataclass
class ListKmsKeysResponse(BaseModel):
    """Complete response model for Kms Keys API"""
    keys: List[KmsKey]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListKmsKeysResponse':
        """Create model from dictionary with camelCase keys, handling nested objects"""
        return cls(
            keys=[KmsKey.from_dict(key) for key in data['keys']],
            totalCount=data['totalCount']
        )


@dataclass
class SingleKmsKeyResponse(BaseModel):
    """Response model for get/create/update/delete API"""
    key: KmsKey

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleKmsKeyResponse':
        return cls(
            key=KmsKey.from_dict(data['key']),
        )


@dataclass
class KmsKeyEncryptDataResponse(BaseModel):
    """Response model for encrypt data API"""
    ciphertext: str


@dataclass
class KmsKeyDecryptDataResponse(BaseModel):
    """Response model for decrypt data API"""
    plaintext: str


@dataclass
class KmsKeySignDataResponse(BaseModel):
    signature: str
    keyId: str
    signingAlgorithm: Union[ECDSASigningAlgorithm | RSASigningAlgorithm]


@dataclass
class KmsKeyVerifyDataResponse(BaseModel):
    signatureValid: bool
    keyId: str
    signingAlgorithm: Union[ECDSASigningAlgorithm | RSASigningAlgorithm]
