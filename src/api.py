"""CloudStore API Module (v2.0)

Provides HTTP API client for CloudStore services.

Changes in v2.0:
- RENAMED: delete_resource() -> delete() (simplified name)
- ADDED: patch() method for partial updates
- ADDED: retry and rate limiting support
- CHANGED: upload_file() parameter 'file_path' renamed to 'local_path'
- CHANGED: API version bumped from v1 to v2 in all endpoints
- CHANGED: CloudStoreClient now requires 'region' parameter
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class APIResponse:
    """Standard API response.

    Changed in v2.0: Added request_id field.
    """

    status_code: int
    data: Any
    headers: dict = None
    request_id: str = ""  # NEW in v2.0


class CloudStoreClient:
    """Main API client for CloudStore.

    Changed in v2.0: Now requires 'region' parameter.

    Usage:
        client = CloudStoreClient(
            base_url="https://api.cloudstore.io",
            api_key="cs_xxx",
            region="us-east-1"
        )
        response = client.get("/documents")
    """

    def __init__(
        self, base_url: str, api_key: str, region: str, timeout: int = 30, max_retries: int = 3
    ):
        """Initialize the CloudStore API client.

        Changed in v2.0: Added required 'region' and optional 'max_retries' parameters.

        Args:
            base_url: The API base URL.
            api_key: Your CloudStore API key.
            region: Deployment region (e.g., "us-east-1", "eu-west-1").
            timeout: Request timeout in seconds (default: 30).
            max_retries: Maximum retry attempts on failure (default: 3).
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.region = region
        self.timeout = timeout
        self.max_retries = max_retries

    def get(self, path: str, params: dict = None) -> APIResponse:
        """Send a GET request.

        Args:
            path: API endpoint path.
            params: Optional query parameters.

        Returns:
            APIResponse with status and data.
        """
        return APIResponse(status_code=200, data={}, request_id="req_xxx")

    def post(self, path: str, data: dict = None) -> APIResponse:
        """Send a POST request.

        Args:
            path: API endpoint path.
            data: Request body as dictionary.

        Returns:
            APIResponse with status and data.
        """
        return APIResponse(status_code=201, data={}, request_id="req_xxx")

    def put(self, path: str, data: dict = None) -> APIResponse:
        """Send a PUT request.

        Args:
            path: API endpoint path.
            data: Request body as dictionary.

        Returns:
            APIResponse with status and data.
        """
        return APIResponse(status_code=200, data={}, request_id="req_xxx")

    def patch(self, path: str, data: dict = None) -> APIResponse:
        """Send a PATCH request for partial updates.

        NEW in v2.0.

        Args:
            path: API endpoint path.
            data: Partial update data.

        Returns:
            APIResponse with status and data.
        """
        return APIResponse(status_code=200, data={}, request_id="req_xxx")

    def delete(self, path: str) -> APIResponse:
        """Send a DELETE request.

        Changed in v2.0: Renamed from delete_resource().

        Args:
            path: API endpoint path.

        Returns:
            APIResponse with status and data.
        """
        return APIResponse(status_code=204, data=None, request_id="req_xxx")

    def upload_file(
        self, path: str, local_path: str, content_type: str = "application/octet-stream"
    ) -> APIResponse:
        """Upload a file to CloudStore.

        Changed in v2.0: Parameter 'file_path' renamed to 'local_path'.

        Args:
            path: Upload endpoint path.
            local_path: Local filesystem path to the file.
            content_type: MIME type of the file (default: application/octet-stream).

        Returns:
            APIResponse with upload details.
        """
        return APIResponse(status_code=200, data={"file_id": "file_xxx"}, request_id="req_xxx")


# API Endpoints (v2)
ENDPOINTS = {
    "documents": "/v2/documents",
    "collections": "/v2/collections",
    "users": "/v2/users",
    "files": "/v2/files",
    "webhooks": "/v2/webhooks",  # NEW in v2.0
}
