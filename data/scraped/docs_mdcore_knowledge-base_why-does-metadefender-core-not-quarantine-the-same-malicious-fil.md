<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/why-does-metadefender-core-not-quarantine-the-same-malicious-fil -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:30:10.292177 -->

# Why does MetaDefender Core not quarantine the same malicious file twice?

This article applies to all MetaDefender Core releases deployed on Windows and Linux systems.

**Behavior:**

When scanning a known malicious file on MetaDefender Core, and quarantine blocked file is enabled, the first instance is quarantined successfully.

However, when scanning the same known blocked file again, the second instance is not quarantined because the original instance is already present in the MetaDefender Core quarantine.

**Explanation:**

Before adding a file to the quarantine, a hash lookup is performed to avoid adding duplicate files. Thus, if a file with the same hash already exists in the quarantine, it won't be added again.

This only works if **hash calculation** is enabled in the workflow. If hash calculation is disabled, the same duplicate file will be added to quarantine again, since the hash is unknown and cannot be compared.

If **Further Assistance** is required, please proceed to log a support case or chat with our support engineer.