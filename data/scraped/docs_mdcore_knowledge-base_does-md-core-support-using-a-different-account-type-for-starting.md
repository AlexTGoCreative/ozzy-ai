<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/does-md-core-support-using-a-different-account-type-for-starting -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:35:20.292817 -->

# Does MD Core support using a different account type for starting application services

Yes, MD Core does support different account types for starting application services.

The default Local System Account can be changed to a user account for MD Core under:

- Services → OPSWAT MetaDefender Core

Before making this change, please ensure that the selected user has full administrative privileges on the server. Insufficient permissions may cause critical MetaDefender Core functionalities to stop working properly.

We recommend performing this configuration during a maintenance window or low-usage period, as the service restart will temporarily interrupt MetaDefender Core operations. After the change, verify that all dependent services start successfully and that scanning, update, and communication functions are working as expected.

If you encounter any issues or require further assistance, please contact OPSWAT support via My OPSWAT at: https://my.opswat.com/home Our support team will be able to provide you with the necessary guidance and resolution for any license-related concerns.