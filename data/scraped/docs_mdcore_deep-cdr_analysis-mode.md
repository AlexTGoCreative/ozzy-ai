<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/analysis-mode -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:56:08.611673 -->

# Analysis mode

If your integrations don't need to use the sanitized file, you can enable this configuration to have a better performance.

To enable this feature: Workflow Management > [Workflow Name] > Deep CDR > Advanced > Enable Analysis Mode (the "Include Sanitization Details" must be enabled)

When this feature is enabled, **the sanitized file is not generated**

#### JSON output

**File is processed with the analysis mode**

JSON

`{`

` "action_ran": "Sanitization Skipped",`

` "sanitization_details": {`

` "skipped_reason": "analysis_mode",`

` "description": "Sanitization is skipped due to analysis mode being selected.",`

` "details": [`

` {`

` "action": "none",`

` "object_name": "XML content"`

` },`

` {`

` "action": "none",`

` "count": 1,`

` "object_name": "image"`

` },`

` {`

` "action": "none",`

` "description": "Sanitization is skipped due to analysis mode being selected.",`

` "details": [`

` {`

` "action": "none",`

` "count": 5,`

` "object_name": "attachment"`

` },`

` {`

` "action": "none",`

` "count": 1,`

` "object_name": "hyperlink"`

` }`

` ],`

` "file_name": "Portfolio.pdf",`

` "object_name": "PDF file",`

` "skipped_reason": "analysis_mode"`

` }`

` ]`

` }`

`}`

**File type is not supported by the analysis mode**

JSON

` `

`{ `

` "actions_ran": "Sanitization Skipped",`

` "sanitization_details": {`

` "description": "Processing is skipped due to analysis mode being selected but not supported for the source and target types.",`

` "details": [],`

` "skipped_reason": "unsupported_analysis_mode"`

` }`

`}`

#### Supported file types

- DOCX, DOCM, DOTX, DOTM, DOC, DOT
- PPTX, PPTM, POTX, POTM, PPSX, PPSM, PPT, POT, PPS
- XLSX, XLSM, XLTX, XLTM, XLSB, XLS XLT
- ODT, OTT, ODP, OTP, ODS, OTS
- VDX, VTX, VSX, VSDM, VSDX, VSSM, VSSX, VSTM, VSTX
- PDF, AI
- CELL, SHOW
- SLDM, SLDX
- XML, SVG, CSV, TXT, JSON
- ICS, VCS
- CRL
- RTF
- HTML, HTA
- HWP, HWT, HWPX
- JTD, JTDC
- EMF, WMF
- P21, SFC, JWC, JWW
- LNK
- XDW
- DWG, DWS, DWT
- Images

#### Performance

File types | Sanitization mode (s) | Analysis mode (s) | Difference (%) |
|---|---|---|---|
| MS Word 2007 | 0.397 | 0.163 | 143 |
| MS Excel 2007 | 0.458 | 0.316 | 44 |
| MS PowerPoint 2007 | 3.518 | 0.763 | 361 |
| MS Word 2003 | 0.248 | 0.148 | 67 |
| MS Excel 2003 | 0.224 | 0.064 | 250 |
| MS PowerPoint 2003 | 9.161 | 4.733 | 93 |
| 0.457 | 0.131 | 248 | |
| XML | 0.039 | 0.022 | 77 |
| RTF | 0.039 | 0.014 | 178 |
| JWW | 0.145 | 0.004 | 3525 |
| JWC | 0.025 | 0.003 | 733 |
| Calendar | 0.014 | 0.003 | 366 |
| Visio XML | 0.573 | 0.069 | 730 |
| OpenDocument Text | 0.728 | 0.136 | 435 |
| OpenDocument SpreadSheet | 0.356 | 0.161 | 121 |
| OpenDocument Presentation | 4.4 | 0.539 | 716 |