<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/what-is-the-impact-of-upgrading-metadefender-core-from-version-5 -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:28:55.613429 -->

# What is the impact of upgrading MetaDefender Core from version 5.12.0 to 5.13.3?

**Overview**
This article provides insights into the key changes introduced in MetaDefender Core version 5.13.3, including updates to OpenSSL, NGINX, PostgreSQL, and the Syslog Server Configuration API. It also explains the potential impact on current operations and offers recommendations to ensure a smooth upgrade process.

**Affected Versions**

**From**: MetaDefender Core 5.12.0**To**: MetaDefender Core 5.13.3

**Key Changes and Their Impact**

**1. OpenSSL and NGINX Security Enhancements
Upgrade Details:**

MetaDefender Core’s NGINX web server will no longer start if weak cipher suites are configured for HTTPS.

Starting with MetaDefender Core 5.2.0, OpenSSL 1.x has been replaced with OpenSSL 3.x.

This upgrade affects key dependencies like PostgreSQL and NGINX, enhancing security and resolving known vulnerabilities.

**Impact on Operations:**

- If weak ciphers are present in your SSL/TLS configuration, the NGINX service will fail to start post-upgrade.
- To avoid downtime, review and update SSL/TLS configurations to remove any unsupported cipher suites prior to upgrading.

**2. Syslog Server Configuration API Enhancements
Upgrade Details:**

Starting in MetaDefender Core 5.13.0, API support has been added for configuring Syslog settings.

Previously, these settings could only be managed via the GUI.

The new API provides greater control and flexibility for managing log forwarding and system monitoring.

**Impact on Operations:**

- Existing Syslog configurations remain unaffected.
- However, if changes are made using the new API, the MetaDefender Core service must be restarted for changes to take effect.

**Recommendations Before Upgrading**

**Review SSL/TLS Cipher Configuration**Ensure no weak cipher suites are used in your HTTPS settings to prevent NGINX startup failures. Refer to the official release notes for supported ciphers.**Backup Current Configurations**Back up all configuration files, SSL certificates, and log settings before performing the upgrade.**Test in a Staging Environment**Validate compatibility and stability by deploying the new version in a test environment prior to production rollout.**Restart MetaDefender Core Service if API Changes Are Made**Any Syslog configuration updates made through the API require a service restart to take effect.

**Conclusion**
MetaDefender Core 5.13.3 brings critical security improvements and greater flexibility for log management. While the upgrade is backward-compatible, reviewing your current configurations and preparing accordingly will help ensure a smooth transition.

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.