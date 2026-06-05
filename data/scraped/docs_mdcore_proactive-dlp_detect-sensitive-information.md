<!-- source: https://www.opswat.com/docs/mdcore/proactive-dlp/detect-sensitive-information -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:59:50.222500 -->

# Detect sensitive information

The main feature of the Proactive DLP engine is to detect and block sensitive data in files, including credit card numbers and social security numbers. The engine supports a wide range of file types, including Microsoft Office documents and PDF.

## Sensitive Data

| Financial Information | 1) Credit Card Number (CCN) 2) ABA Routing Number 3) U.S. Bank Account 4) International Banking Account Number (IBAN) 5) International Securities Identification Number (ISIN) 6) SWIFT Code |
| Personal identity information | 1) Japanese Personal My Number 2) U.S. Individual Taxpayer Identification Number (ITIN) 3) U.S. Social Security Number (SSN) 4) Turkish Identification Number (Kimlik No.) 5) Israeli National ID Number 6) Indian Aadhaar Number 7) Australian Tax File Number (TFN) 8) Indian Permanent Account Number (PAN) 9) Turkish Passport Number 10) Turkish Phone Number |
| Network and device information | 1) IPv4 address or subnet mask Classless 2) Inter-Domain Routing (CIDR) 3) International Mobile Equipment Identity (IMEI/IMEISV) |
| Corporation information | 1) Australian Company Number (ACN) 2)Australian Business Number (ABN) |
| Drug and health information | 1) Australian Medicare Number 2) U.K. National Health Service Number (NHS) 3) ICD-10 Code 4) ICD-9 Code |
Sensitive information (Detect with AI) | 1) Driver's License Number 2) National ID Number 3) Passport Number 4) Date of Birth 5) Social Security Number 6) Personal Name 7) Phone Number 8) Birth Certificate Number 9) UK Tax Identification Number 10) UK Electoral Roll Number 11) UK National Insurance Number 12) Common Medical Condition 13) U.K. National Health Service Number (NHS) 14) U.S. National Drug Code (NDC) 15) Blood Type 16) Vehicle Identification Number 17) Credit Card Number |

Additionally, any specific data pattern can be detected using custom regular expressions

**Defining so simple regexes is not the recommended way to use this engine, For example: \d , \w.** _Because most documents contain many numbers, so the complexity and time needed to scan are going to be increased a lot when you define something so simple. Turning redaction on with this regex would cause even worse performance.

## Certainty score

Certainty score is defined by the relevance of the given hit in its context . It is calculated based on multiple factors such as the number of digits, Bank Identification Number (BIN) lookup, context ...

SSN Certainty levels

- High
- Medium
- Low

CCN/IPv4/ CIDR Certainty levels

- Very High
- High
- Medium
- Low
- Very Low

Custom RegEx Certainty levels

- Medium
- High
- Very High

Custom metadata Certainty levels

- High

## Supported File Types

### Text and Documents

- Ansi Text (*.txt)
- ASCII Text
- CSV (Comma-separated values) (*.csv)
- Tab-separated values (*.tsv)
- iCalendar (*.ics, *.vcs)
- Microsoft Excel for Mac 2.2, 3, 4, 5, 98, 2001, X, 2004, 2008, 2011
- Microsoft Excel for Windows 2, 3, 4, 5
- Microsoft Excel 95, 97, 2000, XP, 2003, 2007, 2010, 2013, 2016 (*.xls)
- Microsoft Excel Office Open XML 2007, 2010, 2013, and 2016 (*.xlsx)
- Microsoft Office Excel XML (*.xml)
- Microsoft PowerPoint 3, 4, 95, 97, 98, 2000, 2001, 2002, 2003, 2004, 2007, 2008, 2010, 2011, 2013, 2016 (*.ppt)
- Microsoft PowerPoint Office Open XML 2007, 2010, 2013, and 2016 (*.pptx)
- Microsoft PowerPoint 97-2003 Template (*.pot)
- Microsoft PowerPoint Template (*.potx)
- Microsoft PowerPoint Show (*.ppsx)
- Microsoft PowerPoint Macro-Enabled Presentation (*.pptm)
- Microsoft PowerPoint Macro-Enabled Show (*.ppsm)
- Microsoft PowerPoint Macro-Enabled Template (*.potm)
- Microsoft PowerPoint 97-2003 Show (*.pps)
- Microsoft Office PowerPoint XML (*.xml)
- Microsoft Rich Text Format (*.rtf)
- Microsoft Word for DOS 1, 2, 3, 4, 5, 6 (*.doc)
- Microsoft Word for Mac 1, 3, 4, 5, 6, 98, 2001, X, 2004, 2008, 2011
- Microsoft Word for Windows 1, 2, 6 (*.doc)
- Microsoft Word 95, 97, 98, 2000, 2002, 2003, 2007, 2010, 2013, 2016 (*.doc)
- Microsoft Word 2003 XML (*.xml)
- Microsoft Word Office Open XML 2007, 2010, 2013, 2016 (*.docx)
- Microsoft/Open XML Paper Specification (_.xps, ._oxps)
- Ichitaro Document (*.jtd)
- OpenOffice/LibreOffice versions 1, 2, 3, 4, and 5 documents, spreadsheets, and presentations (*.sxc, *.sxd, *.sxi, *.sxw, *.sxg, *.stc, *.sti, *.stw, *.stm, *.odt, *.ott, *.odg, *.otg, *.odp, *.otp, *.ods, *.ots, *.odf) (includes OASIS Open Document Format for Office Applications)
- PDF files (*.pdf), note: Encrypted PDF files cannot be indexed, unless the PDF file can be opened without a password and the PDF file permissions allow for text extraction.
- PDF Portfolio files (*.pdf), including embedded non-PDF documents.
- Unicode (UCS16, Mac or Windows byte order, or UTF-8)
- XML (*.xml)
- XML Schema Description Files (*.xsd)
- JSON (*.json)
- Python script, ASCII text executable (*.py)
- Artificial Intelligence Markup Language (*.aiml)
- Microsoft ASP.NET Web Form (*.aspx)
- PHP Hypertext Preprocessor (*.php)
- PowerShell Script (*.ps1)
- Atom web feed (*.atom)
- GPS eXchange Format (*.gpx)
- Resource Description Framework (*.rdf)
- Open Office XML Relationships (*.rels)
- RSS web feed (*.rss)
- Visual Basic Script Files (*.vbs)
- Compass and Ruler geometry (*.zir)
- Document Type Definition (*.dtd)
- Tableau Workbook (*.twb)
- Tableau Datasource (*.tds)
- Tableau Bookmark (*.tbm)
- Windows Script File (*.wsf)
- Bourne Again Shell (
*.bash) Virtual Contact File (*.vcf)

### Email, HTML

- EML (emails saved by Outlook Express) (*.eml)
- MSG (emails saved by Outlook), including attachments (*.msg)
- Eudora MBX message files (*.mbx)
- HTML (*.htm, *.html)
- MIME Encapsulation of Aggregate HTML Documents (.mht)
- Hypertext Markup Language Application (.hta)

### Media (Metadata check only)

- Adobe Photoshop images (*.psd)
- ASF media files (*.asf)
- MP3 (*.mp3)
- WMA media files (*.wma)
- WMV video files (*.wmv)
- GIF (*.gif)
- EMF (*.emf)
- WMF (*.wmf)
- SWF (*.swf)
- MOV (*.mov)

## Supported File Types by AI

- Ansi Text (*.txt)
- ASCII Text
- Microsoft PowerPoint 3, 4, 95, 97, 98, 2000, 2001, 2002, 2003, 2004, 2007, 2008, 2010, 2011, 2013, 2016 (*.ppt)
- Microsoft PowerPoint Office Open XML 2007, 2010, 2013, and 2016 (*.pptx)
- Microsoft PowerPoint 97-2003 Template (*.pot)
- Microsoft PowerPoint Template (*.potx)
- Microsoft PowerPoint Show (*.ppsx)
- Microsoft PowerPoint Macro-Enabled Presentation (*.pptm)
- Microsoft PowerPoint Macro-Enabled Show (*.ppsm)
- Microsoft PowerPoint Macro-Enabled Template (*.potm)
- Microsoft PowerPoint 97-2003 Show (*.pps)
- Microsoft Rich Text Format (*.rtf)
- Microsoft Word for DOS 1, 2, 3, 4, 5, 6 (*.doc)
- Microsoft Word for Mac 1, 3, 4, 5, 6, 98, 2001, X, 2004, 2008, 2011
- Microsoft Word for Windows 1, 2, 6 (*.doc)
- Microsoft Word 95, 97, 98, 2000, 2002, 2003, 2007, 2010, 2013, 2016 (*.doc)
- Microsoft Word Office Open XML 2007, 2010, 2013, 2016 (*.docx)
- PDF files (*.pdf), note: Encrypted PDF files cannot be indexed, unless the PDF file can be opened without a password and the PDF file permissions allow for text extraction.
- PDF Portfolio files (*.pdf), including embedded non-PDF documents.
- Portable Network Graphics (*.png)
- JPEG Image (*.jpeg, *.jpg)
- JSON (*.json)