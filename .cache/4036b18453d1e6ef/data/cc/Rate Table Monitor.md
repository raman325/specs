<!-- PAGE 383 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.82** **Rate** **Table** **Monitor** **Command** **Class,** **version** **1**


The Rate Table Monitor Command Class defines the parameter sets for a range of rates.


**2.2.82.1** **Rate** **table** **supported** **get** **command**


This command is used to request the number of rates and parameter sets supported by the Rate Table
Command Class.


The Rate Table Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.472: Rate Table Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|Command = RATE_TBL_SUPPORTED_GET|



**2.2.82.2** **Rate** **table** **supported** **report** **command**


This command is used to advertise the number of rates and parameter sets supported.


Table 2.473: Rate Table Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|Command = Command = RATE_TBL_SUPPORTED_REPORT|
|Rates Supported|Rates Supported|Rates Supported|Rates Supported|Rates Supported|Rates Supported|Rates Supported|Rates Supported|
|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|Parameter Set Supported Bit Mask 1|
|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|Parameter Set Supported Bit Mask 2|



**Rates** **Supported** **(8** **bits)**


Number of rates supported (1..255).


**Parameter** **Set** **Supported** **Bit** **Mask** **1,** **2** **(16** **bits)**

The Bit Mask field describes the supported parameter set in addition to the default-supported parameter set. The default parameter set comprises of Rate Parameter Set ID, Rate text, Start time
and Duration.


It is possible to extend the default parameter set as follows:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 382




<!-- PAGE 384 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.474: Rate Table Supported Report::Parameter Set Supported Bit Mask encoding

|Parameter Set<br>Supported|Bit Map|Description|
|---|---|---|
|1|Bit 0|Reserved<br>|
|1|Bit 1|Supports _Block tarifs_ if the bit is 1 and the opposite if 0.<br>Block tarifs assign blocks of energy at a set cost, for ex-<br>ample in a two block tarif the frst block say from 0 kWh<br>to 200 kWh is charged at X currency per unit(kWh) all<br>other units consumed over 200kWh will be charged at Y<br>currency per unit for the billing period.<br>|
|1|Bit 2|Supports _Maximum demand tarifs_ if the bit is 1 and the<br>opposite if 0.<br>Maximum demand tarifs are based on the maximum load<br>that is measured for example 20kw over an averaging pe-<br>riod. The charge is based on the max load; hence a 30kW<br>maximum demand would be more costly than a 20kW<br>maximum demand.<br>|
|1|Bit 3|Supports _Subscribed demand tarifs_ if the bit is 1 and the<br>opposite if 0.<br>This type of tarif is used in France and Italy primarily;<br>the standing charge is calculated from the maximum load,<br>for example<br>10A = 10 currency/month, 20A = 20 currency / month.|
|1|Bit 4|Supports Demand Control Plan mapping (DCP ID) if the<br>bit is 1 and the opposite if 0.|



All other bits are reserved and MUST be set to zero by a sending node. Reserved bits MUST be
ignored by a receiving node.


**2.2.82.3** **Rate** **table** **get** **command**


This command is used to request the rate parameter set for a given rate parameter set identifier.


The Rate Table Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.475: Rate Table Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|Command = RATE_TBL_GET|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**

The Rate Parameter Set ID addresses the wanted parameter set. The rate parameter set identifier
MUST be a sequence starting from 1 to Rates Supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 383




<!-- PAGE 385 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.82.4** **Rate** **table** **report** **command**


This command reports rate parameter set for a given rate parameter set identifier.


Table 2.476: Rate Table Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|Command = RATE_TBL_REPORT|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Reserved|Rate Type|Rate Type|Number of Rate Char.|Number of Rate Char.|Number of Rate Char.|Number of Rate Char.|Number of Rate Char.|
|Rate Character 1|Rate Character 1|Rate Character 1|Rate Character 1|Rate Character 1|Rate Character 1|Rate Character 1|Rate Character 1|
|…|…|…|…|…|…|…|…|
|Rate Character N|Rate Character N|Rate Character N|Rate Character N|Rate Character N|Rate Character N|Rate Character N|Rate Character N|
|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|
|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|
|Duration Minute 1|Duration Minute 1|Duration Minute 1|Duration Minute 1|Duration Minute 1|Duration Minute 1|Duration Minute 1|Duration Minute 1|
|Duration Minute 2|Duration Minute 2|Duration Minute 2|Duration Minute 2|Duration Minute 2|Duration Minute 2|Duration Minute 2|Duration Minute 2|



The following part of the command is OPTIONAL depending on the parameters supported. Use the
Rate Table Supported Get Command to obtain supported parameters beside the default above. A
not supported parameter is removed from the command layout.


Table 2.477: Rate Table Report Command Optional

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Consumption Precision 1|Consumption Precision 1|Consumption Precision 1|Consumption Scale 1|Consumption Scale 1|Consumption Scale 1|Consumption Scale 1|Consumption Scale 1|
|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|Min. Consumption Value 1|
|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|Min. Consumption Value 2|
|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|Min. Consumption Value 3|
|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|Min. Consumption Value 4|
|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|Max. Consumption Value 1|
|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|Max. Consumption Value 2|
|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|Max. Consumption Value 3|
|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|Max. Consumption Value 4|
|Max. Demand Precision 1|Max. Demand Precision 1|Max. Demand Precision 1|Max. Demand Scale 1|Max. Demand Scale 1|Max. Demand Scale 1|Max. Demand Scale 1|Max. Demand Scale 1|
|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|Max. Demand Value 1|
|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|Max. Demand Value 2|
|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|Max. Demand Value 3|
|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|Max. Demand Value 4|
|DCP Rate ID|DCP Rate ID|DCP Rate ID|DCP Rate ID|DCP Rate ID|DCP Rate ID|DCP Rate ID|DCP Rate ID|



Refer to description of fields under the Rate Table Set Command (Section 2.2.81.1).


**2.2.82.5** **Rate** **table** **active** **rate** **get** **command**


This command is used to retrieve the rate currently active in the meter.


The Rate Table Active Rate Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 384




<!-- PAGE 386 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.478: Rate Table Activate Rate Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|Command = RATE_TBL_ACTIVE_RATE _GET|



**2.2.82.6** **Rate** **table** **active** **rate** **report** **command**


This command is used to advertise the rate parameter set ID of the rate currently active in the meter.


Table 2.479: Rate Table Activate Rate Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|Command = RATE_TBL_ACTIVE_RATE _REPORT|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**


The Rate Parameter Set ID of the rate currently active in the meter.


**2.2.82.7** **Rate** **table** **current** **data** **get** **command**


This command is used to request a number of time stamped values (current) in physical units according
to the dataset mask.


The Rate Table Current Data Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.480: Rate Table Current Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|Command = RATE_TBL_CURRENT_DATA_GET|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|
|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|
|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**

The Rate Parameter Set ID addresses the wanted parameter set. The rate parameter set identifier
MUST be a sequence starting from 1 to Rates Supported.


**Dataset** **Requested** **(24** **bits)**

The dataset requested parameter indicates which data is requested by the command. This field MUST
be encoded according to the Meter Datasets defined in [26].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 385




<!-- PAGE 387 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.82.8** **Rate** **table** **current** **data** **report** **command**


This command is used to report a number of time stamped values (current) in physical units in the
device.


Table 2.481: Rate Table Current Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|Command = RATE_TBL_CURRENT_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|
|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|
|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|
|Current Precision 1|Current Precision 1|Current Precision 1|Current Scale 1|Current Scale 1|Current Scale 1|Current Scale 1|Current Scale 1|
|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|
|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|
|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|
|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|
|…|…|…|…|…|…|…|…|
|Current Precision N|Current Precision N|Current Precision N|Current Scale N|Current Scale N|Current Scale N|Current Scale N|Current Scale N|
|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|
|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|
|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|
|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|



**Reports** **to** **Follow** **(8** **bits)**


This value indicates how many report frames there are left, the value 0xFF means that the number
of reports have not been calculated yet or that there is more than 255 reports to follow.


**Rate** **Parameter** **Set** **ID** **(8** **bits)**

The Rate Parameter Set ID addresses the wanted parameter set. The rate parameter set identifier
MUST be a sequence starting from 1 to Rates Supported.


**Dataset** **(24** **bits)**

The dataset parameter indicates which data is included in the report. This field MUST be encoded
according to the Meter Dataset defined in [26].


**Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December). A year equal to 0x0000
indicates that a accumulated value is not determined yet.


**Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00..23) in local time.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 386




<!-- PAGE 388 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00..59) in local
time.


**Second** **Local** **Time** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00..59) in local time. The value
60 used to keep UTC from wandering away is not supported.


**Precision** **(N** ***** **3** **bits)**

The precision field describes what the precision of the value is. The number indicates the number of
decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Current** **Scale** **(N*5** **bits)**

The Current Scale is used to indicate the scale (unit) of the following value. This field MUST be
encoded according to the Meter Dataset and Scales defined in [26].


**Current** **Value** **(N** ***** **32** **bits)**

The Current Value advertises a value corresponding to the Dataset Requested field of the Get Command. The field MUST be encoded as a 32-bit signed integer. The first byte (Value 1) MUST carry
most significant byte. _Signed_ _encoding_ shows signed decimal values together with their hexadecimal
equivalents.


NOTICE: The device receiving the Rate Table Current Data Report MUST show the value even
though the Scale is not supported.


**2.2.82.9** **Rate** **table** **historical** **data** **get** **command**


This command is used to request a number of time stamped values (historical) in physical units
according to rate type, dataset mask and time interval.


The Rate Table Historical Data Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 387




<!-- PAGE 389 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.482: Rate Table Historical Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|Command = RATE_TBL_HISTORICAL_DATA_GET|
|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|
|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|
|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|
|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|
|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|
|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|
|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|Start Second Local Time|
|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|
|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|
|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|
|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|Stop Second Local Time|



**Maximum** **Reports** **(8** **bits)**


The maximum reports parameter is used to indicate the maximum number of reports to return based
on the get. Reports are always returned with the most recently recorded value first. If set to 0x00
the meter will return all reports based on the request.


**Rate** **Parameter** **Set** **ID** **(8** **bits)**

The Rate Parameter Set ID addresses the wanted parameter set. The rate parameter set identifier
MUST be a sequence starting from 1 to Rates Supported.


**Dataset** **Requested** **(24** **bits)**

The dataset requested parameters indicate data requested. This field MUST be encoded according to
the Meter Dataset defined in [26].


**Start/Stop** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Start/Stop** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December). A year equal to 0x0000
indicates that an accumulated value is not determined yet.


**Start/Stop** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Start/Stop** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00..23) in local time.


**Start/Stop** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00..59) in local
time.


**Start/Stop** **Second** **Local** **Time** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00..59) in local time. The value
60 used to keep UTC from wandering away is not supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 388




<!-- PAGE 390 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.82.10** **Rate** **table** **historical** **data** **report** **command**


This command is used to report a number of time stamped values (historical) in physical units in the
device.


Table 2.483: Rate Table Historical Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|Command Class = COMMAND_CLASS_RATE_TBL_MONITOR|
|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|Command = RATE_TBL_HISTORICAL_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|
|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|Minute local Time|
|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|
|Historical Precision 1|Historical Precision 1|Historical Precision 1|Historical Scale 1|Historical Scale 1|Historical Scale 1|Historical Scale 1|Historical Scale 1|
|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|
|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|
|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|
|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|
|…|…|…|…|…|…|…|…|
|Historical Precision N|Historical Precision N|Historical Precision N|Historical Scale N|Historical Scale N|Historical Scale N|Historical Scale N|Historical Scale N|
|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|
|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|
|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|
|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|



**Reports** **to** **follow** **(8** **bits)**


This value indicates how many report frames there are left, the value 0xFF means that the number
of reports have not been calculated yet or that there is more than 255 reports to follow.


**Rate** **Parameter** **Set** **ID** **(8** **bits)**

The Rate Parameter Set ID addresses the wanted parameter set. The rate parameter set identifier
MUST be a sequence starting from 1 to Rates Supported.


**Dataset** **(24** **bits)**

The dataset parameter indicates which data is included in the report. This field MUST be encoded
according to the Meter Dataset defined in [26].


**Year** **1,** **2** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December). A year equal to 0x0000
indicates that a accumulated value is not determined yet.


**Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00..23) in local time.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 389




<!-- PAGE 391 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00..59) in local
time.


**Second** **Local** **Time** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00..59) in local time. The value
60 used to keep UTC from wandering away is not supported.


**Historical** **Precision** **(N** ***** **3** **bits)**

The Historical Precision field describes what the precision of the value is. The number indicates the
number of decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Historical** **Scale** **(N** ***** **5** **bits)**


The Historical Scale used to indicate the scale (unit) of the following value. The Historical Scale
parameter is of the variable type Meter Scale; refer to Section 2.2.62.13.


**Historical** **Value** **(N** ***** **32** **bits)**

The Historical Value is a 32 bit signed field defined by dataset requested field. The first byte (Value 1)
is the most significant byte. shows signed decimal values together with their hexadecimal equivalents.


NOTICE: The device receiving the Rate Table Historical Data Report MUST show the value even
though the Scale is not supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 390