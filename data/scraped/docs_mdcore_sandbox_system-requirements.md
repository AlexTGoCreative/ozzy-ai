<!-- source: https://www.opswat.com/docs/mdcore/sandbox/system-requirements -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:01:41.545460 -->

# System requirements

## Dependencies

| Embedded Engine | Remote Engine |
|---|---|
See: How to upgrade to Java 17
| No additional dependencies are required. |

Before version 2.2.0 Visual C++ Redistributable for Visual Studio is required for Windows.

**The required Java version for the embedded Aether(adaptive sandbox) is Java 17. While Java 8 or 11 may still function temporarily, they will no longer work at all after March 2025. Please plan to upgrade to Java 17 before March 2025 to avoid any disruption**

The default system Java version should be set correctly; please check if the correct version is used. The computer should be restarted after Java installation.

`java -version`

`openjdk version "17.0.12" 2024-07-16`

`OpenJDK Runtime Environment (build 17.0.12+7-Ubuntu-1ubuntu222.04)`

`OpenJDK 64-Bit Server VM (build 17.0.12+7-Ubuntu-1ubuntu222.04, mixed mode, sharing)`

## System requirements

### Embedded Sandbox Engine

System requirements depend on the number and type of submitted files, as well as their content and size. The performance also varies based on the configuration of the system and engine workflow. Below, you will find benchmark measurements using different CPU, RAM, and Sandbox parallel processing configurations on various sample sets. These measurements serve as a guideline to help estimate the required resources for your use case.

These are additional requirements on top of the MetaDefender Core recommended system configuration

These measurements are done with default engine workflow settings on Ubuntu Linux

#### Example Configurations

| CPU Cores | RAM | Parallel Count | |
|---|---|---|---|
Config #1 | 4 | 8 | 5 (default) |
Config #2 | 8 | 16 | 10 |

#### Measured daily throughput

Throughput can be limited by license restrictions! See Licensing

| File type | Avg size (MB) | Throughput #1 | Throughput #2 | #1 (MB/s) | #2 (MB/s) |
|---|---|---|---|---|---|
| Adobe | 0.93 | 47856 | 90816 | 0.52 | 0.98 |
| Executable | 0.16 | 50424 | 101040 | 0.09 | 0.19 |
| Image | 1.6 | 121728 | 218328 | 2.25 | 4.04 |
| Media | 0.13 | 73776 | 148176 | 0.11 | 0.22 |
| Office | 1.6 | 42744 | 54720 | 0.79 | 1.01 |
| Text | 8.8 | 71520 | 97344 | 7.28 | 9.91 |

### Remote Aether (Adaptive Sandbox) Engine

For MetaDefender Aether (Standalone) system requirements please refer to our Technical Datasheet and Performance Measurement page.