<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-to-properly-configure-syslog-server-for-metadefender-core- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:30:22.215105 -->

# How to properly configure Syslog Server for MetaDefender Core?

This articles apply to all MetaDefender Core releases deployed on Windows and Linux.

Starting from **MetaDefender Core v5.13.0**, Syslog server configuration can be performed using REST API endpoints in addition to registry settings. While both methods are supported, **API-based configuration takes precedence**.

## Problem

When configuring MetaDefender Core to send log history to a logging system or a SIEM via syslog, you may encounter issues where the logs are not being sent, and unknown errors are logged without capturing scan history.

## Troubleshooting Steps

**1. Using REST API (Core v5.13.0+)**

**If you are using MetaDefender Core v5.13.0 or later**, it is recommended to configure syslog settings using the REST API. For more details on API usage, please refer to: POST - Forcefully apply the new syslog server configurationsAPI

**2. Using Registry (All Versions)**

If you’re using an older version or prefer registry-based configuration, ensure the following keys are correctly set under: `HKEY_LOCAL_MACHINE\SOFTWARE\OPSWAT\Metascan\logger`

.

`syslog`

: Your syslog server, in the format of`<protocol>://<syslog_server_address>:<port>`

.`syslog_level`

: Level of logging. Supported values are:`debug, info, warning, error`

.

Syslog typically uses the UDP protocol on port 514. Please ensure that the protocol (tcp/udp) matches what your Syslog server is configured to receive.

**After making the changes to the registry values, make sure to restart the service of MetaDefender Core, to apply the new configuration.**

Additionally, you can confirm that the MetaDefender Core server can reach the Syslog server over the specified port and protocol. You should ensure that no firewall or network ACL is blocking outbound traffic from MetaDefender Core.

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.