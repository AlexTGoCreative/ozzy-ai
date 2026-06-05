<!-- source: https://www.opswat.com/docs/mdcore/container-deployment/unable-to-deploy-metadefender-core-in-kubernetes-with-containerd -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:08:26.763002 -->

# Unable to deploy MetaDefender Core in Kubernetes with containerd engine 2.2.x

## Summary

We have identified an issue affecting our application deployments in Kubernetes environments using **containerd 2.2.x**. This behavior is caused by a known bug in the container runtime and is not related to changes in our application.

## Issue Description

A known bug in **containerd** version **2.2.x** prevents containers from being successfully created in certain Kubernetes environments. As a result, Pods may fail during startup and remain in a non-running state.

The following is an example when deploying to EKS 1.35 (the log is redacted)

Bash

` `

`Events:`

` Type Reason Age From Message`

` ---- ------ ---- ---- -------`

` Normal Scheduled 82s default-scheduler Successfully assigned default/md-core-7fb8c84585-vk2gt to ip-172-31-5-122.ec2.internal`

` Normal Created 76s kubelet Container created`

` Normal Started 75s kubelet Container started`

` Warning Failed 70s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount1122317056: openat xxx: path escapes from parent`

` Warning Failed 60s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount3050653287: openat xxx: path escapes from parent`

` Warning Failed 48s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount2061916826: openat xxx: path escapes from parent`

` Warning Failed 33s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount2702648643: openat xxx: path escapes from parent`

` Warning Failed 18s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount1893797964: openat xxx: path escapes from parent`

` Normal Pulled 6s (x6 over 70s) kubelet Container image "opswat/metadefendercore-debian:5.17.1" already present on machine and can be accessed by the pod`

` Warning Failed 6s kubelet Error: failed to create containerd container: mount callback failed on /var/lib/containerd/tmpmounts/containerd-mount3629785830: openat xxx: path escapes from parent`

**Reference**: https://github.com/containerd/containerd/issues/12683

## Affected Environments:

- ** Kubernetes 1.35 or containerd 2.2.0+

## Workaround

Until the vendor provides a fix, use one of the following mitigations:

- Downgrade containerd to a supported version (e.g., 1.7.x)
- Use a Kubernetes node image that does not include containerd 2.2.x
- Pin node runtime version in cluster provisioning