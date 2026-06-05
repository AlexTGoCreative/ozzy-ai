<!-- source: https://www.opswat.com/docs/mdcore/metascan-engines/supported-file-type -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:55:47.793013 -->

# Supported file type

Engine Name | Supported File Type |
|---|---|
| CrowdStrike Falcon ML | Portable Executable (PE) Mach object file (Mach-O) Executable and Linkable Format (ELF) CDF & OOXML based Microsoft Office files Adobe File (PDF) |
| Webroot SMD | PE and JS embedded on PDF |
| RocketCyber | Any windows file that contains a PE header. That would include the file format for Windows executables, object code, and DLLs in both 32-bit and 64-bit versions. |
| Scrutiny | exe, dll, sys. |
| Cylance | Windows executables (.acm, .ax, .cpl, .drv, .efi, .mui, .ocx, .src, .sys, .tsp, .exe, .dll) macOS executables (.o, .dylib, .bundle) Linux executables (.o, .ko, .mod, .so) OLE files (.doc, .xls, .ppt) OOXML files (.docx, .xlsx, .pptx) PDF files (.pdf) Archive files (.zip, .7z, .rar, .tar, .gz, .bz2, .xz)
|
| SentinelOne | Windows PE format, Linux ELF format, MACH format (Future), PDF format, DOS COM file, OLE compound file format, OpenXML Document File Format (.docx, xlsx, pptx...), ZIP Archive file format, RAR Archive file format, LZMA Archive file format, BZIP2 Archive file format, TAR Archive file format, CABINET Archive file format, SFX Archive file format, Windows .NET PE File, Microsoft LNK file format, Email Storage Format, Powershell Script files, Python script executable file, Linux shell script executable file, gzip compressed file, PHP script file, ASP script file, ASP.NET Core script file, Batch file, JavaScript file, VBScript file |

Apart from the engines mentioned above, the other antivirus engines do not have specific file type limitations.