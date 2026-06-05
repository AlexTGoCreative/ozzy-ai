<!-- source: https://www.opswat.com/docs/mdcore/metadefender-core -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:53:58.415340 -->

## Developer Guide

This is the API documentation for *MetaDefender Core Public API*. If you
would like to evaluate or have any questions about this documentation,
please contact us via our Contact Us form.

## How to Interact with MetaDefender Core using REST

Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below.

MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender Core as part of the upload process.Note:

## File Analysis Process

MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary. Below is a brief description of the API integration flow:

Upload a file for analysis (

`POST /file`

), which returns the`data_id`

or`batch_id`

: File Analysis).The performance depends on:**Note**:- number of engines
- type of file to be scanned
- MetaDefender Core's hardware

**Batch Upload with multipart/form-data**:- When the request uses
`Content-Type: multipart/form-data`

, MetaDefender Core treats the entire submission as a batch. - A new batch is automatically created for this media type.
- Each part in the request body is processed as an individual file within the batch.
- The API returns a
`batch_id`

instead of a`data_id`

. - All individual file scans are linked to the created batch.

You have 2 ways to retrieve the analysis report:

**Polling**: Fetch the result with previously received data_id or batch_id (`GET /file/{data_id}`

or`GET /file/{batch_id}`

resource) until scan result belonging to data_id/batch_id doesn't reach the 100 percent progress_percentage: (Fetch analysis result)

Too many data_id/batch_id requests can reduce performance. It is enough to just check every few hundred milliseconds.**Note**:**Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.

Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256, sha512) by calling Fetch analysis result by hash.

- The hash can be found in the scan results

Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.

Based on the configured retention policy, the files might be available for retrieval at a later time.**Note**:

OPSWAT provides some sample codes on GitHub to make it easier to understand how the MetaDefender REST API works.

## Auth

### Authentication APIs

User authentication is done via username & password. Additional integrations are available within the product:

**LDAP**integration**Active Directory**integration**SAML**integration (starting with v4.18.0)

### Login

Initiate a new session. Required for using protected REST APIs.

OK

Invalid credentials

Unexpected event on server

### Logout

Destroy session for not using protected REST APIs.

OK

Bad Request.

Invalid user information.

Unexpected event on server

## User Management

### User management APIs

The APIs for manage users and user directories.

## Analysis

### File analysis APIs

Submit each file to MetaDefender Core individually or group them in batches. Each file submission will return a `data_id`

which will be the unique identifier used to retrieve the analysis results.
When `Content-Type: multipart/form-data`

is used, the entire request is treated as a batch. A `batch_id`

is created automatically, and each part in the multipart body is processed as an individual file within that batch.
**Important**: Even though one file is being submitted, if MetaDefender Core is configured to extract the files, all compound file types (archives, Office documents, etc.) will be extracted and each file within will be analyzed as a separate entry.

- This means that if you submit an archive with 100 files in it, MetaDefender Core will process 101 files: original file as it is and each of the 100 child files
- Note that by opening the files, detection ratio can increase even by 30%.

MetaDefender API doesn't support chunk upload. You shouldn't load the file in memory, is recommended to stream the files to MetaDefender Core as part of the upload process.Note:

## Batch

Group the analysis requests in batches.

## Multipart

Upload a file for scan by multiple parts.

## Splitarchive

Processes a split archive uploaded in multiple parts. Only the extracted files from the reassembled split archive are processed; the combined archive file itself is not supported. Therefore, Quarantine and PostAction do not apply.

## Admin

Admin specific API requests.

## License

Activate the product or get licensing information. Will require admin apikey.

## Config

Configure the product through APIs (especially the Settings). Will require admin apikey.

## Yara

YARA engine configuration and source management APIs.

## Engines

Enable/disable or pin/unpin the engines through API.

## Stats

Health check and statistics about MetaDefender Core usage.