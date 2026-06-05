<!-- source: https://www.opswat.com/docs/mdcore/proactive-dlp/detect-intentional-data-leakage -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:58:53.662414 -->

# Detect intentional data leakage

Malicious insiders often employ subtle techniques to evade DLP controls and conceal sensitive information within files or documents. Two common evasion methods include **invisible text** and **small font manipulation**, both of which are now detectable through OPSWAT Proactive DLP’s advanced content inspection.

**Invisible Text Detection:**Detects hidden or white-colored text embedded within documents or images that is not visible to human reviewers but can still be processed by digital systems. This technique is often used to conceal confidential data, trigger automated workflows, or bypass keyword-based inspection mechanisms.**Small Font Detection:**Identifies attempts to hide sensitive data by using extremely small font sizes that make the content unreadable to the human eye but still machine-detectable. This approach can be used to disguise regulated information such as PII, credentials, or source code snippets within otherwise benign files.

By identifying and flagging hidden content manipulation techniques, OPSWAT Proactive DLP enhances detection accuracy and mitigates the risk of data exfiltration resulting from concealed or obfuscated information within files.

Example: