"""CloudStore Utilities Module (v2.0)

Common utility functions used across the CloudStore SDK.

No breaking changes in v2.0 — this module is fully backwards compatible.
"""

import hashlib
import json
from typing import Any


def generate_id(prefix: str = "doc") -> str:
    """Generate a unique document ID.

    Args:
        prefix: ID prefix (default: "doc").

    Returns:
        A unique string ID like "doc_a1b2c3".
    """
    import uuid

    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def validate_api_key(api_key: str) -> bool:
    """Validate that an API key has the correct format.

    API keys must:
    - Start with 'cs_'
    - Be at least 20 characters long
    - Contain only alphanumeric characters and underscores

    Args:
        api_key: The API key to validate.

    Returns:
        True if valid, False otherwise.
    """
    if not api_key.startswith("cs_"):
        return False
    if len(api_key) < 20:
        return False
    return all(c.isalnum() or c == "_" for c in api_key)


def hash_document(data: dict) -> str:
    """Compute a SHA-256 hash of a document's data.

    Args:
        data: Document data dictionary.

    Returns:
        Hex string of the SHA-256 hash.
    """
    serialized = json.dumps(data, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


def paginate(items: list, page: int = 1, per_page: int = 50) -> dict:
    """Paginate a list of items.

    Args:
        items: Full list of items.
        page: Page number (1-indexed, default: 1).
        per_page: Items per page (default: 50).

    Returns:
        Dict with keys: items, page, per_page, total, has_more.
    """
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "items": items[start:end],
        "page": page,
        "per_page": per_page,
        "total": len(items),
        "has_more": end < len(items),
    }


def format_bytes(size_bytes: int) -> str:
    """Format a byte count into a human-readable string.

    Args:
        size_bytes: Size in bytes.

    Returns:
        Formatted string like "1.5 MB" or "256 KB".
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"
