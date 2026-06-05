<!-- source: https://www.opswat.com/docs/mdcore/proactive-dlp/data-tagging-and-classification -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:58:19.869695 -->

# Data tagging and classification

OPSWAT Proactive DLP supports embedding metadata tags into PDF, Word, PowerPoint, and common image file formats. These tags serve as a mechanism for conveying detailed information about the results and outcomes of the PDLP content analysis. The metadata is attached directly to the processed and downloadable file, allowing downstream systems, such as document management platforms, SIEM solutions, and custom automation workflows, to automatically detect, interpret, and act on this information. By enabling consistent identification and traceability of sensitive content, this capability enhances end-to-end policy enforcement, auditing, and content governance across the organization.

Below is the list of metadata tags currently supported by PDLP:

**OPSWAT-PDLP-CLASSIFICATION (opdlp classification):**This tag is designed to convey information about the file classification outcome by summarizing the reason a file or event triggered DLP controls. Examples include cases where the file contains sensitive data, the file or associated user poses potential risks, or a specific DLP policy has been violated. The tag also provides relevant business context to support efficient alert triage and remediation.**OPSWAT-PDLP-CLASSIFICATION-DETAILS (opdlp classification details):**This tag is intended to add more specific details to those classification categories listed in*OPSWAT-PDLP-CLASSIFICATION***OPSWAT-PDLP-REDACTED (opdlp redacted):**This tag is intended to deliver information about the result of the redaction.**OPSWAT-PDLP-CONFIDENCE-SCORE (opdlp confidence score):**This tag represents the PDLP confidence score assigned to the processed file. The DLP confidence score is a numerical value, typically ranging from 0 to 1 (or expressed as 0–100%), that quantifies the likelihood that a file contains sensitive information such as PII, PHI, PCI, or intellectual property. Higher scores indicate greater confidence that the file meets the criteria for a policy violation.

Example: