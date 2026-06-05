<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-do-i-check-the-update-status-of-metadefender-core---s-licens -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:30:35.278337 -->

# How do I check the update status of MetaDefender Core’s licensed AV scan engines?

This article applies to all MetaDefender Core V4 and V5 releases deployed on Windows or Linux systems.

To check whether all of your licensed scan engines are downloaded and up-to-date, please go to your **MetaDefender Core Management Console>Inventory>Modules>Metascan** section, where you will see the current activation and update status of all engines in your deployment, along with associated details.

If certain engines appear to be out-of-date, as highlighted in the screenshot above, please compare these with the current engine update statuses from OPSWAT MetaDefender Core’s licensed AV scan engines online here.

The webpage linked above lists, in real time, the latest updates OPSWAT received from each of our licensed MetaScan engine vendors. On this page, customers can also select the Operating System of the MetaDefender Core they are using, for a clearer view of the associated engines, as highlighted in the image below.

**You can also confirm engine updates in MetaDefender Core by checking specific log entries:**

#### 1.Locate the Log Files

Navigate to the following directory on the MetaDefender Core server:

`C:\Program Files\OPSWAT\MetaDefender Core\data\log\rotate\core`

Inside this directory, you’ll find subfolders for each engine. Select the folder corresponding to the engine you want to check.
**Example:** For the FileType engine, open the folder named `oms_filetype`

.

**2.Confirm the Engine is Running Properly**

Look for a log entry similar to the following:

`[INFO] YYYY.MM.DD hh:mm:ss.mmm: (engine_process) Connected and initialized successfully [msgid: 228]`

**Explanation:**
This message confirms that the engine has started, connected, and initialized successfully. This is your key indicator that the engine is up and running.

**3.Verify Successful Engine Update**

To confirm the engine was updated and is now running the new version, search for the following sequence of log entries:

**a. Engine Shutdown (Old Version)**

`[INFO] YYYY.MM.DD hh:mm:ss.mmm: (engine_process) ==== Engine End ====, engineName='FileType', engineVersion='7.4.2-8214', dbVersion='7.4.3-8347' [msgid: 5589]`

**Explanation:**
This entry shows that the previous engine version `7.4.2-8214`

was shut down.

**b. Engine Startup (New Version)**

`[INFO] YYYY.MM.DD hh:mm:ss.mmm: (engine_process) ==== Engine Start ====, engineName='FileType', engineVersion='7.4.3-8347', dbVersion='7.4.3-8347', pid='6400' [msgid: 5585]`

**Explanation:**
This log confirms that the new engine version `7.4.3-8347`

has started successfully.

**c. Logging Reconfiguration**

`[INFO] YYYY.MM.DD hh:mm:ss.mmm: (engine_process) Swap log config done, filePath='E:/OPSWAT/MetaDefenderCore/data/logs/oms_filetype/oms_filetype.log', engineName='FileType', engineVersion='7.4.3-8347', dbVersion='7.4.3-8347' [msgid: 5586]`

**Explanation:**
This confirms that the system updated the logging configuration to reflect the new engine version.

If you have any difficulty **Updating or Checking the Update Status of MetaDefender Core’s Licensed AV Scan Engines**, please follow these instructions on How to Create Support Package With Bundle Tools?, before creating a support case or chatting with our support engineer.