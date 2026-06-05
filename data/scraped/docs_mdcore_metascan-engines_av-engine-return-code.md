<!-- source: https://www.opswat.com/docs/mdcore/metascan-engines/av-engine-return-code -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:54:41.707238 -->

# AV engine return code

The following values are available for **scan_results.scan_details.<engine name>.scan_result_i**

| Returned Code | Description |
|---|---|
| 0 | No threat detected |
| 1 | Infected |
| 2 | Suspicious |
| 3 | Failed to scan |
| 10 | Not scanned |
| 19 | Cancelled |
| 22 | PUA/PUP detected |
| 23 | File format not supported |