<!-- source: https://www.opswat.com/docs/mdcore/sandbox/supported-file-types -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:00:52.969527 -->

# Supported File Types

## File types

The Adaptive Sandbox engine supports a wide variety of file types, organized by category below:

## Application types

| File Type | OS | Comment |
|---|---|---|
| A3X | Windows | AutoIt v3 Script |
| AU3 | Windows | AutoIt v3 Script |

## Office Documents

| File type | OS | Comment |
|---|---|---|
| DOCX | Windows | Microsoft Word Document |
| DOCM | Windows | Microsoft Word Macro-Enabled Document |
| DOTX | Windows | Microsoft Word Template |
| DOTM | Windows | Microsoft Word Macro-Enabled Template |
| DOC | Windows | Microsoft Word Document |
| DOT | Windows | Microsoft Word Template |
| XLSX | Windows | Microsoft Excel Workbook |
| XLSM | Windows | Microsoft Excel Macro-Enabled Workbook |
| XLS | Windows | Microsoft Excel Workbook |
| XLTX | Windows | Microsoft Excel Template |
| XLTM | Windows | Microsoft Excel Macro-Enabled Template |
| PPTX | Windows | Microsoft PowerPoint Presentation |
| PPTM | Windows | Microsoft PowerPoint Macro-Enabled Presentation |
| PPSX | Windows | Microsoft PowerPoint Slide Show |
| PPT | Windows | Microsoft PowerPoint Presentation |
| PPAM | Windows | Microsoft PowerPoint Add-in |
| POTX | Windows | Microsoft PowerPoint Template |
| POTM | Windows | Microsoft PowerPoint Macro-Enabled Template |
| POT | Windows | Microsoft PowerPoint Template |
| ODT | Windows | OpenDocument Text |
| ODS | Windows | OpenDocument Spreadsheet |
| RTF | Windows | Rich Text Format |
| HWP | Windows | Hangul Word Processor |
| PUB | Windows | Microsoft Publisher |
| ONE | Windows | Microsoft OneNote exported section |

## Executable Files

| File type | OS | Comment |
|---|---|---|
| PE (EXE/DLL) | Windows | PE unpacking & re-analysis |
| PE (dotnet_pe) | Windows | PE.NET decompilation & re-analysis |
| PE (other) | Windows | Other specific PE types (SFX, Golang, Rust, etc.) |
| APK | Android | Android Application Package |
| CPL | Windows | Control Panel Extension |
| ELF | Unix | Executable and Linkable Format |
| LNK | Windows | Windows Shortcut |
| MSI | Windows | Windows Installer Package |

## Image Files

| File type | OS | Comment |
|---|---|---|
| DWG | Windows | VBA macro extraction |
| SVG | Windows | Scalable Vector Graphics |

## Media Files

| File type | OS | Comment |
|---|---|---|
| ASF | Windows | Windows Media Video |
| MP3 | Multi-OS | Digital Audio |

## Other

| File type | OS | Comment |
|---|---|---|
| Java | Multi-OS | Java Decompilation & re-analysis |
| MSC | Windows | Microsoft Management Console |
| OLE | Windows | Object Linking and Embedding |
| SCT | Windows | Windows Scriptlet |

## Adobe Files

| File type | OS | Comment |
|---|---|---|
| Multi-OS | Portable Document Format |

## Text Files

| File type | OS | Comment |
|---|---|---|
| HTML | Windows | Hypertext Markup Language |
| TXT | Windows | Plain Text |
| HTA | Windows | HTML Application |
| WSF | Windows | Windows Script File |
| BAT | Windows | Batch Script |
| JScript | Windows | Microsoft's JavaScript |
| JSE | Windows | JScript Encoded |
| Powershell | Windows | PowerShell Script |
| VBScript | Windows | Visual Basic Script |

## Email Files

| File type | OS | Comment |
|---|---|---|
| EML | Windows | Electronic Mail |
| MBOX | Windows | Mailbox Format |
| RFC822 | Windows | RFC822 Email Format |

## Archive types

The Adaptive Sandbox engine analyzes various archive file types, with certain types being processed through the Archive Engine, as listed below:

| Archive Type | Type-specific analysis | Comment |
|---|---|---|
| 7z | N/A | Extracted by Archive engine |
| ACE | N/A | Extracted by Archive engine |
| BZIP2/BZ2 | N/A | Extracted by Archive engine |
| CAB | Extracted by Archive engine | |
| CHM | YES | |
| DEB | NO | Extracted by Archive engine |
| ISO | NO | Extracted by Archive engine |
| PKG | NO | |
| RAR | N/A | Extracted by Archive engine |
| SFX (PEEXE) | YES | |
| TBZ2 | N/A | Extracted by Archive engine |
| TAR | N/A | Extracted by Archive engine |
| TGZ | N/A | Extracted by Archive engine |
| VHD | N/A | Extracted by Archive engine |
| XPI | NO | Extracted by Archive engine |
| ZIP | N/A | Extracted by Archive engine |