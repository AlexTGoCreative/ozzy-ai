<!-- source: https://www.opswat.com/docs/mdcore/troubleshooting/metadefender-core-service-failed-due-to-weak-cipher -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:07:07.876837 -->

# HTTPS Failure on MetaDefender Core 5.2.0 (or newer)

This article is only applicable when:

- You are planning to use (upgrade / fresh install) MetaDefender Core 5.2.0 or newer
- You already currently configured HTTPS (or planning to do so) on MetaDefender Core

## Issue symptom

After upgrading to MetaDefender Core 5.2.0 or newer (or runing a fresh install), found that MetaDefender Core service failed to start with following error found in NGINX log (for example):

` `

`“38772#35704: SSL_CTX_use_certificate("C:/Windows/Temp/ometascan/https_cert.pem") failed (SSL: error:0A00018E:SSL routines::ca md too weak)”`

## Reason

Starting MetaDefender Core version 5.2.0, the OpenSSL 1.x is replaced by OpenSSL 3.x within the product and other dependencies (PostgreSQL, NGINX) as a security improvement, and prevent potential known vulnerabilities on OpenSSL 1.x.

NGINX's OpenSSL 3.x on MetaDefender Core has the enforcement in place to reject all very weak cipher suites, and prevent being exploited. It only accepts "HIGH" encryption cipher suites https://www.openssl.org/docs/man1.1.1/man1/ciphers.html (MD5 and SHA1 hashing based will not be accepted as well).

As a result, if you already configured MetaDefender Core for HTTPS connection, but using a weak SSL cipher in your certificate, then MetaDefender Core will not be able to start due to NGINX's OpenSSL 3.x enforcement.

## Solution

### If you are already on MetaDefender Core 5.2.0 or newer, and hitting the issue

The ultimate solution is replacing your certificate used for HTTPS configure by another strong one, so that it is created based on strong cipher suites to strenghthen your own security.

If that is not possible now, then following steps below as a workaround:

- Just in case you currently configured HTTPS on MetaDefender Core UI (and being blocked to make any change because MetaDefender Core service is not running): you need to disable HTTPS configuration on MetaDefender Core using a dedicated CLI tool - see details at HTTPS Configuration Removal Tool
- Switch to configure HTTPS on MetaDefender Core via a NGINX custom config file - Enabling HTTPS
- On NGINX custom config file, specify that NGINX should accept any ciphers except ones with no encryption, or no authentication (
`ssl_ciphers ALL:!aNULL;`

)

`ssl on;`

`ssl_certificate "C:/Program Files/OPSWAT/Metadefender Core/nginx/your.crt";`

`ssl_certificate_key "C:/Program Files/OPSWAT/Metadefender Core/nginx/your.key";`

``

`ssl_ciphers ALL:!aNULL;`

### If you are not on MetaDefender Core 5.2.0 or newer yet

Before you decide to upgrade your MetaDefender Core to the version 5.2.0 or newer, check and ensure you are using a strong cipher suite for HTTPS connection with your certificate - Ref: https://helpcenter.gsx.com/hc/en-us/articles/207831828-How-to-identify-the-Cipher-used-by-an-HTTPS-Connection

Otherwise you might need to follow workaround steps mentioned above to force NGINX to accept any ciphers