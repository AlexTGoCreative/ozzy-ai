<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/does-metadefender-core-support-scanning-of--parquet-gpg-files- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:28:43.875045 -->

# Does MetaDefender Core support scanning of .parquet.gpg files?

This article applies to all MetaDefender Core releases deployed on Windows and Linux systems

This is a two‑part inquiry, since the file extension represents a combination of formats:

.parguet extension refers to the Apache Parquet file format. .gpg indicates that the file has been encrypted using the OpenPGP standard.

When a Parquet file is encrypted with OpenPGP, the gpg extension is appended to the existing extension, resulting in a combined extension file.

This article applies to all version of MetaDefender Core

As of File-Type Engine version 7.7.0 MetaDefender Core supports both: • The Parquet file format • The OpenPGP‑encrypted file format This means that files are supported beginning with the release of File Type Engine 7.7.

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.