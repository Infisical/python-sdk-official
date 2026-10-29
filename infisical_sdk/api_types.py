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
class CreateFolderResponseItem(BaseModel):
    """Folder model with path for create response"""
    id: str
    name: str
    createdAt: str
    updatedAt: str
    envId: str
    path: str
    version: Optional[int] = 1
    parentId: Optional[str] = None
    isReserved: Optional[bool] = False
    description: Optional[str] = None
    lastSecretModified: Optional[str] = None

@dataclass
class CreateFolderResponse(BaseModel):
    """Response model for create folder API"""
    folder: CreateFolderResponseItem

    @classmethod
    def from_dict(cls, data: Dict) -> 'CreateFolderResponse':
        return cls(
            folder=CreateFolderResponseItem.from_dict(data['folder']),
        )


@dataclass
class UpdateFolderResponseItem(BaseModel):
    """Folder model with path for update response"""
    id: str
    name: str
    createdAt: str
    updatedAt: str
    envId: str
    path: str
    version: Optional[int] = 1
    parentId: Optional[str] = None
    isReserved: Optional[bool] = False
    description: Optional[str] = None
    lastSecretModified: Optional[str] = None

@dataclass
class UpdateFolderResponse(BaseModel):
    """Response model for update folder API"""
    folder: UpdateFolderResponseItem

    @classmethod
    def from_dict(cls, data: Dict) -> 'UpdateFolderResponse':
        return cls(
            folder=UpdateFolderResponseItem.from_dict(data['folder']),
        )


@dataclass
class DeleteFolderResponseItem(BaseModel):
    """Folder model for delete response, which does not return a path"""
    id: str
    name: str
    createdAt: str
    updatedAt: str
    envId: str
    version: Optional[int] = 1
    parentId: Optional[str] = None
    isReserved: Optional[bool] = False
    description: Optional[str] = None
    lastSecretModified: Optional[str] = None

@dataclass
class DeleteFolderResponse(BaseModel):
    """Response model for delete folder API"""
    folder: DeleteFolderResponseItem

    @classmethod
    def from_dict(cls, data: Dict) -> 'DeleteFolderResponse':
        return cls(
            folder=DeleteFolderResponseItem.from_dict(data['folder']),
        )


@dataclass
class ListFoldersResponseItem(BaseModel):
    """Response model for list folders API"""
    id: str
    name: str
    createdAt: str
    updatedAt: str
    envId: str
    version: Optional[int] = 1
    parentId: Optional[str] = None
    isReserved: Optional[bool] = False
    description: Optional[str] = None
    lastSecretModified: Optional[str] = None 
    relativePath: Optional[str] = None


@dataclass
class ListFoldersResponse(BaseModel):
    """Complete response model for folders API"""
    folders: List[ListFoldersResponseItem]

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListFoldersResponse':
        """Create model from dictionary with camelCase keys, handling nested objects"""
        return cls(
            folders=[ListFoldersResponseItem.from_dict(folder) for folder in data['folders']]
        )


@dataclass
class Environment(BaseModel):
    """Environment model"""
    envId: str
    envName: str
    envSlug: str

@dataclass
class SingleFolderResponseItem(BaseModel):
    """Response model for get folder API"""
    id: str
    name: str
    createdAt: str
    updatedAt: str
    envId: str
    path: str
    projectId: str
    environment: Environment
    version: Optional[int] = 1
    parentId: Optional[str] = None
    isReserved: Optional[bool] = False
    description: Optional[str] = None
    lastSecretModified: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleFolderResponseItem':
        """Create model from dictionary with nested Environment"""
        folder_data = data.copy()
        folder_data['environment'] = Environment.from_dict(data['environment'])
        
        return super().from_dict(folder_data)

@dataclass
class SingleFolderResponse(BaseModel):
    """Response model for get/create folder API"""
    folder: SingleFolderResponseItem

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleFolderResponse':
        return cls(
            folder=SingleFolderResponseItem.from_dict(data['folder']),
        )

class DynamicSecretProviders(str, Enum):
    """Enum for dynamic secret provider types"""
    AWS_ELASTICACHE = "aws-elasticache"
    AWS_IAM = "aws-iam"
    AZURE_ENTRA_ID = "azure-entra-id"
    AZURE_SQL_DATABASE = "azure-sql-database"
    CASSANDRA = "cassandra"
    COUCHBASE = "couchbase"
    ELASTICSEARCH = "elastic-search"
    GCP_IAM = "gcp-iam"
    GITHUB = "github"
    KUBERNETES = "kubernetes"
    LDAP = "ldap"
    MONGO_ATLAS = "mongo-db-atlas"
    MONGODB = "mongo-db"
    RABBITMQ = "rabbit-mq"
    REDIS = "redis"
    SAP_ASE = "sap-ase"
    SAP_HANA = "sap-hana"
    SNOWFLAKE = "snowflake"
    SQL_DATABASE = "sql-database"
    TOTP = "totp"
    VERTICA = "vertica"

@dataclass
class DynamicSecret(BaseModel):
    """Infisical Dynamic Secret"""
    id: str
    name: str
    version: int
    type: str
    folderId: str
    createdAt: str
    updatedAt: str
    defaultTTL: Optional[str] = None
    maxTTL: Optional[str] = None
    status: Optional[str] = None
    statusDetails: Optional[str] = None
    usernameTemplate: Optional[str] = None
    metadata: Optional[List[Dict[str, str]]] = field(default_factory=list)
    inputs: Optional[Any] = None

@dataclass
class SingleDynamicSecretResponse(BaseModel):
    """Response model for get/create/update/delete dynamic secret API"""
    dynamicSecret: DynamicSecret

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleDynamicSecretResponse':
        return cls(
            dynamicSecret=DynamicSecret.from_dict(data['dynamicSecret']),
        )

@dataclass
class DynamicSecretLease(BaseModel):
    """Infisical Dynamic Secret Lease"""
    id: str
    expireAt: str
    createdAt: str
    updatedAt: str
    version: int
    dynamicSecretId: str
    externalEntityId: str
    status: Optional[str] = None
    statusDetails: Optional[str] = None
    dynamicSecret: Optional[DynamicSecret] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'DynamicSecretLease':
        """Create model from dictionary with nested DynamicSecret"""
        lease_data = data.copy()
        if 'dynamicSecret' in data and data['dynamicSecret'] is not None:
            lease_data['dynamicSecret'] = DynamicSecret.from_dict(data['dynamicSecret'])
        
        return super().from_dict(lease_data)

@dataclass
class CreateLeaseResponse(BaseModel):
    """Response model for create lease API - returns lease, dynamicSecret, and data"""
    lease: DynamicSecretLease
    dynamicSecret: DynamicSecret
    data: Any

    @classmethod
    def from_dict(cls, data: Dict) -> 'CreateLeaseResponse':
        return cls(
            lease=DynamicSecretLease.from_dict(data['lease']),
            dynamicSecret=DynamicSecret.from_dict(data['dynamicSecret']),
            data=data.get('data', {}),
        )

@dataclass
class SingleLeaseResponse(BaseModel):
    """Response model for get/delete/renew lease API - returns only lease"""
    lease: DynamicSecretLease

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleLeaseResponse':
        return cls(
            lease=DynamicSecretLease.from_dict(data['lease']),
        )

class AgentVaultTrafficPolicy(str, Enum):
    """Enum for which hosts an agent may reach through an Agent Vault proxy"""
    ANY_HOST = "any-host"
    BUNDLE_HOSTS = "bundle-hosts"

class AgentVaultSessionStatus(str, Enum):
    """Enum for Agent Vault session status"""
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"

class AgentVaultSessionScope(str, Enum):
    """Enum for whose Agent Vault sessions to list"""
    MINE = "mine"
    ALL = "all"

@dataclass
class AgentVaultProxy(BaseModel):
    """Infisical Agent Vault Proxy. Only admins see the settings fields, so they are None for members."""
    id: str
    name: str
    heartbeat: Optional[str] = None
    isHealthy: Optional[bool] = None
    rootCaFingerprint: Optional[str] = None
    rootCaExpiresAt: Optional[str] = None
    trafficPolicy: Optional[str] = None
    allowedHosts: Optional[str] = None
    pollInterval: Optional[int] = None
    createdAt: Optional[str] = None

@dataclass
class SingleAgentVaultProxyResponse(BaseModel):
    """Response model for update/delete/revoke Agent Vault proxy API"""
    proxy: AgentVaultProxy

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleAgentVaultProxyResponse':
        return cls(
            proxy=AgentVaultProxy.from_dict(data['proxy']),
        )

@dataclass
class AgentVaultProxyWithTokenResponse(BaseModel):
    """Response model for create Agent Vault proxy and rotate proxy token API. The token is only returned once."""
    proxy: AgentVaultProxy
    proxyToken: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultProxyWithTokenResponse':
        return cls(
            proxy=AgentVaultProxy.from_dict(data['proxy']),
            proxyToken=data['proxyToken'],
        )

@dataclass
class ListAgentVaultProxiesResponse(BaseModel):
    """Response model for list Agent Vault proxies API"""
    proxies: List[AgentVaultProxy]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultProxiesResponse':
        return cls(
            proxies=[AgentVaultProxy.from_dict(proxy) for proxy in data['proxies']],
            totalCount=data['totalCount'],
        )

@dataclass
class AgentVaultSessionActor(BaseModel):
    """The user or machine identity an Agent Vault session belongs to"""
    type: str
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None

@dataclass
class AgentVaultSessionAccessBundle(BaseModel):
    """An access bundle carried by an Agent Vault session"""
    name: str
    position: int
    id: Optional[str] = None

@dataclass
class AgentVaultSession(BaseModel):
    """Infisical Agent Vault Session"""
    id: str
    status: str
    createdAt: str
    label: Optional[str] = None
    actor: Optional[AgentVaultSessionActor] = None
    expiresAt: Optional[str] = None
    revokedAt: Optional[str] = None
    accessBundles: Optional[List[AgentVaultSessionAccessBundle]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultSession':
        """Create model from dictionary with nested actor and access bundles. accessBundles is None if the response leaves it out."""
        session_data = data.copy()
        if data.get('actor') is not None:
            session_data['actor'] = AgentVaultSessionActor.from_dict(data['actor'])
        if data.get('accessBundles') is not None:
            session_data['accessBundles'] = [
                AgentVaultSessionAccessBundle.from_dict(bundle) for bundle in data['accessBundles']
            ]

        return super().from_dict(session_data)

@dataclass
class CreatedAgentVaultSession(BaseModel):
    """Infisical Agent Vault Session as returned at creation. The token is only returned once."""
    id: str
    token: str
    createdAt: str
    label: Optional[str] = None
    expiresAt: Optional[str] = None
    accessBundles: List[AgentVaultSessionAccessBundle] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'CreatedAgentVaultSession':
        """Create model from dictionary with nested access bundles"""
        session_data = data.copy()
        session_data['accessBundles'] = [
            AgentVaultSessionAccessBundle.from_dict(bundle) for bundle in data.get('accessBundles', [])
        ]

        return super().from_dict(session_data)

@dataclass
class SingleAgentVaultSessionResponse(BaseModel):
    """Response model for get/revoke Agent Vault session API"""
    session: AgentVaultSession

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleAgentVaultSessionResponse':
        return cls(
            session=AgentVaultSession.from_dict(data['session']),
        )

@dataclass
class CreateAgentVaultSessionResponse(BaseModel):
    """Response model for create Agent Vault session API"""
    session: CreatedAgentVaultSession

    @classmethod
    def from_dict(cls, data: Dict) -> 'CreateAgentVaultSessionResponse':
        return cls(
            session=CreatedAgentVaultSession.from_dict(data['session']),
        )

@dataclass
class ListAgentVaultSessionsResponse(BaseModel):
    """Response model for list Agent Vault sessions API"""
    sessions: List[AgentVaultSession]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultSessionsResponse':
        return cls(
            sessions=[AgentVaultSession.from_dict(session) for session in data['sessions']],
            totalCount=data['totalCount'],
        )
