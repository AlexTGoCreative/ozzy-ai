<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/max-file-size -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:57:15.548905 -->

# Max File Size

This document does not specify the maximum supported file size that Deep CDR can handle. Instead, it only presents the file sizes that OPSWAT tested and the time Deep CDR takes to process a single large file.

Processing time may vary depending on the dataset used for testing. The primary factor affecting processing time is the number of objects within a file. For example, a large PDF with a single page containing a big image is processed faster than a large PDF with thousands of pages containing smaller images.

For audio and video files, Deep CDR verifies the input files against their respective specifications, remove unapproved objects, making the process fast. The table below does not cover conversion between different file types.

System spec:

- CPU: Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz (8 CPUs)
- RAM: 32GB
- SSD: 500GB

| File type | File Size (MB) | Processing time (s) | Notes |
|---|---|---|---|
| 2,112 | 393 | ||
| MS Excel 2003 | 1,998 | 86 | Microsoft 2003 allows max 2GB file size |
| MS Excel 2007 | 2,584 | 555 | |
| MS Word 2003 | 952 | 118 | Microsoft 2003 allows max 2GB file size |
| MS Word 2007 | 2,308 | 194 | |
| MS PowerPoint 2003 | 1,912 | 229 | Microsoft 2003 allows max 2GB file size |
| MS PowerPoint 2007 | 2,656 | 165 | |
| RTF | 507 | 30 | In Word, the maximum file size for RTF files is typically around 512MB |
| Visio 2013 | 775 | 79 | |
| Visio XML | 1,221 | 66 | |
| JPG | 361 | 571 | Dimensions: 40500 x 37670 |
| PNG | 530 | 443 | Dimensions: 43200 x 21600 |
| AVI | 827 | 5 | |
| MOV | 1,088 | 9 | |
| MP4 | 951 | 3 | |
| MPEG | 1,251 | 4 | |
| MTS | 1,304 | 3 | |
| MWV | 1,344 | 3 | |
| WEBM | 652 | 2 | |
| MP3 | 1,908 | 13 | |
| OGG | 798 | 4 | |
| WAV | 688 | 35 |