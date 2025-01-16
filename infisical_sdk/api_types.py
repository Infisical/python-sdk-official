from dataclasses import dataclass, field, fields
from typing import Optional, List, Any, Dict
from enum import Enum
import json


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
    def from_dict(cls, data: Dict) -> 'ListSecretsResponse':
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


@dataclass
class BaseKey(BaseModel):
    createdAt: str
    id: str
    name: str
    orgId: str
    updatedAt: str
    description: Optional[str] = None
    isDisabled: Optional[bool] = field(default=False)
    isReserved: Optional[bool] = field(default=True)
    projectId: Optional[str] = None
    slug: Optional[str] = None


@dataclass
class ListKey(BaseKey):
    encryptionAlgorithm: str = "aes-256-gcm"
    version: int = 1

@dataclass
class ListKeysResponse(BaseModel):
    keys: List[ListKey]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListKeysResponse':
        return cls(
            keys=[ListKey.from_dict(key) for key in data['keys']],
            totalCount=data['totalCount']
        )


@dataclass
class SingleKeyResponse(BaseModel):
    key: BaseKey

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleKeyResponse':
        return cls(
            key=BaseKey.from_dict(data['key'])
        )

@dataclass
class EncryptDataResponse(BaseModel):
    ciphertext: str


@dataclass
class DecryptDataResponse(BaseModel):
    plaintext: str
