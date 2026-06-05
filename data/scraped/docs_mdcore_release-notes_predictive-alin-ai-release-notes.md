<!-- source: https://www.opswat.com/docs/mdcore/release-notes/predictive-alin-ai-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:08:16.053484 -->

# Predictive Alin AI release notes

## Predictive Alin AI 3.0.0

### Release information

- Version: 3.0.0
- Release date: 23/03/2026
- Release type: Major

Predictive Alin AI 3.0.0 marks the **General Access release** of OPSWAT’s proprietary machine learning-driven malware detection engine, purpose-built for **high-speed, pre-execution protection** in modern, high-throughput environments.

**What This Means for MetaDefender Customers?**

**Predictive Alin AI**is fully integrated into the MetaDefender platform and accessible across all products and environments, available in both**cloud and on-premises environments**, supporting**Windows and Linux**operating systems**Predictive Alin AI**operates in parallel to MetaScan to enhance detection coverage via machine learning algorithms enhanced by MetaDefender Aether’s dynamic analysis, for reduced false positives and zero-day detection**Predictive Alin AI**targets the primary malware entry points, with extensive support for executable formats and PDF files, where most modern threats originate.

**How Is Predictive Alin AI Continuously Improving?**

Predictive Alin AI has a documented Machine Learning pipeline lifecycle concept for transparency, including:

- Data ingestion and normalization controls (hashing, deduplication, validation)
- Labeling and enrichment through MetaDefender Aether using multi-source evidence (static characteristics, dynamic analysis context, consensus-oriented verdict context, and threat intelligence enrichment)
- Training, evaluation, and quality gating against false-positive benchmarks before promotion
- Continuous refresh and monitoring to adapt to malware evolution

### Key Benefits of Predictive Alin AI

- Fast, pre-execution malware detection (P99 under 100ms) to enable allow, block, and quarantine decisions at scale.
- Faster scan times for high-volume workflows while improving accuracy and reducing false positives (0.1% False Positive Rate and over 90% accurcacy across the board)
- Extensive support for executable formats (PE, ELF, Mach-O) plus PDF for common document-borne threats.
- Available as a custom engine in MetaDefender Cloud and MetaDefender Core.

**Next Steps to Upgrade:**

Customers currently using MetaDefender products can add Predictive Alin AI to unlock high-speed, machine learning–based detection for pre-execution threats while retaining familiar multiscanning capabilities. To discuss upgrade options or transition planning, please contact your OPSWAT representative.

**Predictive Alin AI** reflects where we’re heading with pre-execution malware detection: faster decisions, better accuracy, and the ability to handle high-volume environments without added complexity.

### Release Notes

General Access release of Predictive Alin AI for customer-facing enterprise use.

Reputation integration to improve deflection decisions for known good and known bad files.

File type detection optimized for malware screening workflows across:

- Executables: PE, ELF, Mach-O
- Documents: PDF

File parsing for PE, ELF, Mach-O, and PDF to extract structural signals used as context for ML inference.

Integration availability:

**MetaDefender Cloud**- Predictive Alin AI runs inline as part of the MetaScan package.MetaDefender Core - Predictive Alin AI runs inline as part of the MetaScan package on Linux and Windows.

Standardized engine verdict codes: Reference: https://www.opswat.com/docs/mdcloud/integrations/description-on-scan-result-codes

- 0 - No Threat Detected
- 1 - Infected: The file was analyzed and determined to be malicious.
- 10 - Not Scanned: The file was not analyzed (for example, due to size limits or an internal processing error).
- 23 - Unsupported File Format: The file type is not currently supported by the engine.

Threat detection naming convention for policy integration:

Format: <platform>/malicious_<threat_confidence>

Platform mapping:

- Windows - PE-based executables
- Linux - ELF-based binaries
- Darwin - Mach-O-based binaries
- Generic - non-platform-specific formats such as PDF

Examples:

- PE: Windows/malicious_99
- ELF: Unix/malicious_99
- Mach-O: MacOS/malicious_99
- PDF: Generic/malicious_99

### Compatibility

- Platforms: Windows, Linux
- File types: PE, ELF, Mach-O, PDF

Known considerations

- This is the first General Access release. Establish an initial operational baseline before tightening policy.
- Malicious naming outputs are standardized for policy integration and should be interpreted alongside the broader security context.