<!-- source: https://www.opswat.com/docs/mdcore/utilities-engines -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:04:32.665783 -->

# File Type Verification Engine

With MetaDefender's file type verification technology, users can process files based on their true file types, so the system can take more precautions with risky file types like EXEs, perhaps setting different policies or rules based on file type. Spoofed file types indicate potentially malicious intent, so to mitigate this risk, MetaDefender offers functionality to block files with incorrect extensions, for example, prevents an instance of EXE file which is posed as TXT file from entering the organization. Also, more strict rules, like remediation steps can be applied. For example, Deep CDR is triggered as a post-action for the file type verification. This is highly configurable so that Deep CDR or any other secure processes can happen based on the target file name, file format and any other recognized file property data as well.

#### Configuration:

**Fallback file type detection to current extension if needed**: if this configuration is enabled, Deep CDR, Proactive DLP, Archive Extraction modules and Blocklist/Allowlist features will use the true file type from the file type engine to perform its job first; if it is failed, these modules and features will use the file extension as a backup.

**Except on Deep CDR if the actual file type is not enabled or supported:** when ticked, file extension will not be used as backup if actual file type is not enabled or supported by Deep CDR module.

**Skip processing if actual file type could not be detected:** if the File type engine is crashed/disabled/timeout/cancelled, MetaDefender Core will return "Not scanned".