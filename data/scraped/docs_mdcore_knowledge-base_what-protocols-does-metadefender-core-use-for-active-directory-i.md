<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/what-protocols-does-metadefender-core-use-for-active-directory-i -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:28:31.661622 -->

# What Protocols Does MetaDefender Core Use for Active Directory Integration?

This article applies to all MetaDefender Core releases deployed on Windows/Linux systems.

## Overview

Metadefender Core integrates with Microsoft Active Directory (AD) using Lightweight Directory Access Protocol (LDAP). Unlike other authentication protocols such as Kerberos or NTLM, this application relies solely on LDAP/LDAPS for directory services and user authentication.

## Protocols Not Used

## Kerberos:

- Not used for authentication or Single Sign-On (SSO).
- No Kerberos ticket requests are generated.

### NTLM:

- Not supported.
- The application does not rely on NTLM hashes for authentication.

## Steps to Configure

Refer to the official documentation for detailed configuration steps: User directories

## Verify the Change

Refer to the official documentation for verification steps: User directories

## Troubleshooting

If you have queries, concerns, or issues regarding Metadefender Core AD integration methods, please open a Support Case with the OPSWAT team via phone, online chat, or form, or feel free to ask the community on our OPSWAT Expert Forum.

If **Further Assistance** is required, please proceed to log a support case or chatting with our support engineer.