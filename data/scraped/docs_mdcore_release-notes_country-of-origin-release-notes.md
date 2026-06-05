<!-- source: https://www.opswat.com/docs/mdcore/release-notes/country-of-origin-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:07:30.284686 -->

# Country of Origin release notes

## v2.2.1

Release date: 5/20/2026

- Added support Windows 11 24H2, 25H2, Rocky Linux 10.

## v2.2.0

Release date: 3/25/2026

- Supported Inno Setup Installer.
- Upgraded OpenSSL to version 3.6.1.
- Added support for Debian 13.

## v2.1.0

Release date: 9/24/2025

- Do not return "Allow" for Country filter.

## v2.0.1

Release date: 8/6/2025

- Support CAB file type.
- Support digital signature validation for CAB, EFI, EXE SFX file format.
- Block files in case of failing integrity check.

## v2.0

Release date: 7/7/2025

- Support Ubuntu 22.04 CIS level 2.
- Validate the file integrity against the digital signature.

## v1.2.0

Release date: 6/25/2025

- Allow user to input Trusted root certificates to validate against a digital signature.
- Drop support CentOS 7/RH 7/Debian 10/Ubuntu 20.

## v1.2.1

Release date: 12/1/2024

- Digitally sign all binary files.

## v1.0

Release date: 3/20/2024

- Support block/allow by countries.
- Support block/allow by vendor.
- Support file types: DLL, EXE, EXE_SFX, EFI, and MSI.