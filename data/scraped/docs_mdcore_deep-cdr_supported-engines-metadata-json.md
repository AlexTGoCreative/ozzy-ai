<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/supported-engines-metadata-json -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:56:30.818622 -->

# Supported engines-metadata JSON

## Overwrite file encoding for TXT and HTML

The Deep CDR engine processes the TXT and HTML file as UTF-8 encoding by default. In several cases, the clients determine exactly the encoding of the file, so they can send this information to the engine to have a better detection. To utilize this feature, please see the bellow steps:

- Use MetaDefender Core API to send a file
- Use the
**engines-metadata**to send the encoding

JSON

`{`

` "deep_cdr": {`

` "charset": "ISO-2022-JP"`

` }`

`}`

## Select schema file to validate for XML

See the details here.

JSON

`{`

` "deep_cdr": {`

` "xml2xml.validate_against_schema.schema_name": "person.xsd"`

` }`

`}`