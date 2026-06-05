<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/what-to-do-when-my-metadefender-core-instance-failing-to-load-wi -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:31:54.036052 -->

# What to do when my MetaDefender Core instance failing to load with error 'Extension setting up failed: extension: 'ekm', rc: '-610''?

This article is applied to MetaDefender Core releases deployed on Windows systems.

**Issue**

MetaDefender Core instance fails to load with the error message: `Extension setting up failed: extension: 'ekm', rc: '-610'`

.

**Root Cause**
The issue occurs because the Archive Engine stores temporary files in the `resources`

folder and fails to remove them under certain conditions. These residual files can prevent MetaDefender Core from starting correctly.

**Affected Versions/Platforms**

- MetaDefender Core: Versions prior to
**5.11.0** - Archive Engine: Versions prior to
**7.1**

**Workaround**
To restart the MetaDefender Core instance successfully, you must remove the leftover Archive Engine folders located in the Core's `resources`

directory.

**Steps**:

- Stop all MetaDefender Core services.
- Navigate to:
`C:\Program Files\OPSWAT\MetaDefender Core\data\resources`

- Delete
**all**files and subfolders related to Archive Engine. The folders might be named:

- 7z_XX_windows_XXXXXX
- compression_XX_windows_XXXXXX

- Start the MetaDefender Core service.

**Recommendation**
To prevent this issue from recurring:

- Upgrade the
**Archive Engine**to version**7.1**or later, where this cleanup issue is fixed. - Upgrade
**MetaDefender Core**to version**5.11.0**or later, where additional handling was implemented to enhance stability.

If **Further Assistance** is required, please proceed to log a support case or chatting with our support engineer.