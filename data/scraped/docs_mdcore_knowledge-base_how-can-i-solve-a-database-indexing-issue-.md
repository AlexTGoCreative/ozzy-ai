<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-can-i-solve-a-database-indexing-issue- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:28:04.193839 -->

# How Can I Solve a Database Indexing Issue?

While troubleshooting MetaDefender Core, you may encounter the following error in the logs:

*Failed to delete records, reason='ERROR: index "request_1_pkey" contains unexpected zero page at block 2760'.*

*invoke failed, out='QMap(("error", QVariant(QString, "ERROR: index "request_1_pkey" contains unexpected zero page at block 2760"*

This error indicates an issue with the **PostgreSQL index** on the request_1_pkey table.

**Root Cause**

The error typically occurs when an index in the **PostgreSQL** database becomes corrupted or unreadable. In this case, the request_1_pkey index is damaged, which prevents MetaDefender Core from performing certain operations.

**Solution**

To resolve the issue, you need to **rebuild (reindex)** the corrupted index using a PostgreSQL command.

**Step-by-Step Instructions**

**1. Open Command Prompt**

**2. Navigate to the PostgreSQL Binaries Folder**

cd "C:\Program Files\OPSWAT\MetaDefender Core\postgres\bin"

Adjust the path if MD Core is installed in a different location.

**3. Connect to the MetaDefender Core Database**

Run the following command to access PostgreSQL:

*psql.exe -U <your_postgres_username> -d metadefender_core_8gyrxm*

- Replace <your_postgres_username> with the correct PostgreSQL username used during installation.
- If prompted, enter the PostgreSQL password.

**4. Run the Reindex Command**

Once connected to the database prompt enter:

*Reindex index scan.request1 pkey;*

Please see the following example below:

If Further Assistance is required, please proceed to log a support case or chatting with our support engineer.