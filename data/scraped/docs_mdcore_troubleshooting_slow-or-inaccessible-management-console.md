<!-- source: https://www.opswat.com/docs/mdcore/troubleshooting/slow-or-inaccessible-management-console -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:06:57.187008 -->

# Slow or Inaccessible Management Console

## Overview

This guide addresses performance issues with the MetaDefender Core Web Management Console, including slow loading times and unresponsive pages.

## Symptom

The Web Management Console loads significantly slower than normal

The following pages may become unresponsive or fail to load: Workflow Management:

- Workflows
- Templates
- Security Zones

Check the Nginx logs for related error messages or timeouts

Bash

` `

`2025/09/09 13:10:11 [error] 12300#7664: *534823988 lua tcp socket read timed out, client: ::1, server: , request: "GET /admin/schema HTTP/1.1", host: "localhost:8008", referrer: "http://localhost:8008/"`

`2025/09/09 13:10:11 [error] 12300#7664: *534823988 [lua] resourcehandler.raw:0: (): resourcehandler.lua: Request timed out: timeout, client: ::1, server: , request: "GET /admin/schema HTTP/1.1", host: "localhost:8008", referrer: "http://localhost:8008/"`

`::1 - - [09/Sep/2025:13:10:11 +0530] "GET /admin/schema HTTP/1.1" 500 47 "http://localhost:8008/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0" 150.000`

- The scan function (API POST /file) responds slowly or becomes unresponsive

## Remediation

- This is a know issue of MetaDefender Core version 5.12.0
- The issue has been fixed from MetaDefender Core version 5.13.2
- The customer is recommend to upgrade MetaDefender Core to latest version (as of writing is
**5.15.2**) to fix the issue