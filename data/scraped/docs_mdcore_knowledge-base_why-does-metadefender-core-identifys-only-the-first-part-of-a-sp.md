<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/why-does-metadefender-core-identifys-only-the-first-part-of-a-sp -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:34:42.265123 -->

# Why does MetaDefender Core Identifys Only the First Part of a Split Archive as an Archive File?

When scanning split archives with MetaDefender Core, you may notice that only the first segment (e.g., **archive.zip.001**) is detected as an archive, while subsequent parts (**.002**, **.003**, etc.) are labeled as **data**. This behavior is expected and stems from how split archives are structured and how File Type Engine interprets them.

### What Are Split Archives?

Split archives are large compressed files divided into smaller segments for easier distribution and storage. Instead of a single **archive.zip**, you might see:

`rchive.zip.001`

`archive.zip.002`

`archive.zip.003`

`...`

These parts are **not independent archives**; they must be reassembled before the data can be accessed. Tools like **WinRAR** and **7-Zip** automatically join these segments when you open the first part.

### How MetaDefender Core Processes Split Archives

**1. First Part Contains the Archive Header**

The **.001** file includes:

- The
**archive header**(e.g., ZIP or RAR signature). - Information about the compressed files inside.
- The initial portion of the compressed data.

MetaDefender Core leverages the **File Type Engine** to detect this header and classifies the file as a **Split Archive File**, as shown in the screenshot:

This allows MetaDefender Core to treat **.001** as the entry point for scanning and extraction.

**2. Subsequent Parts Contain Only Raw Data**

Files like **archive.zip.002**, **archive.zip.003**, etc.:

- Contain
**continuation data only**. - Lack headers or metadata to identify them as archives.
- Cannot be opened or scanned independently.

This is why MetaDefender Core labels them as **data**:

This allows MetaDefender Core to treat **.001** as the entry point for scanning and extraction.

This is standard behavior: these segments are inert on their own and meaningful only when combined with **.001**.

**Conclusion**

MetaDefender Core’s classification of only the first segment of a split archive as an archive file is not an error - it’s a reflection of how split archives are designed. The first file (**.001**) contains the critical header and structure needed to rebuild and scan the entire archive. The remaining files are simply data blocks that have no standalone meaning without the first part.

By focusing on **.001**, MetaDefender Core ensures accurate detection, efficient processing, and full threat analysis of multi-part archives. Users should always provide all parts of the archive during scans and remember that **without .001, the rest of the files cannot be properly analyzed or extracted**.

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.