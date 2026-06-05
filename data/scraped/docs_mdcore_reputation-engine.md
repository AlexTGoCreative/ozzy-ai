<!-- source: https://www.opswat.com/docs/mdcore/reputation-engine -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:02:59.900716 -->

# Overview

## Reputation Engine

#### Faster Remediation For False Detections

Reputation Engine matches file hashes against our global database of known good and bad files; and leverages advanced analyses to remediate false detections faster.

Benefits of the Reputation Engine:

- Advanced threat detection - Identify uploaded files as
`Known Good`

,`Known Bad`

by matching hashes against our database of known malicious or safe files. If the file is not yet part of our database, the engine will identify it as`Unknown`

. - Minimized false positives/negatives - Leverage advanced analyses conducted by malware analysts and reverse engineering experts for faster verdicts on suspicious files.

### Layered security powered by Reputation Engine

The Reputation Engine, while formidable in its own right, truly shines when incorporated into a comprehensive cybersecurity strategy that emphasizes defense-in-depth.

OPSWAT's MetaDefender platform is designed to safeguard file uploads with a multi-layered defense approach. It leverages a robust reputation engine alongside other complementary capabilities:

**Reputation Inspection:**This feature draws upon a real-world database to assess the trustworthiness of files.**Static File Analysis:**Utilizing advanced algorithms, this component identifies potentially suspicious patterns and attributes within files.**Dynamic Analysis with Adaptive Sandbox:**By observing files in a controlled, isolated environment, this tool can monitor their behavior in real-time, providing valuable insights into potential threats.

By combining these elements, MetaDefender Core offers comprehensive protection that addresses multiple vectors of attack, ensuring a more resilient defense against cyber threats.

### Mechanism of Reputation Engine

The Reputation Engine serves as the primary defense for file upload security by cross-referencing against a real-world database. When users submit their files to MetaDefender Core, it generates hashes and it assess the uploaded file against the Reputation Database, our engine rapidly categorizes hashes as "Known Good," "Known Bad," or "Unknown." This capability enables users to promptly decide whether to allow, block, or scan files with other detection engines based on their predefined security policies. This prevents threats from entering your environment.

**In case of Known Good or Known Bad verdict, the user can choose whether it is the final verdict for the uploaded file or user chooses to run the other engines of MetaDefender Core.**

### Displaying engine results

Below you will be shown examples of how the three types of file reputation results are displayed inside MetaDefender Core

**Known Good:** The hash matches an entry of known good files in OPSWAT's the real world database.

**Known Bad:** The hash matches an entry of known malicious files in OPSWAT's real-world database.

**Unknown:** There aren't any matches on this hash in OPSWAT's real-world database.