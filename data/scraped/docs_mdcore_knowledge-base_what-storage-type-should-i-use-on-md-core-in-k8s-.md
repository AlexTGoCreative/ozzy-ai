<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/what-storage-type-should-i-use-on-md-core-in-k8s- -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:34:28.677518 -->

# What storage type should I use on MetaDefender Core in K8S?

**Introduction**:

This knowledge base article provides details on what types of storages to use in K8S

**Details**:

If the Database is remote and there is no incentive to keep permanent data like sanitized files with CDR or DLP, an ephemeral storage can be used. This can be done from the values.yaml

md-core: env: resources: ephemeral-storage: "60Gi"

If you need persistence, in that case the persistence storage would be the best option. So, make sure that you comment the storage_configs from null and use the following code from values.yaml, comment out line 61, and uncomment lines from 62 to 74

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.