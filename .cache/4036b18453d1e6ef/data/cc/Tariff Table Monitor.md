<!-- PAGE 477 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.103** **Tariff** **Table** **Monitor** **Command** **Class,** **version** **1**


The Tariff Table Monitor Command Class defines the cost for a range of rates.


**2.2.103.1** **Tariff** **Table** **Supplier** **Get** **Command**


This command is used to request the name of the utility supplier.

The Tariff Table Supplier Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|Command = TARIFF_TBL_SUPPLIER_GET|



**2.2.103.2** **Tariff** **Table** **Supplier** **Report** **Command**


This command is used to advertise the name of the utility supplier.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|Command = TARIFF_TBL_SUPPLIER_REPORT|
|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|Utility Timestamp Year 1|
|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|Utility Timestamp Year 2|
|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|Utility Timestamp Month|
|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|Utility Timestamp Day|
|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|Utility Timestamp Hour Local Time|
|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|Utility Timestamp Minute Local Time|
|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|Utility Timestamp Second Local Time|
|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|
|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|
|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|
|Standing Charge Precision|Standing Charge Precision|Standing Charge Precision|Standing Charge Period|Standing Charge Period|Standing Charge Period|Standing Charge Period|Standing Charge Period|
|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|Standing Charge Value 1|
|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|Standing Charge Value 2|
|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|Standing Charge Value 3|
|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|Standing Charge Value 4|
|Reserved|Reserved|Reserved|Number of Supplier Characters|Number of Supplier Characters|Number of Supplier Characters|Number of Supplier Characters|Number of Supplier Characters|
|Supplier Character 1|Supplier Character 1|Supplier Character 1|Supplier Character 1|Supplier Character 1|Supplier Character 1|Supplier Character 1|Supplier Character 1|
|…|…|…|…|…|…|…|…|
|Supplier Character N|Supplier Character N|Supplier Character N|Supplier Character N|Supplier Character N|Supplier Character N|Supplier Character N|Supplier Character N|



Refer to description of fields under the Tariff Table Supplier Set Command (Section 2.2.102.1).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 476




<!-- PAGE 478 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.103.3** **Tariff** **Table** **Get** **Command**


This command is used to request the tariff for the corresponding rate parameter set.

The Tariff Table Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|Command = TARIFF_TBL_GET|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**


The Rate Parameter Set ID addresses the price for the accompanying rate parameter set. The Rate
Table Supported Report Command determines the number of supported rate parameter sets.


**2.2.103.4** **Tariff** **Table** **Report** **Command**


This command is used to advertise information relating to a given Rate Parameter Set Identifier.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|Command = TARIFF_TBL_REPORT|
|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|Rate Parameter Set ID<br>|
|Tarif Precision|Tarif Precision|Tarif Precision|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|
|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|Tarif Value 1<br>|
|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|Tarif Value 2<br>|
|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|Tarif Value 3<br>|
|Tarif Value 4|Tarif Value 4|Tarif Value 4|Tarif Value 4|Tarif Value 4|Tarif Value 4|Tarif Value 4|Tarif Value 4|



Refer to description of fields under the Tariff Table Set Command (Section 2.2.102.2)


**2.2.103.5** **Tariff** **Table** **Cost** **Get** **Command**


This command is used to request the cost according to rate parameter set ID, rate type, dataset mask
and time interval.

The Tariff Table Cost Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 477




<!-- PAGE 479 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|Command = TARIFF_TBL_COST_GET|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|
|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|
|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|
|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|
|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|
|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**


The Rate Parameter Set ID indicates the requested parameter set. Rate Parameter Set ID equal to
0xFF returns overall accumulated cost.


**Start** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Start** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December).


**Start** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Start** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00-23) in local time.


**Start** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00-59) in local
time.


**Stop** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.
Setting the parameter to 0xFFFF indicates now.


**Stop** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December). A year equal to 0x0000
indicates that an accumulated value is not determined yet. Setting the parameter to 0xFF indicates

now.


**Stop** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31. Setting the parameter to 0xFF indicates now.


**Stop** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00-23) in local time. Setting
the parameter to 0xFF indicates now.


**Stop** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00-59) in local
time. Setting the parameter to 0xFF indicates now.


**Stop** **Second** **Local** **Time** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 478




<!-- PAGE 480 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Specify the number of complete seconds since the start of the minute (00-59) in local time. The value
60 used to keep UTC from wandering away is not supported. Setting the parameter to 0xFF indicates

now.


**2.2.103.6** **Tariff** **Table** **Cost** **Report** **Command**


This command is used to report a number of time stamped values (historical) in physical units in the
device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|Command Class = COMMAND_CLASS_TARIFF_TBL_MONITOR|
|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|Command = TARIFF_TBL_COST_REPORT|
|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|Rate Parameter Set ID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Rate Type|Rate Type|
|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|Start Year 1|
|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|Start Year 2|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|Start Hour Local Time|
|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|Start Minute Local Time|
|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|Stop Year 1|
|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|Stop Year 2|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|Stop Hour Local Time|
|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|Stop Minute Local Time|
|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|
|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|
|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|
|Cost Precision|Cost Precision|Cost Precision|Reserved|Reserved|Reserved|Reserved|Reserved|
|Cost Value 1|Cost Value 1|Cost Value 1|Cost Value 1|Cost Value 1|Cost Value 1|Cost Value 1|Cost Value 1|
|Cost Value 2|Cost Value 2|Cost Value 2|Cost Value 2|Cost Value 2|Cost Value 2|Cost Value 2|Cost Value 2|
|Cost Value 3|Cost Value 3|Cost Value 3|Cost Value 3|Cost Value 3|Cost Value 3|Cost Value 3|Cost Value 3|
|Cost Value 4|Cost Value 4|Cost Value 4|Cost Value 4|Cost Value 4|Cost Value 4|Cost Value 4|Cost Value 4|



**Rate** **Parameter** **Set** **ID** **(8** **bits)**


The Rate Parameter Set ID indicates the requested parameter set. Rate Parameter Set ID equal to
0xFF returns accumulated cost.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Rate** **Type** **(2** **bits)**

Rate Type specifies the type of parameters in the report. This field MUST be encoded according to
Table 2.345.


**Start/Stop** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Start/Stop** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December). A year equal to 0x0000
indicates that a accumulated value is not determined yet.


**Start/Stop** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Start/Stop** **Hour** **Local** **Time** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 479




<!-- PAGE 481 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Specify the number of complete hours that have passed since midnight (00-23) in local time.


**Start/Stop** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00-59) in local
time.


**Currency** **(3** **bytes)**

ISO 4217 defines the currency code. Examples are given in Table 2.519.


**Cost** **Precision** **(3** **bits)**

The precision field describes what the precision of the value is. The number indicates the number of
decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Cost** **Value** **(32** **bits)**

The Cost value is a 32 bit un-signed field. The first byte is the most significant byte.


The value 0xFFFFFFFF is reserved, and SHOULD be used to report that the cost calculation has
not yet been performed.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 480