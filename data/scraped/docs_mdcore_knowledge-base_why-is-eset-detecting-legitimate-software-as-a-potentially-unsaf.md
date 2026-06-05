<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/why-is-eset-detecting-legitimate-software-as-a-potentially-unsaf -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:32:18.839293 -->

# Why is ESET detecting legitimate software as a Potentially Unsafe Application (PUA/PUP)?

This article applies to all MetaDefender Core releases on Windows and Linux with **ESET antivirus licensed**.

**Issue:**

ESET may classify certain legitimate software tools as **Potentially Unsafe Applications (PUA/PUP)**.

These tools—such as remote access utilities, keyloggers, and password crackers—are commonly used for system administration but can be misused for malicious purposes.

To mitigate risk, ESET flags them under the **Win32/PrcView** category and similar classifications.

This classification does not indicate the software is malicious, only that it has the potential to be misused.

If you're experiencing excessive false positives, you can disable PUA/PUP detection in ESET by following the steps below.

- Go to
**Inventory > Modules > Metascan > ESET**. - Disable
**"Detect PUP/PUA"**.

**Workarounds:**

Disabling PUA/PUP detection may reduce protection against potentially risky tools.
As an alternative, you can **keep detection enabled** and **add detected files to the local whitelist**.

Refer to How to locally whitelist a file using allowlist for instructions.

**Related Articles:**

If **Further Assistance** is required, please proceed to log a support case or chatting with our support engineer.