<!-- source: https://www.opswat.com/docs/mdcore/metascan-engines -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:53:07.219596 -->

# MetaDefender Metascan engine roster (anti-malware capabilities)

Engine name | Vendor name | Country | Detection | Heuristic Detection |
|---|---|---|---|---|
| ClamAV | ClamAV | USA | Signature based | Yes |
| AhnLab | Harbin AhnLab Technology | South Korea | Signature based | No |
| Avira | Avira | Germany | Signature and AI based | Yes |
| ESET | ESET | Slovakia | Signature based | Yes |
| Bitdefender | Bitdefender | Romania | Signature based | Yes** |
| K7 | K7 Computing Private | India | Signature based | Yes* |
| Quick Heal | Quick Heal Technologies | India | Signature based | Yes |
| Vir.IT | TG Soft | Italy | Signature based | No |
| Varist | OK | Iceland | Signature based | Yes |
| Emsisoft | Emsisoft | New Zealand | Signature based | Yes |
| IKARUS | IKARUS Security Software | Austria | Signature based | No |
| TACHYON | INCA Internet | South Korea | Signature based | No |
| Zillya! | ALL IT Services | Ukraine | Signature based | Yes* |
| Anity | Antiy Labs | China | Signature based | Yes* |
| Xcitium | Xcitium | USA | Signature based | Yes |
| Trellix | Trellix | USA | Signature based | Yes |
| Sophos | Sophos | UK | Signature based | No |
| CrowdStrike Falcon ML | CrowdStrike | USA | AI based | No |
| RocketCyber | RocketCyber | USA | AI based | No |
| Webroot SMD | OpenText | USA | Signature and AI based | No |
| Lionic | Lionic Corp | Taiwan | Signature based | No |
| Filseclab | Filseclab Corp | China | Signature based | Yes |
| Huorong | Huorong Security | China | Signature based | No |
| Microsoft Defender | Microsoft | USA | Signature based | Yes** |
| NETGATE | Netgate Technologies | Slovakia | Signature based | Yes* |
| Scrutiny | Cyberstanc | USA | AI based | No |
| Xvirus Anti-Malware | Xvirus | Portugal | Signature based | No |
| Systweak | Systweak | India | Signature based | No |
| Aurora | Arctic Wolf | USA | AI based | No |
| CMC | CMC Cyber Security | Vietnam | Signature and AI based | No |
| BKAV Pro | BKAV Corporation | Vietnam | Signature and AI based | No |
| Gridinsoft | Gridinsoft | Ukraine | Signature based | Yes** |
| SentinelOne | SentinelOne | USA | AI based | No |

## Notes on detection flags

*The engines have a "Heuristic Scan" configuration but is not enabled by default

** The engines have Heuristic detection but don't have configurations

For the other capabilities such as Archive extraction, Cloud scan, etc... please check the engine details in the MetaDefender product.

Note: the RocketCyber (Kaseya) engine is end-of-life and is being removed from all MetaDefender packages effective 2026-08-01.

## MetaDefender public sector engine roster

Engine name | Vendor name | Country | Detection |
|---|---|---|---|
| ClamAV | ClamAV | USA | Signature based |
| AhnLab | Harbin AhnLab Technology | South Korea | Signature based |
| Avira | Avira | Germany | Signature and AI based |
| ESET | ESET | Slovakia | Signature based |
| Bitdefender | Bitdefender | Romania | Signature based |
| K7 | K7 Computing Private | India | Signature based |
| Quick Heal | Quick Heal Technologies | India | Signature based |
| Vir.IT | TG Soft | Italy | Signature based |
| Varist | Varist | Iceland | Signature based |
| Emsisoft | Emsisoft | New Zealand | Signature based |
| IKARUS | IKARUS Security Software | Austria | Signature based |
| TACHYON | INCA Internet | South Korea | Signature based |
| Xcitium | Xcitium | USA | Signature based |
| Trellix | Trellix | USA | Signature based |
| Sophos | Sophos | UK | Signature based |
| CrowdStrike Falcon ML | CrowdStrike | USA | AI based |
| RocketCyber | RocketCyber | USA | AI based |
| Webroot SMD | OpenText | USA | Signature and AI based |
| Lionic | Lionic Corp | Taiwan | Signature based |
| Microsoft Defender | Microsoft | USA | Signature based |
| NETGATE | Netgate Technologies | Slovakia | Signature based |
| Scrutiny | Cyberstanc | USA | AI based |
| Xvirus Anti-Malware | Xvirus | Portugal | Signature based |
| Systweak | Systweak | India | Signature based |
| Aurora | Arctic Wolf | USA | AI based |

Note: "Cyren" was renamed to "Varist" in MetaDefender effective 2023-05-24; older snapshots may still show "Cyren".

Please check the configuration page in the product for the detail Detection methods (Heuristic, Archive extraction, ...) of each engine.