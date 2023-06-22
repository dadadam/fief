from enum import StrEnum


class APIErrorCode(StrEnum):
    CANT_DETERMINE_VALID_WORKSPACE = "CANT_DETERMINE_VALID_WORKSPACE"

    WORKSPACE_CREATE_MISSING_DATABASE_SETTINGS = (
        "WORKSPACE_CREATE_MISSING_DATABASE_SETTINGS"
    )
    WORKSPACE_CREATE_INVALID_SSL_MODE = "WORKSPACE_CREATE_INVALID_SSL_MODE"
    WORKSPACE_DB_CONNECTION_ERROR = "WORKSPACE_DB_CONNECTION_ERROR"
    WORKSPACE_DB_OUTDATED_MIGRATION = "WORKSPACE_DB_OUTDATED_MIGRATION"

    ACR_TOO_LOW = "ACR_TOO_LOW"

    CLIENT_CREATE_UNKNOWN_TENANT = "CLIENT_CREATE_UNKNOWN_TENANT"
    CLIENT_HTTPS_REQUIRED_ON_REDIRECT_URIS = "CLIENT_HTTPS_REQUIRED_ON_REDIRECT_URIS"

    OAUTH_PROVIDER_MISSING_OPENID_CONFIGURATION_ENDPOINT = (
        "OAUTH_PROVIDER_MISSING_OPENID_CONFIGURATION_ENDPOINT"
    )
    OAUTH_PROVIDER_REFRESH_TOKEN_NOT_SUPPORTED = (
        "OAUTH_PROVIDER_REFRESH_TOKEN_NOT_SUPPORTED"
    )
    OAUTH_PROVIDER_REFRESH_TOKEN_ERROR = "OAUTH_PROVIDER_REFRESH_TOKEN_ERROR"

    USER_FIELD_SLUG_ALREADY_EXISTS = "USER_FIELD_SLUG_ALREADY_EXISTS"

    USER_CREATE_UNKNOWN_TENANT = "USER_CREATE_UNKNOWN_TENANT"
    USER_CREATE_ALREADY_EXISTS = "USER_CREATE_ALREADY_EXISTS"
    USER_CREATE_INVALID_PASSWORD = "USER_CREATE_INVALID_PASSWORD"

    USER_UPDATE_INVALID_PASSWORD = "USER_UPDATE_INVALID_PASSWORD"
    USER_UPDATE_EMAIL_ALREADY_EXISTS = "USER_UPDATE_EMAIL_ALREADY_EXISTS"
    USER_UPDATE_INVALID_EMAIL_VERIFICATION_CODE = (
        "USER_UPDATE_INVALID_EMAIL_VERIFICATION_CODE"
    )

    USER_CREATE_ACCESS_TOKEN_UNKNOWN_CLIENT = "USER_CREATE_ACCESS_TOKEN_UNKNOWN_CLIENT"

    PERMISSION_CREATE_CODENAME_ALREADY_EXISTS = (
        "PERMISSION_CREATE_CODENAME_ALREADY_EXISTS"
    )
    PERMISSION_UPDATE_CODENAME_ALREADY_EXISTS = (
        "PERMISSION_UPDATE_CODENAME_ALREADY_EXISTS"
    )

    ROLE_CREATE_NOT_EXISTING_PERMISSION = "ROLE_CREATE_NOT_EXISTING_PERMISSION"
    ROLE_UPDATE_NOT_EXISTING_PERMISSION = "ROLE_UPDATE_NOT_EXISTING_PERMISSION"

    TENANT_CREATE_NOT_EXISTING_THEME = "TENANT_CREATE_NOT_EXISTING_THEME"
    TENANT_CREATE_NOT_EXISTING_OAUTH_PROVIDER = (
        "TENANT_CREATE_NOT_EXISTING_OAUTH_PROVIDER"
    )
    TENANT_UPDATE_NOT_EXISTING_THEME = "TENANT_UPDATE_NOT_EXISTING_THEME"
    TENANT_UPDATE_NOT_EXISTING_OAUTH_PROVIDER = (
        "TENANT_UPDATE_NOT_EXISTING_OAUTH_PROVIDER"
    )

    USER_PERMISSION_CREATE_NOT_EXISTING_PERMISSION = (
        "USER_PERMISSION_CREATE_NOT_EXISTING_PERMISSION"
    )
    USER_PERMISSION_CREATE_ALREADY_ADDED_PERMISSION = (
        "USER_PERMISSION_CREATE_ALREADY_ADDED_PERMISSION"
    )

    USER_ROLE_CREATE_NOT_EXISTING_ROLE = "USER_ROLE_CREATE_NOT_EXISTING_ROLE"
    USER_ROLE_CREATE_ALREADY_ADDED_ROLE = "USER_ROLE_CREATE_ALREADY_ADDED_ROLE"

    EMAIL_TEMPLATE_INVALID_TEMPLATE = "EMAIL_TEMPLATE_INVALID_TEMPLATE"
