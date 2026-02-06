# Changelog

## v2.0.0 (2026-01-15)

Major release with breaking changes. See migration guide below.

### Breaking Changes

**Authentication:**
- Removed `basic_auth()` — use `oauth_authenticate()` instead
- `api_key_auth()` now requires a `scope` parameter ("read", "write", or "admin")
- `AuthToken` now includes `refresh_token` and `scope` fields
- `refresh_token()` now requires the token to have a `refresh_token` field

**Database:**
- `connect()` now takes a single `connection_string` instead of `host`, `port`, `database`
- `query()` renamed to `find()` with parameters: `filter` -> `where`, `limit` -> `max_results`
- `update()` renamed to `update_one()`, added `upsert` parameter
- `delete()` renamed to `delete_one()`
- `insert()` now returns a document ID string instead of a Document object

**API Client:**
- `CloudStoreClient.__init__()` now requires a `region` parameter
- `delete_resource()` renamed to `delete()`
- `upload_file()` parameter `file_path` renamed to `local_path`
- All endpoints updated from `/v1/` to `/v2/`

### New Features
- OAuth 2.0 authentication via `oauth_authenticate()`
- Service account authentication via `service_account_auth()`
- `patch()` method for partial updates
- `bulk_insert()` for batch document creation
- `create_index()` for query optimization
- Cursor-based pagination in query results
- Automatic retry with `max_retries` parameter
- Webhook endpoints (`/v2/webhooks`)

## v1.0.0 (2025-06-15)

Initial release of CloudStore SDK.

### Features
- Basic authentication with username/password
- API key authentication with `cs_` prefix
- Token refresh support
- Database operations: connect, insert, query, update, delete
- HTTP API client with GET, POST, PUT, DELETE methods
- File upload support
- Utility functions: ID generation, API key validation, document hashing, pagination
