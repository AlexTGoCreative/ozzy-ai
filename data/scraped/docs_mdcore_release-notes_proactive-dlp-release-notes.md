<!-- source: https://www.opswat.com/docs/mdcore/release-notes/proactive-dlp-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:05:54.755907 -->

# Proactive DLP release notes

## v3.3.1

Release date: 5/18/2026

- Added FIPS support and enhanced structural PDF validation capabilities
- Improved PII AI model performance and overall detection accuracy
- Resolved multiple stability and reliability issues
- Fixed several scanning and detection issues, including Excel AI scanning handling

## v3.3.0

Release date: 4/21/2026

- Added support for resizing text that is too large or too small
- Added capability to highlight detected hits
- Added support for redacting text that is too large or too small
- Introduced threshold configuration for large font detection
- Introduced threshold configuration for cropped image detection
- Added support for font size and invisible text detection in PowerPoint files
- Extended support to WordArt and Shapes in Excel files
- Fixed an issue with incorrect redaction positioning on rotated PDF pages

## v3.2.0

Release date: 1/26/2026

- Custom regex TSV files are now shown on a pop-up, so the user can decide which defined regexes they want to use
- Generic phone number detection
- E-mail address detection with both regex and AI methods
- Electronic Authorization Number detection with both regex and AI methods
- Name detection improvements utilizing AI

## v3.1.0

Release date: 11/05/2025

Security and privacy regulations such as GDPR and PHI can now be configured

DLP now supports scanning filenames

Users can choose whether to anonymize private tags and other user-defined tags in DICOM files

Multiple TSV files can now be added for custom regex scanning

The OCR section has been moved to the root configuration level, and language selection is now available

- OCR now supports English, Hebrew, Hindi, French, Italian, Arabic, and Japanese, and can also detect MRZ (Machine Readable Zone) data from ICAO-compliant ID cards.

Added text-encoding support for French, Italian, Arabic, and Japanese

## v3.0.0

Release date: 07/14/2025

- Tagging system - DLP is now able to add metadata tags to processed PDF, Word, Excel, PowerPoint files and images
- AI scan is now available for Word and PowerPoint files as well
- DLP supports redaction for Json files from now on
- MDB and ACCDB file types are now supported for scanning
- Indian PAN and Aadhar cards are added as pre-defined options

## v2.23.1

Release date: 05/12/2025

- Added support for Amazon Linux 2023 and Oracle Linux
- Resolved DLL loading issue on Windows Server 2016
- Fixed failure in NSFW scan under specific conditions
- Improved stability and error handling for large PDF scans

## v2.23.0

Release date: 04/08/2025

- It is now possible to HASH the hits in the output document for Word, PDF and plain text files
- Toxic text detection is now available in more languages, including French, Spanish, Turkish, Italian, Russian, and Portuguese
- More NSFW categories introduced, including guns and violence
- More PIIs are available via AI scanning, including NHS and UK Electoral Roll Number
- Resolved an issue where enabling AI scan previously disabled regex scan. Both scans now function concurrently

## v2.22.1

Release date: 02/05/2025

- DLP no longer uses "/tmp" directory in order to fully support non-root Docker
- Result UI page became more comprehensive, detailing scan types and processing results
- Switching on AI scan won’t interfere with other features anymore

## v2.22.0

Release date: 01/13/2025

Intentional Leakage Detection

**Small Font Size Recognition**: Detect intentional data leaks by finding text hidden using very small font sizes in PDF, Word, and Excel files**Invisible Text Recognition**: Detect intentional data leaks by identifying hidden text where the text color and background color are the same or very similar in PDF, Word, and Excel files.

New predefined sensitive information types are now supported for detection and redaction:

- Turkish Passport Numbers
- Turkish Phone Numbers
- Turkish ID Numbers (TC Kimlik)
- IMEI/IMEISV (International Mobile Equipment Identity)
- Israeli ID Numbers

Fixed an issue where AI scanning disrupted regex-based scanning

## v2.21.1

Release date: 11/04/2024

- Debian 12 and Rocky Linux 9.4 are now supported
- AI scan failure in case a PDF file has an empty page is now fixed
- Hit validation failure when only a TSV file is used for PDLP is now fixed

## v2.21.0

Release date: 10/02/2024

Anonymization is now supported for PCAP and PCAPNG files

PII detection using Artificial Intelligence

- Supported PII: Driver’s license, passport number, and national ID number
- Languages Supported: English, French, Spanish, German, Italian, and Portuguese
- Supported File Types: PDF and text files

Detection policy update fixed

## v2.20.0

Release date: 07/25/2024

Support the .jp2 file type.

New predefined sensitive information types are now supported for detection and redaction:

- Australia Medicare Number
- Australia Company Number
- Australia Business Number
- Australia Tax File Number
- UK NHS Number

The localization select list in the UI has been replaced with a country-specific sensitive information select list.

The US-SSN has been divided into US-ITIN and US-SSN (they are still referred to as SSN in the result JSON).

The JP-SSN has been renamed to JP-MYNUM (it is still referred to as SSN in the result JSON).

## v2.19.1

Release date: 06/13/2024

- Improve PDF metadata dictionary processing.
- Detection Policy improvements include: precedence, new operators, and parenthesis usage.
- Custom regex file updates no longer require an engine restart.
- Fix date regex issue in Excel files using TSV files.

## v2.19.0

Release date: 04/11/2024

- Support multi-frame GIF files with OCR.
- Support .loc files, FDF files, and Acrobat Forms.
- Support recursive PDF processing (for embedded PDF only).
- Improve Microsoft Office 2007 object processing, including linked objects, tracked changes, background images, SmartArt.
- Improve PDF stamp annotation and form processing.
- Fix watermark scan bug.

## v2.18.1

Release date: 02/15/2024

- Implement more sophisticated TSV file handling related to the “
**custom regexes from file**” feature. - Refine detection of SWIFT codes, reducing both false positives and false negatives.
- Resolved interruption issues related to hit limits during embedded image processing.
- Removed duplicate results that occur when using the best quality OCR.
- Fix the independence of redact settings from TSV file loading.
- Fix a memory leak

## v2.18

Release date: 01/04/2024

Importing custom regular expressions from a file is now supported.

New predefined sensitive information types are now supported for detection and redaction:

- ABA Routing Number
- U.S. Bank Account
- International Banking Account Number (IBAN)
- International Securities Identification Number (ISIN)
- SWIFT Code

OCR capabilities have been improved.

SSE4.2 is now also accepted by Proactive DLP (in addition to SSE4.1) as the required CPU instruction set for OCR.

File metadata handling for scan requests have been improved.

Proactive DLP’s UI workflow settings are now unified across all officially supported MetaDefender Core versions.

Proactive DLP’s UI workflow settings for detection have been redesigned to provide a more compact look.

## v2.17

Release date: 10/20/2023

Announcing Document Identification

Not Safe For Work (NSFW)

- Detect "Not Safe For Work" content in text and images
- Redact textual hits and blur images with NSFW content

Personal document classification

- Detect personal ID on images

Detection of Generic Password and Generic API Key secrets have been improved

## v2.16

Release date: 07/18/2023

Announcing DICOM Anonymization:

- Anonymize patient information according to the Basic Attribute Confidentiality Profile
- Remove sensitive burned-in annotations from DICOM images

Patterns for US SSN numbers have been updated

Fixed issue when DLP engine crashes when files are sent for scanning right after engine initialization

## v2.15.1

Release date: 05/22/2023

- Improved generic password and generic API token detection (secret detection)
- Fixed issue when processing of large text files took very long time
- Fixed issue when CCN hits contained extra character at the end
- Fixed sensitive info substitution in hyperlinks
- Fixed issue when PDLP was unable to detect certain software secrets in XML files
- Allowlist and custom validators now properly working with XML files

## v2.15

Release date: 03/31/2023

Support more secrets:

- Generic passwords
- Generic API tokens
- PostgreSQL credentials
- MYSQL credentials

DOCM and XLSM file types are now supported in scanning

Redact sensitive information in CSV and XML files

Text substitution can be configured instead of redaction in the following document types:

- MS office documents (word, excel, slides)
- PDF files
- Text files

Fixed issue when valid hits can be invalidated due to a bug

Fixed issue with duplicate character validator that resulted in more false positive

## v2.14

Release date: 12/19/2022

Support more secrets:

- Private keys (PEM, PPK)
- IBM Cloud key
- IBM API Connect Credentials
- IBM COS HMAC Credentials

Reorganize the workflow configurations

Improve MS Word processing to reduce false positive detection

Fixed issue when valid hits could be lost when other hits are redacted during PDF processing

Fixed log retention

## v2.13.1

Release date: 11/2/2022

- Allowlist feature has been added to all sensitive info types
- Log retention period can now be configured from the engine configuration
- Encoding detection can be configured in the Workflow rule setting instead of the engine configuration
- Fixed issue where DLP engine updates were failing permanently due to unrecognized OS
- Fixed issue when encoding detection settings were lost during configuration export and import
- Fixed issue where an empty regular expression field in the workflow rule settings caused DLP engine update to fail permanently

## v2.13

Release date: 9/31/2022

Secret detection in text files supporting AWS, Azure and GCP secrets

New optional validators for sensitive data

- Exclude prefix
- Exclude suffix
- Exclude beginning characters
- Exclude ending characters
- Duplicate characters (only for custom regexes)

DLP log level is now selectable in the engine configuration

External dependencies are checked before engine initialization

Some descriptions have been streamlined in the workflow rule settings

Fixed issue when local scan fails on read-only PDF files

Fixed issue when SSN localization could be saved without value

## v2.12

Release date: 7/5/2022

- Improved PDF processing speed
- General improvements in performance due to update from .NET Core 3.1 to .NET 6.
- Improved OCR capabilities
- Improved product logging to enhance product diagnostics
- Fixed issue when the quality of jpeg images dropped after metadata removal
- Fixed issue when DLP fails to process EMF images embedded in a document
- Fixed issue when embedded files can't be opened during recursive PPT processing
- Fixed issue when xls files could not be processed during MD Core local scan

## v2.11.1

Release date: 5 /11/ 2022

- A configuration to choose a default fallback encoding
- Optimize system resource usage for PDF processing
- PDF Watermark: Added line breaks to long texts

## v2.11

Release date: 3/30/2022

- Support watermark feature for MS Word
- Allow the customers to set certainty for the regular expression
- Support encoding detection (for Japanese, Hebrew and UTF8 encodings)
- Processing all annotation object types in PDFs
- Processing all stamp object types in PDFs
- Keeping the original image quality for output files when removing Metadata

## v2.10.1

Release date: 2/16/2022

- Enhance PPT file processing
- Improve metadata processing for image file types
- Fix line break issue with DOC/DOCX when applying watermark
- Fix metadata removal with TIFF file format
- More plain text file support
- Improved image processing (performance)

## v2.10

Release date: 12/22/2021

- Add more supported encodings (for Email Security Gateway use case)
- A configuration to set limit file size per workflow
- Scan and remove Metadata recursively
- Support processing cropped images for XLS/XLSX/PPT/PPTX
- Fixed memory leak issue

## v2.9.1

Release date 12/1/2021

- Detection Policy is available on MetaDefender Core v5 or newer
- A configuration to allow a file if it is redacted (MetaDefender Core v5 or newer)
- Optimize memory usage
- Better encode handling between Email Security Gateway and Proactive DLP

## v2.9

Release date 10/13/2021

Support watermark EMF/WMF/SVG

Detect and Redact sensitive info in several objects

- MS Excel sheet name
- Defined Name object in MS Excel
- Image alternative text in MS Office
- Comment Author in MS Word and Excel
- Header and Footer in MS Word and Excel
- Track changes in MS Word and Excel
- Alternative images in PDF
- Form fields in PDF

Improve recursive processing

- Support RTF as an embedded file
- More details about hit location

Upgraded Qt framework to version 5.15.2

## v2.8.1

Release date: 8/18/2021

- Improve performance for several file types (MS Excel, text, etc ...)
- Fix MS Excel redaction failure in some cases

## v2.8

Release date: 7/8/2021

- A configuration to remove embed objects if recursive processing fails
- Fixed FILE SIZE LIMIT configuration issue
- Fixed embedded image OCR processing
- Improve large plain text file processing

## v2.7.1

Release date: 6/3/2021

- Support unlimited depth and number objects in recursive document processing
- Allow users to set a limit number of returned sensitive info
- Added "," to the default delimiter list
- Improve Excel processing
- Fixed Chinese regular expression in text files (CSV, TXT, ...)
- Fixed missing keyword configuration when upgrading to DLP 2.7

## v2.7

Release date: 4/27/2021

- Drop supporting MetaDefender Core older than 4.17.1
- Recursive scan and redaction of embedded files in MS Office files
- Localization support for Japanese SSN
- Support watermark, metadata detection, OCR for BMP format
- Support "Delimiter" as an optional validator
- Context detection around hits in PDF files has been improved
- Chart detection and redaction has been introduced in Excel
- Improve OCR detection quality
- Improve redaction function for MS Word files

## v2.6.1

Release date: February 8, 2021

- Fix detection issue when an empty cell has a comment (Excel)
- Improve MS Office validation in some regular expression cases

## v2.6.0

Release date: January 11, 2021

- Process the hidden areas in a cropped image (DOCX, DOC)
- Support OCR for standalone image file types (JPG, PNG, TIFF)
- Support OCR for embedded images in DOC, DOCX, XLS, XLSX
- Support remove metadata for document files (PDF, DOC, DOCX, XLS, XLSX)
- Support redaction for RTF

## v2.5.1

Release date: November 12, 2020

- Improve Japanese string detection/redaction in PDF
- Fix a detection issue when a regular expression contains a Hebrew string
- Fix a crash issue when scanning DOC file on Linux

## v2.5

Release date: October 1, 2020

Metadata removal, Watermark, OCR are available on Linux

Advanced watermark configurations: font size, text opacity, text position

New configurations

- Stop the process if found enough sensitive info
- Quality configurations for OCR (Normal, Best)

Support HTML and TXT redaction

10x faster when processing text file

## v2.4.1

Release date: August 8, 2020

- Improved memory usage
- Improved IPv4 and CIDR search
- Added threaded comment search and redaction in Excel files
- Up to 40% speedup when scanning Excel files

## v2.4

Release date: July 7, 2020

- Utilize column and row header to improve certainty level in Excel
- Detect sensitive info in file properties with regular expressions
- Custom keyword list for regular expression
- Support redaction feature on Linux
- Performance improvement: faster processing, less resource usage
- New system requirements on Linux
- End of support Centos 6, Debian 8

## v2.3.2

Release date: May 20, 2020

- Better context calculation for Excel and PDF
- Improve IPv4 detection in TXT
- Distinguish between "Failed to detect" and others

## v2.3.1

Release date: April 21, 2020

- Threaded comment redaction in Excel files.
- Slightly increased PDF scan performance.
- Improved certainty calculation for MS Office and PDF files.
- Fixed wrong context when a single cell in an Excel file contained the same hit multiple times.

## v2.3.0

Release date: April 7, 2020

- Support Optical Character Recognition (OCR) for PDF (Windows only)
- Redact sensitive information for Microsoft Office Excel (XLS/XLSX)
- Better detection method, reduce false positive

## v2.2.1

Release date: Feb 12, 2020

- Improve IPv4/CIDR detection performance
- Better handling temp files
- Remove "Parse Binary" option

## v2.2

Release date: Jan 6, 2020

- Supports watermark addition for PDF
- Redact sensitive information for Microsoft Office Word (DOC/DOCX)
- Support DLP in Linux with limited functions (work with MetaDefender Core 4.17.1 or newer)
- Redact sensitive information based on certainty level (work with MetaDefender Core 4.17.1 or newer)
- Sample Regular expressions to detect Personally identifiable information (PII): email, address, full name, date of birth, driver license, phone number, bank account number

## v2.1.2

Release date: November 27, 2019

- Better error message when an input PDF file is corrupted

## v2.1.1

Release date: October 31, 2019

- Better displaying the words before and after a hit in PDF

## v2.1

Release date: September 8, 2019

- Supports IPv4, Classless Inter-Domain Routing (CIDR) detection
- Supports remove metadata for TIFF, GIF file
- Better CCN detection

## v2.0.1

Release date: August 15, 2019

- Better watermark and redaction handling when a system is under high load
- Improve CCN detection

## v2.0

Release date: June 28, 2019

- Proactive DLP as new name
- Certainty score for sensitive data detection
- Redact sensitive information for text-based PDF file
- Watermark addition for JPEG, TIFF, PNG, GIF
- Supports remove metadata for JPG, PNG file

## v1.0.3

Release date: February 18, 2019

- Improve detection for Microsoft Access format
- Improve context for hits
- Improve processing speed (20%)