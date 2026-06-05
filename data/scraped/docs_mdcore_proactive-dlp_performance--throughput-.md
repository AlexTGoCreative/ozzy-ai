<!-- source: https://www.opswat.com/docs/mdcore/proactive-dlp/performance--throughput- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:58:09.229298 -->

# Performance (Throughput)

We do not guarantee the same performance in your environment. Performance can vary significantly depending on data sets and systems used when running the tests. The sole purpose of this section of the User Guide is to provide a high-level indicator of performance impact when enabling Proactive DLP in your business logic.

## Windows System Info

- RAM: 32GB
- CPU: Intel® Core™ i7-6700 CPU @ 3.40GHz × 8
- OS: Windows Server 2019
- Disk Drive: 256GB SSD

## Linux System Info

- RAM: 32GB
- CPU: Intel® Core™ i7-4790 CPU @ 3.60GHz × 8
- OS: Ubuntu 20.04.1 LTS
- Disk Drive: 256GB SSD

## Resources

- Windows: MetaDefender Core v4.19.0 with 8 engines
- Linux: MetaDefender Core v4.19.0 with 5 engines

## Test Results

File type | Average file size (KB) | Total files | Sensitive files | Detection (s/file) | Detect + Redaction (s/file) | ||
|---|---|---|---|---|---|---|---|
Windows | Linux | Windows | Linux | ||||
| Text | 170 | 1456 | 728 | 0.04 | 0.05 | 0.04 | 0.05 |
| Text | 3174 | 864 | 592 | 0.25 | 0.21 | 0.25 | 0.22 |
| 392 | 1572 | 785 | 0.28 | 0.28 | 0.44 | 0.47 | |
| 6553 | 846 | 242 | 2.5 | 2.72 | 3.0 | 4.9 | |
| Word | 224 | 629 | 314 | 0.14 | 0.16 | 0.15 | 0.16 |
| Word | 2969 | 808 | 128 | 0.26 | 0.26 | 0.36 | 0.35 |
| Excel | 191 | 2942 | 1471 | 0.51 | 0.43 | 0.52 | 0.46 |
| Excel | 1904 | 840 | 192 | 3.3 | 2.8 | 3.3 | 2.7 |