<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-to-backup-and-restore-standalone-database-for-metadefender-c -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:31:16.248901 -->

# How to Backup and Restore standalone database for MetaDefender Core?

This document based on PostgreSQL official documents for backup and restore here

## Prerequisites

- No third‑party application needed
- Windows OS
- PostgreSQL built-in (Metadefender Core standalone mode)

## How to

- Backup database

**Please note**that you need to go to the folder`<installation_folder_MD_Core>/postgres/bin/`

to execute the command below, you need to run it on CMD (Command Prompt) with Administrator privileges.- To back up the database, you need to run the command below.

` `

`<installation_folder_MD_Core>/postgres/bin/pg_dump.exe -h <hostname> -p <port> -U <username> -W <database_name> > <output_path>`

- In order to use
`pg_dump`

to backup exactly database that you would like to backup, we need the database name. To get database name, you need to connect to PostgreSQL local:

`psql --host=localhost --port=5432 --username=postgres --password`

- It requires you to input the password for the user
`postgres`

. After you input the password, you will successfully log in to Postgres. For example:

- type
`\l`

to show all database instances in PostgreSQL.

- To exit PostgreSQL, you can type
`exit`

. - When you know your database instance name, you can use
`pg_dump`

to backup exactly database that you would like to backup.

`pg_dump.exe -h localhost -p 5432 -U postgres -W metadefender_core_zxs0rj > metadefender_core_zxs0rj.sql`

- After finished, you will see the file generated.

- Restore database

- To backup database, you need to stop Metadefender Core first. Then, please start PostgreSQL service by command below.

`<installation_folder_MDCore>\postgres\bin\pg_ctl.exe start -D "<PG_DATA_DIR>" -w -o -p5432`

- For example:

**NOTE**: If your MD Core is on the C drive (system drive), you'll need to utilize the system user to execute the command above for manually starting PostgreSQL.- To use system user, you need to download the PSTool provided by Microsoft PsTools - Sysinternals | Microsoft Learn
- Once you've downloaded PSTool, to utilize it, you must open Command Prompt with Administrator privileges. Next, navigate to the PSTool folder and execute the command
`PsExec.exe -i -s cmd.exe`

. Following this command, a new Command Prompt window will appear, indicating successful execution.

- To determine the user being utilized in the new CMD window, you can execute the command `whoami`

. This will provide you with the user information.

- Then, we will run the command to manually start PostgreSQL. For example: "c:\Program Files\OPSWAT\MetaDefender Core\postgres\bin\pg_ctl.exe" start -D "c:\Program Files\OPSWAT\MetaDefender Core\data\pg_data" -w -o -p5432

- You will see the output below.

- Once you've successfully initiated PostgreSQL manually, you'll need to log in to PostgreSQL and delete the current MD Core database. To accomplish this, you can utilize the following command:

`drop database metadefender_core_zxs0rj;`

- Here is example:

- When you dropped the current database of MD Core, you create the new database again with the same instance name.
- To create database, you can use the command below. Please note that the name of database should be the same.

`create database metadefender_core_zxs0rj;`

- You can recheck by command
`\l`

to list all database.

- You can see that the new database with name "metadefender_core_zxs0rj" created, and currently, it does not have any access privileges.
- Next, exit PostgreSQL and import your data from the the dump file to the new database. You can use command below to import the database.

` `

`<installation_folder_MDCore>\postgres\bin\psql.exe --host=localhost --port=5432 --username=postgres -f <YOU_DUMP_FILE> <database_name>`

- For example:

`.\psql.exe --host=localhost --port=5432 --username=postgres -f metadefender_core_zxs0rj.sql metadefender_core_zxs0rj`

- You will the output like this

- After you finish import database, you need to stop PostgreSQL. You can use command below to stop

`<installation_folder_MDCore>\postgres\bin\pg_ctl.exe stop -D "<PG_DATA_DIR>" -w -o -p5432`

- For example:

- Finally, you start Metadefender Core service. While starting, MD Core will create new internal user and grant access priviledge for the new database.
- You can recheck by access to PostgreSQL and show status all database, after MD Core service successfully start and running.

`psql --host=localhost --port=5432 --username=postgres --password`

- For example:

- You can see that the new database has new access privileges for
`internal_user`

`usr_a686fade0737fb766781618526d826b0046b3245`

If you require further assistance, please log a support case or chat with our support engineer.