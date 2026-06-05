<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/can-metadefender-core-process-microsoft-purview-information-prot -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:31:41.727847 -->

# Can MetaDefender Core Process Microsoft Purview Information Protection Encrypted Files?

This article applies to all MetaDefender Core releases deployed on Windows and Linux systems.

Some organizations use **Microsoft Purview Information Protection (MPIP)** to classify and encrypt sensitive data. A common question is whether **MetaDefender Core (MD Core)** can scan and process these encrypted and classified files directly.

This article clarifies MetaDefender Core’s current capabilities and provides guidance on handling such files effectively.

## Issue

- Customers want to process files that are
**encrypted and classified**by Microsoft Purview Information Protection using MetaDefender Core engines. - There is uncertainty about whether MetaDefender Core natively supports these encrypted formats.
- No official documentation exists on direct integration or support for Microsoft Purview encrypted files.

## Resolution

**MetaDefender Core cannot process encrypted files from Microsoft Purview Information Protection.**
To ensure successful scanning:

- Process files with MetaDefender Core
**before**they are encrypted and classified by Microsoft Purview Information Protection.

## Programmatic Handling

If the goal is to detect **classification labels** (not the encrypted content itself), this can be achieved through **regex-based detection in Proactive DLP** on the file’s metadata.
Refer to the following documentation for implementation guidance: Leverage metadata info added by data classification systems

This method only enables label detection — it does not decrypt or scan the encrypted file content.

Additionally, encrypted files protected by Microsoft Purview are currently detected by MetaDefender Core with the following **file type identifiers**:

`MSO-ENCRYPTED-MSIP`

`PDF-ENCRYPTED-MSIP`

Customers can configure policies in MetaDefender Core to **allow or block** these file types based on their organization’s security requirements.

## Additional Notes

- MetaDefender Core supports a wide range of file formats, but encrypted content is treated as opaque data unless decrypted before scanning.
- Ensure your data flow enforces
**“scan before encrypt”**as a best practice.

If **Further Assistance** is required, please proceed to log a support case or chatting with our support engineer.