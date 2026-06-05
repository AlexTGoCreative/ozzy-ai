<!-- source: https://www.opswat.com/docs/mdcore/sandbox/sandbox-core-high-availability-setup -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:01:30.464728 -->

# Sandbox-Core High Availability Setup

*Setting up Core-Sandbox pairs (comprising essential system components) in each Availability Zone (AZ) or data center. It helps ensure high availability (HA) across multiple locations.*

#### Limiting cross-data center traffic

It is recommended to limit cross-data center traffic as much as possible. The goal is to minimize the communication between different data centers. This reduces the risk of issues that can arise from data traveling across long distances.

#### Using a Load Balancer (LB) on top of each Core-Sandbox pair

To have a proper High Availability (HA) configuration, it is recommended to deploy a Load Balancer on top of a Core-Sandbox pair following the Using external Load Balancer guide.

#### Isolating communication and ensuring each AZ can function independently

A given Core-Sandbox pair should only communicate with each other. There should be no need for any cross-communication between AZs.

If AZ#1 goes down (with all its servers), then AZ#2 must be able to fully take over the processing of incoming requests.

The key point is that each AZ must be able to function independently. It cannot rely on any resources in another AZ. A proper High Availability (HA) configuration retains its full functionality even if an entire AZ is unavailable.

#### Monitoring system resources

In general, the end user should monitor the usage of system resources for both Core and Sandbox in each AZ to see if there is a performance bottleneck in the processing pipeline.

To handle a failover scenario, it is sufficient to monitor the health status of Core using this API endpoint: https://docs.opswat.com/mdcore/metadefender-core#healthcheck

If the Core instance in AZ#1 is not responding or its queue is getting full (perhaps due to a Sandbox issue), then the application load balancer can decide to send all new requests to Core in AZ#2.