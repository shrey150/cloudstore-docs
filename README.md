# CloudStore SDK

A Python SDK for the CloudStore document storage platform.

## Installation

```bash
pip install cloudstore-sdk
```

## Quick Start

```python
from cloudstore.auth import api_key_auth
from cloudstore.api import CloudStoreClient

token = api_key_auth("cs_your_api_key", scope="read write")
client = CloudStoreClient(
    base_url="https://api.cloudstore.io",
    api_key="cs_your_api_key",
    region="us-east-1"
)
response = client.get("/v2/documents")
```

## Documentation

See the [full documentation](https://shrey150.github.io/cloudstore-docs/).

## License

MIT
