<!-- source: https://www.opswat.com/docs/mdcore/release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T08:55:03.019898 -->

# Release notes

Version | 5.19.0 |
|---|---|
Release date | 21 May 2026 |
Scope | This major version introduces a brand new technology - OPSWAT AI Content Inspector for AI-driven document fraud detection, automated support package generation via My OPSWAT Central Management, and differentiated RMS-protected document verdicts. The version also includes health check enhancements, Deep CDR filename exceptions, email notification improvements, engine management controls, 3rd-party library upgrades, and a few bug fixes. |

- Microsoft Visual C++ Redistributable version 14.44 or later is required for version 8.0 of the following modules: File Type, Archive Extraction, Archive Compression, Country of Origin, and Deep CDR.
- Making sure to check out the Known Limitations.

## New Features, Improvements and Enhancements

**New Technology: OPSWAT AI Content Inspector**

OPSWAT AI Content Inspector is a new technology introduced in MetaDefender Core. It is an AI-driven content authenticity and document fraud detection engine designed to help organizations identify suspicious or manipulated content before review, approval, or payout processes.

It analyzes visual, textual, and structural signals across documents and images to detect potential fraud in invoices, insurance claims, accident photos, and other high-risk content.

**Automated support package generation and transfer to My OPSWAT Central Management**

MetaDefender Core’s support packages can now be generated on demand from MOCM and automatically uploaded to MOCM for centralized retrieval. This is particularly valuable for instances in remote or restricted environments where Support previously had to coordinate with the local administrator to collect logs.

**Differentiated verdict for RMS-protected Office documents**

Password-protected and RMS-protected (label-protected) Office documents were previously classified under a single verdict, "Password Protected Document." Both file types are now reported separately as *Password Protected Document* and *RMS Protected Document*. The new verdict is recognized end-to-end in verdict filtering on Processing History, the verdict result highlighter, scheduled report emails, and email notifications for processing activity.

To preserve backward compatibility, *RMS Protected Document* is enabled by default in existing settings (such as email notifications and scheduled reports) during upgrade or configuration import, so customers continue to receive coverage equivalent to their previous configuration.

**Further Enhancements**

**1) Faster processing result retrieval during engine updates**

Processing result API calls could previously stall behind an in-progress engine update, occasionally exceeding the 150-second NGINX timeout for customers with large workloads. The internal lookup of engine configuration last-modified time is now served from a cache, so result retrieval no longer waits on engine updates to complete and returns results promptly even while engines are mid-update.

**2) Verdict origin indicator for scan categories and errors**

The management console now indicates whether a scan category or error (for example, "Calculate Hash Error") was determined by MetaDefender Core itself or by the underlying scan engine. A visual indicator clarifies the origin so administrators and Support can more quickly route and triage issues.

**3) Adaptive Sandbox skip handling for unsupported file types**

Adaptive Sandbox previously sent files with the Metascan verdict `Unsupported File Type`

for sandbox analysis because that verdict was missing from the skip-evaluation list. This verdict is now recognized, ensuring unsupported file types are skipped from sandbox processing as intended and reducing unnecessary sandbox resource consumption.

**4) A clearer blocked reason for scans interrupted by the MetaDefender Core restart**

When the MD Core service restarts mid-scan, in-process scans are now reported with an explicit failed block reason rather than an empty reason. This makes interrupted scans easier to identify in processing history and downstream reporting, improving auditability after unexpected restarts.

**5) Deep CDR output filename exception by filename and extension**

Deep CDR users can now define output filename exceptions based on filename or extension, in addition to the existing exceptions based on detected true type. This enables, for example, converting one extension to .txt while preserving another extension's original suffix in the sanitized output filename, even when both files share the same detected true type.

**6) Engine package compatibility flag**

The `stat/packages`

API now includes a boolean-supported field on each engine and database package entry, making it clearly visible whether a package is compatible with the currently running MetaDefender Core version. This simplifies inventory and compatibility validation for administrators and integrators.

**7) Delayed start for the MetaDefender Core service on Windows**

On Windows, the MD Core service is now configured with the "Automatic (Delayed Start)" startup type. This ensures the operating system has finished initializing dependent services — particularly network interfaces — before MD Core starts, preventing a few unexpected behaviors.

**8) Additional SBOM fields in the PDF report**

The Software Bill of Materials (SBOM) PDF report has been expanded with additional fields requested for compliance frameworks such as CERT-in. Customers benefit from a richer SBOM artifact that more closely aligns with regulatory and industry reporting requirements.

**9) Additional Metascan engine information in the Export Result**

The Export Result option for processing details now includes per-engine information for Metascan engines. The "AV Engines" column in Advanced Export has been renamed to "Engine Name," and two new fields — "Engine Version" and "Database Version" — are now exported alongside it. These values are also preserved for results that were originally scanned on a previous MetaDefender Core version after the upgrade.

**10) Reorganized workflow configuration tabs**

The Workflow configuration tabs have been reorganized by functional group, making settings easier to discover and configure.

**11) Improved tab display for long engine names in Advanced Export**

Engine names in the Advanced Export tab are now properly fitted within their containers, eliminating overflow that occurred for engines with long display names.

**12) Disk space monitoring in health check policies**

Health check policies can now monitor the free disk space on the MetaDefender Core installation drive. If available space falls below the configured threshold, the instance is flagged as not ready for file processing.

**13) Outdated engine detection in health check policies**

Health check policies can now flag engines whose definitions have not been updated within a configurable number of days. Administrators can specify which engines are required and how many days old their definitions can be before the health check fails.

**14) Email notifications based on final scan status**

Email notifications can now be triggered by a file's final status, such as when a file is blocked, in addition to the existing scan-result triggers (Infected, Suspicious, and so on). This is useful when you care more about enforcement outcomes than the specific findings behind them.

**15) Prevent engine downgrade**

MetaDefender Core now includes a setting that blocks downgrades of engine and database packages, protecting deployments from accidental rollbacks to outdated threat definitions. This setting is disabled by default.

**16) Proxy connectivity test**

Administrators can now validate proxy settings before saving them. The test verifies connectivity to the updater and activation server, helping avoid misconfigurations that would otherwise only surface when updates silently fail.

**17) Out-of-date engine notification banner**

The system banner now includes a setting to notify administrators when scan engines are out of date. A global threshold can be configured in days, with the option to override it per engine.

**18) Configuration History — Collapsed Diff View**

The Configuration History page now displays only the changed lines in a collapsed diff view, making it easier for administrators to identify what was modified in configuration or workflow policy changes.

**Security Enhancements**

Upgraded 3rd party libraries:

- NGINX v1.30.1
- PostgreSQL v14.23

**Bug Fixes**

- Fixed an issue where some My OPSWAT Central Management-related configuration screens reported a successful save while the underlying value failed validation.
- Fixed an issue where the Adaptive Sandbox verdict was reported as "System Error" in the PDF export when the scan was cancelled mid-processing.
- Fixed an issue where archive scan results displayed an "Exceeded Archive File Number" extraction issue without an associated count of affected files. The count is now correctly populated for the root archive.
- Fixed an issue where the workflow rule name filter in Executive Reports did not reflect renamed rules, leaving the old name in the filter. The filter now correctly reflects the current rule name.

## Known Limitations

Kubernetes v1.35 or containerd v2.2.0 could not deploy MetaDefender Core images | This issue is a bug of Until the vendor provides a fix, use one of the following mitigations: - Downgrade containerd to a supported version (e.g., 1.7.x)
- Use a Kubernetes node image that does not include containerd 2.2.x
- Pin node runtime version in cluster provisioning
More details at Unable to deploy MetaDefender Core in Kubernetes with containerd engine 2.2.x |
Slow or Inaccessible Management Console |
In version 5.12.0, an issue was identified that caused some APIs to load more slowly than expected. As a result, the Web Management Console might experience slower performance or become unresponsive Please read more details on this page: Slow or Inaccessible Management Console. |
The 'Proxy server requires password' setting cannot be disabled once it has been enabled |
In version 5.14.1, there was an issue that prevented disabling the |
Database connection failure occurred in a specific circumstance after upgrading to version 5.11.0 |
This issue does not affect all cases when upgrading to version 5.11.0. After applying the authentication method - If the application was previously upgraded from version 5.5.1 or older to version 5.6.0 or newer, this issue will occur when users upgrade to version 5.11.0.
We prepare a Knowledge Base (KB) for troubleshooting the issue and bringing the system back online: How to troubleshoot an error related to connection to database failing after an upgrade to v5.11.0? The issue will not occur in the following scenarios: - Upgrading directly from version 5.5.1 or older to version 5.11.0.
- Upgrading from a fresh installation of version 5.6.0 or newer to version 5.11.0.
|
Archive compression may fail with very large archive files that contain a large number of subfiles |
MetaDefender Core has a limitation when compressing very large archive files that contain a high number of subfiles. In our test scenario, it failed when processing an archive with 300,000 or more subfiles. |
Reuse processing result by hash might be slow in high-load situations |
Since its introduction in version 5.8.0, this feature has helped improve overall performance and reduce significant load when processing similar files. However, we have realized this feature might run slowly in high-load scenarios against large database sizes. |
Temporary files in the resource folder may not be properly cleaned up if the Archive Extraction engine crashes | Starting from MetaDefender Core version 5.10.1, if the Archive Extraction engine crashes, temporary files from specific extraction transactions may not be properly cleaned up. However, this issue is relatively rare. |
Reject importing non-empty required_engines setting in containerized environments | This issue occurs only in containerized environments. If the config zip file includes non-empty
- Extract the config zip file.
- Open the "
`export_settings.json` " and set "`required_engines` " to an empty array. - Recompress the files into a new zip.
- When executing the docker run command, set the following environment variables:
`MDCORE_HEALTH_CHECK` ,`MDCORE_REQUIRED_ENGINES` . For more details, please refer to Health Check settings on docker
|
The Engine Update feature may not work as expected in certain environments | We have observed that the Engine Update feature may not work properly in an environment protected by a Palo Alto firewall. In the log file, you might find the error message ' If upgrading to the latest version of MetaDefender Core does not solve the issue, please consider setting up MetaDefender Update Downloader product. This product is responsible for downloading engines, and MetaDefender Core will retrieve and update its engines from there. |
Stability issues on Red Hat / CentOS systems with kernel version 372.13 | MetaDefender Core version 5.2.1 or later may not function correctly with Red Hat or CentOS operating systems that use kernel 372.13. Red Hat is addressing the kernel issues. Please try upgrading to kernel version |
PostgreSQL and MetaDefender Core services cannot initialize in certain containerized environments |
In a containerized environment, MetaDefender Core version 5.2.0 or newer may work properly when: - The Linux kernel version of the host machine is newer than 4.18.0 including 5.x.y and 6.x.y.
- The Docker base image is CentOS 7.
- The bundled PostgreSQL database is used (
`DB_TYPE=local` ).
- Switch to using a Docker base image RHEL 8 or Debian.
- Switch to using a remote PostgreSQL database.
|
MetaDefender Core's NGINX web server will not start if weak cipher suites are used for HTTPS | On MetaDefender Core version 5.2.0 and later, OpenSSL 1.x has been replaced by OpenSSL 3.x within the product and its dependencies, including PostgreSQL and NGINX, to enhance security and address known vulnerabilities in OpenSSL 1.x. However, NGINX's implementation of OpenSSL 3.x in MetaDefender Core enforces strong encryption by rejecting all weak cipher suites. It only accepts "HIGH" encryption cipher suites as defined by OpenSSL https://www.openssl.org/docs/man1.1.1/man1/ciphers.html. This means ciphers based on MD5 and SHA1 hashing are no longer supported. Consequently, if you previously configured MetaDefender Core for HTTPS connections using a weak SSL cipher with your certificate, the service will not start due to NGINX's OpenSSL 3.x security enforcement. To prevent and remediate the issue before upgrading MetaDefender Core, please refer to the following resources: HTTPS Failure on MetaDefender Core 5.2.0 (or newer). |
TCP socket port exhaustion may cause the service trouble, preventing from restarting, and Workflow configuration corrupted | This issue affected MetaDefender Core (MD Core) version 5.15.0 and earlier and is enhanced starting from version 5.15.1. TCP socket port exhaustion might be triggered by other applications; for example, MetaDefender KIOSK v4.7.6.3514 (fixed in later releases). Consequently, MD Core may behave abnormally, corrupt its Workflow Configuration, and fail to restart. |
Workflow configuration fails to synchronize from OPSWAT Central Management to MetaDefender Core after creating a new Workflow template | This issue affects MetaDefender Core versions 5.17.0 and 5.17.1. Workflow configuration from OPSWAT Central Management will fail to synchronize to MetaDefender Core (MD Core) once a new Workflow template is created. To restore normal synchronization, the newly created Workflow template must be deleted. As a workaround for creating new templates on these affected MD Core versions, the Clone Workflow Template feature can be used as an alternative. |
Temporary files may persist if an OPSWAT AI Content Inspector scan is canceled | In version 5.19.0, canceling a scan while the OPSWAT AI Content Inspector engine is actively processing may leave intermediate files in the temporary directory. These files do not affect the current or any subsequent scan results.
|