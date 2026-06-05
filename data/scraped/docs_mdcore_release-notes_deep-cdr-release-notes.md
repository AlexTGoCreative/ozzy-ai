<!-- source: https://www.opswat.com/docs/mdcore/release-notes/deep-cdr-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:06:20.429910 -->

# Deep CDR release notes

## v7.8.2

Release date: 5/20/2026

Supported 3MF file sanitization.

Supported image removal in PowerPoint 2007 and Excel 2007 files.

Supported removing control document variables in Word 2007.

Supported dynamic safe URL redirection in PDF and OpenOffice documents.

Added option to skip image loading in HTML to PDF conversion.

Improved processing performance and memory usage:

- Reduced memory consumption when converting PDF to TIFF.
- Optimized calcChain elements processing for XLSX with many external sheets.
- Streamlined Word, PowerPoint, and Excel 2007 sanitization with single-pass processing.

Fixed newline preservation in HTML attribute values.

## v7.8.1

Release date: 4/15/2026

New file type support: IFC, LYRX, BLZ.

MS Office 2007 Enhancements

- Improved Excel 2007 processing performance with optimized single-pass SmartTag handling.
- Removed ActiveX definitions in PowerPoint 2007 and Excel 2007.
- Enhanced content type processing for Excel 2007.
- Improved external link handling in Excel 2007.
- Added support for removing embedded font extension definitions in Office 2007 files.
- Removed embedded object definitions and zeroed content in PowerPoint 2007.
- Added support for removing template field codes in Word 2007 files.
- Added support for dynamic safe URL redirect addresses in HTML/RTF/TXT/Office 2003/Office 2007 files.

Added support for preserving special TIFF tags (Artist, Copyright, Make, SMinSampleValue, SMaxSampleValue, ...)

Improved CRLF line ending handling in HTML output for compatibility with Microsoft Exchange.

Improved BOM-based encoding handling in XML files.

Fixed empty RTF output when removing metadata containing the rempersonalinfo node.

Fixed an issue where JWW files became unreadable after sanitization.

Allow skip loading images in conversion of HTML to images.

## v7.8.0

Release date: 3/25/2026

MS Office 2007 Enhancements:

- Added support for image removal in Word 2007.
- Removed structured document tags in Word 2007.
- Removed author information inserted through Field Codes in Word 2007.
- Removed embedded objects referenced via "oleLink" in Excel 2007.
- Removed Relationship nodes in Definition path, Usage of embedded object when removing Embedded objects.
- Enhance removal of embedded object with multiple definitions.
- Handle document properties with exceptional paths.

PDF Enhancements:

- Handled XSS in PDF text fields.
- Handled concatenated PDF files.
- Implemented custom ratio scaling for PDF to rasterized PDF conversion.
- Enhanced processing flow for innocent actions in PDF files.
- Disassociated "Document open action" from "Block File > Script objects" section.
- Prevented hyperlinks in comments from being re-added during re-sanitization.

Support namespace in SVG sanitization.

Enhanced XML Base64 processing for attribute values and self-closing nodes.

TIFF Enhancements:

- Preserved compression method for TIFF64 files.
- Preserved EXIF tag RPCCoefficientTag in TIFF images.

Added QR Sanitize support for cgBI PNG format.

Fixed inconsistent sanitized image count behavior in RTF files.

Added support for obfuscated emoji detection in TXT sanitization.

Support Debian 13.

Upgrade OpenSSL to 3.6.1.

## v7.7.2

Release date: 2/5/2026

Supported new file type: YENC.

MS Office 2007 Enhancements:

- Supported removal of custom property data.
- Improved error messages for invalid file structures.
- Removed all linked data when removing comments.

PDF Enhancements:

- Removed DTD data when removing XFA forms.
- Added support for removing watermark annotations.

Improved VCF Sanitization:

- Handled QUOTED-PRINTABLE encoding.
- Handled hyperlinks in text form.
- Extended Base64-encoded data sanitization to arbitrary fields.

Other Improvements:

- Handled script tags with namespaces in SVG.
- Improved handling of hyperlinks in RTF files.

## v7.7.1

Release date: 1/14/2026

Added support for VCF, JAR, WAR, LZ4, MAR.

Added support for converting CgBI PNG files to other formats.

MS Office 2007 enhancements:

- Added support for converting DOCX/XLSX files to rasterized PDF.
- Added support for removing image metadata in Microsoft Office 2007 files.
- Added support for removing database field codes, DataBinding element in DOCX files.
- Enhanced OLE object removal in DOCX files.
- Reported hlinkfile and hlinkpres as hyperlinks in PPTX files.

PDF enhancements:

- Added support for removing text, popup, and free-text annotations.
- Improved handling of PDF files containing /ObjStm objects.
- Completely removed all related information when removing embedded objects.
- Added dynamic fallback from Very Low to Low image quality.
- Replaced invalid header versions with a valid one (1.7).

Removed beta labels for several file types.

Added CIS Level 2 support for Windows Server 2022.

## v7.7

Release date: 12/16/2025

- Added support for High Efficiency Image File Format (HEIF).
- Added support for cgBI PNG image format.
- Improved LNK file sanitization, with command details shown in specific scenarios.
- More accurate reporting of comment counts in Microsoft Word and Excel 2007.
- Improved comment removal for PowerPoint (PPTX) files.
- Updated the "Allowlist External Image" feature to exclude other types of external objects.
- Added audio frame data validation for MP3.
- Allow configuration of processing threads for video conversion.
- Fixed rare omsMediaService crashes when processing HEIC files.
- Reduced Linux package size by up to 20%.
- Upgraded the third-party conversion tool to a newer version.
- Improved VSIX sanitization with enhanced structural validation and removal of untracked files.
- Improved removal of embedded OLE objects in MPP files.

## v7.6.3

Release date: 11/19/2025

- Fixed backward compatibility issue with the old MetaDefender Core (5.6.1 or older).

## v.7.6.2

Release date: 11/12/2025

Support new sanitizations: STEP (STP), AV1 Image File format (AVIF), Microsoft Project (MPP). 3D Mesh Layer (3DML), Visual Studio Extension (VSIX), 3D Assembly (EASM).

PDF Improvements:

- Enhance processing of JP2 images.
- Improve hyperlink handling.
- Return "action" details when removing Javascript.
- Add "Very Low" quality option for PDF to Image conversion.
- Expose details about "unused objects".

XLSX improvements:

- Enhance XLS to XLSX sanitization to ensure compliance with a specific validation tool.
- Improve hyperlink handling in case of non-standard formular structure.

Add a new option to configure output dimensions when converting TIFF to BMP.

Provide more detailed feedback when sanitizing a broken GIF file.

Enhance WMV output when input files lack a video stream.

Add support control framerate in video conversion.

Allow character encoding fallback in XML sanitization.

Add support for removing "foreignObject" elements from SVG files.

Improve invisible text detection in TXT files.

Return detailed conversion and sanitization information, including source and target file types.

## v7.6.1

Release date: 10/14/2025

- Expose suspicious data removed during GIF sanitization.
- Handle empty X-ALT-DESC fields in ICS files.
- Add support for "Display Hyperlinks in Comments" in PDF sanitization.
- Add support for removing unapproved tags in HTML sanitization.
- SVG sanitization improvements:
- Return more detailed information when SVG sanitization occurs.
- Reclassified the removal of Windows event attributes under JavaScript.

## v7.6.0

Release date: 9/24/2025

Support RIBC data table format (RIBC).

Support PPT to PPTX conversion and OLE-based FLA to WAV.

Skip signed PDF files based on provided certificate files.

Enhance XML sanitization:

- Support validating XML files against an XSD schema.
- Support recursively sanitizing base64-encoded data in specified XML paths.

Enhance DWFX sanitization:

- Support removing embedded fonts.
- Sanitize hyperlinks in .fpage and XML files.

Apply syntactic checks to multiple XML structure files in MS Excel/PowerPoint 2007.

Support DocuWorks version 10.

Support sanitizing objects under a foreignObject element in SVG.

Support analysis mode for “Process ASCII-based QR code” in MS Word.

Return returning header and footer validation results for MS Word 2007.

Return raw data information in image sanitization (when Include Processed Objects is enabled).

Support validation of the RIBC Table in UTIB sanitization.

Support JSON files in UTF-8 with BOM.

Enhance image processing speed in MS PowerPoint 2007.

Enhance JP2 image sanitization for PDF.

Handle escaped characters in script nodes properly.

Distinguish between email addresses and hyperlinks in several file formats.

## v7.5.2

Release date: 8/19/2025

Support for new file types:

- MPP to PDF, MPP to XLSX,
- Archive file: LZIP, ASAR.
- Other: B3DM, DWFX.

New configuration in HTML sanitization to replace "." with "[.]" in hyperlinks for domains.

Support sanitizing ASCII-based QR codes in TXT files.

Support removing "href" and "xlink:href" in the "script" node during SVG sanitization.

Support "Excluded file types for Recursion" in MS Word sanitization to remove embedded files instead of performing recursive sanitization.

Support allowing User-Defined Named Actions in PDF.

Support base64 data in XML.

Added syntactic validation for Custom XML property files in MS Office documents.

Improved scan results to show structure validation outcomes more clearly.

Fixed an issue where Deep CDR’s skip allowlisted feature was not working in some cases.

Added support for Windows Server 2025 and Ubuntu 24.04.

## v.7.5.1

Release date: 7/24/2025

Support new file types:

- AVC to AVC (the file type is enabled on-demand, please contact Customer Support or Sales team if you want to use it).
- Convert XPS to PDF, PPTX to PPT.
- Convert OPUS to WAV, FLA to WAV.

Detect and report ASCII QR code in HTML.

Improve sanitization for HTML with UTF-16 content.

Upgrade OpenSSL to 3.3.3.

## v7.5.0

Release date: 6/25/2025

Support new file type:

- WSQ, ODG, HEVC, TTML, MPD.
- Convert PDF to rasterized PDF, VSD to PDF.
- Convert MPP to WAV, PAF to WAV, M4A to WAV, CAF to WAV.

Support QR code created using ASCII characters in RTF.

Support QR code for PDF.

Enhance sanitization:

- Validate MS Excel 2007 file structure against zip format.
- Handle a specific non-standard multiple HTML tags case.
- Support new version of HEIC.
- Better handling big MS Excel 2007, TIFF files.
- Improve PDF, ICS, MS Powerpoint sanitization.

Upgrade .NET to version 8.

## v7.4.2

Release date: 5/28/2025

Support new filetype conversions:

- Video: MTS to MP4, OGG to MP4, WMV to MP4, MP4 to AVI, AVI to MP4, AVI to WMV, MTS to WMV, SWF to WMV, WMV to AVI, MP4 to WMV
- Audio: M4A to MP3, OPUS to MP3, WAV to MP3, WAV to MP4
- Others: ICO to BMP, ICO to PNG, DOCX to DOC, XLSX to XLS, ODT to PDF, OTT to PDF, PDF to PPTX

Enhance Word 2007 sanitization:

- Validate many XML structure files against the XSD schemas.
- Validate file structure against zip format.

Enhance WAV sanitization.

Support Amazon Linux 2023.

## v7.4.1

Release date: 4/24/2025

Support new file types:

- Sanitization: URL, MDZip
- Conversion: XLS to XLSX, TIF to PDF

Support validating footer and header in MS Word, Excel 2007.

Support QR code created using ASCII characters in MS Word 2007.

Optimize resource usage when removing comments.

Enhance timeout handling in case of recursive sanitization.

Improve ICS sanitization in case of invalid html content.

## v7.4

Release date: 3/27/2025

New options for MS Office 2007:

- Remove Smart Tag.
- Validate Document Properties.
- Validate Template Name.

Support returning "Reason for action" to explain why Deep CDR removes/ sanitizes/validates an object (support Smart Tag, Document Properties, Template Name only)

New configuration in HTML to allow output with pretty-printing style.

New file type support:

- convert MJ2 to MP4, MOV, AVI and WMV.
- SCDOC

Skip signed Macro.

Support sanitization of base64 encoded data in JSON.

Support skipping sanitization in special cases (Unsupported version, Exceeded file size, password protected, Invalid file structure).

Support QR code created using ASCII characters in MS Word 2003.

Better handling MP4, ICS, EML, PDF, CSV sanitization.

Improve WEBP sanitization speed.

Improve VSTO removal in DOCX.

Update sanitization description to be clearer.

## v7.3.2

Release date: 2/19/2025

- Support ZSTD, YZ1 sanitization.
- Allow users to input exceptional characters when removing control characters in TXT sanitization.
- Optimize resource usage for handling very large MP4 files.
- Enhance metadata removal for MP4, MOV, OGG files.
- Support metadata removal when converting from MP3 to MP4.
- Improve handling of charset values with double quotes (Content-Type: text/html;charset="...") in HTML sanitization.
- Improve
`/FontMatrix`

attribute processing to address CVE-2024-4367. - Fix PDF form processing to prevent the removal of more objects than necessary.
- Update error messages for image sanitization when exceeding the size limit.
- Remove the Beta label for several file types.

## v7.3.1

Release date: 1/15/2025

- Support removing invisible characters in TXT.
- Better handling HTML encode.
- Improve ODP sanitization to avoid missing images.

## v7.3

Release date: 12/18/2024

Support TNEF sanitization.

A new configuration in MS Office 2007 to allow external images by given paths.

A new speed mode for image sanitization

Add "hidden watermark" to several file types to prove that Deep CDR validated the file structure.

Add "pixel data" in sanitization details for image sanitization.

Improvement:

- OpenOffice (ODP, ODS, ODT) sanitization: better handling charts, images.
- Preserve color palette in PNG.
- Preserve HTML style tag "<!--" in HTML sanitization.
- Handle MS Excel 2003 only contains a Book stream without a WorkBook stream.
- Remove redundant data in AVI.
- Handle NULL data in DictionaryObject in PDF.
- Faster process XLSX contains large sheets.

Support Rocky Linux 9.4, Debian 12.

## v7.2.3

Release date: 11/13/2024

Support MHT to MHT sanitization.

Support new file type conversions:

- MKV, MOV and OPUS to MP4.
- MKV, M4V, 3GP and MTS to WMV.
- MKV, M4V, MPEG, MTS and MOV to AVI.

Support QR sanitization for MS Office.

Enhance hyperlink processing for MS Office,

**SHOW**file.Enhance process hyperlinks in HTML.

Enhance EmbeddedPress removal towards preserving WordArt in JTD.

Distinguish internal hyperlinks and external hyperlinks for the PowerPoint 2007.

Optimize PDF hyperlink processing to use less system resource.

Digitally sign all binary files.

## v7.2.2

Release date: 10/23/2024

- Fix Japanese encoding in the HTML sanitization.

## v7.2.1

Release date: 10/8/2024

Support new file types:

- EML, MSG, MBX and ESZ to ZIP.
- 3GP, MP3, MPEG, M4V to MP4.
- OTT to PDF.

Extend Analysis mode for Audio, Image, Video.

Support removing Book stream, printerSettings and hidden sheets in MS Excel.

Enhance DDE detection in MS Excel.

Handle the DDE with Japanese full-width characters in CSV.

Handle HTML with ISO-2022-JP properly.

Enhance VBA project processing in MS Office sanitization.

Enhance OLE object removal in RTF sanitization

## v7.2

Release date: 9/18/2024

Support new file types:

- TGA, ACM, MBX, JNLP.
- GPKG, B3DM to ZIP.
- CSV to XLSX.

New configurations in the Blocking mode:

- Blocking CVS files with formulas
- Blocking PDF files with invalid digital signature

New configuration in PDF to allow users to keep embedded objects base on file types.

Handle white colored QR code.

Handle "

**onbegin**" event in HTML and SVG.Report DDE objects in MS Office more accurately.

Distinguish regular hyperlink and HYPERLINK functions in MS Excel.

Enhance TIFF, JPG, and DWF sanitization.

## v7.1.1

Release date: 7/24/2024

- Sanitize Windows Compressed Enhanced Metafile (EMZ) files.
- Block files with "
**Invalid file structure**" in the`Blocking mode`

. - Sanitize XML-DOCX files.
- Support QR code with transparent background in BMP, PNG.
- Validate digital signature in signed PDF files.
- Remove Beta labels for several file types.

## v7.1

Release date: 6/25/2024

Support new file type: Microsoft Power BI (PBIX), PowerPoint XML Presentation (XML-PPTX), Broadcast Wave 64 (BW64), Multiple Network Graphic (MNG), and Bean Markup Language (BML).

Support DWG version 2000.

Support macro

**allowlist**for MS Office 2003.Support more objects in PDF, including:

- PostScript,
- Reference XObject, and
- Named action.

Support Japanese full-width formula signs in CSV sanitization.

Support Shift-JIS encoding for TXT to PDF conversion.

Support Shift-JIS binder ins XBD.

Support Ubuntu 22.04.

Enhance metadata removal for embedded images in MS Office.

Enhance MS Word 2007 sanitization with documents missing main rels.

Enhance image sanitization in PDF.

Improve HTML encoding in EML sanitization.

## v.7.0.1

Release date: 4/22/2024

- Resolve service startup failures.
- Improve HTA hyperlink handling.

## v7.0

Release date: 4/3/2024

- Support DWF to DWF sanitization.
- Support new file types: Adobe Illustrator Template (AIT), Log (LOG), and Research Institute on Building Cost (RIBC).
- Support allowlisting of macros for Microsoft Word 2003.
- Improve sanitization for Microsoft Excel, Microsoft Office 2007, HTA, and EML.
- Return metadata object details for several file types.
- Upgrade the engine to use .NET 6.

## v6.8.2

Release date: 2/5/2024

- Enhance signed PDFs with compressed catalog processing.

## v6.8.1

Release date: 1/16/2024

- Enhance macro processing for Microsoft Excel.
- Enhance hyperlink processing for PDFs.

## v6.8.0

Release date: 12/19/2023

Support new file types:

- Archive files: e-dossier (ES3), System Center Configuration Manager Package Files (PCK).
- Shape format (DBF), Printing (PRN), and MS Excel Add-ins (XLAM).

QR code enhancements:

- Support BPM format.
- Add the capability to block images if they are QR codes.
- Improve processing of QR code with rotation.

Add a new hyperlink configuration for PDFs to prevent PDF readers turning text to hyperlinks

Return metadata object details for MS Office 2003/2007 and PDFs.

Improve attachment handling for EML sanitization.

Enhance custom XML removal.

Improve JWW sanitization.

Fix the temp file removal issue during high load.

## v6.7.2

Release date: 11/9/2023

- Better handling Japanese texts in the PDF sanitization.
- Improve non-English encoding when converting MS Office.
- Fix a race condition issue during a high-load situation.

## v6.7.1

Release date: 10/5/2023

- Fix crash issue when processing a specific webp file

## v6.7

Release date: 9/27/2023

- Support QR code sanitization
- New file type support: Material Exchange Format (MXF), V-nas BFO (BFO), Storyist Document (STORY), HTML Archive (HAR), VTXT, CAB to CAB
- Return base64 data in CDR details for OLE objects (it is configurable)
- Add watermark to images structural data inside documents
- Support removing windows event attributes on XML file format
- Show the reason of Blocked by Deep CDR
- Remove BETA label for EGG, WMA, OGG, OPUS, HEIC, JWC, JHD, APNG, TSV, OFT, BWF, W64, RF65, AIFF
- Fixed sanitization failure for a zip file with specific LNK files in it

## v6.6.2

Release date: 8/9/2023

- Support DocuWork Container (XCT) sanitization
- Fix engine crash when processing TIFF file

## v6.6.1

Release date: 7/19/2023

- Support AltChunk resource in MS Office
- Improve PDF validation rule
- Support new encoding in XML sanitization

## v6.6

Release date: 6/20/2023

- Block file based on sanitization details (require MetaDefender Core 5.5.1+)
- New file type support: GeoTIFF, OneNote (ONE), Advanced Audio Coding (AAC), Flash Video (FLV), MPEG-2 Tranmission (MTS), AutoCAD DXF (DXF), Shapefile (SHP, SHX), Powerpoint add-on (PPAM), Tableau workbook (TWB), DocuWorks Binder (XBD), Resource Description Framwork (RDF)
- Support removing customXML in DOCX/XLSX/PPTX
- Improve sanitization for JSON, WAV, MP3, MP4, Images
- Improve logging

## v6.5.2

Release date: 4/13/2023

- Optimize the sanitization process during highload
- Improve AutoCAD sanitization
- Improve logging

## v6.5.1

Release date: 4/2/2023

- Enhance URI checking in Calendar file sanitization
- Handle big PDF Outline tree

## v6.5

Release date: 3/15/2023

- New file type support: Audio Interchange File Format (AIFF), Justsystem Hanako (JHD).
- Support RTF font table processing
- Support TXT with ISO/IEC 8859-1 encoding
- Improve the dependencies check to display proper messages
- Improve WMV processing
- Enhance external image removal in Excel 2007
- Enhance hyperlink processing in ICS
- Split the processors to services to improve the stability

## v6.4.1

Release date: 2/13/2023

- Support new file types: Tableau Packaged Workbook (TWBX), Tableau Datasource (TDS), ShadowProtect Full Backup File (SPF)
- Enhance JPEG sanitization to prevent file size from increasing

## v6.4

Release date: 1/11/2023

- New file type support: BWF, W64, RF64
- Support encoding Shift-JIS in TXT sanitization
- Handle SVG bomb attack

## v6.3.2

Release date: 12/2/2022

- Support new file types: OFT, OPUS
- Fix an issue when converting a big SVG to BMP
- Preserve EML header when sanitizing files

## v6.3.1

Release date: 11/3/2022

Support DOCX to RTF conversion

Enhance HTML sanitization

- Better Zero-font removal
- Support "base" tag and relaitive link

Apply image size setting to BMP

Improve PDF sanitization

## v6.3

Release date: 10/5/2022

- Support Analysis mode
- Support APNG converstion to PNG, Ogg Vorbis Compressed Audio File (OGG), Tab-Separated Values (TSV) sanitization
- Support "Skipped Signed File" configuraiton for MS Office
- Allow user to set log level in the web management console
- Support recursive sanitization for PDF
- Introduce size limit settings for TIFF
- Display an error message when missing engine dependencies (MetaDefender Core 5.2.1+)
- Enhance comment removal in HTML

## v6.2.2

Release date: 8/22/2022

- Support JW CAD (JWC), Windows Media Audio (WMA) sanitization
- Remove linked objects in ODT sanitization
- Remove Content Description, Extended Description and Content Branding when removing metadata in WMV/WMA

## v6.2.1

Release date: 8/2/2022

- A configuration to skip processing digital signed MS Office Word/Excel 2003 and MS Office 2007
- Enhance WMV sanitization
- Allow whitelist macro hash with case insensitive
- Better handling signature in PDF file

## v6.2

Release date: 6/29/2022

Support new file types:

- MPEG-4 format for Audio (M4A)
- High Efficiency Image File Format (HEIC), the file type is enabled on-demand, please contact Customer Support or Sales team if you want to use it.

Better handle executable actions in PDF (all annotations and actions)

Sanitize Visual Studio macro (VSTO) in MS Office documents

A new GIF configuration (GIF Layer Count Limit) to limit the number of GIF layers

Improve LNK sanitization to show sanitization details better

Better timeout handling

Handle loading external resources in MS Office processing

Remove BETA label for WEBM, VDX, VTX, VSX,TIFF64

## v6.1.3

Release date: 6/2/2022

- Improve PDF sanitization

## v6.1.2

Release date: 5/16/2022

- Process more objects in PDF sanitization
- Preserve empty encoding declaration in XML
- Fixed line folding issue for ICS sanitization

## v6.1.1

Release date: 4/27/2022

- Report JavaScript Hyperlink as JavaScript in PDF sanitization details
- Using LZW compression for BMP to TIFF, PNG to TIFF, DWF/DXF to TIFF conversions
- Optimize PDF sanitization resource

## v6.1

Release date: 3/28/2022

- Support JSON, CRL file format (BETA)
- Remove BETA label for several file types
- A new configuration to return hyperlink without processing for Microsoft Office and PDF
- Support whitelisting hyperlink for Open Office, PDF, Hancom, JustSystems Ichitaro, Visio, HTA, XDW
- Improve PDF, TXT, Excel, SVG, LNK, HTML, JWW sanitization
- Improve debug log: log location is moved to the engines log folder, support log rotation

## v6.0.2

Release date: 2/10/2022

- Enhance stability
- Fix HTML encoding issue

## v6.0.1

Release date: 1/10/2022

- Change Blacklist/Whitelist to Blocklist/Allowlist
- Remove unnecessary files in the package

## v6.0

Release date: 12/15/2021

Significant improvement on Linux version:

- Performance increases 50% in average
- Add 200+ file type conversions

Support whitelisting hyperlink for MS Office, RTF, HTML, Calendar file

Remove BETA label for several file formats

Support big TIFF, Nikon Raw Image

**(**NEF), Hangul Word Processor 2010 Document (HPWX) file formatHandle more image formats in PDF

Improve timeout handling

libgdiplus 6.0.5 or above is required for some file type conversions

## v5.14 (Windows Only)

Release date: 11/22/2021

- Improve PNG sanitization to avoid increasing file size
- Enhance RTF/PDF sanitization to handle unexpected cases
- Support new file type conversion: EGG to the other archive file types

## v5.14 (Windows Only)

Release date: 10/4/2021

Support new file types (beta):

- VDX to VDX, VSX to VSX, VTX to VTX,
- WebM

Support MPEG-1 encode in MPEG sanitization

Remove beta label for several file types, please check the Supported File Types page to see the full beta list

Better macro handling in MS Office 2007

Enhance HTML sanitization with specific encoding and non-ASCII characters

## v5.13.1

Release date: 8/17/2021

- Handle MPEG-1 encode in MPEG sanitization
- Improve PDF/HTML sanitization to handle corner cases, none standard format.

## v5.13

Release date: 7/5/2021

- Remove BETA label for AI, JTDC, HWT, DWT, DWS, WAV, SVG, VCS, ICS, TXT, PPS, XML
- Performance improvement on Linux
- Support strict validation configuration for WAV
- Support new file type: XDW (DocuWorks Image). Customers need to install and active DocuWorks 9 or newer on the system to use this feature
- Several minor bug fixes
- libgomp (Centos), libgomp1 (Ubuntu) is required

## v5.12.3 - hotfix

Release date: 6/15/2021

- Fixed the configuration issue when upgrading from Core 4.19.x to Core 4.20.x

## v5.12.3

Release date: 6/3/2021

- Support strict validation configuration for MP4/MOV
- Remove BETA label for MP4/MOV
- A new configuration to control image quality for Image sanitization
- Improve PDF sanitization

## v5.12.2

Release date: 5/18/2021

- Support MOV sanitization
- A new configuration to control JPEG file size/quality in PDF file
- Improve m4a sanitization

## v5.12.1

Release date: 4/27/2021

- Improve XML sanitization performance on Linux: 10x faster
- Fix PDF hang issue
- Better handling Think Cell object in Microsoft Office

## v5.12

Release date: 4/8/2021

- End of support Windows 7, 8, and 8.1; Centos 6+; and RedHat 6+
- Recursively sanitize PST (require .NET Core 3.1 or newer to be installed on Linux
- Support new file types: JW CAD (JWW), SXF Feature Comment (SFC), P21 ( STEP Data Model)
- A new configuration to process CDATA in XML
- Improve CSV, DWG sanitization on Linux

## v5.11.2

Release date: 3/1/2021

- Improve XLSB sanitization
- Support to remove event attribute in HTML file
- Fix sanitization failure when a TIFF file has unknown custom tags
- Fix compound file corrupted after sanitization

## v5.11.1

Release date: 1/27/2021

- Fix a crash issue when sanitizing LNK file
- Fix sanitization failures with some specific XLM, PDF, PNG files.

## v.5.11

Release date: 1/11/2021

- Per-file configuration will be available as part of Workflow (requires MD Core 4.20.0 and above)
- Whitelist Macro based on Macro content
- Enhance engine communication on Linux
- Support XLS to CSV conversion

## v5.10.3

Release date: 12/07/2020

- Reduce resource usage when sanitizing XML files
- Fix a crash issue when sanitizing Excel files

## v5.10.2

Release date: 11/16/2020

- Fixed a hang issue with XLSX sanitization
- Fixed a PDF timeout issue

## v5.10.1

Release date: 10/28/2020

- A better way to remove VBA macro in XLS
- Fixed a bug that causes some specific PDF files cannot be opened after sanitizing
- Fixed memory leak issue in MP3 sanitization

## v5.10

Release date: 09/28/2020

Support new file types:

- Open Office Spreadsheet (ODS, OTS)
- Open Office Presentation (ODP, OTP)
- Hangul Word template (HWT)

Support recursive sanitization for MS Office 2003 (DOC, XLS, PPT) , Open Office (ODT, OTT, ODS, OTS, ODP, OTS) , Rich text format (RTF)

New configuration to remove JavaScript hyperlink in HTML

Preserve object thumbnail after removing OLE objects in Office 2003

Improve Chart object handling in XLSB

Better hyperlink handling in RTF: remove hyperlinks properly, keep bookmark links

Improve XFA form sanitization in PDF

Enhance processing PpAction (mouse over llink and mouse click link) objects in Powerpoint 2007

## v5.9.3

Release date: 9/1/2020

- Better handling JSON details
- Improve TXT sanitization
- Better HTML redirection in cases a hyperlink is escaped
- New file type conversion: XLSM to CSV, XLTX to CSV, DOC to RTF, DOCM to RTF, HTML to TXT

## v5.9.2

Release date: 8/10/2020

Support new file types:

- File type conversions on Linux: PPTX/PPSX/SVG to BMP
- TIP Test selection engine (TSE, TSEC, TSEZ)
- WinACE archive format (ACE) conversion to other archive file formats

Better handling embedded PDF file in MS Excel 2007

Improve PDF, TIFF, RTF sanitization

## v5.9.1

Release date: 7/15/2020

- Hotfix to work with MetaDefender Kiosk Secure Image

## v5.9

Release date: 7/7/2020

Support new file types:

- Digital Imaging and Communications in Medicine (DCM)
- AutoCAD Drawing Standards (DWS), AutoCAD Drawing Template (DWT),
- Microsoft Powerpoint Slide 2007+ (SLDX), Microsoft Office PowerPoint Slide 2007 - Macro-Enabled (SLDM)
- Windows Shortcut File (LNK)
- HD Photo (WDP), Google Web Image (WebP)
- DOC to DOCX, DOT to DOTX conversion

A new configuration to allow hyperlink redirection in Microsoft Offices, Microsoft Visio documents, Hancom documents, PDF, RTF, ICS, VCS, ODT

Better timeout handling for Microsoft Office, PDF sanitization

Improve HWP sanitization: better image handling, separate chart configuration with embedded objects, fix memory leak

Better handling Tiff images, unused objects, 3D objects in PDF sanitization

## v5.8.1

Release date: 5/20/2020

- Support ALZip (ALZ) sanitization
- Support removal of thread comment in Microsoft Excel
- A new configuration to allow zero font in HTML file
- Improve SVG, XML, UTF-16 HTML sanitization

## v5.8

Release date: 4/14/2020

Microsoft Visual C++ 2017 Redistributable is a new requirement

New configurations:

- A configuration to skip a PDF file with digital signatures
- A configuration to process a HTML file which has multiple <html> tags in it.
- A configuration to keep/remove chart in Microsoft Office files

Support new file types: HTML Application (HTA), Adobe Illustrator (AI), WinRAR (RAR to RAR)

Improve Microsoft Office sanitization: better file path handling, improve parser performance

Better PDF timeout handling

Improve image quality when converting from PDF to TIFF

## v5.7.4

Release date: 3/23/2020

- Better handling special signs (",+) in CSV
- Improve hyperlink removal in RTF

## v5.7.3

Release date: 3/5/2020

- Handle Meta Refresh tag in HTML
- Better OLE object handling in DOCX

## v5.7.2

Release date: 2/18/2020

- Better hyperlink handling in PDF
- Improve embedded font removal in DOCX
- More stable JPG, ICO, CUR sanitization
- Minor changes in configuration UI

## v5.7.1

Release date: 1/29/2020

- Fixed compatibility with FIPS compliance
- Better handling PDF/A-2
- New configurations to control image quality in PDF
- Return hyperlink list when choosing "Display hyperlink with domain only" in HTML sanitization

## v5.7.0

Release date: 12/26/2019

New configurations to sanitize hyperlinks in HTML

- Return hyperlinks without processing them
- Replace with text
- Add a prefix URL to hyperlinks

More details about the sanitized objects for MS Office, PDF, HTML

New UI Configuration (available in MetaDefender Core 4.17.1 or newer)

New support file type

- Icon file format (.ico)
- Cursor file format (.cur)
- Hancom Cell (.cell)
- Hancom Show (.show)

Improve PDF sanitization speed

Better disk I/O usage

## v5.6.5

Release date: 12/2/2019

- Fixed additional break line when sanitizing HTML
- Better handling metadata removal in Microsoft Office 2007

## v5.6.4

Release date: 11/19/2019

- Improve PDF sanitization: betting handling metadata, none standard PDF files

## v5.6.3

Release date: 11/7/2019

- Better processing Cross Reference Table ( xref ) in PDF
- Improve multi-threads handling for JTD sanitization

## v5.6.2

- Preserve newline character when sanitizing CSV
- Better handling PDF Form with empty decoded data

## v5.6.1

- Better handling invalid file structure for TIFF
- Better handling MP3 version 2.5

## v5.6.0

Better handling CSV formulas starting with special characters

Microsoft Office sanitization improvement

- Sanitize recursively all supported file types embedded in Microsoft Office 2007 documents
- Better handling file path when processing
- Improved invalid file structure detection for DOC

PDF sanitization improvements:

- Supported sanitize PDF file generated by Adobe Illustrator
- Improved PDF form sanitization

Optimized system resource usage (RAM, I/O)

## v5.5.3

- Supported TXT to TXT sanitization
- Introduced new options to process formulas in CSV
- Improved memory usage when sanitizing big HTML files
- Better handling invalid structure JPG files

## v5.5.2

- Better resource usage for image processing
- Better disarming process for Microsoft Office sanitization

## v5.5.1

Supported new file types:

- Text file (TXT)
- Audio Video Interleave (AVI), Moving Picture Experts Group (MPEG)
- Outlook Personal Folder (PST)

Supported a new configuration to process image link in HTML

Improved 20% PDF sanitization speed

## v5.5.0

Deep CDR as new name

Supported new file types:

- Media file format: MPEG-1 Audio Layer-3 (MP3) , Waveform Audio (WAV)
- Archive file: Cabinet Archive (CAB), ARJ Archive (ARJ), LZH Archive (LZH), LZMA Archive (LZMA)
- Email file: Outlook Message (MSG)

Improved XLS/XLSM sanitization: better Macro/VBA handling

Better embedded object removal for XLSX/PPTX sanitization

Improved ODT sanitization: remove linked images; hidden text, paragraphs, comments

Improved Deep CDR details

## v5.4.3

- Improved file handling for HTML, CSV, images sanitization
- Improved process management in Linux sanitization
- Better encode handling for RTF sanitization
- Improved logging

## v5.4.2

- Better DDE handling for DOCX
- Improved PDF sanitization: better handling MetaData, XFA form, Security setting
- Better temp file handling for JTDC sanitization

## v5.4.1

- Improved Linux sanitization stability
- Improved ODT sanitization: font, embedded sheet handling
- Better DDE handling for DOC/XLS/XLT
- Better link handling for DOCX

## v5.4.0

Supported new 26 file formats, more than 100 sanitization types:

- Video file format: MPEG-4 Part 14 (MP4), Windows Media Video (WMV)
- Email file format: Electronic Mail (EML)
- Microsoft PowerPoint: Microsoft PowerPoint (97-2003) Show (PPS), Microsoft PowerPoint (97-2003) Template (POT), Microsoft PowerPoint Macro-Enabled Show (PPSM), Microsoft PowerPoint Template (POTX), Microsoft PowerPoint Macro-Enabled Template (POTM),
- Microsoft Excel: Microsoft Excel (97-2003) Template (XLT), Microsoft Excel Template (XLTX), Microsoft Excel Macro-Enabled Template (XLTM)
- Microsoft Visio: Microsoft Visio Drawing (VSDX), Microsoft Visio Macro-Enabled Drawing (VSDM), Microsoft Visio Drawing Stencil (VSSX), Microsoft Visio Template (VSTX), Microsoft Visio Macro-Enabled Template (VSTM), Microsoft Visio Macro-Enabled Stencil ( VSSM), Microsoft Visio Stencil XML file type (VSX), Microsoft XML for Visio Template (VTX), Microsoft Visio XML Drawing (VDX)
- OpenDocument Document Template (OTT)
- MIME HTML (MHT)
- AutoCAD: Drawing Interchange Format (DXF), Design Web Format (DWF)
- 3D files: Digital Asset Exchange (DAE), 3D Studio (3DS), Universal 3D (U3D), Google Draco (DRC), AVEVA Plant Design Management System Model (RVM)
- RTF to PDF

Return forensic info to show which objects were sanitized, removed

Improved image sanitization speed, memory usage

Improved PDF sanitization: better error classification, metadata handling, script handling, form handling

Improved XLS, PPT sanitization: duplicated object handling, macro handling, image handling

Improved HTML sanitization: handle hyperlink better, preserve content in "pre" tag, remove redundant data

More stable Linux sanitization for DOCX, PPTX

## v5.3.4

- Better handling empty HTML file
- Improved PDF parser to handle file structure better

## v5.3.3

- Improved handling hidden content in DOCX sanitization
- Improved ODT sanitization in Linux

## v5.3.2

- Improved error message for Microsoft XML Spreadsheet 2003 (.xml) sanitization
- Improved PDF sanitization: XFA form, Metadata parser

## v5.3.1

- Enhanced XLS sanitization in case files only contain Macros
- Improved forensic info in HWP sanitization

## v5.3.0

- Sanitization of recursively embedded documents in Microsoft Office 2007 documents
- Sanitization of Calendar data files: iCalendar (.ics) & vCalender v1.0 (.vcs)
- Enhanced EMF/WMF sanitization
- Improved image sanitization to prevent advanced steganography attacks
- Extended file support that now includes Ichitaro Document to Compressed format (JTDC), a compressed version of JTD
- Enhanced PDF sanitization functionality, including handling of digital signatures, JavaScript, form fields, and layers

## v5.2.12

- Enhanced handling DDE with RTF file type
- Improved handling external objects in Microsoft Office document
- Improved handling Forms in PDF
- Improved error message for password protect documents

## v5.2.11

- Enhanced the EMF sanitization inside PPT for Linux
- Improved error messages for invalid file structure in DOC, PPT
- Improved the TIFF sanitization inside PDF
- Better CDATA node handling in HTML sanitization
- Better temp file handling in Microsoft Office 2007 sanitization

## v5.2.10

- Better OLE handling for HWP
- Enhance file structure validation for PDF, Microsoft Office

## v5.2.9

- Better failure handling for PDF, DOCX sanitization
- Enhanced Microsoft Office sanitization: remove more linked objects, control stream.

## v5.2.8

- Improved PPT sanitization speed
- Improved CSV sanitization speed in Linux
- Improved WMF/EMF sanitization to prevent device independent bitmap (DIB) copy vulnerability (CVE-2017-0190) and buffer overflow vulnerability (CVE-2005-2123, CVE-2005-2124)
- Improved forensic info and error message

## v5.2.7

- Sanitization detail is available on MetaDefender Core REST API (version 4.12.1 and newer) (Beta)
- Improved WMF/EMF sanitization to prevent code execution
- Improved WMF/EMF sanitization for images inside document files
- Support Windows Metafile (WMF), Enhanced Metafile (EMF), Microsoft Visio Drawing (VSDX, VSDM) sanitization on Linux (Beta)
- Better embedded object handling for Microsoft Office file types
- Supported external media objects removal for PPT sanitization
- Better removing PDF metadata
- Improved HTML sanitization speed on Linux
- Added performance report for Linux

## v5.2.6

- Enhanced steganography sanitization for PNG

## v5.2.5

- Support Windows Metafile (WMF), Enhanced Metafile (EMF) sanitization on Windows (Beta)
- Better non-standard objects handling for PDF
- Enhanced HWP sanitization: content, image handling.

## v5.2.4

- Improved Microsoft Office sanitization speed on Linux
- Improved PDF sanitization speed on Linux
- Improved HWP sanitization speed on Linux
- Improved JTD sanitization speed on Linux

## v5.2.3

- Supported Microsoft Visio Drawing (VSDX, VSDM) sanitization on Windows (Beta)
- Improved hyperlink sanitization for HTML
- Improved hyperlink sanitization for HWP

## v5.2.2

- Supported external media objects removal for PPTX/PPSX sanitization
- Improved hidden text removal for DOCX/DOTX sanitization

## v5.2.1

- Fixed the issue of loading customized configuration on a 64bit system
- Handle NULL character in content for HTML to HTML sanitization
- Preserve UTF-8 BOM encoding for CSV sanitization

## v5.2.0

- Handle big file size sanitization on Windows
- Improved PPSX sanitization: better OLE object, Command handling
- Improved file size with Microsoft Office files contain EMF/WMF images
- On Linux, additional file types support: DOCM2DOCM, DOTM2DOTM, DOTX2DOTX, XLS2XLS, XLSM2XLSM, XLSB2SXLSB, PPT2PPT, PPSX2PPSX, PPTM2PPTM, RTF2RTF, HTML2HTML, WMF2JPG, XML-DOC2PDF, XML-XLS2PDF, XML-DOCX2PDF, JTD2JTD, HWP2HWP, DWG2DWG

## v5.1.20

- Fixed XML, SVG sanitization issue

## v5.1.19

- Enhanced Linux CDR performance
- Supported more file types in Linux CDR: XML2XML, SVG2SVG, DOT2DOT, GIF2GIF

## v5.1.18

- Removed Linux BETA label
- Improved HWP sanitization: better image handling, stream processing.
- Fixed HTML sanitization issue when sanitizing links, scripts

## v5.1.17

- Increased HWP sanitization speed
- Handling missing fonts for DOC sanitization on Linux
- Handling attachment removal for PDF with non-standard format
- Better handling of temporary files for DOCX, PPTX, XLSX sanitization

## v5.1.16

- Fixed moniker type issue in PPT
- Fixed some handling embedded font in PDF

## v5.1.15

- Improved Linux sanitization for DOCX
- Added support iso-2022-jp for HTML sanitization
- Enhanced CSV sanitization
- Enhanced PNG sanitization inside Microsoft Office documents

## v5.1.14

- Enhanced Macro removal for AutoCAD (Beta)
- Adding support additional potentially malicious objects in DOCX
- Supported none Unicode encoding for HTML sanitization
- Enhanced sanitization of some non-standard format PDF
- Enhanced sanitization of some non-standard format RTF

## v5.1.13

- Supported SVG to SVG sanitization (Beta)
- Adding support additional Potentially Malicious Objects (PMO) object types in PPTX
- Adding support additional PMO object types in XLSM
- Improve handling file structure integrity with a specific DOCX type

## v5.1.12

- Enhanced PPTX, PDF sanitization
- Better handling of temporary files for image sanitization

## v5.1.11

- Supported AutoCAD (Beta)
- Introduced new type of process_hyperlink_behavior for HTML
- Enhanced PPT sanitization
- Fixed bug on PDF sanitization: inverted colors in Linux, remove_form, ...
- Fixed image sanitization failure on Linux
- Fixed embedded object removal for JTD

## v5.1.10

- Updated omsFileTypeConversion.exe icon for rebrand
- Fixed JTD sanitization lost images and objects
- Fixed bugs on Microsoft Office files: DDE, Macro,...
- Handled OLE Link for Microsoft Office files

## v5.1.9

- Improved Linux sanitization
- Fixed bugs on PDF sanitization: corrupted files, crashed
- Distinguished Generic XML and Microsoft Office XML sanitization

## v5.1.8

- Fixed bugs on PDF and DOCM sanitization

## v5.1.7

- process_tag in HTML configuration was changed to process_hyperlink_behavior, default value is 1
- Removed metadata in RTF file
- Enhanced JPG, PDF, HTML sanitization

## v5.1.6

- Supported DDE sanitization for DOC, XLS and CSV file format
- Enhanced sanitization on ODT file format
- Enhanced DLP support for DOC and DOCX sanitization (hidden text)
- Enhanced Microsoft Office 2007 file format (DOCX, XLSX, PPTX) sanitization (comment, revision)
- Enhanced stabilization for HTML, XLS and PPTX file format
- Enhanced validation for HTML and RTF file format

## v5.1.5

- Improved PDF sanitization (reduced sanitized file size, optimized image processing time in PDF,...)
- Supported ODT sanitization (for both Windows and Linux)
- Improved JPG sanitization (reduced processing time)

## v5.1.4

- Supported DDE sanitization for DOCX and XLSX file format

## v5.1.3

- Enhanced metadata sanitization for Microsoft Office 2007 file format ( Title, Subject, Comments, Author, Last Modified By, Company, Modified Date)
- Improved TIFF to TIFF sanitization

## v5.1.2

- Improved DOC, PDF, HTML sanitization for validation
- Supported Form object sanitization in PDF

## v5.1.1

- Supported metadata sanitization for Microsoft Office 2003 file format (DOC, XLS, PPT)