<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-to-resolve-ssl-tls-errors-with-metadefender-core-webhook-cal -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:33:23.589867 -->

# How to Resolve SSL/TLS Errors with MetaDefender Core Webhook Callbacks?

This article applies to MetaDefender Core 5 releases deployed on Windows, Linux.

#### Issue:

When the webhook callback functionality is invoked, it may fail due to SSL/TLS errors. The core.log file will contain an error similar to the following:

(core.webhook) SSL/TLS failed, issue='The issuer certificate of a locally looked up certificate could not be found, No certificates could be verified'

#### Resolution:

**Windows**

Obtain the webhook server's SSL certificate chain (root CA, intermediate CA, and server certificate).

Open the Microsoft Management Console (mmc.exe).

Add the Certificates snap-in for the local computer.

Navigate to

`Trusted Root Certification Authorities > Certificates`

.Import the root, intermediate, and server certificates into the

`Trusted Root Certification Authorities`

store.Restart the OPSWAT MetaDefender Core service:

- OPSWAT MetaDefender Core

After the service restart, the trusted root certificates will be exported to a certificate located in the MetaDefender Core installation folder Data folder (by default`C:\Program Files\OPSWAT\MetaDefender Core\data`

).

**Linux**

By default, MetaDefender Core loads root CAs from the following locations:

`/etc/ssl/certs/`

`/usr/share/ssl/`

`/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem`

**Steps to import the certificates:**

**Debian/Ubuntu**

`sudo cp -f <cert_file> /usr/local/share/ca-certificates/`

`sudo update-ca-certificates`

`sudo systemctl restart ometascan`

**CentOS/RHEL**

`sudo cp -f <cert_file> /etc/pki/ca-trust/source/anchors/`

`sudo update-ca-trust enable`

`sudo update-ca-trust extract`

`sudo systemctl restart ometascan`

#### Steps to Reproduce:

Trigger a webhook callback to confirm that the SSL/TLS error occurs. Check the core.log for the SSL/TLS error.

#### Prevention:

Ensure the webhook server’s SSL certificate chain is trusted by the operating system by installing the intermediate or root certificate authorities in the local certificate store.

If Further Assistance is required, please proceed to log a support case or chatting with our support engineer.