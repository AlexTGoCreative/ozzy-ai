<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/why-are-japanese-filenames-garbled-when-submitting-files-to-meta -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:28:18.887033 -->

# Why Are Japanese Filenames Garbled When Submitting Files to MetaDefender Core via API?

This article applies to all MetaDefender Core V4 and V5 releases deployed on Windows or Linux systems.

When submitting files to MetaDefender Core via API, filenames containing Japanese characters may appear garbled in **History > Processing History**, even though the file itself is processed successfully.

## Cause

For API-based submissions, MetaDefender Core derives the displayed filename from the `filename`

and `filepath`

values provided in the HTTP request headers. HTTP headers do not reliably support multibyte character sets. As a result, filenames containing Japanese characters may not be interpreted correctly if sent without encoding.

## Scope Clarification

Filename encoding behavior differs depending on how the file is submitted:

**API submissions**Filenames are read directly from HTTP request headers.**Archive submissions (ZIP, TAR, CAB)**Filenames of extracted child files are processed during archive extraction and may use automatic UTF-8 or Shift-JIS detection.

Encoding settings configured under **Archive Extraction** apply only to filenames of files extracted from archives and do not affect filenames provided through API requests.

## Resolution

To ensure filenames containing Japanese characters are displayed correctly when submitting files via API:

- Encode the filename using UTF-8.
- Apply URL encoding (%-encoding) to the UTF-8 encoded filename.
- Send the encoded value in the
`filename`

(and`filepath`

, if applicable) request header.

This is the recommended and supported approach for handling non-ASCII filenames in API submissions.

## Additional Information

- The archive encoding configuration does not influence API-submitted filenames.
- File content processing is not affected; only the displayed filename may appear garbled if encoding is not applied.

If Further Assistance is required, please proceed to **create a support case or chat with our support engineer**.