<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-to-retrieve-the-crl-and-ocsp-urls-for-the-server-and-ica-cer -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:32:06.538957 -->

# How to retrieve the CRL and OCSP URLs for the Server and ICA Certificates?

**Purpose**

This document explains how to retrieve the **CRL (Certificate Revocation List)** and **OCSP (Online Certificate Status Protocol)** URLs from a server's SSL/TLS certificate and its Intermediate Certificate Authority (ICA) certificate, using a web browser. These URLs are often required for configuring firewall rules to allow outbound certificate validation.

**Steps for Chrome or Edge (similar steps for Firefox)**

**1. Open the Website**

Go to the website in question using Chrome or Edge (e.g., https://activation.dl.opswat.com, https://update.dl.opswat.com).

**2. View the Certificate**

- Click the
**site information icon**in the address bar. - Click
**“Connection is secure”**or**“Certificate is valid”**. - A
**certificate window**will appear.

**3. Examine the Certificate Chain**

- In the certificate window, go to the
**"Details"**tab (or similar, depending on the browser). - Select each certificate in the chain one by one (server, intermediate CA) to see the details.

**4. Find CRL and OCSP URLs**

For each certificate, search for the following fields::

**CRL Distribution Points****Authority Information Access**

These URLs are used by clients to check if a certificate has been revoked.

**5. Compile URLs for Firewall Whitelisting**

For each certificate in the chain, list all:

- CRL URLs
- OCSP URLs

**Example Whitelist Entries:**

`http://crl.example-ca.com/example-ca.crl`

`http://ocsp.example-ca.com`

Make sure these are accessible from inside your firewall, typically over **port 80 (HTTP)**.

**Notes**

- These URLs are not always present; absence means revocation may not be supported.
- Most revocation services (CRL/OCSP) are still served over
**HTTP**, not HTTPS. - If OCSP stapling is enabled on the server, external OCSP queries may be reduced—but firewall whitelisting is still recommended.

**Troubleshooting**

- If CRL/OCSP URLs are unreachable, try accessing them directly in the browser to test connectivity.
- Use browser developer tools (F12) and Network tab to watch OCSP requests in real time, if needed.

If **Further Assistance** is required regarding this topic, please proceed to log a **support case or chat with a support engineer**.