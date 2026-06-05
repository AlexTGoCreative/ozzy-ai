<!-- source: https://www.opswat.com/docs/mdcore/installation -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:05:08.104904 -->

# Recommended System Configuration

MetaDefender Core supports a wide range of deployment options, including air-gapped environments, providing the flexibility to choose the environment that best suits customers' requirements and infrastructure.

- Physical server.
- Virtualization platforms like VMware, Hyper-V and XenServer.
- Cloud Deployment.
- Container Deployment.
- MetaDefender Cluster Deployment.

Before installing MetaDefender Core, please refer to the recommended minimum system configuration listed below. The requirements are based on a standardized customer deployment and may require more or less resources to achieve the level of performance desired in your environment. Please note that the server specifications are built to allow a high volume daily processing. Please refer to Performance and Load Estimation for more details.

The recommendations below are for MetaDefender Core, API usage only. For any other use cases, please consult the user guide of the licensed products for accurate recommendations.

For certain use cases these might be adjusted and customized on specific needs and SLAs. We highly recommend to engage our ProServ team to assist in fine tuning MetaDefender and get the maximum performance out of your systems.

## Microsoft Windows Deployments

### [Windows] Supported Operating Systems

**Only support 64-bit platforms**.

- Windows Server 2019, 2022, 2025
- Windows 11 only for End-User systems (e.g. Kiosk deployments):
- 11 23H2
- 11 IoT (22H2)
- 11 24H2 and 11 IoT 24H2
- 11 25H2 and 11 IoT 25H2
- Based on Microsoft License Terms, you're not allowed to use Windows Desktop as a server, therefore, MetaDefender Core can't be used on these systems for server use cases.

Fast Startup mode is unsupported.

End-customer is responsible of verifying the OS license agreement and choose the right OS based on their planned usage of MetaDefender.

OPSWAT has discontinued support for Windows Server 2016 and Windows 10 versions prior to 21H2 in MetaDefender Core and its associated engines starting October 2025.

More details at End of Life Support for Windows Server 2016 and Windows 10 versions before 21H2 in MetaDefender Core.

### [Windows] Recommended System Configuration

The resources listed below (CPU, RAM, disk space) are the minimum recommended for MetaDefender Core:

| Package | CPU cores | Free System RAM | Free Disk Space |
|---|---|---|---|
| MetaDefender Core 8 | 8 | 8 GB | 16 GB (product and engines) + 50GB (temp files during processing) + 100GB (when using local PostgreSQL database) |
| MetaDefender Core 12 | 16 | 16 GB | 24 GB + 50 GB + 100 GB |
| MetaDefender Core 16 | 16 | 16 GB | 32 GB + 50 GB + 100 GB |
| MetaDefender Core 20 | 32 | 16 GB | 40 GB + 50 GB + 100 GB |
| MetaDefender Core MAX | 32 | 32 GB | 120 GB + 50 GB + 100 GB |

- SSD is recommended for system where MetaDefender Core is installed.
- See more disk space details in Storage Usage Information.
- For virtualization deployments such as VMware, Hyper-V, and XenServer, we recommend static resource allocation for CPU, RAM, and SSD storage to prevent stability issues.
- If Deep CDR and/or Proactive DLP are licensed, add at least 8 GB of additional RAM and 4 additional CPU cores (for a total of at least 12 CPU cores).
- If Embedded Adaptive Sandbox licensed, add at least 8 GB of additional RAM and 4 additional CPU cores (for a total of at least 12 CPU cores).
- SBOM processing requires additional disk space. Ensure at least 15 GB of free disk is available for the engine to operate properly.

### [Windows] Third Party Dependencies

- .NET framework 4.5 or above
- Microsoft Visual C++ Redistributable for Visual Studio 2015–2022 (x64), version 14.44 or later.
- PostgreSQL: Only applicable when using a pre-installed PostgreSQL server running remotely.
- From 14.5 to 14.22
- From 15.7
- From 16.4

Some engines also have dependencies as described below:

| Engine Name | Dependency |
|---|---|
| Deep CDR | Microsoft Visual C++ 2017 Redistributable Package (Only applicable to engine version 5.8.0 or above) |
| Archive engine | Microsoft Visual C++ 2015 - 2022 Redistributable x86 (Required for YZ1 extraction/compression) |
| ESET | MetaDefender Core temporary directory should have more than 200MB free disk space |
| Embedded Adaptive Sandbox | Amazon Corretto 17Visual C++ Redistributable for Visual Studio is required for versions prior to 2.2.0. For more details: Dependencies and system Requirements |
| Reputation | Visual C++ Redistributable for Visual Studio version 14.44 or higher. CPU must support AVX2 (BMI2) instruction set. |
| Proactive DLP | CPU must support AVX2 and SSE4.1 instruction set to use OCR feature |
| Scrutiny | Microsoft Visual C++ 2015 - 2019 Redistributable x86 and x64 |
| Systweak | .NET runtime 6.0, 7.0 or 8.0 |
| Bkav Pro | Microsoft Visual C++ 2015 - 2022 Redistributable x64 |

### [Windows] Installation Details

MetaDefender Core on Windows uses "C:\Program Files\OPSWAT" folder for storing resources or the installation directory.

MetaDefender will use its resources folder to store temp files as part of the analysis.

**It's recommended to exclude this folder from real-time protection monitoring***.* Knowledge base:

- How to set up exclusions on anti-malware software to prevent disruption
- Mitigating scan failure triggered by real-time protection service
- Can local AVs interrupt ongoing scans?

## Linux Deployments

### [Linux] Supported Operating Systems

**Only support 64-bit platforms.**

- Red Hat Enterprise Linux 8, 9
- Rocky Linux 9
- Oracle Linux 9 (version 9.5 or later)
- Debian 11, 12, 13
- Ubuntu 22.04, 24.04
- Amazon Linux 2023 is supported via Amazon Machine Image (AMI)

The product may not function correctly with Red Hat Enterprise Linux or Rocky Linux operating systems running old kernel version such as 372.9, 372.13.

The recommended solution is to * upgrade to at least kernel version 372.26*. This should help ensure proper functionality.

OPSWAT will discontinue support for the following OS in MetaDefender Core and its associated engines:

- Debian 11 since
**July****2026**.

Some AV engines could be failed to initialize and run on MetaDefender Core (e.g. ESET, Kaspersky) due to execution permission required by them on `/var/tmp/ometascan`

folder.

Please follow steps at Why have the ESET and Kaspersky scan engines failed to initialize on the hardened Linux OS? for remediation details.

End-customer is responsible of verifying the OS license agreement and choose the right OS based on their planned usage of MetaDefender.

### [Linux] Recommended System Configuration

The resources listed below (CPU, RAM, disk space) are the minimum recommended for MetaDefender Core:

| Package | CPU cores | Free System RAM | Free Disk Space |
|---|---|---|---|
| MetaDefender Core 5 | 4 | 4 GB | 10 GB (product and engines) + 50GB (temp files during processing) + 100GB (when using local PostgreSQL database) |
| MetaDefender Core 10 | 8 | 8 GB | 20 GB + 50 GB + 100 GB |
| MetaDefender Core MAX | 16 | 16 GB | 40 GB + 50 GB + 100 GB |

- SSD is recommended for system where MetaDefender Core resides on.
- See more disk space details in Storage Usage Information.
- For virtualization deployments such as VMware, Hyper-V, and XenServer, we recommend static resource allocation for CPU, RAM, and SSD storage to prevent stability issues.
- If Deep CDR and/or Proactive DLP are licensed, add at least 8 GB of additional RAM and 4 additional CPU cores (for a total of at least 12 CPU cores).
- If the Embedded Adaptive Sandbox is licensed, add at least 8 GB of additional RAM and 4 additional CPU cores (for a total of at least 12 CPU cores).
- SBOM processing requires additional disk space. Ensure at least 15 GB of free disk is available for the engine to operate properly.

### [Linux] Third Party Dependencies

**Dependencies list:**

- openssl
- grep
- lib32stdc++6 (>= 4.5)
- libc6-i386 (>= 2.10)
- procps
- zlib1g
- libcurl3 (>= 7.19.7)
- libcurl4
- tar (Ubuntu/Debian)
- lsb_release (Rocky Linux 9.x/Red Hat 9.x)
- postgresql:
- From 14.5 to 14.22
- From 15.7
- From 16.4

Not all the above dependencies will need to be installed, it is dependent on different Unix distro and version

Some engines also have dependencies as described below:

| Engine name | Dependency |
|---|---|
| Archive engine | To extract password protected MS Office files, you need to install .NET 8 dependencies, libgdiplus 6.0.4 or libgdiplus 6.0.5 Rocky Linux 9.x/Red Hat 9.x: libnsl |
| Deep CDR | - Rocky Linux 9.x: libgomp, ncurses-compat-libs, libnsl
- CentOS: libgomp, ncurses-compat-libs
- Red Hat 8.x: libgomp, ncurses-compat-libs, libnsl
- Red Hat 9.x: libgomp, ncurses-compat-libs, libnsl, compat-openssl11
- Ubuntu/Debian: libgomp1, libncurses5
- libgdiplus 6.0.4 or libgdiplus 6.0.5
- .NET 8 dependencies
|
| Embedded Adaptive Sandbox | openjdk-17-jre For more details: Dependencies and system Requirements |
| Reputation | CPU must support AVX2 (BMI2) instruction set |
| FileType engine | libnsl Amazon Linux 2023: libxcrypt-compat |
| Country of Origin | libnsl Amazon Linux 2023: libxcrypt-compat |
| Proactive DLP |
CPU must support AVX2 and SSE4.1 instruction set to use OCR feature |
| RocketCyber | libgomp |

Note: Some dependencies may need to be installed from external repositories, not from the OS default repositories.

### [Linux] Installation Details

MetaDefender Core default installation path is using /var folder for storing resources:

`/var/lib/ometascan`

: installation folder with all its resources (database, DLP processed / CDR sanitized / quarantined file storage, engine package and definition updates).`/var/log/ometascan`

: application logs.`/var/run/ometascan`

: runtime folder for Core related processes.`/var/lib/ometascan`

: all successful deployed engines data files.`/usr/lib/ometascan`

: all shared libraries required by MetaDefender Core, bundled PostgreSQL server related binaries and libraries.`/var/tmp/ometascan/resources`

: all temporary processing files for MetaDefender Core to process.

## Storage Usage Information

Based on the configuration, MetaDefender Core will need additional disk space to store analysis/result data, quarantined files and temporary files:

| Data Storage | |
|---|---|
Analysis Reports (Processing History) | Approximately 5GB is required for every 1M analysis reports stored. - 100 GB is recommended as a baseline. Database storage requirements are affected by Data Retention settings, engine settings and scanning load.
|
Quarantined Files | Depends on the customers' dataset and configuration |
Sanitized Files | Depends on the customers' dataset and configuration |
Temporary processing files | Depends on the customers' dataset and configuration - A 1GB non-archive file requires 1GB free disk space at least.
- A 1GB archive file requires (1 * 2)GB free disk space at least.
- 50GB is a baseline and should be adjusted based on observation of the solution within the environment, with consideration to peak times and overall file makeup (e.g. complexity, size, archives).
|
Note | Options are available to control how large and/or complex files are handled to limit the amount of system resources required. See Workflow Configuration Template for more information. |

## Custom Engines

The recommendations above are specific for MetaDefender pre-packaged bundles.

However for additional Custom Engines, please review the Knowledge base to review additional requirements (if any) for the selected engine.

## Browser Requirements for the MetaDefender Core Management Console

One of the following browsers is suggested to view the MetaDefender Core Management Console:

- Microsoft Edge
- Chrome
- Firefox
- Safari

Chrome, Firefox, Safari and Microsoft Edge browsers are tested with the latest available version at the time of release.

## Network Bandwidth

In online environment where MetaDefender Core is configured to download engine update packages directly from OPSWAT update server source, then using gigabit network speed (125 MB/sec) is highly recommended to avoid potential network related issue while downloading files, or at least 100 Mbps (12.5 MB/sec) network speed.

If you have installed or if you wish to use the MetaDefender Core in a restricted environment, you will have to allow access to the following hosts:

- https://activation.dl.opswat.com - for license online activation.
- https://update.dl.opswat.com - for engines and databases download.

Note: IP address-based allowlisting on your firewall might fail after some time since OPSWAT uses CDN (AWS Cloudfront) to faster delivery updates over the world, and IP address of edge servers might change over time.

Depending on your location, connections with OPSWAT cloud-based servers be forwarded to specific AWS Cloudfront's edge locations, each is assigned with its own unique IP address ranges. You might also need to allow correct AWS Cloudfront's corresponding IP address ranges by referring to https://ip-ranges.amazonaws.com/ip-ranges.json

Even the OPSWAT update servers host updates for all of the available engines we support, sometimes custom engines might try to connect to their own cloud for updates, but this can be disabled in firewall and they will be updated just from OPSWAT cloud servers instead.