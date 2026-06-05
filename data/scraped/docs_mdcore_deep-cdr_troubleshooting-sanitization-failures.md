<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/troubleshooting-sanitization-failures -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:57:48.108079 -->

# Troubleshooting sanitization failures

To distinguish different errors happened during the sanitization process, Data Sanitization engine classifies the errors to different categories The information is available in JSON output when retrieving scan result though REST API.

Sanitization failure

`...`

`"post_processing": {`

` "actions_failed": "Sanitization Failed",`

` "actions_ran": "",`

` "converted_destination": "",`

` "converted_to": "",`

` "copy_move_destination": "",`

` "sanitization_details": {`

` "failure_category": "invalid file structure",`

` "details": "Startxref not found"`

` }`

`},`

`...`

*details* is an optional key
*sanitization_details* is not available for all of the file types such as archive, eml file types.

| Possible actions_failed values for Deep CDR | Description |
|---|---|
| Sanitization Failed | File is failed to sanitize, check failure_category to have more details |
| Sanitization Timed Out | Time to process the file is longer than the configured time |

| failure_category | description |
|---|---|
| invalid file structure | File is corrupted or it does not match specification |
| unsupported version | MS Office file is created with format before MS Office 97 or DWG file is created with AutoCAD before version 2004 |
| exceeded file size | This file size is bigger than the configured file size |
| password protected | Document needs a password to unlock |
| processing time out | The sanitization process is timeout |
| failed to sanitize | Other failures during sanitization, should not happen |