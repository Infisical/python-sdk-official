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
    """Enum for which hosts an agent may reach through an Agent Vault proxy.

    BUNDLE_HOSTS is the old name of SERVICE_HOSTS and the same member, so a proxy's traffic policy compares equal to
    either one, and AgentVaultTrafficPolicy("bundle-hosts") is SERVICE_HOSTS.
    """
    ANY_HOST = "any-host"
    SERVICE_HOSTS = "service-hosts"
    BUNDLE_HOSTS = "service-hosts"

    @classmethod
    def _missing_(cls, value):
        if value == "bundle-hosts":
            return cls.SERVICE_HOSTS
        return None

class AgentVaultSessionStatus(str, Enum):
    """Enum for Agent Vault session status"""
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"

class AgentVaultSessionScope(str, Enum):
    """Enum for whose Agent Vault sessions to list"""
    MINE = "mine"
    ALL = "all"

class AgentVaultMemberType(str, Enum):
    """Enum for the kinds of Agent Vault member: users, machine identities and groups"""
    USER = "user"
    MACHINE_IDENTITY = "machineIdentity"
    GROUP = "group"

class AgentVaultDelegationScope(str, Enum):
    """Enum for which users a machine identity can create Agent Vault sessions on behalf of"""
    ALL_MEMBERS = "all-members"
    SELECTED = "selected"

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
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultProxy':
        """Create model from dictionary. An Infisical version from before service-hosts was named reports bundle-hosts, which reads as service-hosts."""
        proxy_data = data.copy()
        if proxy_data.get('trafficPolicy') == 'bundle-hosts':
            proxy_data['trafficPolicy'] = AgentVaultTrafficPolicy.SERVICE_HOSTS.value

        return super().from_dict(proxy_data)

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
    """The user or machine identity an Agent Vault session belongs to, or the user it was started on behalf of"""
    type: str
    id: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None

@dataclass
class AgentVaultSessionAccessBundle(BaseModel):
    """The access bundle an Agent Vault session carries. id is None once the bundle is deleted."""
    name: str
    id: Optional[str] = None

@dataclass
class AgentVaultInlineService(BaseModel):
    """A service sent with an Agent Vault session, without its token, password or values. type is http, mcp, postgres, mysql or ssh, and the API returns only that type's fields: hostPattern, allowedMethods, allowedPathPrefixes, customHeaders and substitutions for http; serverUrl, transport, hostPattern and customHeaders for mcp; host, port, database and tls for postgres and mysql; host and port for ssh. Its nested settings, such as credential and tls, are left as the API returns them."""
    id: str
    name: str
    type: str
    hostPattern: Optional[str] = None
    serverUrl: Optional[str] = None
    transport: Optional[str] = None
    allowedMethods: Optional[List[str]] = None
    allowedPathPrefixes: Optional[List[str]] = None
    credential: Optional[Dict[str, Any]] = None
    customHeaders: Optional[List[Dict[str, Any]]] = None
    substitutions: Optional[List[Dict[str, Any]]] = None
    description: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    tls: Optional[Dict[str, Any]] = None

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
    accessBundle: Optional[AgentVaultSessionAccessBundle] = None
    onBehalfOf: Optional[AgentVaultSessionActor] = None
    services: Optional[List[AgentVaultInlineService]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultSession':
        """Create model from dictionary with nested actor, on-behalf-of user, access bundle and inline services. accessBundle and services are None if the response leaves them out."""
        session_data = data.copy()
        if data.get('actor') is not None:
            session_data['actor'] = AgentVaultSessionActor.from_dict(data['actor'])
        if data.get('onBehalfOf') is not None:
            session_data['onBehalfOf'] = AgentVaultSessionActor.from_dict(data['onBehalfOf'])
        if data.get('accessBundle') is not None:
            session_data['accessBundle'] = AgentVaultSessionAccessBundle.from_dict(data['accessBundle'])
        if data.get('services') is not None:
            session_data['services'] = [AgentVaultInlineService.from_dict(service) for service in data['services']]

        return super().from_dict(session_data)

@dataclass
class CreatedAgentVaultSession(BaseModel):
    """Infisical Agent Vault Session as returned at creation. The token is only returned once."""
    id: str
    token: str
    createdAt: str
    projectId: Optional[str] = None
    label: Optional[str] = None
    expiresAt: Optional[str] = None
    accessBundle: Optional[AgentVaultSessionAccessBundle] = None
    services: List[AgentVaultInlineService] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict) -> 'CreatedAgentVaultSession':
        """Create model from dictionary with nested access bundle and inline services"""
        session_data = data.copy()
        if data.get('accessBundle') is not None:
            session_data['accessBundle'] = AgentVaultSessionAccessBundle.from_dict(data['accessBundle'])
        session_data['services'] = [
            AgentVaultInlineService.from_dict(service) for service in data.get('services', [])
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

@dataclass
class AgentVaultServiceRef(BaseModel):
    """An Agent Vault service, by ID and name"""
    id: str
    name: str

@dataclass
class AgentVaultAccessBundleRef(BaseModel):
    """An Agent Vault access bundle, by ID and name"""
    id: str
    name: str

@dataclass
class AgentVaultService(BaseModel):
    """A service in an Agent Vault access bundle. type is http, mcp, postgres, mysql or ssh, and the API returns only that type's fields: hostPattern, allowedMethods, allowedPathPrefixes, customHeaders and substitutions for http; serverUrl, transport, hostPattern, allowedTools and customHeaders for mcp; host, port, database and tls for postgres and mysql; host and port for ssh. Its nested settings, such as credential and tls ({"enabled", "verify", "ca"}), are left as the API returns them."""
    id: str
    accessBundleId: str
    name: str
    type: str
    hostPattern: Optional[str] = None
    serverUrl: Optional[str] = None
    transport: Optional[str] = None
    allowedMethods: Optional[List[str]] = None
    allowedPathPrefixes: Optional[List[str]] = None
    credential: Optional[Dict[str, Any]] = None
    customHeaders: Optional[List[Dict[str, Any]]] = None
    substitutions: Optional[List[Dict[str, Any]]] = None
    variableReferences: Optional[List[Dict[str, Any]]] = None
    personalValues: Optional[Dict[str, Any]] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    allowedTools: Optional[List[str]] = None
    description: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    tls: Optional[Dict[str, Any]] = None

@dataclass
class AgentVaultAccessBundle(BaseModel):
    """Infisical Agent Vault Access Bundle. Only list sets the counts, hostPatterns and servicesRequiringSetup."""
    id: str
    name: str
    description: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    serviceCount: Optional[int] = None
    memberCount: Optional[int] = None
    hostPatterns: Optional[List[str]] = None
    servicesRequiringSetup: Optional[List[AgentVaultServiceRef]] = None
    services: Optional[List[AgentVaultService]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultAccessBundle':
        """Create model from dictionary with nested services"""
        bundle_data = data.copy()
        if data.get('servicesRequiringSetup') is not None:
            bundle_data['servicesRequiringSetup'] = [
                AgentVaultServiceRef.from_dict(service) for service in data['servicesRequiringSetup']
            ]
        if data.get('services') is not None:
            bundle_data['services'] = [AgentVaultService.from_dict(service) for service in data['services']]

        return super().from_dict(bundle_data)

@dataclass
class SingleAgentVaultAccessBundleResponse(BaseModel):
    """Response model for get/create/update/delete Agent Vault access bundle API"""
    accessBundle: AgentVaultAccessBundle

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleAgentVaultAccessBundleResponse':
        return cls(
            accessBundle=AgentVaultAccessBundle.from_dict(data['accessBundle']),
        )

@dataclass
class ListAgentVaultAccessBundlesResponse(BaseModel):
    """Response model for list Agent Vault access bundles API"""
    accessBundles: List[AgentVaultAccessBundle]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultAccessBundlesResponse':
        return cls(
            accessBundles=[AgentVaultAccessBundle.from_dict(bundle) for bundle in data['accessBundles']],
            totalCount=data['totalCount'],
        )

@dataclass
class AgentVaultGrantee(BaseModel):
    """A user, machine identity or group that an Agent Vault access bundle is granted to"""
    type: str
    id: str
    grantedAt: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None
    isOrgMembershipPending: Optional[bool] = None

@dataclass
class ListAgentVaultGranteesResponse(BaseModel):
    """Response model for list Agent Vault access bundle grantees API"""
    members: List[AgentVaultGrantee]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultGranteesResponse':
        return cls(
            members=[AgentVaultGrantee.from_dict(member) for member in data['members']],
            totalCount=data['totalCount'],
        )

@dataclass
class AgentVaultGrantChangeResponse(BaseModel):
    """Response model for grant/revoke Agent Vault access bundle API. Its grantees have only type, id and grantedAt."""
    members: List[AgentVaultGrantee]
    skipped: List[AgentVaultGrantee]

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultGrantChangeResponse':
        return cls(
            members=[AgentVaultGrantee.from_dict(member) for member in data['members']],
            skipped=[AgentVaultGrantee.from_dict(member) for member in data['skipped']],
        )

@dataclass
class AgentVaultMember(BaseModel):
    """A user, machine identity or group that's a member of Agent Vault, with its Agent Vault role"""
    type: str
    id: str
    role: Optional[str] = None
    isActive: Optional[bool] = None
    addedAt: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    isOrgMembershipPending: Optional[bool] = None
    name: Optional[str] = None
    isManagedByAgentVault: Optional[bool] = None
    orgId: Optional[str] = None

@dataclass
class ListAgentVaultMembersResponse(BaseModel):
    """Response model for list available Agent Vault grantees and delegation subjects API"""
    members: List[AgentVaultMember]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultMembersResponse':
        return cls(
            members=[AgentVaultMember.from_dict(member) for member in data['members']],
            totalCount=data['totalCount'],
        )

def _missing_access_bundles(data: Dict) -> Optional[List[AgentVaultAccessBundleRef]]:
    """Parses missingAccessBundles, which only some delegation responses include, so it's None when left out."""
    bundles = data.get('missingAccessBundles')
    return None if bundles is None else [AgentVaultAccessBundleRef.from_dict(bundle) for bundle in bundles]

@dataclass
class AgentVaultDelegationMachineIdentity(BaseModel):
    """The machine identity an Agent Vault delegation belongs to"""
    id: str
    name: str

@dataclass
class AgentVaultDelegationUser(BaseModel):
    """A user in an Agent Vault delegation. missingAccessBundles is only set by get, set, add_subjects and remove_subjects."""
    id: str
    username: str
    addedAt: str
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    missingAccessBundles: Optional[List[AgentVaultAccessBundleRef]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultDelegationUser':
        """Create model from dictionary with nested missing access bundles"""
        user_data = data.copy()
        user_data['missingAccessBundles'] = _missing_access_bundles(data)

        return super().from_dict(user_data)

@dataclass
class AgentVaultDelegationGroup(BaseModel):
    """A group in an Agent Vault delegation. missingAccessBundles is only set by get, set, add_subjects and remove_subjects."""
    id: str
    name: str
    addedAt: str
    missingAccessBundles: Optional[List[AgentVaultAccessBundleRef]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultDelegationGroup':
        """Create model from dictionary with nested missing access bundles"""
        group_data = data.copy()
        group_data['missingAccessBundles'] = _missing_access_bundles(data)

        return super().from_dict(group_data)

@dataclass
class AgentVaultDelegation(BaseModel):
    """Infisical Agent Vault Delegation: which users a machine identity can create sessions on behalf of"""
    machineIdentity: AgentVaultDelegationMachineIdentity
    scope: str
    users: List[AgentVaultDelegationUser]
    groups: List[AgentVaultDelegationGroup]
    createdAt: str
    updatedAt: str
    missingAccessBundles: Optional[List[AgentVaultAccessBundleRef]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'AgentVaultDelegation':
        """Create model from dictionary with nested machine identity, users, groups and missing access bundles"""
        delegation_data = data.copy()
        delegation_data['machineIdentity'] = AgentVaultDelegationMachineIdentity.from_dict(data['machineIdentity'])
        delegation_data['users'] = [AgentVaultDelegationUser.from_dict(user) for user in data['users']]
        delegation_data['groups'] = [AgentVaultDelegationGroup.from_dict(group) for group in data['groups']]
        delegation_data['missingAccessBundles'] = _missing_access_bundles(data)

        return super().from_dict(delegation_data)

@dataclass
class SingleAgentVaultDelegationResponse(BaseModel):
    """Response model for Agent Vault delegation API. delegation is None when remove_subjects ends the delegation."""
    delegation: Optional[AgentVaultDelegation] = None

    @classmethod
    def from_dict(cls, data: Dict) -> 'SingleAgentVaultDelegationResponse':
        return cls(
            delegation=AgentVaultDelegation.from_dict(data['delegation']) if data.get('delegation') is not None else None,
        )

@dataclass
class ListAgentVaultDelegationsResponse(BaseModel):
    """Response model for list Agent Vault delegations API"""
    delegations: List[AgentVaultDelegation]
    totalCount: int

    @classmethod
    def from_dict(cls, data: Dict) -> 'ListAgentVaultDelegationsResponse':
        return cls(
            delegations=[AgentVaultDelegation.from_dict(delegation) for delegation in data['delegations']],
            totalCount=data['totalCount'],
        )
