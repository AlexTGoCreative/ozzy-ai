<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/end-of-life-support-for-ubuntu-20-04-and-amazon-linux-2-in-metad -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:32:57.127462 -->

# End of Life Support for Ubuntu 20.04 and Amazon Linux 2 in MetaDefender Core

As of April 2025, Ubuntu 20.04 LTS has reached its End of Life (EOL), meaning it no longer receives security updates, patches, or support from Canonical. Amazon Linux 2 support for MetaDefender Core and its engines will also be discontinued after June 30, 2025, aligning with the initial EOL date set by MetaDefender Core, despite Amazon Linux 2's extended EOL to 2026. This article outlines the implications, risks, and recommendations for continuing to use these operating systems with MetaDefender Core.

## Background

MetaDefender Core relies on the underlying operating system for security updates and stability. With Ubuntu 20.04 and Amazon Linux 2 reaching EOL, Canonical and Amazon Web Services (AWS) have ceased providing updates, leaving systems vulnerable to new security threats. To ensure the security and reliability of MetaDefender Core deployments, OPSWAT strongly recommends upgrading to supported operating systems.

## Impact on MetaDefender Core

Running MetaDefender Core on Ubuntu 20.04 or Amazon Linux 2 after their EOL introduces significant risks, including:

**Security Vulnerabilities**: Without security patches, these operating systems are exposed to new exploits and threats.**Compatibility Issues**: MetaDefender Core updates and new features may not function correctly on unsupported platforms.**Compliance Risks**: Many regulatory standards require systems to run on actively supported operating systems.**Lack of Support**: OPSWAT technical support may be limited or unavailable for issues related to EOL operating systems.

## Recommendations

To maintain a secure and supported MetaDefender Core environment, OPSWAT recommends the following:

**Upgrade to a Supported Operating System**Transition to a supported operating system, such as Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, or Amazon Linux 2023, which receive active security updates and are fully compatible with the latest MetaDefender Core versions. Refer to the MetaDefender Core System Requirements for a complete list of supported platforms.**Plan Your Migration****Assess Your Environment**: Identify all systems running Ubuntu 20.04 or Amazon Linux 2.**Test Compatibility**: Deploy MetaDefender Core on the new operating system in a staging environment to ensure compatibility with your workflows.**Execute Migration**: Follow OPSWAT’s migration guides to transfer configurations, policies, and data to the new platform.**Validate Post-Migration**: Verify that MetaDefender Core operates as expected after the upgrade.

**Extended Security Maintenance (Optional)**For Ubuntu 20.04, Canonical offers an Extended Security Maintenance (ESM) program, which provides additional security updates for a fee. This may serve as a temporary solution for organizations unable to migrate immediately. However, ESM does not guarantee full compatibility with MetaDefender Core, and OPSWAT recommends upgrading to a fully supported OS as soon as possible. Amazon Linux 2 does not offer an equivalent extended support program, making migration to a supported OS even more critical.

## Continuing with Ubuntu 20.04/Amazon Linux 2 - Pinning Your Engine (Not Recommended)

If migration is not immediately feasible, you may choose to pin your MetaDefender Core engine to a specific version compatible with Ubuntu 20.04 or Amazon Linux 2. This approach, however, is **not recommended** due to the following risks:

**Security Exposure**: The operating system will remain unpatched, increasing the risk of exploitation.**Limited Functionality**: Pinned engines do not receive new features, bug fixes, or performance improvements.**Unsupported Configurations**: OPSWAT may not provide support for issues arising from EOL operating systems, even with pinned engines.**Compliance Violations**: Running an EOL operating system may violate organizational or regulatory compliance requirements.

To pin your engine:

- Access the MetaDefender Core management console.
- Navigate to
**Settings > Update Settings**. - Select the option to pin the engine to the current version.
- Save the configuration.

**Note**: Pinning should only be a temporary measure while planning your migration to a supported operating system.

## Conclusion

The EOL of Ubuntu 20.04 and Amazon Linux 2 poses significant risks to the security and functionality of MetaDefender Core deployments. OPSWAT strongly urges users to upgrade to a supported operating system, such as Ubuntu 22.04 LTS or Amazon Linux 2023, to ensure continued security, compatibility, and support. For assistance with migration or additional guidance, contact OPSWAT Support or refer to the MetaDefender Core Documentation.

If **Further Assistance** is required, please proceed to log a **support case or chatting with our support engineer**.