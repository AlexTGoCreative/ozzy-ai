<!-- source: https://www.opswat.com/docs/mdcore/metascan-engines/set-up-windows-defender-as-a-custom-engine -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:55:15.721246 -->

# Set up Windows Defender as a custom engine

In order to set up and use Windows Defender as a custom engine in MetaDefender Core, the following conditions must be met:

- The native Windows Defender / Windows Security must exist on the Windows OS.
**Real-time protection**must be turned on.

In case of the **Real-time protection** feature is disabled, it can be enabled on the **Manage settings** screen.

- The MetaDefender Core
**Installation**folder must be**Allowlisted**(Excluded):

The **Add or remove exclusions** feature can add a folder as an exclusion.

**Passive Mode**must be enabled for Windows Defender:- download the Windows_Defender_Passive_Mode archive and extract it.
- execute
the
**enable_windows_defender_passive_mode.reg**to automatically add the following two keys to the registry. - If you want to change Windows Defender back to
active mode, execute the
**disable_windows_defender_passive_mode.reg**or modify the two above registries to**00000000**.

Always check if RTP is still on after enabling passive mode! If not, try disabling passive mode!

`[HKEYLOCAL MACHINE\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection]`

`"DisableRoutinelyTakingAction"=dword:00000001`

`"ForceDefenderPassiveMode"=dword:00000001`

Considering that this custom engine uses the native Windows Defender available on your system, the behavior of the engine relies on your Windows Defender local settings.

So, for example, if you do not want to submit files to Microsoft servers using the cloud feature, you should turn these settings off in the Windows Defender configuration.

## Turning off Cloud protection

In order to turn off cloud protection or automatic sample submission, turn each feature off in Windows Defender’s settings