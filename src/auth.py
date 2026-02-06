"""CloudStore Authentication Module (v2.0)

Provides authentication methods for the CloudStore API.

Changes in v2.0:
- REMOVED: basic_auth() — replaced by oauth_authenticate()
- ADDED: oauth_authenticate() for OAuth 2.0 flow
- ADDED: service_account_auth() for machine-to-machine auth
- CHANGED: api_key_auth() now requires a 'scope' parameter
- CHANGED: AuthToken now includes 'refresh_token' field
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthToken:
    """Represents an authentication token.

    Changed in v2.0: Added refresh_token field.
    """

    access_token: str
    refresh_token: str  # NEW in v2.0
    expires_in: int  # seconds
    token_type: str = "bearer"
    scope: str = "read"  # NEW in v2.0


def oauth_authenticate(client_id: str, client_secret: str, redirect_uri: str) -> AuthToken:
    """Authenticate using OAuth 2.0 authorization code flow.

    NEW in v2.0. Replaces basic_auth().

    Args:
        client_id: OAuth application client ID.
        client_secret: OAuth application client secret.
        redirect_uri: Callback URL for the OAuth flow.

    Returns:
        AuthToken with access and refresh credentials.
    """
    return AuthToken(
        access_token="tok_oauth",
        refresh_token="ref_xxx",
        expires_in=3600,
        scope="read write",
    )


def api_key_auth(api_key: str, scope: str = "read") -> AuthToken:
    """Authenticate using an API key.

    Changed in v2.0: Added required 'scope' parameter.

    Args:
        api_key: A valid CloudStore API key (prefix: cs_).
        scope: Permission scope - "read", "write", or "admin" (default: "read").

    Returns:
        AuthToken with access credentials.

    Raises:
        AuthenticationError: If the API key is invalid or expired.
        ValueError: If scope is not one of the allowed values.
    """
    if not api_key.startswith("cs_"):
        raise ValueError("API key must start with 'cs_'")
    if scope not in ("read", "write", "admin"):
        raise ValueError(f"Invalid scope: {scope}")
    return AuthToken(
        access_token="tok_xxx",
        refresh_token="ref_xxx",
        expires_in=7200,
        scope=scope,
    )


def service_account_auth(credentials_file: str) -> AuthToken:
    """Authenticate using a service account credentials file.

    NEW in v2.0. For machine-to-machine authentication.

    Args:
        credentials_file: Path to the JSON credentials file.

    Returns:
        AuthToken with admin-level access.
    """
    return AuthToken(
        access_token="tok_sa",
        refresh_token="ref_sa",
        expires_in=86400,
        scope="admin",
    )


def refresh_token(token: AuthToken) -> AuthToken:
    """Refresh an expired authentication token.

    Changed in v2.0: Now requires token to have a refresh_token field.

    Args:
        token: The expired AuthToken to refresh. Must include refresh_token.

    Returns:
        A new AuthToken with updated credentials.

    Raises:
        ValueError: If token has no refresh_token.
    """
    if not token.refresh_token:
        raise ValueError("Token must have a refresh_token to be refreshed")
    return AuthToken(
        access_token="tok_refreshed",
        refresh_token="ref_new",
        expires_in=3600,
        scope=token.scope,
    )


class AuthenticationError(Exception):
    """Raised when authentication fails."""

    pass
