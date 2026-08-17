from infisical_sdk import InfisicalSDKClient, SymmetricEncryption

import random
import base64
import os
import string

def loadEnvVarsFromFileIntoEnv():
  d = dict()
  with open("./.env", "r") as fp:
      for line in fp:
          line = line.strip()
          if line and not line.startswith("#"):
            line = line.split("=", 1)
            d[line[0]] = line[1]

  for key, value in d.items():
    os.environ[key] = value

loadEnvVarsFromFileIntoEnv()

sdkInstance = InfisicalSDKClient(host=os.getenv("SITE_URL"))


SECRETS_PROJECT_ID = os.getenv("SECRETS_PROJECT_ID")
KMS_PROJECT_ID = os.getenv("KMS_PROJECT_ID")
SECRETS_ENVIRONMENT_SLUG = os.getenv("SECRETS_ENVIRONMENT_SLUG")

MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_ID = os.getenv("MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_ID")
MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_SECRET = os.getenv("MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_SECRET")
SITE_URL = os.getenv("SITE_URL")


sdkInstance.auth.universal_auth.login(MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_ID, MACHINE_IDENTITY_UNIVERSAL_AUTH_CLIENT_SECRET)


def random_string(length: int = 10) -> str:
    # Use only lowercase letters, numbers, and hyphens
    allowed_chars = string.ascii_lowercase + string.digits + '-'
    return ''.join(random.choices(allowed_chars, k=length))




################################################# SECRET TESTS #################################################

new_secret = sdkInstance.secrets.create_secret_by_name(
    secret_name=f"TEST_{random_string()}",
    project_id=SECRETS_PROJECT_ID,
    secret_path="/",
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    secret_value=f"secret_value_{random_string()}",
    secret_comment=f"Optional comment_{random_string()}",
    skip_multiline_encoding=False,
    secret_reminder_repeat_days=30,  # Optional
    secret_reminder_note=f"Remember to update this secret_{random_string()}"  # Optional
)

print(f"Created secret: [key={new_secret.secretKey}] | [value={new_secret.secretValue}]")

updated_secret = sdkInstance.secrets.update_secret_by_name(
    current_secret_name=new_secret.secretKey,
    project_id=SECRETS_PROJECT_ID,
    secret_path="/",
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    secret_value=f"new_secret_value_{random_string()}",
    secret_comment=f"Updated comment_{random_string()}",  # Optional
    skip_multiline_encoding=False,
    secret_reminder_repeat_days=10,  # Optional
    secret_reminder_note=f"Updated reminder note_{random_string()}",  # Optional
    new_secret_name=f"NEW_NAME_{random_string()}"  # Optional
)

print(f"Updated secret: [key={updated_secret.secretKey}] | [value={updated_secret.secretValue}]")
secret = sdkInstance.secrets.get_secret_by_name(
    secret_name=updated_secret.secretKey,
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    secret_path="/",
    expand_secret_references=True,
    include_imports=True,
    version=None  # Optional
)

print(f"Retrieved secret: [key={secret.secretKey}] | [value={secret.secretValue}]")


all_secrets = sdkInstance.secrets.list_secrets(
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    secret_path="/",
    expand_secret_references=True,
    include_imports=True
)


all_secrets.secrets = [secret for secret in all_secrets.secrets if secret.secretKey != "TEST"]
if len(all_secrets.secrets) != 1:
    raise Exception("Expected 1 secret, got {}".format(len(all_secrets.secrets)))


# Print all secret keys
for idx, secret in enumerate(all_secrets.secrets):
    print(f"Listed secrets key {idx}: [{secret.secretKey}] | [value={secret.secretValue}]")

deleted_secret = sdkInstance.secrets.delete_secret_by_name(
    secret_name=updated_secret.secretKey,
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    secret_path="/"
)

print(f"Deleted secret: [key={deleted_secret.secretKey}] | [value={deleted_secret.secretValue}]")

################################################# FOLDER TESTS #################################################

new_folder = sdkInstance.folders.create_folder(
    name=f"test-folder-{random_string()}",
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    path="/",
    description=f"Optional description_{random_string()}"  # Optional
)

print(f"Created folder: [id={new_folder.id}] | [name={new_folder.name}]")

new_folder_name = f"renamed-folder-{random_string()}"

updated_folder = sdkInstance.folders.update_folder(
    folder_id=new_folder.id,
    name=new_folder_name,
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    path="/",
    description=f"Updated description_{random_string()}"  # Optional
)

if updated_folder.name != new_folder_name:
    raise Exception("Expected folder name {}, got {}".format(new_folder_name, updated_folder.name))

print(f"Updated folder: [id={updated_folder.id}] | [name={updated_folder.name}]")

folder = sdkInstance.folders.get_folder_by_id(
    id=updated_folder.id
)

print(f"Retrieved folder: [id={folder.id}] | [name={folder.name}] | [path={folder.path}]")

all_folders = sdkInstance.folders.list_folders(
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    path="/"
)

for idx, listed_folder in enumerate(all_folders.folders):
    print(f"Listed folders name {idx}: [{listed_folder.name}] | [id={listed_folder.id}]")

deleted_folder = sdkInstance.folders.delete_folder(
    folder_id_or_name=updated_folder.id,
    project_id=SECRETS_PROJECT_ID,
    environment_slug=SECRETS_ENVIRONMENT_SLUG,
    path="/",
    force_delete=True
)

print(f"Deleted folder: [id={deleted_folder.id}] | [name={deleted_folder.name}]")

################################################# KMS TESTS #################################################

kms_key = sdkInstance.kms.create_key(
    name=f"test-key-{random_string()}",
    project_id=KMS_PROJECT_ID,
    encryption_algorithm=SymmetricEncryption.AES_GCM_256,
    description=f"Optional description_{random_string()}"
)

print(f"Created KMS key: [key={kms_key.id}] | [name={kms_key.name}]")


plantext = "Hello, world!"

encrypted = sdkInstance.kms.encrypt_data(
    key_id=kms_key.id,
    base64EncodedPlaintext=base64.b64encode(plantext.encode()).decode()
)

print(f"Encrypted: {encrypted}")

decrypted = sdkInstance.kms.decrypt_data(
    key_id=kms_key.id,
    ciphertext=encrypted
)

print(f"Decrypted: {base64.b64decode(decrypted.encode()).decode()}")

key_by_id = sdkInstance.kms.get_key_by_id(
    key_id=kms_key.id
)

print(f"Key by ID: {key_by_id}")

key_by_name = sdkInstance.kms.get_key_by_name(
    key_name=kms_key.name,
    project_id=KMS_PROJECT_ID
)

print(f"Key by Name: {key_by_name}")

list_keys = sdkInstance.kms.list_keys(
    project_id=KMS_PROJECT_ID
)

print(f"List keys: {list_keys}")


deleted_key = sdkInstance.kms.delete_key(
    key_id=kms_key.id
)

print(f"Deleted key: {deleted_key}")