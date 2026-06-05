<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:53:23.177818 -->

# Supported File Types

## What is CDR?

An increasingly popular and effective method of compromising computer security, especially as part of a targeted attack, involves sharing common document types or image files with victims. Even though the original versions of these files do not contain executable data, attackers have found ways to trigger these files to execute embedded malicious code. Popular techniques used to accomplish this include VBA macros, exploit payloads, and embedded Flash or JavaScript code. This type of attack has a high success rate because most users don’t expect common file types to contain infections. For high-risk files or scenarios, Content Disarm & Reconstruction (CDR) prevents any possibility of malicious content (including zero-day threats) from executing. High-risk files can be sanitized through several different methods:

- Removing hidden exploitable objects (e.g., scripts, macros, etc.)
- Converting the file format

## Supported File Types (total 227)

| Source File Type | Description | Target Sanitized Types |
|---|---|---|
| doc | Microsoft Word 97-2003 Document | doc, docx, pdf, rtf |
| dot | Microsoft Word 97-2003 Template | dot, dotx |
| xls | Microsoft Excel 97-2003 Workbook | xls, pdf, csv, xlsx |
| xlt | Microsoft Excel 97-2003 Template | xlt, pdf, png |
| ppt | Microsoft PowerPoint 97-2003 Presentation | ppt, pdf, pptx |
| pot | Microsoft PowerPoint 97-2003 Template | pot, pdf, png |
| rtf | Microsoft Rich Text Format | rtf, pdf* |
| docx | Microsoft Word Document | docx, doc, txt, html, pdf, ps, jpg, bmp, png, tiff, svg, rtf |
| docm | Microsoft Word Macro-Enabled Document | docm, docx, txt, html, pdf, ps, jpg, bmp, png, tiff, svg, rtf |
| dotx | Microsoft Word Template | dotx |
| dotm | Microsoft Word Macro-Enabled Template | dotm, dotx |
| xlsx | Microsoft Excel Workbook | xlsx, xls, csv, html, tiff*, pdf, ps, jpg, bmp, png, svg |
| xlsm | Microsoft Excel Macro-Enabled Workbook | xlsm, xlsx, csv, html, tiff*, pdf, ps, jpg, bmp, png, svg |
| xlsb | Microsoft Excel Binary Workbook | xlsb |
| xltx | Microsoft Excel Template | xltx, pdf, png, csv |
| xltm | Microsoft Excel Macro-Enabled Template | xltm, pdf, png, csv* |
| xlam | Microsoft Excel Add-in | xlam |
| csv | Comma-separated values | csv, xlsx |
| tsv | Tab-separated values | tsv |
| pptx | Microsoft PowerPoint Presentation | pptx, ppt, html, pdf, ps, jpg, bmp, png, tiff*, svg |
| potx | Microsoft PowerPoint Template | potx, pdf, png |
| pptm | Microsoft PowerPoint Macro-Enabled Presentation | pptm, pptx, html, pdf, ps, jpg, bmp, png, tiff*, svg |
| potm | Microsoft PowerPoint Macro-Enabled Template | potm, pdf, png |
| pps | Microsoft PowerPoint 97-2003 Show | pps, pdf, png |
| ppsm | Microsoft PowerPoint Macro-Enabled Show | ppsm, pdf, png |
| ppsx | Microsoft PowerPoint Show | ppsx, bmp |
| ppam | Microsoft Powerpoint add-on | ppam |
| sldx | Microsoft Powerpoint Slide 2007+ | sldx |
| sldm | Microsoft Office PowerPoint 2007 Slide - Macro Enabled | sldm |
| vsd | Microsoft Visio Drawing | pdf |
| vsdx | Microsoft Visio Drawing | vsdx, pdf, xps, jpg, png, bmp, tiff, svg, emf*, html, xaml, swf |
| vssx | Microsoft Visio Stencil | vssx, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vstx | Microsoft Visio Template | vstx, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vsdm | Microsoft Visio Macro-Enabled Drawing | vsdm, pdf, xps, jpg, png, bmp, tiff, svg, emf*, html, xaml, swf |
| vssm | Microsoft Visio Macro-Enabled Stencil | vssm, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vstm | Microsoft Visio Macro-Enabled Template | vstm, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vsx | Microsoft Visio XML Stencil | vsx, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vtx | Microsoft Visio XML Template | vtx, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| vdx | Microsoft Visio XML Drawing | vdx, pdf, xps, jpg, png, bmp, tiff_, svg, emf_, html, xaml, swf |
| one | Microsoft OneNote | one |
| odt | OpenDocument Text | odt, pdf |
| ods | OpenDocument Spreadsheet | ods |
| ott | OpenDocument Document Template | ott, pdf |
| ots | OpenDocument Spreadsheet Template | ots |
| odp | OpenDocument Presentation | odp |
| otp | OpenDocument Presentation Template | otp |
| htm/html | Hypertext Markup Language | html, pdf, ps, jpg, bmp, png, svg, txt |
| mht | MIME HTML | mht, pdf, jpg, bmp, png, tiff |
| hta | HTML Application | hta |
| mar | Mozilla Archive | mar |
| Adobe Portable Document Format | pdf, html, svg, jpg, bmp, png, tiff, txt, pptx | |
| ai | Adobe Illustrator | ai |
| ait | Adobe Illustrator Template | ait |
| xps | XML Paper Specification | pdf |
| hwp | Hangul Word Processor | hwp |
| hwt | Hangul Word Template | hwt |
| hwpx | Hangul Word Processor | hwpx |
| cell | Hancom Cell | cell |
| show | Hancom Show | show |
| jtd | Ichitaro Document | jtd |
| jtdc | Ichitaro Compressed Document | jtdc |
| jhd | Justsystem Hanako | jhd |
| xml | Extensible Markup Language | xml |
| xml-doc | Microsoft Word 2003 XML Document | pdf |
| xml-docx | Microsoft Word XML Document | xml-docx, pdf |
| xml-xls | Microsoft XML Spreadsheet 2003 | pdf |
| xml-pptx | Powerpoint XML Presentation | xml-pptx |
| jnlp | Java Network Launching Protocol | jnlp |
| bml | Bean Markup Language | bml |
| twbx | Tableau packaged workbook | twbx |
| twb | Tableau workbook | twb |
| tds | Tableau Datasource | tds |
| pbix | Microsoft Power BI | pbix |
| rdf | Resource Description Framwork | rdf |
| mpp | Microsoft Project File | mpp, pdf, xlsx |
| vcs | vCalendar | vcs |
| ics | iCalendar | ics |
| vcf | Virtual Contact File | vcf |
| lnk | Windows Shortcut | lnk |
| url | URL | url |
| jpg | JPEG Image | jpg, bmp, png, tiff, svg, gif, ps, eps, pdf* |
| mj2 | Motion JPEG 2000 | mp4, avi, mov, wmv |
| jpx | JPEG 2000 | jpx |
| bmp | Windows Bitmap Image | bmp, jpg, png, tiff, svg, gif, ps, eps, pdf* |
| png | Portable Network Graphics | png, jpg, bmp, tiff, svg, gif, ps, eps, pdf* |
| apng | Animated PNG | apng, png |
| mng | Multiple Network Graphic | mng |
| tiff | Tagged Image File Format | tiff, jpg, bmp, png, svg, gif, ps, eps, pdf |
| tiff64 | Big Tagged Image File Format | tiff64, jpg, png, gif, bmp |
| nef | Nikon Raw Image | nef, jpg, bmp, png, svg, gif |
| svg | Scalable Vector Graphics | svg, jpg, bmp, png, tiff, gif, ps, eps |
| gif | Graphics Interchange Format | gif, jpg, bmp, png, tiff, svg, ps, eps, pdf* |
| tga | Truevision Advanced Raster Adapter | tga |
| wmf | Windows Metafile | wmf, jpg, bmp, png, tiff, svg, gif, ps, eps, pdf* |
| emf | Windows Enhanced Metafile | emf |
| emz | Windows Compressed Enhanced Metafile | emz |
| ico | Icon | ico, bmp, png |
| cur | Cursor | cur |
| webp | Google Image File Format for Web | webp |
| wdp | HD Photo | wdp |
| dwfx | Design Web Format XPS | dwfx |
| dwg | AutoCAD | dwg |
| dwt | AutoCAD Drawing Template | dwt |
| dws | AutoCAD Drawing Standards | dws |
| sfc | SXF Feature Comment | sfc |
| p21 | STEP Data Model | p21 |
| stp | STEP Data Model | stp |
| ifc | Industry Foundation Classes | ifc |
| jww | JW CAD | jww |
| jwc | JW CAD | jwc |
| bfo | V-nas BFO | bfo |
| dxf | AutoCAD DXF | dxf, pdf, jpg, png, bmp, gif, tiff |
| dwf | Design Web Format | dwf, pdf, jpg, png, bmp, gif, tiff |
| 3ds | 3D Studio | 3ds, dae, stl, fbx |
| 3MF | 3D Manufacturing Format | 3MF |
| dae | Digital Asset Exchange | dae, 3ds, stl, fbx |
| u3d | Universal 3D | u3d, 3ds, dae, stl, pdf, drc, rvm, fbx |
| drc | Google Draco | drc, 3ds, dae, pdf, u3d, rvm, fbx |
| rvm | AVEVA Plant Design Management System Model | rvm, 3ds, dae, stl, pdf, u3d, drc, fbx |
| dcm | Digital Imaging and Communications in Medicine | dcm |
| shp | Shapefile | shp |
| shx | Shapefile | shx |
| dbf | Shapefile | dbf |
| lyrx | ArcGIS Layer Files | lyrx |
| heic | High Efficiency Image Container | heic, jpg, pdf |
| heif | High Efficiency Image File | heic, bmp, png, jpg |
| avif | AV1 Image File Format | avif |
| avc | Advanced Video Codec | avc |
| wsq | Wavelet Scalar Quantization FBI fingerprint format | wsq |
| odg | OpenDocument Drawing | odg |
| wmv | Windows Media Video | wmv, mp4, avi |
| wma | Windows Media Audio | wma |
| mpeg | Moving Picture Experts Group | mpeg, mp4, avi |
| wav | Waveform Audio | wav, mp3, mp4 |
| mp3 | MPEG-1 Audio Layer-3 | mp3, mp4 |
| paf | Ensoniq’s Paris Audio File | wav |
| mpc | Musepack Audio Format | wav |
| mp4 | MPEG-4 Part 14 | mp4, avi, wmv |
| mov | QuickTime video format | mov, mp4, avi |
| avi | Audio Video Interleave | avi, mp4, wmv |
| webm | Video file format | webm |
| flv | Flash Video | flv |
| fla | Flash Audio | wav |
| swf | Shockwave Flash | wmv |
| bwf | Broadcast wave format | bwf |
| bw64 | Broadcast wave 64 | bw64 |
| w64 | Sony wave64 autdio format | w64 |
| rf64 | BWF-compatible multichannel audio file format | rf64 |
| m4a | MPEG-4 Audio | m4a, mp3, wav |
| m4v | MPEG-4 Video | mp4, wmv, avi |
| mkv | Matroska Video | mp4, wmv, avi |
| hevc | High Efficiency Video Coding | hevc |
| 3gp | Third Generation Partnership Project | mp4, wmv |
| mts | MPEG-2 Tranmission | mts, wmv, avi, mp4,wmv |
| ogg | Ogg Vorbis Compressed Audio | ogg, mp4 |
| aiff | Audio Interchange File Forma | aiff |
| aac | Advanced Audio Coding | aac |
| acm | Audio Compression Manager | acm |
| caf | Core Audio Format | wav |
| opus | Ogg Opus | opus, mp4, mp3, wav |
| mxf | Material Exchange Format | mxf |
| vtxt | AmiVoice Voice To Text | vtxt |
| eml | Electronic mail | eml, zip |
| msg | Microsoft Outlook Message | msg, zip |
| tnef | Transport Neutral Encapsulation Format | tnef |
| oft | Microsoft Outlook Template | oft |
| pst | Outlook Personal Folder | pst |
| mbx | Outlook Express Mailbox | mbx, zip |
| txt | Text | txt, pdf |
| json | JSON | json |
| ttml | Timed Text Markup Language | ttml |
| mpd | MPEG-Dash | mpd |
| xdw | DocuWork Image | xdw* |
| xbd | DocuWork Binder | xbd* |
| xct | DocuWork Container | xct* |
| crl | Certificate Revocation List | crl |
| spf | StorageCraft ShadowProtect | spf |
| prn | HP Printer Job Language data | prn |
| zei | ZUGFeRD | zei |
| utib | UTIB | utib |
| har | HTML Archive | har |
| story | Storyist Document | story |
| 7z | 7-zip Archive | 7z, zip, gz, xz, tar |
| gz/gzip | GNU Zipped Archive | gz, 7z, zip, xz, tar |
| rar | WinRAR Archive | rar, zip, 7z, gz, xz, tar |
| xz | XZ Archive | xz, zip, 7z, gz, tar |
| zip | ZIP Archive | zip, 7z, gz, xz, tar |
| alz | ALZip | zip, 7z, gz, xz, tar |
| tar | Tape Archive | tar, zip, 7z, gz, xz |
| bz2 | BZ2 Archive | zip, 7z, gz, xz, tar |
| lzma | LZMA Archive | zip, 7z, gz, xz, tar |
| lzh | LZH Archive | zip, 7z, gz, xz, tar |
| arj | ARJ Archive | zip, 7z, gz, xz, tar |
| cab | Cabinet Archive | cab, zip, 7z, gz, xz, tar |
| lz4 | Lempel-Ziv 4 Compressed Archive | lz4 |
| wsp | Windows Sharepoint | zip, 7z, gz, xz, tar |
| ace | WinAce archive format | zip, 7z, gz, xz, tar |
| tse | TIP Test Selection Engine | tse, zip, 7z, gz, xz, tar |
| tsez | TIP Test Selection Engine | tsez, zip, 7z, gz, xz, tar |
| tsec | TIP Test Selection Engine | tsec, zip, 7z, gz, xz, tar |
| egg | EGG archive format | zip, 7z, gz, xz, tar |
| gpkg | GeoPackage Encoding Standard | gpkg, zip |
| b3dm | Batched 3D Model | b3dm, zip |
| x3p | Xml 3D Surface Profile | x3p |
| asics | Associated Signature Container | asics |
| asice | Associated Signature Container | asice |
| jar | Java Application | jar |
| war | Java Web Application Archive | war |
| log | Log file | log |
| pck | System Center Configuration Manager Package Files | pck |
| aem | AppleSingle/AppleDouble Encoded Macintosh | aem |
| ribc | Research Institute on Building Cost | ribc |
| ribcd | RIBC Data Table | ribcd |
| esz | E-szigno | esz, zip |
| base64 | Base64 Encoding | base64 |
| yenc | yenc Encoding | yenc |
| zstd | Zstandard Compressed | zstd |
| yz1 | Yamazaki Zipper Compressed Archive | yz1* |
| scdoc | SpaceClaim Document | scdoc |
| mdzip | MagicDraw | mdzip |
| lz | Lzip Compressed Archive | lz |
| asar | Atom Shell Archive | asar |
| 3dml | 3D Mesh Layer | 3dml |
| easm | 3D CAD Assembly File | easm |
| vsix | Visual Studio Extension | vsix |
| blz | BriefLZ | blz |
| taz | TAR Zipped Archive | taz |

- (*) Only supported on Windows for now.
- For the archive sanitization, please enable it in the Compression tab

Sanitization is in BETA for these file types:

AVC, SPF, TWBX, UTIB, STORY, ASICS, ASICE, ES3, PCK, B3ML, B3DM, MDZIP, LZ, ASAR, MPD, DWFX, AVIF, 3DML, MPP, STP, VSIX, EASM, HEIF, YENC, VCF, IFC, LYRX, BLZ, X3P, TAZ

XML sanitization is specific to XML vulnerability. It does not eliminate other threat such as Microsoft Office XML formats.

HTML/TXT sanitization is designed for Email Security purposes, should not use for sanitizing normal HTML, TXT traffic. TXT with "Remove Invisible Characters" can be used for the LLM Guard use cases.

HWP: there are two versions of HWP, v3.0 and v5.0. v3.0 document can be created from only legacy old Hangul Word Processor. For this reason, we do not support HWP v3 and result in "failed to sanitize". We recommend this old version file as suspicious. If you need support for v3.0, please contact support.

XDW/XBD/XCT: Customers need to> install and activate DocuWorks 9 or newer on the system to use this feature

HEIC/HEVC/HEIF/AVC/AVIF: it is enabled on-demand, please contact Customer Support or Sales team to enable it.

## Single / Multiple Output File

If target contains only one file, it will be not zipped and treat as single output file. For example, If a PDF file has only one page, converts to JPG will be JPG. If a PDF file has more than one page, there will be multiple JPG files and will result in a ZIP file. The following sanitization result in potentially multiple files (single ZIP file).

- PDF->HTML
- PDF->IMG
- DOCX→HTML, IMG
- XLSX->HTML, CSV, IMG
- PPTX→HTML, IMG

**Notes:**

Deep CDR removes active content that can drive a malicious behavior. These objects are usually non-visual, such as javascript, hidden malicious code in an image (steganography). However, those objects can also be visible such as hyperlinks, active code that change the data (e.g. macros). Even though is not within CDR process's scope, it might also alter the content if it's configured to do so.

For images and media files, we don’t “edit” the content, which means the original file and sanitized file will have the same content. However, the quality may be altered due to several steps performed to disarm the content by decoding, processing and encoding it again.

**Known Issues**

- Conversion from HTML to an image would fail if the size of the HTML file is bigger than 90KB
- AutoCAD file (.DWG): with version 2007-2009, when removing macro from the original file (if it has), opening sanitize file will display an error message "Failed to load project from storage" appeared but the file still works as usual
- Support TXT in ASCII, UTF-8, Shift-JIS and ISO/IEC 8859-1 encoding only
- When converting Excel files to TXT, only the first sheet is converted
- Support AI in PDF format
- If the file names inside XCT contain multibyte characters after sanitization, it will be different from the original. As a workaround, users can change the system default code page setting by the following steps: Settings > Time & language > Language & region > Administrative language settings > Change system locale, and check Beta: Use Unicode UTF-8 for worldwide language support