<!-- source: https://www.opswat.com/docs/mdcore/deep-cdr/setup-output-file-name -->
<!-- product: metadefender_core -->
<!-- doc_type: concept -->
<!-- crawled_at: 2026-06-05T08:57:37.211036 -->

# Setup output file name

To set up output filename for sanitized file, go to **Policy** > **Workflow rules** > choose **workflow name**

In the output filename format field, variables listed below can be used. Beside variables, any characters can be used as static text, except these:

`<>:"\|/?*$`

Available variables:

- ${dataid} - this string identifies a file processing and can be used to retrieve results of processing
- ${datetime} - date and time at the time of sanitization
- ${original.basename} - name of the file to be sanitized, without file extension
- ${original.extension} - extension of the file to be sanitized
- ${converted.extension} - extension based on the target file type

## Example usage

`${original.basename|long}_sanitized_${dataid}.${converted.extension}`

Example output:

`testfile_sanitized_db3761f43e4545ab886f5930dbb037f3.pdf`

## Variables

### Data ID

`${dataid}`

The result is the dataid of the sanitized file.

### Original filename

`${original.basename}`

`${original.basename|<attribute>}`

| Attribute | Description |
|---|---|
| short (default) | filename until the first '.', ie. archive.tar.gz |
| long | filename until the last '.', ie. archive.tar.gz |

### Original file extension

`${original.extension}`

`${original.extension|<attribute>}`

| Attribute | Description |
|---|---|
| short (default) | extension from the last '.', ie. archive.tar.gz |
| long | extension from the first '.', ie. archive.tar.gz |

### Converted file extension

`${converted.extension}`

The result is the selected target extension used for sanitization.

### Date and time

`${datetime}`

`${datetime|epoch}`

`${datetime|<format>}`

Without any format string, the default format is 'yyyy_MM_dd-hh_mm'. With **epoch** format the result will be the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then. When giving custom format, the '.', '_' and '-' characters also can be used.

| Expression | Output |
|---|---|
| d | the day as number without a leading zero (1 to 31) |
| dd | the day as number with a leading zero (01 to 31) |
| ddd | the abbreviated localized day name (e.g. 'Mon' to 'Sun'). Uses the system locale to localize the name. |
| dddd | the long localized day name (e.g. 'Monday' to 'Sunday'). Uses the system locale to localize the name. |
| M | the month as number without a leading zero (1-12) |
| MM | the month as number with a leading zero (01-12) |
| MMM | the abbreviated localized month name (e.g. 'Jan' to 'Dec'). Uses the system locale to localize the name. |
| MMMM | the long localized month name (e.g. 'January' to 'December'). Uses the system locale to localize the name. |
| yy | the year as two digit number (00-99) |
| yyyy | the year as four digit number |

These expressions may be used for the time:

| Expression | Output |
|---|---|
| h | the hour without a leading zero (0 to 23 or 1 to 12 if AM/PM display) |
| hh | the hour with a leading zero (00 to 23 or 01 to 12 if AM/PM display) |
| H | the hour without a leading zero (0 to 23, even with AM/PM display) |
| HH | the hour with a leading zero (00 to 23, even with AM/PM display) |
| m | the minute without a leading zero (0 to 59) |
| mm | the minute with a leading zero (00 to 59) |
| s | the second without a leading zero (0 to 59) |
| ss | the second with a leading zero (00 to 59) |
| z | the milliseconds without leading zeroes (0 to 999) |
| zzz | the milliseconds with leading zeroes (000 to 999) |
| AP or A | use AM/PM display. A/AP will be replaced by either "AM" or "PM". |
| ap or a | use am/pm display. a/ap will be replaced by either "am" or "pm". |
| t | the timezone (for example "CEST") |