from infisical_sdk import InfisicalSDKClient
from infisicalapi_client.models.api_v3_secrets_raw_get200_response_secrets_inner import ApiV3SecretsRawGet200ResponseSecretsInner

sdkInstance = InfisicalSDKClient(host="https://app.infisical.com")

sdkInstance.auth.universalAuth.login("<>", "<>")

# new_secret = sdkInstance.secrets.create_secret_by_name(
#     secret_name="NEW_SECRET",
#     project_id="d7b2b891-2c07-4bc8-bb3f-d29ca4c7187b",
#     secret_path="/",
#     environment_slug="dev",
#     secret_value="secret_value",
#     secret_comment="Optional comment",
#     skip_multiline_encoding=False,
#     secret_reminder_repeat_days=30,  # Optional
#     secret_reminder_note="Remember to update this secret"  # Optional
# )

# updated_secret = sdkInstance.secrets.update_secret_by_name(
#     current_secret_name="NEW_SECRET",
#     project_id="d7b2b891-2c07-4bc8-bb3f-d29ca4c7187b",
#     secret_path="/",
#     environment_slug="dev",
#     secret_value="new_secret_value",
#     secret_comment="Updated comment",  # Optional
#     skip_multiline_encoding=False,
#     secret_reminder_repeat_days=10,  # Optional
#     secret_reminder_note="Updated reminder note",  # Optional
#     new_secret_name="NEW_NAME_2"  # Optional
# )


# secret = sdkInstance.secrets.get_secret_by_name(
#     secret_name="NEW_NAME_2",
#     project_id="d7b2b891-2c07-4bc8-bb3f-d29ca4c7187b",
#     environment_slug="dev",
#     secret_path="/",
#     expand_secret_references=True,
#     include_imports=True,
#     version=None  # Optional
# )

# deleted_secret = sdkInstance.secrets.delete_secret_by_name(
#     secret_name="NEW_NAME_2",
#     project_id="d7b2b891-2c07-4bc8-bb3f-d29ca4c7187b",
#     environment_slug="dev",
#     secret_path="/"
# )
