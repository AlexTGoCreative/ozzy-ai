<!-- source: https://www.opswat.com/docs/mdcore/container-deployment/docker-image-published-on-opswat-docker-hub -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:08:03.905607 -->

# Docker image published on OPSWAT Docker Hub

OPSWAT publish all official **public** docker images on Docker Hub:

`opswat/metadefendercore-<os-type>:<version>`

The docker images are all bundled with the official release MetaDefender Core.

**Note:**

To ensure better tracking of the running image version, it is advisable for users to not use the `:latest`

tag when deploying containers in production.

Instead, it is recommended to specify a meaningful tag such as `5.13.2`

.

More information:

https://hub.docker.com/r/opswat/metadefendercore-debian

https://hub.docker.com/r/opswat/metadefendercore-rocky-nonroot

## Pull from the OPSWAT Docker Hub repository

`docker pull <repository>/metadefendercore-<platform>[:<version>]`

`<repository>`

- OPSWAT repository address`<platform>`

- can be`debian`

,`rocky`

`<version>`

- desired Core version (optional, default is`latest`

)

Example:

`docker pull opswat/metadefendercore-debian:latest`

## Run MetaDefender Core Docker image

`docker run -d [--name <container_name>] \`

` [-e "<env_var>=<value>"] \`

` [-v <ignition_folder>:<container_ignition_folder>] \ `

` [-v <host_folder>:<container_folder>] \`

` [-u <user ID>] \`

` -p <rest_port>:8008 <image_name>`

For IKARUS, `--shm-size=1gb`

should be added when starting the docker.

If you're using Kubernetes (K8S), the section below should be specified in the yaml file:

### [Parameter] Container Name

**Argument**: `--name <container_name>`

**Description**: Your container’s name

**Example**: `--name mdcore01`

### [Parameter] Init Details (Environmental Variables & Ignition File)

**Argument**: `-v <ignition_folder>:<container_ignition_folder> -e "<env_var>=<value>"`

**Description**:

You must configure MetaDefender Core (default local admin account, database connection etc.) before running MetaDefender Core docker image. It could be done via either one of following options **(do not use all options**, otherwise the ignition file settings will be ignore and overwritten):

- Using ignition file (
`-v`

) - Using environmental variables (
`-e`

) - Using
`IGNITION_JSON`

#### Option 1: Using environmental variables

`-e "<env_var>=<value>"`

: set an environmental variable to configure, each environmental variable need one -e argument.

Available environmental variables:

| Environmental variable | Necessity | |
|---|---|---|
| DB_MODE | required | database mode |
| DB_TYPE | required | database type |
| DB_HOST | required | database host |
| DB_PORT | required | database port |
| DB_USER | required | database user |
| DB_PWD | required | database password Support some specific characters: Not support |
| MD_INSTANCE_NAME | optional | instance name Note: For deployments using a remote database type and multiple containers, avoid assigning the same instance name |
| MD_USER | optional | username to create the first admin user |
| MD_PWD | optional | password to create the first admin user |
| MD_EMAIL | optional | email to create the first admin user |
| APIKEY | optional | the API key will be assigned to the admin user for license auto deactivation, activation, HTTPS enabling, proxy enabling and health check enabling. Requirements: - Must be exactly 36 characters in length.
- Can contain only lowercase hexadecimal characters [0-9],[a-f].
- Must include at least 10 lowercase letters [a-f].
- Must include at least 10 numeric digits (0-9].
- Must not contain more than 3 consecutive lowercase letters.
- Must not contain more than 3 consecutive numeric digits.
Note: At the moment, the application still accepts the simplified API key format. However, in future releases, if the provided API key does not comply with the defined security requirements, the container will fail to start during the initialization phase. |
| LICENSE_KEY | optional | an license key for license auto activation |
| STORAGE_PATH | optional | a full path of storage for sanitized, DLP processed and quarantined files |
| DATA_DIR | optional | a full path of MetaDefender Core working data directory |
| REST_ADDRESS | optional | REST binding address for MetaDefender Core’s Nginx to be allowed |
| REST_PORT | optional | REST binding port for MetaDefender Core’s Nginx to be allowed |
| IGNITION_JSON | optional | The ignition file settings, only JSON format is accepted. For example: For database password, this support some specific characters: Not support |
| CORE_CONF_JSON | optional | MetaDefender Core configuration file settings, only JSON format is accepted. For example: |
| CERT_PATH | optional | A full path to folder containing certificate file and private key file. There files must have the same filename meanwhile its extensions must be After being added, the filename without extension will be the name of the certificate in MetaDefender Core |
| MDCORE_CERT_PASSPHRASE | optional | A passphrase for encrypted private key when adding new certificate via CERT_PATH environment variable. Passphrase must be less than or equal 1023 characters Passphrase does not support single quote character |
| MDCORE_SSL_PROTOCOLS | optional | Specify the TLS version.
Accepted values (case-insensitive): `TLSv1.2,TLSv1.3` |
| MDCORE_SSL_ADVANCED_CONFIGS | optional | Configure advanced SSL settings such as cipher suites, session timeout, and caching. Accepted values (case-insensitive):
|
| MDCORE_DB_NAME | optional | Used for customizing the PostgreSQL database name of MetaDefender Core. By default, in shared DB mode, it is |
| MDCORE_DB_PRIVATE_USERNAME | optional | PostgreSQL server's internal user created for MetaDefender Core own operational purpose. If not specified, then MetaDefender Core will auto generate this user. Details: Customize Internal PostgreSQL User |
| MDCORE_DB_PRIVATE_PASSWORD | optional | PostgreSQL server's internal user password created for MetaDefender Core own operational purpose. If not specified, then MetaDefender Core will auto generate this user. Details: Customize Internal PostgreSQL User |
| PROXY | optional |
If the user wants to use proxy, set it to |
| PROXY_HOST | optional | Default: empty string
This field is required if PROXY is set to true |
| PROXY_PORT | optional | Default: empty string
This field is required if PROXY is set to true |
| PROXY_USER | optional | Username for proxy authentication |
| PROXY_PWD | optional | Password for proxy authentication |
| PROXY_EXCLUSION | optional | List of IPs to be added to proxy exception |
| MDCORE_HEALTH_CHECK | optional |
- Enables the health check feature.
- Applies up to three customized health check criteria, if configured.
- Disables the health check feature.
- Ignores all customized health check criteria.
- Enables the health check feature using default settings:
- Queue threshold
**:**100 - Minimum number of AVs
**:**0 - Required engine list: Empty
- Disable the threshold validation for all required engines
- Disables disk space threshold validation.
- Queue threshold
|
| MDCORE_QUEUE_THRESHOLD | optional | Health check criteria. Threshold for scan queue. Unit is %. Default: 100 (%). When allocated slots percentage exceeds the threshold, MetaDefender Core will set itself unhealthy. |
| MDCORE_MINIMUM_NUMBER_AV | optional | Health check criteria. Minimum number of AV engines. Default: 0. When number of active AV engines is less than or equal to the predefined value, MetaDefender Core will set itself unhealthy. |
| MDCORE_REQUIRED_ENGINES | optional | Health check criteria. A list of mandatory engines. Default: all the engines of a license. When any predefined engines are not active, MetaDefender Core will set itself unhealthy. |
| MDCORE_REQUIRED_ENGINES_THRESHOLD | optional | Use this setting to define threshold policies for required engines. ## FormatProvide the value in the following JSON format:
## Example
If this setting is
|
| MDCORE_DISK_SPACE_THRESHOLD | optional | Use this setting to define the threshold policy for disk space If To configure a threshold, enter an integer value representing the percentage ( |
| UPGRADE_DB | optional |
- Enable database upgrade process. This migrates Workflow Rules and other settings.
- Require
`MDCORE_UPGRADE_FROM_DB_NAME` variable. - Require super-user permission for
`DB_USER` . - Only support shared-database mode
`DB_MODE=4` and remote PostgreSQL`DB_TYPE=remote` .
- Database upgrade process will not run.
|
| MDCORE_UPGRADE_FROM_DB_NAME | optional |
If this variable does not exist, upgrade process will exit with code 1. |
| MIGRATE_HISTORY | optional |
- Database upgrade process migrates processing history, quarantine history, module update and configuration history.
- Database upgrade process will not migrate these kinds of data.
|
| MDCORE_LICENSE_COMMENT | optional |
Add the comment for the license when activating. |
| OLMS_HOST_URL | optional | The OLMS server endpoint. If users want to use OLMS, this variable is required. MetaDefender Core will treat OLMS higher priority than the normal way in license activation. |
| OLMS_TOKEN | optional | Token created from OLMS server. If users want to use OLMS, this variable is required. |
| OLMS_RULE | optional | Rule containing licenses from OLMS server. If users want to use OLMS, this variable is required. |
| OLMS_REST_PORT | optional |
OLMS port for REST API. |
| OLMS_SOCKET_PORT | optional |
OLMS port for socket interface. |
| OLMS_CONNECTION_TYPE | optional |
Can be |
| OLMS_USE_PROXY | optional |
If the user want to use proxy for the OLMS activation |
| OLMS_PROXY_SERVER | optional |
Proxy server address This field is required if OLMS_USER_PROXY is set to |
| OLMS_PROXY_PORT | optional |
Proxy port This field is required if OLMS_USER_PROXY is set to |
| OLMS_PROXY_PROXY_TYPE | optional |
Proxy type. Accepted values: - socks4
- socks5
- http
This field is required if OLMS_USER_PROXY is set to |
| OLMS_PROXY_USERNAME | optional |
Proxy username |
| OLMS_PROXY_PASSWORD | optional |
Proxy password |

The priority for overriding configs is:

JSON environmental variable (IGNITION_JSON, CORE_CONF_JSON) > single environmetal variable

For example, the following command will start a container with `global/restport=8009`

, and ignore `REST_PORT=8010`

:

`docker run -it --name core -p 8009:8009 \`

`-e DB_MODE=4 \`

`-e DB_TYPE=remote \`

`-e DB_HOST=192.168.0.1 \`

`-e DB_PORT=5432 \`

`-e DB_USER=postgres \`

`-e DB_PWD=admin \`

`-e REST_PORT=8010 \`

`-e IGNITION_JSON='{"user/name": "admin", "user/password": "admin", "user/email": "admin@local"}' \`

`-e CORE_CONF_JSON='{"global/restport": "8009", "logger/loglevel": "info"}' \`

`opswat/metadefendercore-debian:latest`

If missing any of the required environmental variables, docker run **will return failed** with error message `<ENV> is missing. Please set <ENV> before running container.`

When deploying in a Kubernetes environment with multiple replicas and a remote database, avoid setting the same instance name across all Pods. Specifically, be cautious when using the `MD_INSTANCE_NAME`

environment variable or the `global/instance_name`

field in `CORE_CONF_JSON`

.
Using a shared instance name will cause all Pods to use the same database private user. If any Pod restarts, this private user’s password will be regenerated, resulting in the other Pods becoming non-functional.

#### Option 2: Using ignition file

`-v <ignition_folder>:<container_ignition_folder>`

- (optional) mounting the folder containing the ignition file to the container’s folder

`<ignition_folder>`

- ignition folder path containing the ignition file`<ignition_folder>/ometascan.conf`

`<container_ignition_folder>`

- container’s folder to be mounted to`/opt/ometascan/core_data/opswat`

(by default)

The `internal/data_directory`

parameter is **not** supported in the `ometascan.conf`

ignition file when using containerized deployments. Any configuration of this parameter will be ignored.

#### Example

Setup a PostgreSQL version 14 server. After that, we assume that remote PostgreSQL server’s information is

- host =
**192.168.0.1** - port =
**5432** - user =
**postgres** - password =
**admin** - type =
**remote**

In case of local PostgreSQL:

- host =
**localhost** - type =
**local**

**Option 1 - using environmental variables**

`mkdir /ometascan-config`

`docker run -d --name core01 \`

` -e APIKEY=9f54e1b62d19a889d718cb3d9db145a4b8bb \`

` -e LICENSE_KEY=... \`

` -e DB_MODE=4 \`

` -e DB_TYPE=remote \`

` -e DB_HOST=192.168.0.1 \`

` -e DB_PORT=5432 \`

` -e DB_USER=postgres \`

` -e DB_PWD=123 \`

` -e MD_USER=localadmin \`

` -e MD_PWD=password \`

` -e MD_EMAIL=admin@local \`

` -e STORAGE_PATH=/metadefendercore \`

` -e IGNITION_JSON='{"user/name": "admin", "user/password": "admin", "user/email": "admin@local"}' \`

` -e CORE_CONF_JSON='{"global/restport": "8008", "logger/loglevel": "info"}' \`

` -e CORE_DATA_PATH=/home/core_data_dir \`

` -e CERT_PATH=/home/cert \`

` -p 8008:8008 opswat/metadefendercore-debian:latest`

**Option 2 - using ignition file**

`mkdir /ignition_folder`

`touch /ignition_folder/ometascan.conf`

``

`# Create /ignition_folder/ometascan.conf based on`

`# https://onlinehelp.opswat.com/corev4/10.2._Deployment_automation_support.html`

`echo "[global]" >> /ignition_folder/ometascan.conf`

`echo "dbmode=1" >> /ignition_folder/ometascan.conf`

` `

`echo "[dbserver]" >> /ignition_folder/ometascan.conf`

`echo "type = remote" >> /ignition_folder/ometascan.conf`

`echo "host = 10.40.50.194" >> /ignition_folder/ometascan.conf`

`echo "port = 5432" >> /ignition_folder/ometascan.conf`

`echo "user = postgres" >> /ignition_folder/ometascan.conf`

`echo "password = 123" >> /ignition_folder/ometascan.conf`

``

`echo "[user]" >> /ignition_folder/ometascan.conf`

`echo "name = localadmin" >> /ignition_folder/ometascan.conf`

`echo "password = password" >> /ignition_folder/ometascan.conf`

`echo "email = admin@local" >> /ignition_folder/ometascan.conf`

``

`docker run -d --name core01 \`

` -e "APIKEY=9f54e1b62d19a889d718cb3d9db145a4b8bb" \`

` -e "LICENSE_KEY=..." \`

` -v /ignition_folder:/opt/ometascan/core_data/opswat \`

` -p 8008:8008 opswat/metadefendercore-debian:latest`

**Option 3 - using ignition file with a full configuration package (.zip)**

**Note:**

a. When using Local Update Folder, let's make sure *pickupfolder* (*Pick up update from*) in the settings_export.json is correct.

- Format:
`<DATA_DIR>/path/to/update-folder`

- For example:
`"pickupfolder": "/opt/ometascan/core_`

data/var/lib/ometascan/update_`autoadd"`

b. If you want to activate license or enable HTTPS during container starting, please make sure apikey of an administrator in .zip package matches with

- apikey under [user] section (if present) in ignition file
- or
`APIKEY`

environment variable (if present)

`mkdir /ignition_folder`

`touch /ignition_folder/ometascan.conf`

``

`# Create /ignition_folder/ometascan.conf based on`

`# https://onlinehelp.opswat.com/corev4/10.2._Deployment_automation_support.html`

`echo "[global]" >> /ignition_folder/ometascan.conf`

`echo "dbmode=1" >> /ignition_folder/ometascan.conf`

` `

`echo "[dbserver]" >> /ignition_folder/ometascan.conf`

`echo "type = remote" >> /ignition_folder/ometascan.conf`

`echo "host = 10.40.50.194" >> /ignition_folder/ometascan.conf`

`echo "port = 5432" >> /ignition_folder/ometascan.conf`

`echo "user = postgres" >> /ignition_folder/ometascan.conf`

`echo "password = 123" >> /ignition_folder/ometascan.conf`

``

`echo "[user]" >> /ignition_folder/ometascan.conf`

`echo "name = localadmin" >> /ignition_folder/ometascan.conf`

`echo "password = password" >> /ignition_folder/ometascan.conf`

`echo "email = admin@local" >> /ignition_folder/ometascan.conf`

``

`echo "[config]" >> /ignition_folder/ometascan.conf`

`# Path to a file in json/zip format that contains a previously exported configuration to be imported`

`# Make sure the file path of zip to be mounted. For example, -v /path/to/:/path/to/`

`echo "import = /path/to/settings_export_package.zip" >> /ignition_folder/ometascan.conf`

`# Password to decrypt .zip configuration package.`

`# This can be omitted if using json file`

`echo "import_password = password" >> /ignition_folder/ometascan.conf`

``

`docker run -d --name core01 \`

` -e "APIKEY=9f54e1b62d19a889d718cb3d9db145a4b8bb" \`

` -e "LICENSE_KEY=..." \`

` -v /ignition_folder:/opt/ometascan/core_data/opswat \`

` -p 8008:8008 opswat/metadefendercore-debian:latest`

### [Parameter] User

**Argument**: `-u <user ID>`

**Description**: [Optional] run container with any user ID (UID) or group ID (GID). Range: [1000, 65533]

If not specified, the container will run as `root`

user. Otherwise, a user will be used for `non-root`

option.

**Example**: `-u 1011`

When running container with non-root user (`-u <user ID>`

param), you are expected to grant write permission to the _**ignition folder** _and _**ignition file**_for a user with the respectively uid on the host machine, before running the container. There are 2 ways to do this:

- Grant write permission for others (e.g. chmod 777)
- Change owner to uid 1011 or gid 1011 (e.g. chown 1011:1011), then grant write permission for owner or group owner (e.g.: chmod 755)

### [Parameter] Host Folder

**Argument**: `-v <host_folder>:<container_folder>`

**Description**: [Optional] mounting any additional folder from your host to the container (for managing config file, persistent data, storing log)

**Example**: `-v /var/mdcore:/temp`

### [Parameter] REST Port

**Argument**: `-p <rest_port>:<internal_port>`

**Description**: Port on the host machine to map with Core REST and web console management port

**Example**: `-p 30808:8008`

### [Parameter] Image Name

**Argument**: `<image_name>`

**Description**: MetaDefender Core docker image was built/pulled earlier

**Example**: `mdcore:debian`

## Start / Stop container

`docker start <container_name>`

`docker stop -t <timeout> <container_name>`

`<container_name>`

- container’s name for using later`<timeout>`

- timeout in second before Docker forces stop the container, this can result in lost data and restart the container abnormally, so this need to be set to long timeout, minimum 30 is recommended.

Example:

`docker stop -t 30 core01`

`docker start core01`

## Access to view MetaDefender Core logs

`docker logs [-f] [-n <number_of_lines>] <container_name>`

`<container_name>`

- container’s name for using later`[-f]`

- keep following the log`[-n <number_of_lines>]`

- number of last lines existed in log file will be shown instantly when running this command.

Example:

`docker logs -f -n 100 core01`

## Collecting Logs by Generating a Support Package

` `

`#Step 1: Run the following command to generate support package file`

`docker exec <container_name> /bin/bash -c "cd /opt/ometascan/core_data && /opt/ometascan/usr/bin/ometascan-collect-support-data.sh"`

``

`#Step 2: Copy the file from container to host machine`

`docker cp <container_name>:/opt/ometascan/core_data/<support-package-file>.tar.gz <target_folder>`

`<container_name>`

: The name of the container.`<support-package-file>.tar.gz`

: The generated support package file. You can find the file name in the console output after executing the command in Step 1.`<target_folder>`

: The destination folder on the host machine where the support package file will be saved.

Example:

` `

`docker exec mdcore /bin/bash -c "cd /opt/ometascan/core_data && /opt/ometascan/usr/bin/ometascan-collect-support-data.sh"`

``

`#output: Support file created: ometascan-5.14.1-1-support-1666784477.tar.gz`

``

`docker cp mdcore:/opt/ometascan/core_data/ometascan-5.14.1-1-support-1666784477.tar.gz ./`

## Configure MetaDefender settings

You can modify the `/etc/ometascan/ometascan.conf`

file. It can be modified in 2 ways:

- Directly inside the container by using docker exec to go inside the container and modify
- Mount the
`/etc/ometascan`

folder to host when starting the container, then modify the file on host folder

## Database Maintenance

` `

`#Run the following command`

`docker exec <container_name> /bin/bash -c "/opt/ometascan/usr/sbin/ometascan-vacuum-db"`

``

`#Example output:`

`Running vacuum with config file: /opt/ometascan/core_data/ometascan.conf`

`Postgres info: Postgres private user is not defined,`

`Postgres info: Database name, metadefender_core_brxnpu`

`Postgres info: Postgres private password is not defined,`

`Postgres info: Generating private password for the first time, metadefender_core_brxnpu`

`Postgres info: PG_DATA path in dat file = /opt/ometascan/core_data/var/lib/ometascan/pg_data,`

`Postgres info: PG_DATA path in conf file = /opt/ometascan/core_data/var/lib/ometascan/pg_data,`

`Postgres info: Same DIR,`

`Postgres info: The service and the config are mismatched, re-config the service..., /opt/ometascan/core_data/var/lib/ometascan/pg_data`

`Postgres info: PG_DATA path in dat file = /opt/ometascan/core_data/var/lib/ometascan/pg_data,`

`Postgres info: PG_DATA path in conf file = /opt/ometascan/core_data/var/lib/ometascan/pg_data,`

`Postgres info: Saving /var/tmp/ometascan/ometascan-pg.init,`

`Postgres info: Replacing /etc/init.d/ometascan-pg,`

`Postgres info: Checking for database upgrade,`

`Postgres info: DBMode is standalone, checking for deploymentId,`

`Postgres info: Upgrade database status: 0,`

`Postgres service init done`

`Creating connection with: localhost`

`Creating connection done`

`Created out dir: /opt/ometascan/core_data/analyze_and_cleanup_database`

`Working dir: /opt/ometascan/usr/lib/ometascan/postgres`

`Running vacuum DONE`

`<container_name>`

: The name of the container.

Reference: Database Maintenance | MetaDefender Core 4.19.0 or above