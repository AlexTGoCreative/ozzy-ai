<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/using-the-metadata-header-to-track-api-file-submissions-in-metad -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:31:00.318478 -->

# Using the metadata Header to Track API File Submissions in MetaDefender Core

This article applies to all MetaDefender Core releases deployed on Windows and Linux systems.

## Overview

MetaDefender Core supports a `metadata`

HTTP header on the `POST /file`

API endpoint. This header can be used to attach custom, client-defined metadata to a file submission.

This is useful when you need to identify which internal record, transaction, user session, case, ticket, or unique file submission a scan belongs to.

The `metadata`

header accepts a JSON object. The field names are defined by the client, so there is no fixed list of required metadata keys.

## Use case

In some environments, the file name alone is not enough to reliably identify where a scan result came from.

For example:

- A single source system may submit many files.
- Multiple files may have the same name.
- The same file may be submitted more than once.
- The same file hash may appear in multiple submissions.
- A sanitized file must be correlated back to the original scan request.
- A scan result must be mapped back to an external ticket, case, transaction, or database record.

To avoid ambiguity, clients can submit a unique identifier, such as a UID, in the `metadata`

header and store the returned MetaDefender Core `data_id`

for later lookups.

## How it works

When a file is submitted through `POST /file`

, the client can include a `metadata`

header containing a JSON object.

Example metadata payload:

`{`

` "uid": "abc123",`

` "source_system": "system-A",`

` "client_ref": "ref-001"`

`}`

The `metadata`

header can be used for:

- Additional parameters for predefined post actions and external scanners, as part of STDIN input.
- Customized macro variables for watermarking text, used by the Proactive DLP engine feature.
- Additional context or verbose information for each file submission, appended into the JSON scan result.

It is strongly recommended to URL encode the `metadata`

header before sending it to MetaDefender Core to help prevent unexpected issues related to encoding errors or unsafe characters.

### Note for post-action and external scanner integrations

When metadata is passed to post-action scripts or external scanners through STDIN, characters that could be used for command injection, such as spaces, parentheses, angle brackets, ampersands, pipes, and similar characters, may be HTML-entity-escaped before being passed to the script or scanner.

If your post-action script or external scanner reads metadata from STDIN, make sure it accounts for this escaping behavior.

## Example file submission

`curl --request POST \`

` --url 'http://<core-host>:8008/file' \`

` --header 'Content-Type: application/octet-stream' \`

` --header 'apikey: <your_apikey>' \`

` --header 'filename: test.txt' \`

` --header 'metadata: {"uid":"abc123","source_system":"system-A","client_ref":"ref-001"}' \`

` --data-binary '@/path/to/test.txt'`

Example response:

`{`

` "data_id": "2381c1b26a2e4de1bdb4d64883f5b91a",`

` "status": "In Progress"`

`}`

The returned `data_id`

should be stored by the client application. It is the primary MetaDefender Core identifier used to retrieve the scan result and, if applicable, the sanitized file.

## Recommended correlation flow

- Generate a unique identifier on the client side, such as a UID.
- Submit the file to MetaDefender Core using
`POST /file`

. - Include the UID in the
`metadata`

header. - Capture the
`data_id`

returned by MetaDefender Core. - Store the mapping between the client UID and the MetaDefender Core
`data_id`

. - Retrieve the scan result using
`GET /file/{data_id}`

. - Retrieve the sanitized file, if available, using
`GET /file/converted/{data_id}`

.

Example client-side mapping:

`{`

` "uid": "abc123",`

` "data_id": "2381c1b26a2e4de1bdb4d64883f5b91a",`

` "source_system": "system-A",`

` "submitted_file_name": "test.txt"`

`}`

## Verify metadata in the scan result

After submitting the file, retrieve the result by `data_id`

:

`curl --request GET \`

` --url 'http://<core-host>:8008/file/<data_id>' \`

` --header 'apikey: <your_apikey>'`

The scan result should include the submitted metadata in the JSON response.

Example:

`{`

` "data_id": "2381c1b26a2e4de1bdb4d64883f5b91a",`

` "metadata": {`

` "uid": "abc123",`

` "source_system": "system-A",`

` "client_ref": "ref-001"`

` },`

` "process_info": {`

` "...": "..."`

` },`

` "scan_results": {`

` "...": "..."`

` }`

`}`

## Retrieve the sanitized file

If the selected workflow performs sanitization and a sanitized output is available, retrieve it using the same `data_id`

:

`curl --request GET \`

` --url 'http://<core-host>:8008/file/converted/<data_id>' \`

` --header 'apikey: <your_apikey>' \`

` --output sanitized_file`

This means the same `data_id`

can be used to correlate:

- The original file submission
- The scan result
- The submitted metadata
- The sanitized output, if one was produced

## PowerShell test example

The following example submits `C:\test.txt`

with metadata, captures the returned `data_id`

, and verifies that the metadata is present in the scan result.

`$coreUrl = "http://<core-host>:8008"`

`$apikey = "<your_apikey>"`

`$filePath = "C:\test.txt"`

``

`$metadata = @{`

` uid = "abc123"`

` source_system = $env:COMPUTERNAME`

` client_ref = "ref-001"`

`} | ConvertTo-Json -Compress`

``

`$headers = @{`

` "apikey" = $apikey`

` "filename" = [System.IO.Path]::GetFileName($filePath)`

` "metadata" = $metadata`

`}`

``

`$submitResponse = Invoke-RestMethod ``

` -Method Post ``

` -Uri "$coreUrl/file" ``

` -Headers $headers ``

` -ContentType "application/octet-stream" ``

` -InFile $filePath`

``

`$dataId = $submitResponse.data_id`

`Write-Host "Data ID: $dataId"`

``

`$result = Invoke-RestMethod ``

` -Method Get ``

` -Uri "$coreUrl/file/$dataId" ``

` -Headers @{ "apikey" = $apikey }`

``

`$result.metadata | ConvertTo-Json -Depth 10`

Expected metadata output:

`{`

` "uid": "abc123",`

` "source_system": "HOSTNAME",`

` "client_ref": "ref-001"`

`}`

## Linux curl test example

The following example submits `/tmp/test.txt`

to MetaDefender Core with a custom UID in the `metadata`

header, captures the returned `data_id`

, and then retrieves the scan result to verify that the metadata is present.

`CORE_URL="http://<core-host>:8008"`

`APIKEY="<your_apikey>"`

`FILE_PATH="/tmp/test.txt"`

``

`METADATA='{"uid":"abc123","source_system":"linux-host","client_ref":"ref-001"}'`

``

`SUBMIT_RESPONSE=$(curl -sS --request POST \`

` --url "$CORE_URL/file" \`

` --header "Content-Type: application/octet-stream" \`

` --header "apikey: $APIKEY" \`

` --header "filename: $(basename "$FILE_PATH")" \`

` --header "metadata: $METADATA" \`

` --data-binary "@$FILE_PATH")`

``

`echo "$SUBMIT_RESPONSE"`

Extract the `data_id`

from the response using standard shell tools:

`DATA_ID=$(echo "$SUBMIT_RESPONSE" | sed -n 's/.*"data_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')`

``

`echo "Data ID: $DATA_ID"`

Retrieve the scan result and verify that the metadata is present:

`curl -sS --request GET \`

` --url "$CORE_URL/file/$DATA_ID" \`

` --header "apikey: $APIKEY"`

In the returned JSON, check for the `metadata`

section. It should contain the values submitted with the file, for example:

`"metadata": {`

` "uid": "abc123",`

` "source_system": "linux-host",`

` "client_ref": "ref-001"`

`}`

## Important notes

- The
`metadata`

header applies to`POST /file`

. - The
`metadata`

header is only honored on`POST /file`

. If submitted to`POST /process`

, the header is ignored and no metadata will be returned in the result. - The value must be a valid JSON object.
- It is strongly recommended to URL encode the
`metadata`

header before sending it to MetaDefender Core. - Use simple metadata field names, without any spaces.
- Metadata is only returned when querying scan results by
`data_id`

. Queries by file hash do not return the`metadata`

field. - Store the UID-to-
`data_id`

mapping on the client side for reliable lookups. - Use
`data_id`

for retrieving the scan result and sanitized output. - Sanitized files are only available if the selected workflow performs sanitization and the processed file is retained according to the configured retention policy.
- For tracking the originating system, deployment, host, or product, use the separate
`client-identity`

header instead.

## Troubleshooting

### Metadata does not appear in the result

Confirm that the scan result is being queried by `data_id`

:

`GET /file/{data_id}`

Metadata is not returned in hash-based result queries.

### API returns HTTP 400

Confirm that:

- The
`metadata`

header contains a valid JSON object. - The metadata value is correctly escaped or URL encoded.
- Metadata field names do not contain spaces.

### Sanitized file cannot be retrieved

Confirm that:

- The selected workflow performed sanitization.
- A sanitized output was produced.
- The sanitized file has not been removed by retention cleanup.
- The correct
`data_id`

is being used.

### Post-action script receives escaped characters

If a post-action script or external scanner reads metadata from STDIN, some characters may be HTML-entity-escaped before being passed to the script. Update the script logic to handle these escaped values if needed.

If **Further Assistance** is required, please proceed to log a **support case or chat with one of our support engineers**.