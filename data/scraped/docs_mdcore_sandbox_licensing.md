<!-- source: https://www.opswat.com/docs/mdcore/sandbox/licensing -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:00:42.174162 -->

# Licensing

This page applies to the **Embedded Aether (Adaptive Sandbox)** engine version **2.2.0** and above.

## License Usage and Execution Limits

Your MetaDefender Core license includes a **daily execution limit** for the **Embedded Aether (Adaptive Sandbox)** engine, which determines the maximum number of scans that can be performed within a single day. The execution count resets at midnight (UTC).

Restart the engine after activating a new license for the changes to take effect. Current scan count will not reset on license actions.

### Soft Limit (Warning)

Your license allows exceeding the limit by 20%. During this period, known as the **soft limit**, the system will continue to allow scans but will display a warning indicating the remaining available executions.

### Hard Limit (Enforcement)

If the number of executed scans exceeds 120% of the daily limit, the **hard limit** is enforced, and further executions will be blocked until the next day. A license error will be returned, preventing additional scans.

## Overuse Adjustment

If the soft limit is reached for 7 consecutive days, the soft limit will become the hard limit, effectively reducing the maximum number of scans allowed per day. The original soft limit is reverted the next day if the scan limit is not reached.

## Example Scenarios:

License limit: 100 scans/day

Soft limit: 101-120 scans → Warning displayed, but scans continue.

Hard limit: 121+ scans → Execution blocked until midnight.

If soft limit is reached 7 consecutive days → New hard limit set to 100 scans/day, and the 20% buffer is no longer available. Warning zone starts with scan number 81.

Ensure that your scanning usage stays within acceptable limits to avoid disruptions. If you require more executions, consider upgrading your license.