<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/how-can-i-identify-which-metadefender-core-instance-sent-an-aler -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:33:48.398869 -->

# How can I identify which MetaDefender Core instance sent an alert email?

This article applies to all MetaDefender Core V5 releases deployed on Windows systems.

### Overview

When you have multiple MetaDefender Core instances configured to send alerts, the emails can look identical (same sender, same content). This makes it difficult to identify which Core triggered a specific alert (e.g., an AV engine with outdated patterns).

MetaDefender Core supports **email subject macros** that let you insert a unique identifier (such as **Deployment ID** or **Instance Name**) directly into the subject.

### Applies to

- Environments with
**two or more MetaDefender Core instances**sending alerts to the same mailbox - Especially useful for update/engine-related alerts (e.g., “outdated patterns”)

### Resolution

#### Option A (Recommended): Add a unique identifier to the email subject

- Log in to the
**MetaDefender Core**web console on**Core #1**. - Go to
**Settings → Email Notification**. - In the relevant alert section, set
**Custom Email Subject Format**to include an identifier macro, for example:**Most common (works in all modes):**`MDCore ${deployment_id} - ${severity} - AV update alert`

**Shared database mode (if available):**`MDCore ${instance_name} - ${severity} - AV update alert`

MetaDefender Core supports these macros in the email subject:

- `${severity}`

- `${deployment_id}`

- `${instance_name}`

*(shared database mode only)*

- Save changes.
- Repeat steps
**1–4**on**Core #2**, using the same subject format.

**Result:** Each alert email subject will clearly show the originating Core via **Deployment ID** (or **Instance Name**).

### Where to find the Deployment ID

On each Core:

- Go to
**Settings → License** - Locate
**Deployment ID**

### Option B (Immediate workaround): Identify the sender using email headers

If you already received duplicate emails and need to identify the sender **right now**, open the email’s **original headers** and look for the **Received** lines. These typically show the IP/host that connected to your SMTP server.

### Validation

- Trigger (or wait for) a known alert (e.g., engine update/pattern alert).
- Confirm the email subject contains
`${deployment_id}`

(or`${instance_name}`

) and that it matches the expected Core in**Settings → License**.

### Notes / Best Practice

- If both Cores must notify the same recipients,
**subject tagging**is the simplest and cleanest way to avoid confusion. - If you are in shared database mode,
`${instance_name}`

can be especially readable for operations teams (when properly named).

If **Further Assistance** is required, please proceed to log a **support case or chat with one of our support engineers**.