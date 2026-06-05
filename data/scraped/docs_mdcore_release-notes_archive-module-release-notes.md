<!-- source: https://www.opswat.com/docs/mdcore/release-notes/archive-module-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:07:52.760840 -->

# Archive Module release notes

## v7.8.2

Release date: 5/20/2026

- Supported X3P extraction and compression.
- Supported GPKG and TAZ compression.
- Supported VMDK files containing ISO data.
- Improved extraction for virtual disks with an empty main subfile by honoring the "Handle unsupported file systems" setting.
- Suppressed split archive errors for ZIP, CAB, CHM, and EXE_SFX files extracted from ZLIB streams.
- Fixed PST compression failure caused by duplicated input paths when "Reuse processing result" is enabled.

## v7.8.1

Release date: 4/15/2026

- New format support: SquashFS, Web Archive (WARC), BLZ.
- Enhanced EXE_SFX extractor to handle failure in case of extract-on-error is enabled.
- Added support for extracting data appended after the end of payload in XZ archives.
- Loosened header validation rules for CPIO extraction to improve compatibility.
- Loosened Linux data corruption rules in virtual disk extraction.
- Fixed EML extractor to use correct line endings (CRLF) for generated HTML content.
- Implemented extract-on-error support for PST extraction.
- Improved X12 EDI extraction performance.

## v7.8.0

Release date: 3/25/2026

- Added support for 3MF, Delta ESD, and BLZ file formats.
- Enhanced PST sanitization to better handle corrupted files.
- Optimized X12EDI processing by skipping unnecessary DATA file extraction.
- Preserved entry names during recursive compression.
- Resolved extraction issues by correctly distinguishing NSISBI from NSIS formats.
- Added “Extract on Error” support for 3DML extraction.
- Improved handling of GPKG files with empty or missing tables.
- Upgraded OpenSSL to version 3.6.1.
- Added support for Debian 13.

## v7.7.2

Release date: 2/5/2026

- Added support for YENC decoding.
- Improved handling of long file paths on Windows when extracting Inno Setup installers.
- Upgraded 7-Zip library to version 25.01.
- Better way to handle big OST extraction.

## v7.7.1

Release date: 1/14/2026

- Added support for UFDR, LZ4, Mozilla Archive (MAR).
- Added CIS Level 2 support for Windows Server 2022.

## v7.7

Release date: 12/16/2025

- Added support for combining split extracted files (requires MetaDefender Core 5.17.0 or later) for 7z, ZIP, RAR, TAR, WinZip, XZ, Clonezilla and GZ formats.
- Added the ability to enable or disable CLI extraction within workflows.
- Improved TAR extraction reliability, preventing failures when end-of-archive blocks are missing.
- Enhanced VMDK extraction to properly extract disk partitions.
- Fixed cases where EXE SFX extraction could fail.
- Improved 3DML, MSG compression.
- Reduced Linux package size by up to 35%.

## v7.6.2

Release date: 11/12/2025

- Added support for QCOW extraction.
- Refined the logic for handling
**"**Other extraction errors**"**to exclude**"**Unsupported format**"**errors in some cases. - Improved the Zlib extraction failure message.

## v7.6.1

Release date: 10/14/2025

Added support for MBR and EXT file formats.

Introduced a configuration option to control the UTF-8 name field in ZIP file format.

Added support for extracting encrypted ALZ/EGG archives using a provided password.

External command-line extraction improvements:

- Allow users to define an “encrypted archive” pattern in the json configuration file.
- A configuration to block files if command-line extraction fails.

Migrated the Skip File Type setting from Global to Workflow.

Enhanced extraction for AppImage and Inno Setup files.

## v7.6.0

Release date: 9/24/2025

- Support extracting data after the end of payload for zlib.
- Enhance error message structure in case of extraction failure.
- Support extracting on GUID Partition Table (GPT).
- A configuration option to handle unsupported file system for VMDK.
- Handle legacy time format in MBX to avoid extraction loops.

## v7.5.2

Release date: 8/20/2025

- Added support for new file types: AppImage, LZIP.
- Support extracting disk images without partitions in VMDK.
- Support extracting data after the end of the payload in Gzip and Tar.
- New configuration option to handle extraction failures caused by "data after the end of payload."
- Improved logic for detecting invalid file structures.
- Improved logic for detecting timeout.
- Enhance B3DM extraction.
- Added support for Windows Server 2025 and Ubuntu 24.04.

v7.5.1

Release date: 7/23/2025

- Support new file types: ASAR.
- Enhance zip-based extraction to respect the encoding setting.
- Upgrade WinRAR module to 7.11.
- Support running an external command line to extract files.

## v7.5

Release date: 6/25/2025

Support new file types: PYZ.

Improve Inno installer extraction:

- Support versions newer than 6.4.0.
- Fix failure extraction in some cases.

Upgrade .NET to version 8.

## v7.4.2

Release date: 5/27/2025

- Support new filetype extractions: VHDX, Inno Installer.
- Support Amazon Linux 2023.

## v7.4.1

Release date: 4/23/2025

Classify the archive failure categories be more meaningful:

- Separate "Others" with "Other extraction errors".
- Rename "General unextractable errors" to "Not extractable".

Support MDZIP extraction.

Enhance PEM extraction.

## v7.4

Release date: 3/27/2025

Support configurations in workflow (requires MD Core 5.14.0)

Support extraction of new file types:

- PCAP with http, ftp, imap protocol.
- Multipart SMIME
- SCDOC

Stabilize PST compression.

Improve EML compression:

- Preserve entry names, attachment properties for TNEF attachments.
- Handle extraction of empty files.

Add a new configuration allowing content-type mismatching with EML email body.

Improve compression of archive files containing many child files.

Enhance MSG extraction.

Fix inconsistent behaviors for handling password protected files.

## v7.3.2

Release date: 2/19/2025

- Support YZ1 extraction.
- Support extracting object attachments in TNEF extraction.
- Support re-encoding Base64 files in compression.
- Handle EML files with special characters in attachment filenames.
- Fix incomplete MSG extraction and prevent adding random bytes to files.
- Enhance extraction of P7M file with PEM format.

## v7.3.1

Release date: 1/15/2025

- Handle "object attachment" in TNEF file.
- Resource optimization in case of extracting large ZLIB file.
- Improve MSG compression method.
- Improve MBX extraction.
- Enhance "extract on error" with encrypted archive files.

## v7.3

Release date: 12/18/2024

- Support extracting concatenated ZIP, ZILB.
- Support ISO-8859-8 charset attachment file name in EML.
- Support Rocky Linux 9.4, Debian 12.
- Enhance extracting password-protected files.
- Improve for PST, MSG:
- Add tombstone files for blocked files.
- Improve compression feature.

## v7.2.2

Release date: 11/21/2024

- Support new file types: 3DML, NAR, Git Pack, NUPKG, SXC, SXD, SXF, SXI, SXM, SXW, STC, STD, STI, STW, HPWX, PBIT, PBIX, SHOW, SLDM, SLDX, VVSX, VSIX, PPAM.
- Support UTF-8 password for ZIP.
- Return more details about extraction errors.
- Enhance PST sanitization.
- Digitally sign all binary files.

## v7.2.1

Release date: 10/8/2024

- Support decoding base64 file.
- Handle encoding in CAB extraction and compression.
- Enhance CPIO extraction.

## v7.2

Release date: 9/18/2024

- Support new file types: TNEF, MBX, MHT, GPKG, B3DM, DWF and DWFX.
- Support the APFS file system in DMG extraction.
- Enhance canceling timed out extraction and cleaning up temp files in high load situation
- Improve VMDK extraction by using less disk space and increasing speed.

## v7.1.2

Release date: 8/19/2024

- Fix high memory consumption when extracting MS Office files.

## v7.1.1

Release date: 7/24/2024

- Support VMDK and ZSTD extraction.
- Enhance cancelation of extraction in high-load situations.
- Fix EXE_SFX hang issue.

## v7.1

Release date: 6/25/2024

- Support new file types: RAW with HFS format and MS OLE.
- Support GPG asymmetric keypair extraction (users must provide the GPG Home directory with all keys imported).
- Support skipping extraction for selected file types.
- Add a new configuration to allow extract on error.
- Support Ubuntu 22.04.

## v7.0.1

Release date: 4/10/2024

- Fix SMINE extraction failures in some cases.

## v7.0

Release date: 4/3/2024

- Support RAW (with NTFS Format), git-bundle, RIBC, and SMINE extraction.
- Enhance UTIB, TAR, and split Encase extraction.
- Upgrade 7z to a newer version.
- Upgrade the engine to .NET 6.

## v6.5.3

Release date: 3/6/2024

- Enhance EXE SFX file extraction.
- Auto-handling entry name encoding (supported UTF-8 and SJIS).
- Upgrade third-party libraries to resolve a vulnerability.

## v6.5.2

Release date: 2/5/2024

- Fix the temp file issue when extracting PST files.
- Fix failures when extracting .DOSSZIE file.

## v6.5.1

Release date: 1/16/2024

- Enhance VHD extraction.

## v6.5

Release date: 12/18/2023

- Support new file types: e-dossier (ES3), System Center Configuration Manager Package Files (PCK)
- Better handling big archive files.
- Password protected PST file is handled properly.
- Enhance temp file generation.

## v6.4.1

Release date: 11/9/2023

- Better handling EML file encoding in base64

## v6.4

Release date: 9/27/2023

- New configuration to preserve children filenames inside an archive file when creating a sanitized file
- Support UUencoding (UU, UUE), Encase (E01) extraction

## v6.3.2

Release date: 8/9/2023

- Fixed the compression issue when creating a RAR file with Chinese file path

## v6.3.1

Release date: 7/19/2023

- Support extraction for non-standard VIB files

## v6.3

Release date: 6/20/2023

- Support CRX extraction
- Return an attribute to identify whether a file is encrypted or not after decrypted (requires MetaDenfender Core 5.5.1+)
- Improve logging
- Enhance PST extraction and compression
- Support hiding internal data for Archive sanitization

## v6.2.3

Release date: 5/22/2023

- Remove an unnecessary file (MSG.data) when extracting MSG files

## v6.2.2

Release date: 4/25/2023

- Improve SFX extraction performance
- Support EXE_SFX decryption

## v6.2.1

Release date: 3/29/2023

- Fix performance degradation in MetaDefender Core 5.4.1+
- Remove the UNC path in the PidLidReminderFileParameter when sanitizing a MSG file (CVE-2023-23397)

## v6.2

Release date: 3/15/2023

Support extraction for new file types:

- XPI (Firefox extension)
- VTAR (VM Tar)
- GPT-styled VHD
- Split CAB

Preserve filename/folder name encoded with special encodings like Shift-JIS

Improve HFS extraction

## v6.1.1

Release date: 2/13/2023

- Support extraction for SPF
- Fix engine failed to decrypt/encrypt MS Office, PST dues to long socket path

## v6.1.0

Release date:1/11/2023

- Support extraction for UTIB
- Enhance extraction and compression of EML
- Enhance extraction of Self-Extracting Executable files
- Preserve symlinks in TAR compression

## v6.0.2

Release date: 12/2/2022

- Preserve MS Word/Excel format during decryption
- Support retaining password for DOT, DOCM, DOTX, DOTM, XLT, XLSM, XLTX, XLTM, XLSB

## v6.0.1

Release date: 10/27/2022

- Enhance EML extraction
- Support UTF-8 password when decryption PDF files
- Support log level configuration
- Support APK with Signature Scheme v2

## v6.0

Release date: 10/5/2022

- VC++ Redist 2017 is required
- Dependency check when intializing the engine

## v5.3.28

Release date: 9/7/2022

- Add line breaks when writing base64 encoded data in EML

## v5.3.27

Release date: 8/22/2022

- Enhance password-protected decryption for Excel file

## v5.3.26

Release date: 8/1/2022

- Enhance PST, HFS extraction

## v5.3.25

Release date: 6/29/2022

- Handle password with special characters in PGP decryption

## v5.3.24

Release date: 5/30/2022

- Support non-ASCII password in PDF decryption
- Support archive extraction with Copy method
- Improve archive extraction on Linux

## v5.3.23

Release date: 4/27/2022

- Fix a bug that causes a failure when extracting a big TAR file
- Support non-ASCII password in PDF decryption

## v5.3.22

Release date: 3/28/2022

- Support extracting password protected workbook/worksheet in Excel
- Support extracting password protected POT, PPS, XLT

## v5.3.21

Release date: 2/10/2022

- Support ALZ, EGG encrypted extraction
- Enhance service behavior when missing .NET Core
- Support re-encrypt MS Office files on Linux

## v5.3.20

Release date: 1/5/2022

- Better timeout handling when recombine EML, MSG, PST
- Fixed temp files left over after scanning
- Enhance Power Point password decryption
- Support Email Template (OFT) extraction

## v5.3.19

Release date: 11/22/2021

- Support EGG extraction
- Improve VHD extraction
- Support to extract PGP/GPG file with password (need to have preinstalled GnuPG)

## v5.3.18

Release date: 9/29/2021

- Support MS Office 2003 decryption
- Support JMOD, MSIX, APPX file extraction
- Improve temp file handling

## v5.3.17

Release date: 8/17/2021

- Support IPA, OST file format extraction
- Fixed crashed issues when processing PST file.
- Fixed EML issues: broken attachments after extracting, attachment file names are changed
- Fixed MSG sanitization failure when attachment filenames contain special symbols

## v5.3.16

Release date: 7/8/2021

- Support X12EDI, TBWX file format extraction

## v5.3.15

Release date: 6/3/2021

- Improve the logic counting files before extracting
- Improve cleanup mechanism

## v5.3.14

Release date 4/27/2021

- Better handling in case of exceeded archive file size
- A better error message
- Crash issue

## v5.3.13

Release date: 4/8/2021

- Fixed high CPU usage on Ubuntu

## v5.3.12

Release date: 4/1/2021

- Support password extraction for PST and MS Office files on Linux (require .NET Core to be installed)
- Retain password protection for RAR
- Improve DMG extraction on Linux

## v5.3.11

Release date: 3/3/2021

- Update the module to use VS C++ 2017
- Improve password-protected PDF, .DMG extraction

## v5.3.10

Release date: 1/27/2021

- Support PST extraction (on Windows only)
- Return an error message when decrypting a PDF file with a wrong password

## v5.3.9

Release date: 12/29/2020

- Enhance NSIS extraction

## v5.3.8

Release date: 12/1/2020

- Fixed a hang issue when canceling an extraction request

## v5.3.7

Release date: 10/26/2020

- Better MSG extraction and compression

## v5.3.6

Release date: 10/1/2020

- Support CHM extraction
- Support detect partial extraction for ALZ, ACE

## v5.3.5

Release date: 9/1/2020

- Improve ACE, CAB extraction

## v5.3.4

Release date: 8/8/2020

- Support ACE extraction

## v5.3.3

Release date: 7/6/2020

- Better split encrypted archive handling
- Improve 7z self-extracting archive processing

## v5.3.2

Release date: 5/20/2020

- Support ALZip (ALZ) extraction
- Better EML, MSG extraction