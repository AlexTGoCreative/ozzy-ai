<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/deep-cdr-performance--throughput- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:56:19.965588 -->

# Deep CDR Performance (Throughput)

## Performance Tuning Guide

Processing time and resources consumed by the engine vary relatively greatly depending on several aspects, e.g., nature and complexity of file structure, number of objects or components inside input files, etc. File size can be an aspect but is not necessary to contribute proportionally to processing time and resources consumption.

Depending on load and its complexity, users can tune some parameters to achieve a suitable balance on processing speed and throughput.

**Timeouts**: a duration given to the engine for processing a file. Higher value gives the engine more chances to complete processing with complex files.- To set a value for this parameter, go to
**Workflow Management > Workflows >****[Workflow name]****> Deep CDR**

- To set a value for this parameter, go to
**Parallel count**: number of files being processed by the engine in parallel. Lower value puts low stress on the engine, giving it chances to complete processing with complex files.- Too large value can cause a domino effect that results in series of failures due to processing timed out.
- Ones may keep it at 20 by default and, when necessary, should not increase it over 40.
- To set a value for this parameter, see
**parallelcount_ds**on MetaDefender Configuration.

**Number of Image Processing Threads**: number of CPU cores being used for processing images. Higher value may drain CPU resources. Recommended value: <number of CPU cores>/8.- To set a value for this parameter, go to
**Inventory > Modules > Deep CDR**.

- To set a value for this parameter, go to

### Load with complex files

- Timeouts should be set to a high value, e.g., 30 minutes or 60 minutes.
- Parallel count should be set to a low value, e.g., 15 or 10.
- Number of Image Processing Threads should be set as recommended, <number of CPU cores>/8.

### Load with less complex files

- Timeouts can be set to a low value, e.g., 5 minutes or 10 minutes.
- Parallel can be set to a high value, e.g., 20 but should not exceed 40.
- Number of Image Processing Threads should be set as recommended, <number of CPU cores>/8.

## Throughput Test

We do not guarantee the same performance in your environment. Performance can vary significantly depending on data sets and systems used when running the tests. The sole purpose of this section of the User Guide is to provide a high-level indicator of performance impact when enabling sanitization in your business logic.

### Windows System Info

- RAM: 32.0 GB
- CPU: Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz
- OS: Window 10 x64
- Disk Drive: SSD 100.0 GB

### Linux System Info

- RAM: 32 GB
- CPU: 16
- OS: CentOS Linux release 7.6.1810
- Disk Drive: 100 GB

### Resources

MetaDefender Core version

- v5.x Windows:
**MetaDefender Core v5.0.0 with 8 engines** - v5.x Linux:
**MetaDefender Core v5.0.0 with 10 engines**

- v5.x Windows:
Default Deep CDR configuration

- Window version: 6.0.0.10522

### Test Results

| Conversion type | Total file | Average file size (KB) | Average Time (s) Windows | Average Time (s) Linux |
|---|---|---|---|---|
| pdf2pdf | 700 | 840.608 | 0.612 | 0.371 |
| ai2ai | 500 | 1218.385 | 0.319 | 0.249 |
| docx2docx | 700 | 423.394 | 0.352 | 0.299 |
| dotx2dotx | 600 | 595.435 | 0.371 | 0.312 |
| docm2docm | 600 | 159.145 | 0.451 | 0.246 |
| dotm2dotm | 450 | 891.869 | 0.422 | 0.384 |
| xlsx2xlsx | 750 | 188.021 | 0.327 | 0.208 |
| xlsm2xlsm | 300 | 255.125 | 0.459 | 0.359 |
| xlsb2xlsb | 400 | 91.181 | 0.262 | 0.224 |
| xltx2xltx | 500 | 175.446 | 0.281 | 0.196 |
| xltm2xltm | 600 | 242.917 | 0.373 | 0.206 |
| pptx2pptx | 600 | 920.062 | 0.548 | 0.563 |
| pptm2pptm | 450 | 1316.683 | 0.605 | 0.714 |
| potx2potx | 300 | 532.595 | 0.441 | 0.466 |
| potm2potm | 300 | 534.049 | 0.472 | 0.484 |
| ppsm2ppsm | 300 | 533.087 | 0.455 | 0.483 |
| ppsx2ppsx | 300 | 661.106 | 0.417 | 0.331 |
| doc2doc | 800 | 490.112 | 0.491 | 0.477 |
| dot2dot | 500 | 222.872 | 0.366 | 0.349 |
| xls2xls | 1000 | 711.596 | 0.656 | 0.408 |
| xlt2xlt | 900 | 856.013 | 0.740 | 0.379 |
| ppt2ppt | 500 | 1340.349 | 0.909 | 0.948 |
| pot2pot | 200 | 1455.610 | 0.752 | 0.673 |
| pps2pps | 200 | 1324.390 | 0.697 | 0.621 |
| jpg2jpg | 700 | 712.840 | 0.498 | 0.369 |
| png2png | 700 | 469.696 | 0.688 | 0.509 |
| bmp2bmp | 600 | 788.215 | 0.293 | 0.276 |
| gif2gif | 400 | 2055.788 | 0.833 | 0.406 |
| tiff2tiff | 300 | 125.937 | 2.336 | 1.589 |
| html2html | 2000 | 333.108 | 0.232 | 0.206 |
| rtf2rtf | 2000 | 119.624 | 0.195 | 0.192 |
| csv2csv | 1350 | 129.233 | 0.184 | 0.180 |
| hwp2hwp | 1111 | 538.338 | 0.283 | 0.253 |
| hwt2hwt | 1111 | 538.338 | 0.244 | 0.212 |
| hwpx2hwpx | 500 | 550.725 | 0.277 | 0.208 |
| jtd2jtd | 1112 | 799.942 | 0.226 | 0.212 |
| jtdc2jtdc | 900 | 930.778 | 0.203 | 0.187 |
| svg2svg | 1800 | 19.566 | 0.179 | 0.180 |
| emf2emf | 1900 | 343.260 | 0.187 | 0.183 |
| wmf2wmf | 2000 | 165.267 | 0.207 | 0.183 |
| vsdm2vsdm | 600 | 204.497 | 0.302 | 0.248 |
| vsdx2vsdx | 800 | 101.889 | 0.230 | 0.210 |
| vssm2vssm | 600 | 244.680 | 0.383 | 0.358 |
| vssx2vssx | 600 | 55.265 | 0.190 | 0.226 |
| vstm2vstm | 600 | 207.689 | 0.384 | 0.378 |
| vstx2vstx | 500 | 54.581 | 0.198 | 0.225 |
| vdx2vdx | 200 | 903.018 | 0.524 | 0.316 |
| vsx2vsx | 200 | 435.260 | 0.348 | 0.307 |
| vtx2vtx | 200 | 582.117 | 0.465 | 0.317 |
| txt2txt | 1000 | 101.732 | 0.174 | 0.197 |
| xml2xml | 2700 | 130.711 | 0.178 | 0.187 |
| xml-doc2pdf | 800 | 246.213 | 0.199 | 0.248 |
| xml-docx2pdf | 500 | 263.272 | 0.215 | 0.269 |
| xml-xls2pdf | 550 | 366.042 | 0.310 | 0.867 |
| odt2odt | 1000 | 271.258 | 0.331 | 0.462 |
| ott2ott | 1000 | 280.982 | 0.340 | 0.492 |
| ods2ods | 799 | 66.608 | 0.195 | 0.186 |
| ots2ots | 800 | 129.761 | 0.253 | 0.241 |
| odp2odp | 700 | 1128.388 | 0.645 | 1.008 |
| otp2otp | 700 | 699.048 | 0.449 | 0.701 |
| show2show | 450 | 825.788 | 0.469 | 0.442 |
| cell2cell | 700 | 136.628 | 0.228 | 0.204 |
| ico2ico | 500 | 191.910 | 0.184 | 0.191 |
| cur2cur | 550 | 43.626 | 0.176 | 0.171 |
| dwg2dwg | 900 | 567.597 | 0.194 | 0.234 |
| dwt2dwt | 900 | 567.597 | 0.193 | 0.22 |
| dws2dws | 900 | 567.597 | 0.195 | 0.225 |
| dwf2pdf | 400 | 85.633 | 0.768 | 1.029 |
| dxf2pdf | 800 | 77.971 | 0.177 | 0.565 |
| hta2hta | 600 | 366.105 | 0.374 | 0.357 |
| 3ds23ds | 550 | 1093.854 | 0.198 | 0.220 |
| dae2dae | 650 | 868.029 | 0.222 | 0.214 |
| drc2drc | 800 | 67.599 | 0.249 | 0.264 |
| u3d2u3d | 750 | 515.637 | 0.242 | 0.284 |
| rvm2rvm | 600 | 1251.032 | 0.204 | 0.234 |
| ics2ics | 600 | 31.381 | 0.182 | 0.231 |
| vcs2vcs | 750 | 0.436 | 0.174 | 0.287 |
| wdp2wdp | 400 | 2343.969 | 0.701 | 0.630 |
| dcm2dcm | 700 | 3320.839 | 0.324 | 0.357 |
| sldx2sldx | 600 | 920.062 | 0.536 | 0.554 |
| sldm2sldm | 450 | 1316.683 | 0.614 | 0.637 |
| webp2webp | 300 | 290.296 | 0.827 | 1.426 |
| lnk2lnk | 400 | 1.623 | 0.190 | 0.267 |
| avi2avi | 400 | 3005.967 | 0.312 | 0.157 |
| mp32mp3 | 300 | 4293.660 | 0.329 | 0.260 |
| mpeg2mpeg | 100 | 13352.240 | 0.695 | 0.343 |
| wav2wav | 100 | 13425.500 | 0.740 | 0.365 |
| mht2pdf | 700 | 308.138 | 0.452 | 0.214 |