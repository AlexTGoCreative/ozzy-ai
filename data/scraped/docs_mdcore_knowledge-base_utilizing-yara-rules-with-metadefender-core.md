<!-- source: https://www.opswat.com/docs/mdcore/knowledge-base/utilizing-yara-rules-with-metadefender-core -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T09:29:58.267370 -->

# How to Utilize YARA Rules with MetaDefender Core?

This guide is intended for users who wish to leverage YARA rules within MetaDefender Core for enhanced malware detection and specific file pattern recognition during the scanning process.

**Access MetaDefender Core User Interface**: Open your preferred web browser and navigate to the MetaDefender Core's IP address or hostname on the nginx port (default 8008) to access its user interface.**Access the YARA Rules Configuration**: Once in the MetaDefender Core UI, navigate to the YARA Rules configuration. This can be found under Inventory - Modules - Utilities - YARA.**Create a YARA Rule**: In the provided text field, create a new YARA rule that describes the characteristics of the malware or file patterns you wish to detect. Alternatively, if you have a URL or a path to a file containing YARA rules, you can provide that instead.

Here are a few example rules:

**Simple String Match Rule:**

`yara `

``

`rule HelloWorld `

``

`{ `

``

` strings: `

``

` $my_text_string = "Hello, World" `

``

` condition: `

``

` $my_text_string `

``

`}`

**Case-Insensitive String Match Rule**:

`yara `

``

`rule CaseInsensitiveStringDetect `

``

`{ `

``

` strings: `

``

` $a = /malware/i `

``

` condition: `

``

` $a `

``

`}`

**Binary Pattern Match Rule**:

`yara `

``

`rule BinaryPatternDetect `

``

`{ `

``

` strings: `

``

` $a = { DE AD BE EF } `

``

` condition: `

``

` $a `

``

`}`

**Multiple Strings Match Rule**:

`yara `

``

`rule MultipleStringsDetect `

``

`{ `

``

` strings: `

``

` $a = "string 1" `

``

` $b = "string 2" `

``

` condition: `

``

` $a and $b `

``

`}`

**Regular Expression Match Rule**:

`yara `

``

`rule RegexpDetect `

``

`{ `

``

` strings: `

``

` $a = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/ `

``

` condition: `

``

` $a `

``

`}`

**Save the YARA Rule**: After creating your rule or providing the URL or file path, save it in the MetaDefender Core UI.**Enable YARA in Workflow:**Go to the Workflow section in the MetaDefender Core UI. This is accessible by following this path: Workflow - Select desired workflow - YARA. Ensure that YARA is enabled for each workflow where you wish to apply the rule.**Review the Results:**Examine the scan results to see if the YARA rule identified any matches in the uploaded files. If a match is found, it indicates that the file contains the pattern described in the rule.

**Conclusion:**

By integrating YARA rules with MetaDefender Core, users can significantly enhance their malware detection capabilities. These rules provide a powerful way to identify specific file patterns during the scanning process, thereby leading to a more robust and effective threat detection. This guide should enable users to create, implement, and utilize YARA rules effectively within MetaDefender Core.

For more information on YARA, please refer to the official YARA Documentation: YARA

If you need further assistance, don't hesitate to create a support case or chat with our support engineer.