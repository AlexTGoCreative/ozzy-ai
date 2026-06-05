<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/why-are-metadefender-core-syslog-messages-flagged-as-non-complia -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:34:15.732771 -->

# Why are MetaDefender Core Syslog Messages Flagged as Non-Compliant with certain syslog standards?

This article applies to MD Core version 5.16.0 and older

**Issue:**

Syslog messages sent from MetaDefender Core are flagged in Wireshark as “Message conforms to neither RFC 5424 nor RFC 3164; trailing data appended.” This raises a question regarding whether MetaDefender Core syslog output complies with RFC 3164 or RFC 5424 standards.

**Symptoms:**

When capturing syslog packets from MetaDefender Core, user may observe the following:

`[Expert Info (Note/Protocol): Message conforms to neither RFC 5424 nor RFC 3164; trailing data appended] Example: Syslog message: DAEMON.INFO: 2025-06-24T03:35:53Z localhost.localdomain MSCL[156240] Send additional configs, configs='{"SysLog": … }' The syslog message includes a <pri> header (e.g., <30>) followed by timestamp and hostname, but deviates from the strict structure defined in the RFCs.`

**Resolution:**

Syslog messages in current versions of MetaDefender Core (≤ 5.16.x) may not fully comply with certain syslog format standards.

Enhanced support for fully compliant syslog messages is planned for upcoming versions.

There is no immediate workaround. The syslog output can still be parsed or processed by most syslog collectors as long as they are configured to handle non-strict message formats.

If you require further assistance, please follow these instructions on How to Create Support Package?, before creating a support case or chatting with our support engineer.