<!-- source: https://www.opswat.com/docs/mdcore/proactive-dlp/document-identification -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:59:26.822147 -->

# Document Identification

## I. NSFW (Not Safe for Work)

This section provides the controls and settings related to the detection and management of content that is categorized as NSFW within text and images.

**Detection categories:** Here is a list of categories OPSWAT PDLP can detect:

**Toxic Text:**Detects toxic or harmful language in text content, helping prevent the transfer of offensive, abusive, or inappropriate communication.**Suggestive Content:**Images that are sexually suggestive but do not depict explicit sexual acts.**Explicit Content**: Images depicting explicit sexual acts or pornography.**Animated Adult Content**: Hentai and other animated images with pornographic themes.

**Violence:**Detects imagery containing acts of aggression, physical harm, or graphic violence. This includes scenes depicting injury, assault, or excessive brutality.**Weapons and Explosives:**Identifies images containing firearms, bombs, or explosive materials. This detection helps mitigate the risk of circulating or exfiltrating content related to weaponry or potential threats.**Political Content:**Flags visual materials containing political symbols, campaigns, figures, or protest imagery. This ensures that communications remain compliant with internal neutrality and non-political content policies.**Drugs and Substance Abuse:**Detects the presence or depiction of illegal drugs, paraphernalia, or substance use. This category supports compliance with workplace conduct standards and helps prevent the distribution of inappropriate imagery.**Self-Harm and Suicide:**Identifies visual content that depicts or suggests self-harm, suicidal behavior, or related paraphernalia. This detection enables early identification of distressing content and promotes responsible content handling.

**Functionality:** Enables or disables the detection of NSFW content in both textual and visual data.

**Optical Character Recognition (OCR):**Scans and recognizes text within images. This helps in identifying NSFW text that might be embedded in graphics**OCR Quality:**Determines the accuracy and efficiency of the OCR process*Normal*: detect the information without pre-processing images*Best*: pre-processing images before detecting the image to have a better detection rate, however, performance will be impacted

**Redact Hits:**Automatically redacts (blurs & Blackout) the detected NSFW content**Allow if detections at or above threshold are redacted**: This setting ensures that there is no interruption in the flow of content after making changes and redacting some portion of the content*Redaction Threshold:*Defines the sensitivity level for redaction

**Example**

Here is an example of how the toxic text can work in action and detect the words which is not okay for work

This feature uses AI functionality to analyze both images and text to determine whether the content is toxic or not safe for work. You have the option to enable or disable the AI-powered feature within the configuration settings. By default, this feature is disabled but can be activated or deactivated at any time based on user preference. If you enable the AI-powered feature, OPSWAT will not use your content to train or fine-tune its services. You should not rely on any results generated from AI-based functionality without verifying them.

## II. Personal Document Configuration

This section focuses on identifying documents, determining if uploaded items are personal documents, like passports or ID cards or Driver License. Based on the detection, customers can choose to block or allow the content.

**Functionality**: Enables or disables the automatic detection of personal documents, such as IDs, driver license, and other sensitive ID cards.

**Default Behaviour:**Defines the action taken when a personal document is detected*Allow*: If a customer wishes to permit identified images, this setting can be activated, but only images verified as personal documents will be allowed.*Block*: If a customer wants to restrict identified images, enabling this feature will ensure those images are blocked.

Below are the supported personal document identification categories:

**Identification Documents:**Detects documents containing personal identification details or official ID formats. This includes passports, driver’s licenses, ID cards, social security cards, and similar records used to verify individual identity.**Financial Documents:**Identifies materials containing banking, investment, or financial account information. Includes bank statements, loan documents, tax forms, invoices, receipts, and payment confirmations.**Animal and Pet Documents:**Detects veterinary records, pet ownership certificates, vaccination cards, and registration documents related to animals.**Energy and Utility Documents:**Recognizes documents issued by energy, water, or telecommunications providers. Includes bills, statements, and contracts that often contain addresses, account numbers, and payment information.**Employment Documents:**Identifies HR-related documents such as employment contracts, offer letters, pay slips, performance evaluations, and resignation forms. These often include sensitive employee identifiers and confidential company data.**Government and Tax Documents:**Detects documents issued by government agencies or containing regulatory, tax, or filing information. Includes tax returns, government correspondence, permits, and legal filings.

**Example**

This feature uses AI functionality to differentiate between various documents and identify whether the document contains any government issued identification documentation of any person. You have the option to enable or disable the AI-powered feature within the configuration settings. By default, this feature is disabled but can be activated or deactivated at any time based on user preference. If you enable the AI-powered feature, OPSWAT will not use your content to train or fine-tune its services. You should not rely on any results generated from AI-based functionality without verifying them.