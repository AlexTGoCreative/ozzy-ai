<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/deep-cdr-details -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:56:42.469777 -->

# Deep CDR Details

Together with an error message, Deep CDR module also returns forensic info to describe what happened during the process in the case file was successfully sanitized.

Sample forensic info

`...`

`"post_processing": {`

` "actions_failed": "",`

` "actions_ran": "Sanitized",`

` "converted_destination": "",`

` "converted_to": "",`

` "copy_move_destination": "",`

` "sanitization_details": {`

` "description": "Sanitized successfully.",`

` "details": [`

` {`

` "action": "sanitized",`

` "object_name": "XML content"`

` },`

` {`

` "action": "removed",`

` "count": 1,`

` "object_details": [`

` "<ddeLink xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/...."`

` ],`

` "object_name": "DDE"`

` },`

` {`

` "action": "removed",`

` "count": 2,`

` "object_details": [`

` "http://metadefender.com/",`

` "http://google.com/"`

` ],`

` "object_name": "hyperlink"`

` },`

` {`

` "object_name":"XLS file",`

` "file_name":"Microsoft_Excel_97-2003_Worksheet.xls",`

` "description":"Sanitized successfully.",`

` "details":[`

` {`

` "action":"removed",`

` "count": 1,`

` "object_details": [`

` "Attribute VB_Name = \"Sheet1\"...."`

` ],`

` "object_name":"macro"`

` }`

` ],`

` "action":"sanitized"`

` },`

` {`

` "object_name":"XLSX file",`

` "file_name":"Microsoft_Excel_Worksheet.xlsx",`

` "description":"invalid file structure.",`

` "details":"Relationship file sharedStrings.xml does not exist",`

` "action":"removed"`

` },`

` {`

` "action": "removed",`

` "binary_object_details": [`

` "TVqQAAMAAAAEAAAA..."`

` ],`

` "binary_object_encoding": "base64",`

` "count": 1,`

` "object_name": "OLE",`

` "object_sha256": [`

` "eec41d62ab5d2e1d880b338c47a2156a5ee7e58f3448f58cc8120392ddc8c730"`

` ]`

` },`

` {`

` "action": "sanitized",`

` "count": 3,`

` "object_name": "image"`

` },`

` {`

` "action": "removed",`

` "count": 1,`

` "object_details": [`

` "Attribute VB_Name = \"Module1\"\r\nSub test_Macro()\r\n..."`

` ],`

` "object_name": "macro",`

` "object_sha_256": "3316B9DCF27981E42F98344FC680CBD2FB22DFE91E190DDECE56FA3C94EB628E"`

` },`

` {`

` "action": "validated",`

` "count": 1,`

` "file_name": "\\docprops\\app.xml",`

` "object_metadata": [`

` "Invalid Extended Property namely \"vt:vector\" at Line 1, Position 1066"`

` ],`

` "object_name": "invalid document properties",`

` "reason_for_action": "Follow ISG for Microsoft Office 2007 Chapter 4.8, 4.9 and 4.10"`

` }`

` ],`

` "sanitized_file_info": {`

` "file_size": 127845,`

` "sha256": "7db16cce0ea736757ebda14f64004319abdf15ad8db321bc212c03a52fee3f2d"`

` }`

` }`

`},`

`...`

To enable this feature, please check "Include Sanitization Details" and "Include Processed Objects" option in Workflow Deep CDR Setting.

To include the base64 object, please check "Include Binary Objects".

The length of object details is limited to 5000 characters. If it exceeds the limit, it will be truncated.

Sanitization details info is optional, not avaialble in all file types

| Possible action_ran values for Deep CDR | Description |
|---|---|
| Sanitized | File is sanitized successfully. |
| Sanitized Partially | Only applicable to the archive file sanitization, some children files are failed to sanitize. |
| Sanitization Skipped | File is skipped because of the configurations. |
| Sanitization Timeout | Santization process is timeout |

| skipped_reason | Description |
|---|---|
| analysis_mode | Files skipped when running in the analysis mode. |
| unsupported_analysis_mode | Files skipped when running in the analysis mode and the file types are not supported. |
| signed_file | Files skipped because they contain digital signatures. |
| marked_as_skipped | Files explicitly marked as skipped due to configuration settings. Check "failure_category" to know the details. |