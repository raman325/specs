<!-- PAGE 277 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.52** **Language** **Command** **Class,** **version** **1**


The Language Command Class is used to specify the language settings on a device.


**2.2.52.1** **Language** **Set** **Command**


This command is used to set the language at the receiving node. The receiving node SHOULD use
the default language in case the received language is not supported.


Table 2.329: Language Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|
|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|Command = LANGUAGE_SET|
|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|
|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|
|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|
|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|
|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|



**Language** **(24** **bits)**

The code definition of the languages may be found in ISO 639-2:1998 ‘Codes for the representation
of names of languages - Part 2: Alpha-3 code’. In the table below are some examples of the alpha-3
codes listed:


Table 2.330: Example ISO 639-2:1998 alpha-3 codes

|Language|Language 1|Language 2|Language 3|
|---|---|---|---|
|English|e|n|g|
|Flemish; Dutch|d|u|t|
|French|f|r|e|
|German|g|e|r|
|Italian|i|t|a|
|Polish|p|o|l|
|Russian|r|u|s|
|Walloon|w|l|n|



**Country** **(16** **bits)** The code definition of the countries may be found in ISO 3166-1 ‘Country Codes:
Alpha-2 codes’’. The use of the country field is OPTIONAL and only defined in case it is necessary
for distinguishing geographical variants. The number of data fields transmitted MUST be determined
from the length field in the frame. In the table below are some examples of the alpha-2 codes listed:

|Table 2.331: Example ISO 3166-1 Country|alpha-2 codes Country 1|Country 2|
|---|---|---|
|Country|Country 1|Country 2|
|Belgium|B|E|
|Italy|I|T|
|Netherlands|N|L|
|Poland|P|L|
|United Kingdom|G|B|
|United States|U|S|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 276




<!-- PAGE 278 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.52.2** **Language** **Get** **Command**


This command is used to request the current language setting in a device.


The Language Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.332: Language Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|
|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|Command = LANGUAGE_GET|



**2.2.52.3** **Language** **Report** **Command**


This command returns the current language setting in a device.


Table 2.333: Language Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|Command Class = COMMAND_CLASS_LANGUAGE|
|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|Command = LANGUAGE_REPORT|
|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|Language 1|
|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|Language 2|
|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|Language 3|
|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|Country 1|
|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|Country 2|



For fields’ description, refer to Section 2.2.52.1 Language Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 277