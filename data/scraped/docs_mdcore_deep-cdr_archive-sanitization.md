<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/archive-sanitization -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:57:26.266735 -->

# Archive Sanitization

MetaDefender Core is able to sanitize whole uploaded archives and give a modified version of the original archive.

Usually this means that a sanitized archive contains:

All allowed child files.

- Or their sanitized versions (if available).

Sanitized versions of blocked child files (if blocked child files are sanitized successfully).

## Operation

If archive sanitization is enabled for a type, then all archives within the original with the same type get sanitized as well. If there are other archives inside the original for which the sanitization is disabled and their result is not allowed then those archives won't get into the sanitized archive.

To enable the archive sanitization: **Workflow Management > Workflows > Workflow name > Compression**

Use cases

Given the following file as example:

Zip to zip is enabled

Zip to Zip and Rar to Zip are enabled

Zip to Zip, Rar to Zip and JPG to PNG sanitization are enabled