<!-- source: https://www.opswat.com/docs/mdcore/integration -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:04:45.962299 -->

# Scan result codes and explanations

These are the possible values returned for file scans. These values appear in *scan_all_result_i* and *scan_all_result_a*:

This article explains how to obtain the possible scan results: How can I run tests to see the different scan results on MetaDefender Core?

| Code | Scan result | Relation | Description |
|---|---|---|---|
| 0 | No Threat Detected | Metascan engine | No threat detection or the file is empty. |
| 1 | Infected | Metascan engine | One or more threats have been found. |
| 2 | Suspicious | Metascan engine | Classified as a potential threat without a specific identification. |
| 3 | Failed | Metascan engine / MetaDefender Core | The scan failed due to the system or application error. |
| 7 | Allowlisted | MetaDefender Core | The scan is skipped for good because one of file characteristics meet certain pre-configured conditions (based on hash / file type / file name etc.). |
| 8 | Blocklisted | MetaDefender Core | The scan is skipped for bad because one of file characteristics meet certain pre-configured conditions (based on hash / file type / file name etc.). |
| 9 | Exceeded Archive Depth | Archive Extraction engine | Reached archive handling limit for archive depth level (Max recursion level). |
| 10 | Not Scanned | Metascan engine | The scan is not performed by Metascan engines either due to engine updates or other engine-specific failure reasons. If Metascan is disabled, this will be the final result. |
| 12 | Encrypted Archive | Archive Extraction engine | The scan is not performed because the file type is detected as an encrypted (password-protected) archive but without having a correct password to decrypt. |
| 13 | Exceeded Archive Size | Archive Extraction engine | Reached archive handling limit for archive size limit (Max total size of extracted files). |
| 14 | Exceeded Archive File Number | Archive Extraction engine | Reached archive handling limit for archive file size limit (maximum number of files extracted). |
| 15 | Password Protected Document | Archive Extraction engine | A document that is protected by a password [e.g., Office documents or PDFs that require a password to view its contents] but without having correct password to decrypt. |
| 16 | Exceeded Archive Timeout | Archive Extraction engine | The archive extraction process on a certain archive file reached the given timeout value (Archive analysis timeout). |
| 17 | Mismatch | File type analysis engine | The file extension is not a part of the allowed extensions associated with the true file type. |
| 18 | Potentially Vulnerable File | File-Based Vulnerability Assessment | A Potentially Vulnerable File is a file associated with vulnerable components or applications identified by OPSWAT’s File-Based Vulnerability Assessment technology. |
| 19 | Cancelled | MetaDefender Core | The scan is canceled because the client terminated the connection or explicitly submitted a cancellation request. |
| 20 | Sensitive Data Found | Proactive DLP | Sensitive Data Found file detected by Proactive DLP refers to a file that contains information classified as sensitive according to predefined criteria set by the organization's data security policies. |
| 21 | Yara Rule Matched | YARA engine | File content matched at least one of the pre-defined YARA rules. |
| 22 | Potentially Unwanted | Metascan engine | Potentially unwanted application (PUA) classified by Metascan AV engines. |
| 23 | Unsupported File Type | Metascan engine | The engine does not support scanning this file type. Certain Metascan AV engines such as AI-based engines only scan specific file types such as executable files or documents. https://docs.opswat.com/mdcore/metascan-engines/supported-file-type-for-ai-engines. |
| 24 | Extraction Failed | Archive Extraction engine | Archive extraction failed due to some reasons which could be found under the archive processing section (e.g. insufficient disk space, file content data error, etc.). |
| 26 | Suspicious Verdict by Sandbox (displayed as | Adaptive Sandbox | When Adaptive Sandbox labels a file with a "Suspicious" verdict, it means that the file exhibited behaviors or characteristics that are commonly associated with malware or other malicious activity but are not conclusively harmful. Starting from MD Core version 5.17.1, the Core UI will display |
| 27 | Likely Malicious Verdict by Sandbox (displayed as | Adaptive Sandbox | Adaptive Sandbox has identified behaviors or characteristics in the file that strongly suggest it is harmful, but the evidence is not entirely conclusive to label it as definitely malicious. Starting from MD Core version 5.17.1, the Core UI will display |
| 28 | Malicious Verdict by Sandbox (displayed as | Adaptive Sandbox | Adaptive Sandbox has definitively determined that the file is harmful. Starting from MD Core version 5.17.1, the Core UI will display |
| 29 | Blocked Verdict by Sandbox | Adaptive Sandbox | This indicates that the Adaptive Sandbox has determined that this file is dangerous and needs to be blocked by the Core. This verdict appears when a file is blocked but does not fall under any predefined verdicts mentioned above. The result also depends on the configuration of the Adaptive Sandbox. |
| 30 | Blocked Verdict by Deep CDR | Deep CDR | It indicates that a file was blocked based on a decision by the Deep CDR engine. This occurs when the user has enabled the file blocking feature in the Deep CDR configuration. For example, users can enable the option to block files if Office documents contain hyperlinks, embedded objects, QR codes, etc. |
| 31 | Global Timeout Exceeded | MetaDefender Core | The global processing timeout takes precedence over any engine timeout and is disabled by default. Certain scans may be terminated when enabled if they exceed the pre-defined global processing timeout. |
| 32 | Vulnerable Verdict by SBOM | SBOM | This indicates that software components contain known vulnerabilities that could potentially be exploited and therefore may require attention or remediation. Please note that this case may also include a License Risk Found. You should check the SBOM details for more information. |
| 33 | Non-vulnerable Verdict by SBOM | SBOM | This indicates that software components have been evaluated and found to be free of security weaknesses based on the current vulnerability data. |
| 34 | Blocked Verdict by SBOM | SBOM | This indicates that the SBOM has determined that software components have security weaknesses or risks and need to be blocked by the Core. This verdict appears when the item is blocked but does not fall under any of the predefined verdicts. The result also depends on the configuration for the SBOM. |
| 38 | Known Bad | Reputation engine | The Reputation engine found the file as a known (recognizable) harmful one. For more details, the Reputation Engine cross-references file hashes with a database of known malicious files and utilizes advanced analysis to quickly address false positives. For further information, please refer to this link: Metadefender Core v5.9.0: Powerful New Engines for Proactive Threat Detection. Please note that the Reputation Engine is not enabled by default. |
| 39 | Known Good | Reputation engine | The Reputation engine found the file as a known good one. For more details, the Reputation Engine cross-references file hashes with a database of known malicious files and utilizes advanced analysis to quickly address false positives. For further information, please refer to this link: Metadefender Core v5.9.0: Powerful New Engines for Proactive Threat Detection. Please note that the Reputation Engine is not enabled by default. |
| 40 | Unknown | Reputation engine | Reputation engine does not come to final conclusion to determine if the file is harmful or not (inconclusive). |
| 41 | Allowed Verdict by COO | Country of Origin | Based on the current configuration, the Country of Origin engine indicates that the file comes from an allowed source. |
| 42 | Blocked Verdict by COO | Country of Origin | Based on the current configuration, the Country of Origin engine indicates that the file comes from an unallowed source. |
| 45 | License Risk Verdict by SBOM | SBOM | This indicates that the software components present one or more license risks. Please note that this case may have Vulnerabilities Found, but they do not meet the pre-configured threshold to impact the decision to block the file. You should check the SBOM details for more information. |
| 46 | Blocked Verdict by File Type | File type analysis engine | Other scenarios, apart from Mismatch, where a file is flagged as blocked by the FileType engine. This is dependent on the specific configuration of the FileType engine. |
| 47 | Multipart Upload Timed Out | MetaDefender Core | Cases where multipart uploading is used to upload processed files to MetaDefender Core, and this upload action times out. |
| 48 | Sanitized | Deep CDR | When the `Block files if sanitized successfully` setting is enabled in the Deep CDR workflow settings, and the file is successfully sanitized, the file will be blocked. This verdict has the lowest priority compared to other block verdicts. |
| 51 | Exceeded Limited Sandbox File Size | Adaptive Sandbox | When the `Block files that exceed the file size threshold` setting is enabled in the Adaptive Sandbox workflow settings, the file will be blocked if its size exceeds the configured threshold. |
| 52 | Blocked Verdict by Archive Extraction | Archive Extraction engine | The file has been blocked based on the recommendation from the Archive Extraction engine. The reason for the block is detailed in the Archive Extraction scan result. |
| 53 | Blocked Verdict by Archive Compression | Archive Compression engine | The file has been blocked based on the recommendation from the Archive Compression engine. The reason for the block is detailed in the Archive Compression scan result. |
| 54 | Sandbox Execution Limit Reached | Adaptive Sandbox | When the `Block files if execution limit reached` setting is enabled in the Adaptive Sandbox workflow settings, the file will be blocked if the license execution limit is reached. |
| 55 | Rejected | MetaDefender Core | The request was rejected due to policy, validation, or configuration constraints. |
| 56 | Empty Split Archive | Archive Extraction engine | The reassembled archive contains no nested file. |
| 57 | Split Archive Upload Timed Out | Archive Extraction engine | The split-archive upload session exceeded the configured time window. |
| 58 | Unsupported Split Archive Type | Archive Extraction engine | The archive format of the split upload is not supported. |
| 59 | Split Archive Not Supported | Archive Extraction engine | The Archive Extraction engine version does not support split-archive. |
| 60 | Exceeded Archive Expansion Factor | Archive Extraction engine | Reached the archive handling limit due to the expansion factor limit (Max expansion factor). |
| 61 | Allowed Verdict by Threat Intelligence | Threat Intelligence | The file being allowed by Threat Intelligence, is a rare verdict in practice, unless you explicitly configure the system to block files when this verdict occurs. |
| 62 | Blocked Verdict by Threat Intelligence | Threat Intelligence | The file has been blocked based on the recommendation from the Threat Intelligence engine. The reason for the block is detailed in the Threat Intelligence scan result. |
| 63 | AI Content Detected | OPSWAT AI Content Inspector | The analysis engine did find sufficient evidence that the content was generated by artificial intelligence. |
| 64 | AI Content Uncertain | OPSWAT AI Content Inspector | The analysis engine could not confidently determine whether the content was AI-generated or human-written. |
| 65 | AI Content Not Detected | OPSWAT AI Content Inspector | The analysis engine did not find sufficient evidence that the content was generated by artificial intelligence. |
| 66 | RMS Protected Document | Archive Extraction engine | A document that is protected by Microsoft Rights Management Services (RMS) and can not be read for processing. |
| 255 | In Progress | MetaDefender Core | The scan is still in progress, not yet finished. |
| 256 | Multipart Uploading | MetaDefender Core | Parts of the file are being uploaded; processing has not started. |
| 257 | Split Archive Uploading | Archive Extraction engine | Split-archive parts are being uploaded; processing will begin after all parts are received. |