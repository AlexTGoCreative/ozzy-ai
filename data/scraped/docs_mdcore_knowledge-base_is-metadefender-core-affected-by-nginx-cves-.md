<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/is-metadefender-core-affected-by-nginx-cves- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:29:22.119916 -->

# Is MetaDefender Core affected by NGINX CVEs?

- This article applies to MetaDefender Core prior to 5.18.0

**Issue**

### Impact assessment for six NGINX vulnerabilities against MetaDefender Core:

- CVE-2026-42945: Not affected. MD Core’s rewrite rules do not use nested or overlapping capture groups, capture substitutions such as $1/$2, or the vulnerable rewrite patterns described in the advisory.
- CVE-2026-42946: Not affected. MD Core does not use the scgi_pass or uwsgi_pass modules in the NGINX configuration.
- CVE-2026-40460: Not affected. MD Core does not use the HTTP/3 QUIC module.
- CVE-2026-42926: Not affected. The NGINX configuration does not use proxy_http_version 2.
- CVE-2026-40701: Low risk. The vulnerability only affects deployments using specific mTLS and OCSP validation settings in NGINX. Please verify whether ssl_verify_client on|optional and ssl_ocsp on are enabled in the active NGINX configuration.
- CVE-2026-42934: Not affected. The vulnerable configuration combination (charset/source_charset/charset_map together with proxy_pass and proxy_buffering off) is not used in the NGINX configuration.

**Resolution**

- Upgrade to MetaDefender Core 5.19.0 or later for NGINX 1.30.1.
- If you must stay on 5.18.0 temporarily, please log a support case

If you require further assistance, please follow these instructions on How to Create Support Package?, before creating a support case or chatting with our support engineer.