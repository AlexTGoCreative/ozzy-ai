<!-- source: https://www.opswat.com/docs/mdcore/container-deployment -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:04:10.654084 -->

# Overview

## Introduction

This Installation Guide provides step-by-step instructions for installing MetaDefender Core in your own Kubernetes cluster in whatever environment you have it deployed.

Organizations interested in protecting their solutions deployed in Kubernetes technology can leverage MetaDefender to analyze and sanitize files. MetaDefender can scan and either sanitize or check for known vulnerabilities, depending on the type of traffic it's seeing. Analyzing files before they are made accessible to the end-users is critical to ensure that no malicious content is allowed and distributed through the web application.

This guide is for IT infrastructure architects, administrators and DevOps professionals who are seeking to prevent potential malicious traffic being allowed in their environments. Threat Prevention is ensured for both productivity files that might be uploaded and for known vulnerabilities that can be identified for all running services/applications. The vulnerability scanning is checking known vulnerabilities for unpatched OS and running applications.

#### Guide Structure

- Kubernetes Components
- Deploying on K8S
- Upgrade/Deployment Strategy on K8S
- High Availability on K8S
- Scaling K8S Cluster
- Troubleshooting

## Kubernetes Supported Versions

| Kubernetes Version | Known Limitations |
|---|---|
| 1.22.17 and later | None |
| Before 1.22.17 | When pod eviction, automation of core deactivation fails. |