<!-- source: https://www.opswat.com/docs/mdcore/release-notes/file-type-module-release-notes -->
<!-- product: metadefender_core -->
<!-- doc_type: changelog -->
<!-- crawled_at: 2026-06-05T09:06:05.377485 -->

# File Type Module release notes

## v7.8.3

Release date: 5/20/2026

- Supported OTF, LST, Mach-O, and IDML detection.
- Improved GPT detection to distinguish GPT files from GPT metadata.
- Improved DLL archive detection performance.
- Improved detection accuracy so CSV and YAML files are correctly identified instead of being returned as generic TXT.
- Reduced false positives:
- Refined MBX, EML and ERB detection.
- Refined PS1 detection to avoid misclassifying when Machine Learning is available.

## v7.8.2

Release date: 5/7/2026

- Fixed a crash that occurred when detecting data files larger than 7GB.

## v7.8.1

Release date: 4/15/2026

- New file type support: Web Archive (WARC), SQUASHFS, LYRX, WIM, BLZ.
- Reduced memory usage and improved performance.
- Adjusted confidence scoring for TXT files detected by third-party engines to reduce false positives.
- Improve LM model detection for TXT and JSON.

## v7.8.0

Release date: 3/25/2026

- Added support for CGR, CATPART, INDB, TXF, ICA, and IFC file formats.
- Improved detection accuracy for PostScript and HTML files.
- Enhanced detection speed for JSON and password-protected PDF files.
- Detected embedded files in Microsoft Office 2007 as OLE format.
- Fixed stability issues to improve overall reliability.
- Allowed users to define which file formats are subject to file type mismatches.
- Upgraded OpenSSL to 3.6.1.
- Added support for Debian 13.

## v7.7.2

Release date: 2/5/2026

- Supported LZOP, YENC, PEM CMS detection.
- Improved PKG detection.
- Improved custom rule detection performance.
- Improve detection by Machine Learning:
- Added support for 100+ text-based format.
- Reduced overfitting to weak or misleading patterns for more reliable results.

## v7.7.1

Release date: 1/14/2026

- Supported new detections for Z, X3P, MAR, LZ4.
- Better DTD, CSV, AVIF detection.
- Added CIS Level 2 support for Windows Server 2022.

## v7.7

Release date: 12/16/2025

- Support detecting specific file types only for use cases that do not rely on file type identification.
- Add new detections for High Efficiency Image File Format (HEIF), Safari Web Archive (WEBARCHIVE), Parquet (PARQUET), Keyhole Markup Language (KMZ) and NIST Biometric (NIST) files.
- Enhance ISO file detection.
- Support a minimum threshold length for a file to be detected as Base64.
- Support additional attributes in engine-metadata.
- Improved detection support for large TAR archive, HEIC, Pytorch Archive files.

## v7.6.2

Release date: 11/12/2025

- Support new detections for QEMU Copy-On-Write (QCOW1/QCOW2/QCOW3), AV1 Image file format (AVIF), eDrawings Assembly (EASM), COM.
- Include the "sourceName" attribute in the like_type_ids.
- Improve detection accuracy for: PICKLE, SWF, ZIP, ISO.
- Improve the Machine Learning detection.

## v7.6.1

Release date: 10/14/2025

- Block files based on their properties.
- Support the RDP file format.
- Improve the detection performance of XML-based files.

## v7.6.0

Release date: 9/24/2025

- Update ML model to OPSWAT LM v3 to have a better detection, please check this page to see a full list of supported file types by ML.
- Support new file types: WMZ, L01, EVTX, WOFF2, DES, OLE-based FLA, VBA, MATLAB, REG, JUPYTERNB, LUA, PERL, JAVA, VBS, GO, R, COFFEESCRIPT, CSHARP, RUST, MARKDOWN, RUBY, CSPROJ, TYPESCRIPT, TEX, MAKEFILE, SQL.
- Enhance TAR , WMF, MP3, RIBC, ZIP

## v7.5.3

Release date: 8/20/2025

- Support for new file types: UFDR, AppImage, HDF5 (v0, v1), and encrypted Hancom Office documents.
- Improve OVA detection for large files.
- Enhance MP3, CAB, ASN1, JSON detection.
- Add support for Windows Server 2025 and Ubuntu 24.04.

## v7.5.2

Release date: 7/24/2025

- Improve detection for: ICO, ASN1 DER, AC3, XML, ZIP-based.
- Enhance memory and string handling to resolve an engine crash issue.
- Optimize engine load time with the Machine Learning module.

## v7.5.1

Release date: 7/15/2025

- Support new file types: VMware OVA (OVA), PyTorch (PT), HDF5 version 2 (HDF5), and ONNX (ONNX).
- Properly handle the import of engine configurations.

## v7.5.0

Release date: 6/25/2025

- Support new file types: Python Zip (PYZ), Atom Shell Archive (ASAR), LZip (LZ), MS Access (MDB), Microsoft Project File (MPP), Ensoniq’s Paris Audio File (PAF), Core Audio Format (CAF), COMSOL Multiphysics Binary (MPHBIN), RIBC Data Table (utibwktmp, mthbwktmp), Wavelet Scalar Quantization FBI fingerprint format (WSQ), Advanced Video Coding (AVC, H264), High Efficiency Video Coding (HEVC), Media Presentation Description (MPD), Timed Text Markup Language (TTML), OpenDocument Drawing (ODG), Flash (FLA).
- Improve detection for NSISBI, MP4, WAV, HTML, APK, ASN1 PEM.
- Remove Beta label for "Extract Metadata" feature.
- Drop support CentOS 7/RH 7/Debian 10/Ubuntu 20.

## v7.4.3

Release date: 5/28/2025

- Support new file types: Inno Installer.
- Improve detection for HTML with ISO-2022-JP encoding.
- Support Amazon Linux 2023.

## v7.4.2

Release date: 5/7/2025

- Utilize "score" in the custom rule to overwrite some native detections.
- Enhance AI detection feature.

## v7.4.1

Release date: 4/23/2025

- Support new file types: Pickle (PKL), BRD, URL, MDZIP, PyTorch (Zip-based), new APK version.
- Return "detected_by" value to identify how a file type is detected.
- Enhance detection rule feature.
- Improve engine initialization process.
- Fix GPG detection for big file size.

## v7.4

Release date: 3/27/2025

- Support file type detection with custom rules.
- Support new file types: PRTCAD, SafeTensor (STS), variant of JPG2000 (J2K, MJ2, JPM)
- Add ZERO filetype id for zero byte file.
- Improve Git Pack, OVA, P7M, EOT detection.
- Upgrade the AI model to have better detection.

## v7.3.1

Release date: 2/19/2025

- Support new file types: OVA, DAV, DXF, R12
- Support detect encryption for encrypted-entry RAR.
- Enhance Yml/YAML detection.
- Support engines-metadata for remaining settings.
- Enhance Json detection with "Classify with Machine Learning".

## v7.3

Release date: 12/18/2024

- Support new file type detections: YZ1, DrawIO, SCDOC.
- Support Rocky Linux 9.4, Debian 12.
- Migrate configurations from global to workflows.
- Improve detection for text files that have control characters.
- Improve detection for text with Shift-JIS file encoding.
- Improve WMZ, ZLIB detection.

## v7.2.2

Release date: 11/13/2024

- Support new file type detections: NAR, Git Pack, PCAPNG, PBIVIZ, 3DML.
- Enhance TGA detection for big files.
- Improve JTDC, EML detection.
- Mismatch detection: Support asterisk (*) in the "Accepted extensions" field.
- Digitally sign all binary files.

## v7.2.1

Release date: 10/8/2024

- Support the detection of NVR file.
- Improve PCAP, WMZ, EML, JS, and CSS file detection.

## v7.2

Release date: 9/18/2024

- Allow users to configure accepted extensions to avoid mismatches.
- Support the detection of base64 text files.
- Support new file types: SQLite, B3DM, EXT, GPKG, PCAP, Hikvision DVR (HIK), ACM, TGA 1.0, JNLP, ZUGFeRD XML, and MBX.
- Improve LOC, ICS, DWF, and PDF file detection.
- Improve PERL, YML, BAT, ASPX file detection with AI.

## v7.1.1

Release date: 7/22/2024

- Enhance detection for TGA, VMDK, VMX, and VMXF files.

## v7.1

Release date: 6/25/2024

- A new configuration to utilize Google Magika to improve text-based detection.
- Support new file types: Bean Markup Language (BML), Power BI (PBIX, PBIT), Broadcast Wave 64 (BW64), and CompoundFile (OLE).
- Improve DM and Git-bundle processing.
- Support detecting MS Office documents larger than 5GB.
- Support Ubuntu 22.04.

## v7.0.2

Release date: 5/22/2024

- Fix detection for the ZED and DSK file formats.

## v7.0.1

Release date: 4/22/2024

- Improve detection for JSON and LOC file formats.

## v7.0

Release date: 4/3/2024

- Support new file types: Encrypted ZED, PowerPoint add-in (PPA), Forms Data Format (FDF), New Technology File System (NTFS), Multiple Image Network Graphics (MNG), GPS location data (LOC), TrueType Font (TTF), GGUF, Design Web Format XPS (DWFX), Adobe Illustrator Template (AIT), Research Institute on Building Cost (RIBC), and Web Open Font Format (WOFF).
- Improve file type detection for tar POXIS, MTS, EXE, DLL, and OpenPGP files.
- Upgrade Exif tool to a newer version.

## v6.5.2

Release date: 2/5/2024

- Support new file types: PYC and VIB with multiple payloads.

## v6.5.1

Release date: 1/16/2024

- Enhance detection for TXT file mismatches that occur with PRN and CSS file.

## v6.5.0

Release date: 12/18/2023

- Support new file types: Digital Negative (DNG), Report Definition Language (RDL), Microsec E-Szigno (ESZ), Nuget (NUPKG), 3D CAD (STP), Parasolid Model Part Text Format (PXT), Parasolid Model Part Binary Format (PXB), Initial Graphics Exchange (IGS), VSIX package (VSIX), Microsoft Excel Workspace (XLW), Virtual Hard Disk v2 (VHDX), JasperReports Format (JRXML), MS Excel Add-in (XLAM)
- Improve TAR, JHDC detection
- Display MISP metadata in better format
- Better handling big PDF file

## v6.4.2

Release date: 12/5/2023

- Fix TAR file detecion timeout

## v6.4.1

Release date: 11/9/2023

- Support VOX file type detection

## v6.4

Release date: 9/27/2023

- Support new file types: Git Bundle (BUNDLE), Encapsulated PostScript(.EPS, .EPSF, .EPSI), ActiveMime(.MSO), VTXT, Storylist document (STORY), DocuWork Container (XCT), Society Of Exploration Geophysicists (SGY, SEGY), Printer (PRN)
- Return EXIF metadata for more file formats
- Return custom metadata from MISP files
- Enhance IPA detection rule

## v6.3.2

Release date: 8/9/2023

- Fixed engine crash on Linux when analyzing some CERT files

## v6.3.1

Release date: 7/19/2023

- Support DocuWork container detection

## v6.3

Release date: 6/21/2023

- Detect new file format: Material Exchange Format (MXF), Advanced Audio Coding (AAC), Shapefile (SHP and SHX), MPEG-2 Transport Stream (M2TS), DocuWork Binder (XBD), Vnas CAD Format BFO (BFO), Split GZ (GZ), Apache NIFI (NIFI)
- Better clean up temporary files when analyzing DMG files
- Distinguish between WAR and JAR
- Enhance Exiftool process monitoring
- Improve JSON detection
- Optimize detection flow for media file types
- Detect encrypted archive faster

## v6.2.3

Release date: 5/22/2023

- Improve performance when scanning text files in some cases

## v6.2.2

Release date: 4/25/2023

- Detect encrypted HWP file
- Enhance DAT detecttion
- Improve performance for Winrar SFX detection

## v6.2.1

Release date: 4/3/2023

- Enhance the filetype engine to handle big files

## v6.2

Release date: 3/15/2023

- Detect new file format: AppleSingle/AppleDouble, Arcserve ShadhowProtect (SPF), Google Chrome Plugin (CRX)
- Improve logging

## v6.1.1

Release date: 2/13/2023

- Detect new file format: Firebird database files (FDB), Tableau Data Extract (TDE), VTAR
- Better way to manage EXIF process
- Enhance CSV, JSON, ICS, VCS detection
- Fix file type output contains none UTF-8 characters

## v6.1.0

Release date: 1/11/2023

- Support to return Exif info for images, MS Office 2003, MS Office 2007, PDF (Beta, require MetaDefender Core 5.3.0 or later)
- Detect ATC, EFI, JHD, JHDC, AIFF, BWF, RF64, W64, INF, PPK files
- Optimize performance for big XML files
- Enhance detection of MS Office 2007, JSON files

## v6.0.2

Release date: 12/2/2022

- Detect .p12 and .pfx as cert file extension
- Fix text detection slowness when files have many spaces
- Enhance dection of encrypted PowerPoint 2007, Excel 2007, OPUS, ATR
- Enhance detection rule for files starting with Draw string

## v6.0.1

Release date: 11/7/2022

- Improve OpenPGP, LZMA detection
- Support UTIB detection
- Fix crash issue on invalid certifcate files

## v6.0.0

Release date: 10/5/2022

- VC++ Redist 2017 is required
- Support new file type detection: MPEG Transport Stream (MTS)
- A global configuration to allow including file info details in the result.
- Dependency check when intializing the engine

## v5.3.21

Release date: 8/22/2022

- Support engines-metadata header (require MetaDefender Core 5.2.1 or newer)
- Enhance VDX detection
- Improve performance for detecting big Text, AI
- Improve logging

## v5.3.20

Release date: 8/2/2022

- Enhance detection for EML, ICS/VCS, CPIO and MS Office 2007

## v5.3.19

Release date: 7/11/2022

- Better classification for MPEG-4 Part 14 file types: .mp4, .m4a, .m4p, .m4b, .m4r and .m4v
- Enhance JSP, XLSB detection
- Support Executable and Linkable Format (ELF) file detection

## v5.3.18

Release date: 5/30/2022

- Enhance Text file detection
- Classify EICAR file as a text file
- Enhance CERT and CRL detection

## v5.3.17

Release date: 4/27/2022

- Support new file type detection: JW CAD (JWC)
- Enhance PDF detection to detect restricted PDF
- Support logging

## v5.3.16

Release date: 3/23/2022

- Improve INI, JSON, DLL, DBF, Excel 2 worksheet, PPAM
- Support new file type detection: FlashPix (FPX), Revenant Game Archive (RVM), Microsoft OneNote (ONE)

## v5.3.15

Release date: 2/10/2022

- Support new file type detections: Audio Codec 3 (AC3), OGG, Animated Portable Network Graphics (APNG), 3D manufacturing format
**(**3MF), E57, Downloadable Sound (DLS), QualComm PureVoice (QCP), Revit (RVT), DJVU, High Efficiency Image (HEIC), - Detect encrypted PDF files protected by Microsoft Information Protection (MISP)
- Support TSD, ALZ, EGG encrypted file detection
- Improve INI detection

## v5.3.14

Release date: 12/20/2021

- Fix PGP false positive detection
- Support new file type detections: e-book file format (EPUB), Targa raster graphic (TGA), ZSTD

## v5.3.13

Release date: 12/10/2021

- Support new file type detections: Silverlight app (XAP), Email template (OFT), Autodesk Filmbox (FBX), Universal 3D (U3D), CAD software (STL)

## v5.3.12

Release date: 11/22/2021

- Support new file type detections: Bourne Again Shell (Bash), EGG, Security Certificate (CER), Windows Media Player Skin Package (WMZ), Certificate Revocation List (CRL), Big TIFF, Encrypted OpenOffice XML documents, Argus (AVUX), PCX, PGP, Nikon Raw Image (NEF), Acronis True Image (TIB)
- Adjust MIME-Type for CSV, TSV, EMZ

## v5.3.11

Release date 9/29/2021

- Support new file type detections: Restricted-permission message (RPMSG),
- Improve detection for ARC, encrypted MS Office 2007, PS1

## v5.3.10

Release date: 8/10/2021

- Support new file type detections: Windows Compressed Enhanced Metafile file (EMZ), iOS application archive (IPA), Matroska Multimedia Container (MKV), WebM
- Enhance PRT, MSG detection

## v5.3.9

Release date: 7/1/2021

- Support OST file type detection

## v5.3.8

Release date: 6/3/2021

- Support new file type detections: X12 EDI, Tableau (TDSX, TBM, TDS, TWB, TWBX)

## v5.3.7

Release date: 4/27/2021

- Improve TAR, DLL, AIP (Azure Information Protection), DBF (ArcGIS) file type detection

## v5.3.6

Release date: 4/1/2021

- Support detection for P7M

## v5.3.5

Release date: 3/1/2021

- Improve detection for HAR, DSN, CELL, encrypted PDF

## v5.3.4

Release date: 1/27/2021

- Support P21 file type detection
- Improve detection for JavaScript file format
- Fix a crash issue when reading an invalid compound file

## v5.3.3

Release date: December 29, 2020

- Improve detection for Cimplicity Binary Format (CIM), F4V, SXF Feature Comment (SFC), Jw_cad (JWW), DocuWorks (XDW)

## v5.3.2

Release date: December 1, 2020

- Better detection for TSV (Tab-separated values), DSD (DART DSD) , XLS (Excel binary) file format

## v5.3.1

Release date: October 26, 2020

- Support detection for Associated Signature Containers - Extended (ASiCE) and Binary Document (BDOC) file format

## v5.3.0

Release date: October 1, 2020

- Reduce 50% resource usage while processing speed is 2x faster
- Better password protection detection for OpenOffice files

## v5.2.26

Release date: September 1, 2020

- Better detection for Microsoft CAB and Installshield CAB file format

## v5.2.25

Release date: August 10, 2020

- Improve JPEG, ACE detection
- Improve mismatched detection logic for text file format

## v5.2.24

Release date: July 6, 2020

- Support new file type detections: DCM, WEBP, LNK, WSP, JP2, ODS, OTS

## v5.2.23

Release date: May 20, 2020

- Support new file type detections: OpenSSL encrypted with a salted password, WDP, ALZ.
- Improve DWT and DWS detection, Encrypted Microsoft Office file detection