<!-- PAGE 300 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62** **Meter** **Table** **Monitor** **Command** **Class,** **version** **1**


The Meter Table Monitor Command Class defines the Commands necessary to read historical and
accumulated values in physical units from a water meter or other metering device (gas, electric etc.)
and thereby enabling automatic meter reading capabilities


**2.2.62.1** **Meter** **Table** **Point** **Adm.** **Number** **Get** **Command**


This command is used to request the Meter Point Administration Number to identify customer.


The Meter Table Adm. Number Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.362: Meter Table Point Adm Number Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|Command = METER_TBL_TABLE_POINT_ADM_NO_GET|



**2.2.62.2** **Meter** **Table** **Point** **Adm.** **Number** **Report** **Command**


This command reports parameters used for identification of customer and metering device.


Table 2.363: Meter Table Point Adm Number Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|
|Reserved|Reserved|Reserved|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|
|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|
|…|…|…|…|…|…|…|…|
|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|



Fields MUST be according to descriptions in the Meter Table Point Adm Number Set Command from
the Meter Table Configuration Command Class, version 1.


**2.2.62.3** **Meter** **Table** **ID** **Get** **Command**


This command is used to request the parameters used for identification of customer and metering
device.


The Meter Table ID Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.364: Meter Table ID Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|Command = METER_TBL_TABLE_ID_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 299




<!-- PAGE 301 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.4** **Meter** **Table** **ID** **Report** **Command**


This command reports parameters used for identification of customer and metering device.


Table 2.365: Meter Table ID Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|
|Reserved|Reserved|Reserved|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|
|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|
|…|…|…|…|…|…|…|…|
|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Meter** **ID** **Characters** **(5** **bits)**

This field is used to indicate the length of the Meter ID Character field in bytes.

This field MUST be in the range 1..32.


**Meter** **ID** **Character** **(N** **bytes)**

This field is used to identify the individual metering device.

The length of this field in bytes MUST be according to the _Number_ _of_ _Meter_ _ID_ _Characters_ field.

Each byte of this field MUST be encoded with ASCII representation and be in the range 0x00..0x7F.

A controlling node can use the Manufacturer Specific Command Class in conjunction for product
identification.


**2.2.62.5** **Meter** **Table** **Capability** **Get** **Command**


This command is used to request the meter table capabilities of a supporting device.


The Meter Table Capability Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.366: Meter Table Capability Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|Command = METER_TBL_TABLE_CAPABILITY_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 300




<!-- PAGE 302 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.6** **Meter** **Table** **Capability** **Report** **Command**


This command is used to advertise meter table capabilities of the sending node.


Table 2.367: Meter Table Capability Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|
|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Reserved|Reserved|Reserved|Reserved|Pay Meter|Pay Meter|Pay Meter|Pay Meter|
|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|
|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|
|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|
|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|
|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|
|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|
|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|
|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|
|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|



**Rate** **Type** **(2** **bits)**

This field is used to indicate if the actual reading advertises import or export values.


The Import value for a meter reading MUST indicate that the reading indicates a consumed amount.


The Export value for a meter reading MUST indicate that the reading indicates a produced amount.

This field MUST be encoded according to the Rate Types values defined in [26].


**Meter** **Type** **(6** **bits)**

This field is used to specify the type of metering physical unit that is being reported.

This field MUST be encoded according to the Meter Types values defined in [26].


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Pay** **Meter** **(4** **bits)**

This field is used to indicate the type of payment that is used for the meter.

This field MUST be encoded according to the Pay meter values defined in [26].


**Dataset** **Supported** **(24** **bits)**

This field is used to advertise which datasets are supported and can be requested from the metering
node with the Meter Table Current Data Get Command.

This field MUST be encoded according to the Meter dataset bitmask values defined in [26].


**Dataset** **History** **Supported** **(24** **bits)**

This field is used to advertise which datasets are supported and can be requests from the metering
node with the Meter Table Historical Data Get Command.

This field MUST be encoded according to the Meter dataset bitmask values defined in [26].


**Data** **History** **Supported** **(24** **bits)**

This field is used to advertise the total number of entries that the supporting node can hold in memory
for historical values.

This field MUST be in the range 0..16777215.


The value 0 MUST indicate that Historical data cannot be requested to the sending node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 301




<!-- PAGE 303 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.7** **Meter** **Table** **Status** **Supported** **Get** **Command**


This command is used to request the supported operating status event parameters and logging depth
of the metering device.


The Meter Table Status Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.368: Meter Table Status Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|Command = METER_TBL_STATUS_SUPPORTED_GET|



**2.2.62.8** **Meter** **Table** **Status** **Supported** **Report** **Command**


This command is used to report the supported operation status and logging depth of these in the

meter.


Table 2.369: Meter Table Status Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|Command = METER_TBL_STATUS_SUPPORTED_REPORT|
|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|Supported Operating Status 1|
|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|Supported Operating Status 2|
|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|Supported Operating Status 3|
|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|



**Supported** **Operating** **Status** **(24** **bits)**

This field is used to advertise which operating statuses are supported and can be sent by the metering
node in the Meter Table Status Report Command.

This field MUST be encoded as a bitmask according to the Operating status values defined in [26].


If the Operating Status event is supported, the corresponding bit MUST be set to 1.


If the Operating Status event is not supported, the corresponding bit MUST be set to 0.

A supporting node MAY support no operating status event and set this field to 0.


**Status** **Event** **Log** **Depth** **(8** **bits)**

This field MUST indicate the supported depth of the event log.

This field MUST be in the range 0..255.

If the supporting node can only return the current status, this field MUST be set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 302




<!-- PAGE 304 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.9** **Meter** **Table** **Status** **Depth** **Get** **Command**


This command is used to request the current operating status of the metering device or to request a
number of the latest status event from the logs.


The Meter Table Status Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.370: Meter Table Status Depth Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|
|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|Status Event Log Depth|



**Status** **Event** **Log** **Depth** **(8** **bits)**

This field is used to indicate the number of last recorded events that should be returned.


The value 0x00 MUST indicate that the receiving node MUST return the current status only.


Values in the range 0x01..0xFE MUST indicate the number of last recorded event that the receiving
node SHOULD return.


The value 0xFF MUST indicate that the receiving node SHOULD return its entire status event log.


**2.2.62.10** **Meter** **Table** **Status** **Date** **Get** **Command**


This command is used to request a number of status events recorded in a certain time interval.


The Meter Table Status Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


If a supporting node does not support a status event log history, it MUST return the current state of
the meter (refer to the Meter Table Status Report Command).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 303




<!-- PAGE 305 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.371: Meter Table Status Date Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|
|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|
|Start - Year 1|Start - Year 1|Start - Year 1|Start - Year 1|Start - Year 1|Start - Year 1|Start - Year 1|Start - Year 1|
|Start - Year 2|Start - Year 2|Start - Year 2|Start - Year 2|Start - Year 2|Start - Year 2|Start - Year 2|Start - Year 2|
|Start - Month|Start - Month|Start - Month|Start - Month|Start - Month|Start - Month|Start - Month|Start - Month|
|Start - Day|Start - Day|Start - Day|Start - Day|Start - Day|Start - Day|Start - Day|Start - Day|
|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|Start - Hour Local Time|
|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|Start - Minute Local Time|
|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|Start - Second Local Time|
|Stop - Year 1|Stop - Year 1|Stop - Year 1|Stop - Year 1|Stop - Year 1|Stop - Year 1|Stop - Year 1|Stop - Year 1|
|Stop - Year 2|Stop - Year 2|Stop - Year 2|Stop - Year 2|Stop - Year 2|Stop - Year 2|Stop - Year 2|Stop - Year 2|
|Stop - Month|Stop - Month|Stop - Month|Stop - Month|Stop - Month|Stop - Month|Stop - Month|Stop - Month|
|Stop - Day|Stop - Day|Stop - Day|Stop - Day|Stop - Day|Stop - Day|Stop - Day|Stop - Day|
|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|Stop - Hour Local Time|
|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|Stop - Minute Local Time|
|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|Stop - Second Local Time|



**Maximum** **Reports** **(8** **bits)**

This field is used to indicate the maximum number of Meter Table Status Report Command that
can be returned to advertise the requested status event history. The most recent recorded log entries
MUST be returned first.


The value 0x00 MUST indicate that there is no maximum number of reports for returning the event
log and the supporting node MUST return as many Reports as necessary to advertise the requested
entry logs.


Values in the range 0x01..0xFF MUST indicate an actual upper limit number of reports to advertise
the requested entry logs.


**Start/Stop** **-** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Start/Stop** **-** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December).


**-**
**Start/Stop** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Start/Stop** **-** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00-23) in local time.


**Start/Stop** **-** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00-59) in local
time.


**Start/Stop** **-** **Second** **Local** **Time** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00-59) in local time. The value
60 used to keep UTC from wandering away is not supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 304




<!-- PAGE 306 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.11** **Meter** **Table** **Status** **Report** **Command**


This command is used to advertise the current status and optionally historical status data of the

meter.


Table 2.372: Meter Table Status Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|Command = METER_TBL_STATUS_DEPTH_GET|
|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|
|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|Current Operating Status 1|
|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|Current Operating Status 2|
|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|Current Operating Status 3|
|Event 1 - Type|Reserved|Reserved|Event 1 - Operating Status Event ID|Event 1 - Operating Status Event ID|Event 1 - Operating Status Event ID|Event 1 - Operating Status Event ID|Event 1 - Operating Status Event ID|
|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|Event 1 - Year 1|
|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|Event 1 - Year 2|
|Event 1 - Month|Event 1 - Month|Event 1 - Month|Event 1 - Month|Event 1 - Month|Event 1 - Month|Event 1 - Month|Event 1 - Month|
|Event 1 - Day|Event 1 - Day|Event 1 - Day|Event 1 - Day|Event 1 - Day|Event 1 - Day|Event 1 - Day|Event 1 - Day|
|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|Event 1 - Hour Local Time|
|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|Event 1 - Minute Local Time|
|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|Event 1 - Second Local Time|
|…|…|…|…|…|…|…|…|
|Event N - Type|Reserved|Reserved|Event N - Operating Status Event ID|Event N - Operating Status Event ID|Event N - Operating Status Event ID|Event N - Operating Status Event ID|Event N - Operating Status Event ID|
|Event N - Year 1|Event N - Year 1|Event N - Year 1|Event N - Year 1|Event N - Year 1|Event N - Year 1|Event N - Year 1|Event N - Year 1|
|Event N - Year 2|Event N - Year 2|Event N - Year 2|Event N - Year 2|Event N - Year 2|Event N - Year 2|Event N - Year 2|Event N - Year 2|
|Event N - Month|Event N - Month|Event N - Month|Event N - Month|Event N - Month|Event N - Month|Event N - Month|Event N - Month|
|Event N - Day|Event N - Day|Event N - Day|Event N - Day|Event N - Day|Event N - Day|Event N - Day|Event N - Day|
|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|Event N - Hour Local Time|
|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|Event N -Minute Local Time|
|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|Event N - Second Local Time|



**Reports** **to** **follow** **(8** **bits)**

This field MUST be used if multiple Meter Table Status Report Commands are used to report the
requested Operating status.


Values in the range 0x00..0xFE MUST indicate the actual number of commands following the actual
command.


The value 0xFF MUST indicate that the number of remaining commands have not been calculated
yet or is higher than 255.


**Current** **Operating** **Status** **(24** **bits)**

This field is used to advertise which operating statuses are currently active at the sending node.

This field MUST be encoded as a bitmask according to the Operating status values defined in [26].


If the _Operating_ _Status_ _event_ is active, the corresponding bit MUST be set to 1.


If the _Operating_ _Status_ _event_ is not active, the corresponding bit MUST be set to 0.


**Event** **-** **Type** **(N** ***** **1** **bit)**

This field is used to advertise the type of the actual event in the event log. It represents the transition
to or from a state.


The value 0 MUST indicate that the sending node entered the state described by the corresponding
Operating Status Event ID at the reported time.


The value 1 MUST indicate that the sending node left the state described by the corresponding
Operating Status Event ID at the reported time.


**Event** **-** **Operating** **Status** **Event** **ID** **(N** ***** **5** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 305




<!-- PAGE 307 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the identifier of the actual event in the event log.

This field MUST be encoded according to the Operating status Event identifier values defined in [26].


**Event** **-** **Year** **(N** ***** **16** **bits)**

This field is used to specify the year in the usual Gregorian calendar for the actual event. The first
byte (Year 1) MUST be the most significant byte.


**Event** **-** **Month** **(N** ***** **8** **bits)**

This field is used to specify the month of the year between 01 (January) and 12 (December) for the
actual event. This field MUST be in the range 1..12.


**Event** **-** **Day** **(N** ***** **8** **bits)**

This field is used to specify the day of the month for the actual event. This field MUST be in the
range 1..31


**Event** **-** **Hour** **Local** **Time** **(N** ***** **8** **bits)**

This field is used to specify the number of complete hours that have passed since midnight in local
time for the actual event. This field MUST be in the range 0..23.


**Event** **-** **Minute** **Local** **Time** **(N** ***** **8** **bits)**

This field is used to specify the number of complete minutes that have passed since the start of the
hour in local time for the actual event. This field MUST be in the range 0..59.


**Event** **-** **Second** **Local** **Time** **(N** ***** **8** **bits)**

This field is used to specify the number of complete seconds since the start of the minute in local time
for the actual event. The value 60 used to keep UTC from wandering away is not supported. This
field MUST be in the range 0..59.


**2.2.62.12** **Meter** **Table** **Current** **Data** **Get** **Command**


This command is used to request a number of time stamped values (current) in physical units according
to the dataset mask.


The Meter Table Current Data Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.373: Meter Table Current Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|Command = METER_TBL_CURRENT_DATA_GET|
|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|Dataset Requested 1|
|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|Dataset Requested 2|
|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|Dataset Requested 3|



**Dataset** **Requested** **(24** **bits)**

This field is used to indicate which datasets are requested from the supporting node.

This field MUST be encoded as a bitmask and according to the Meter dataset bitmask values defined
in [26].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 306




<!-- PAGE 308 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.13** **Meter** **Table** **Current** **Data** **Report** **Command**


This command is is used to report a number of time stamped values.


Table 2.374: Meter Table Current Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Rate Type|Rate Type|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|
|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|
|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|
|Current Meter Precision 1|Current Meter Precision 1|Current Meter Precision 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|
|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|
|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|
|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|
|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|
|…|…|…|…|…|…|…|…|
|Current Meter Precision N|Current Meter Precision N|Current Meter Precision N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|
|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|
|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|
|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|
|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Reports** **to** **follow** **(8** **bits)**

This field MUST be used if multiple Meter Table Current Data Report Commands are used to report
the requested values.


Values in the range 0x00..0xFE MUST indicate the actual number of commands following the actual
command.


The value 0xFF MUST indicate that the number of remaining commands have not been calculated
yet or is higher than 255.


**Rate** **Type** **(2** **bits)**

This field is used to specify the type of parameters advertised in this command. This field MUST be
encoded according to the rate types values defined in [26].


**Dataset** **(24** **bits)**

This field is used to indicate which datasets are included in this command. This field MUST be
encoded as a bitmask and according to the Meter dataset bitmask values defined in [26].

The length of the _Current_ _Meter_ _Precision_, _Current_ _Meter_ _Scale_ and _Current_ _Value_ fields MUST be
according to the number of bits set in this field.


**Year** **(16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 307




<!-- PAGE 309 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to specify the year in the usual Gregorian calendar. The first byte (Year 1) MUST
be the most significant byte. A year equal to 0x0000 MUST indicate that an accumulated value is
not determined yet.


**Month** **(8** **bits)**

This field is used to specify the month of the year between 01 (January) and 12 (December). This
field MUST be in the range 1..12.


**Day** **(8** **bits)**

This field is used to specify the day of the month. This field MUST be in the range 1..31.


**Hour** **Local** **Time** **(8** **bits)**

This field is used to specify the number of complete hours that have passed since midnight in local
time. This field MUST be in the range 0..23.


**Minute** **Local** **Time** **(8** **bits)**

This field is used to specify the number of complete minutes that have passed since the start of the
hour in local time. This field MUST be in the range 0..59.


**Second** **Local** **Time** **(8** **bits)**

This field is used to specify the number of complete seconds since the start of the minute in local
time. The value 60 used to keep UTC from wandering away is not supported. This field MUST be in
the range 0..59.


**Meter** **Precision** **(N** ***** **3** **bits)**

This field is used to indicate how many decimal places are included in the corresponding Current Value
field. For example, the Current Value field set to 1025 with this field set to 2 MUST be interpreted
as equal to 10.25.


**Meter** **Scale** **(N** ***** **5** **bits)**

This field is used to indicate the scale (unit) for the corresponding Current Value field reading. This
field MUST be encoded according to the Meter Scale values defined in [26].


**Current** **Value** **(N** ***** **4** **bytes)**

This field is used to advertise an actual meter reading.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12, Signed field
encoding (two’s complement representation).

Readings MUST be advertised according to the _Dataset_ field. The first reading MUST correspond to
the first bit set in the _Dataset_ field, the second reading MUST correspond to the second bit set in the
_Dataset_ field, and so on.


A controlling node MUST always show the value even if the reading type or scale are unknown.


A controlling node SHOULD implement the capability to update its list of Meter datasets and scales,
so that new Meter readings and scales added in [26] are not presented as unknown. If a controlling
node receives an unknown Meter reading or scale, it SHOULD allow the user to assign a free-text
description to that Meter reading


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 308




<!-- PAGE 310 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.62.14** **Meter** **Table** **Historical** **Data** **Get** **Command**


This command is used to request a number of time stamped values (historical) in physical units
according to rate type, dataset bitmask and time interval.


The Meter Table Historical Data Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.375: Meter Table Historical Data Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|Command = METER_TBL_HISTORICAL_DATA_GET|
|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|Maximum Reports|
|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|Historical Dataset Requested 1|
|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|Historical Dataset Requested 2|
|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|Historical Dataset Requested 3|
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

This field is used to indicate the maximum number of Meter Table Historical Data Report Commands
that can be returned to advertise the requested historical data. The most recent recorded values
MUST be returned first.


The value 0x00 MUST indicate that there is no maximum number of reports for returning the event
log and the supporting node MUST return as many Reports as necessary to advertise the requested
historical values.


Values in the range 0x01..0xFF MUST indicate an actual upper limit number of reports to advertise
the requested historical values.


**Dataset** **History** **(24** **bits)**

This field is used to indicate which datasets are requested from the supporting node.

This field MUST be encoded as a bitmask and according to the Meter dataset bitmask values defined
in [26].


**Start/Stop** **Year** **(16** **bits)**

This field is used to specify the year in the usual Gregorian calendar. The first byte (Year 1) MUST
be the most significant byte.


**Start/Stop** **Month** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 309




<!-- PAGE 311 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to specify the month of the year between 01 (January) and 12 (December). This
field MUST be in the range 1..12.


**Start/Stop** **Day** **(8** **bits)**

This field is used to specify the day of the month. This field MUST be in the range 1..31.


**Start/Stop** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00-23) in local time.


**Start/Stop** **Minute** **Local** **Time** **(8** **bits)**

This field is used to specify the number of complete minutes that have passed since the start of the
hour (00-59) in local time. This field MUST be in the range 0..59.


**Start/Stop** **Second** **Local** **Time** **(8** **bits)**

This field is used to specify the number of complete seconds since the start of the minute in local
time. The value 60 used to keep UTC from wandering away is not supported. This field MUST be in
the range 0..59.


**2.2.62.15** **Meter** **Table** **Historical** **Data** **Report** **Command**


This command is used to report a number of time stamped values.


Table 2.376: Meter Table Historical Data Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Rate Type|Rate Type|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|
|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|
|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|
|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|
|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|
|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|
|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|
|Historical Precision 1|Historical Precision 1|Historical Precision 1|Historical Precision 1|Historical Scale 1|Historical Scale 1|Historical Scale 1|Historical Scale 1|
|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|Historical Value 1,1|
|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|Historical Value 1,2|
|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|Historical Value 1,3|
|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|Historical Value 1,4|
|…|…|…|…|…|…|…|…|
|Historical Precision N|Historical Precision N|Historical Precision N|Historical Precision N|Historical Scale N|Historical Scale N|Historical Scale N|Historical Scale N|
|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|Historical Value N,1|
|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|Historical Value N,2|
|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|Historical Value N,3|
|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|Historical Value N,4|



**Reports** **to** **Follow** **(8** **bits)**

This field MUST be used if multiple Meter Table Current Data Report Commands are used to report
the requested values.


Values in the range 0x00..0xFE MUST indicate the actual number of commands following the actual
command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 310




<!-- PAGE 312 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0xFF MUST indicate that the number of remaining commands have not been calculated
yet or is higher than 255.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Rate** **Type** **(2** **bits)**

This field is used to specify the type of parameters advertised in this command. This field MUST be
encoded according to the rate types values defined in [26].


**Dataset** **(24** **bits)**

This field is used to indicate which datasets are included in this command. This field MUST be
encoded as a bitmask and according to the Meter dataset bitmask values defined in [26].

If no historical data has been registered for the requested period, this field MUST be set to 0 and the
_Historical Scale_, _Historical Precision_ and _Historical Value_ fields MUST be omitted from the command.


**Historical** **Year** **(16** **bits)**

This field is used to specify for the dataset the year in the usual Gregorian calendar. The first byte
(Year 1) MUST be the most significant byte. A year equal to 0x0000 indicates that an accumulated
value is not determined yet.


**Historical** **Month** **(8** **bits)**

This field is used to specify for the dataset the month of the year between 01 (January) and 12
(December). This field MUST be in the range 1..12.


**Historical** **Day** **(8** **bits)**

This field is used to specify for the dataset the day of the month. This field MUST be in the range
1..31.


**Historical** **Hour** **Local** **Time** **(8** **bits)**

This field is used to specify for the dataset the number of complete hours that have passed since
midnight in local time. This field MUST be in the range 0..23.


**Historical** **Minute** **Local** **Time** **(8** **bits)**

This field is used to specify for the dataset the number of complete minutes that have passed since
the start of the hour in local time. This field MUST be in the range 0..59.


**Historical** **Second** **Local** **Time** **(8** **bits)**

This field is used to specify for the dataset the number of complete seconds since the start of the
minute in local time. The value 60 used to keep UTC from wandering away is not supported. This
field MUST be in the range 0..59.


**Historical** **Precision** **(N** ***** **3** **bits)**

This field is used to specify how many decimal places are included in the corresponding _Historical_
_Value_ field. For example, the _Historical_ _Value_ field set to 1025 with this field set to 2 MUST be
interpreted as equal to 10.25.


**Historical** **Scale** **(5** **bits)**

This field is used to indicate the scale (unit) of the corresponding _Historical_ _Value_ field reading. This
field MUST be encoded according to the Meter Scale values defined in [26].


**Historical** **Value**

This field is used to advertise an actual historical meter reading.

The first byte MUST be the most significant byte.

This field MUST be encoded using signed representation and comply with Table 2.12, Signed field
encoding (two’s complement representation).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 311




<!-- PAGE 313 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Readings MUST be advertised according to the _Dataset_ field. The first reading MUST correspond to
the first bit set in the _Dataset_ field, the second reading MUST correspond to the second bit set in the
_Dataset_ field, and so on.


A controlling node MUST always show the value even if the reading type or scale are unknown.


A controlling node SHOULD implement the capability to update its list of Meter datasets and scales,
so that new Meter readings and scales added in [26] are not presented as unknown. If a controlling
node receives an unknown Meter reading or scale, it SHOULD allow the user to assign a free-text
description to that Meter reading


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 312

---

<!-- PAGE 314 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.63** **Meter** **Table** **Monitor** **Command** **Class,** **version** **2**


The Meter Table Monitor Command Class defines the Commands necessary to read historical and
accumulated values in physical units from a water meter or other metering device (gas, electric etc.)
or electric sub-metering device and thereby enabling automatic meter reading capabilities.


**2.2.63.1** **Compatibility** **Considerations**


The Meter Table Monitor Command Class, version 2 is backwards compatible with the Meter Table
Monitor Command Class, version 1.

All commands and fields not mentioned in this version MUST remain unchanged from the Meter
Table Monitor Command Class, version 1.


**2.2.63.2** **Meter** **Table** **Point** **Adm.** **Number** **Report** **Command**


This command reports parameters used for identification of customer and metering device.


Table 2.377: Meter Table Point Adm Number Report Command,

version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|Command = METER_TBL_TABLE_POINT_ADM_NO_REPORT|
|Reserved|Reserved|Reserved|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|Number of Meter Point Adm. Number Characters|
|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|Meter Point Adm. Number Character 1|
|…|…|…|…|…|…|…|…|
|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|Meter Point Adm. Number Character N|



Fields not described below MUST remain unchanged from version 1.


**Number** **of** **Meter** **Point** **Adm.** **Number** **Characters** **(5** **bits)**

If the _Meter_ _Table_ _Point_ _Adm,_ _Number_ has not been set using the Meter Table Configuration Command Class, this field MUST be set to 0x00 and the _Meter_ _Point_ _Adm._ _Numbers_ _Character_ field
MUST be omitted.


**2.2.63.3** **Meter** **Table** **ID** **Report** **Command**


This command reports parameters used for identification of customer and metering device.


Table 2.378: Meter Table ID Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|Command = METER_TBL_TABLE_ID_REPORT|
|Reserved|Reserved|Reserved|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|Number of Meter ID Characters|
|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|Meter ID Character 1|
|…|…|…|…|…|…|…|…|
|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|Meter ID Character N|



Fields not described below MUST remain unchanged from version 1.


**Number** **of** **Meter** **ID** **Characters** **(5** **bits)**

This field is used to indicate the length of the _Meter_ _ID_ _Character_ field in bytes.

This field MUST be in the range 0..32.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 313




<!-- PAGE 315 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0 MUST indicate that the Meter ID is not used and the _Meter_ _ID_ _Character_ field MUST
be omitted from the command.


**2.2.63.4** **Meter** **Table** **Capability** **Report** **Command**


This command is used to advertise meter table capabilities.


Table 2.379: Meter Table Capability Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|Command = METER_TBL_TABLE_CAPABILITY_REPORT|
|Rate Type|Rate Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|Meter Type|
|Reserved|Reserved|Reserved|Reserved|Pay Meter|Pay Meter|Pay Meter|Pay Meter|
|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|Dataset Supported 1|
|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|Dataset Supported 2|
|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|Dataset Supported 3|
|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|Dataset History Supported 1|
|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|Dataset History Supported 2|
|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|Dataset History Supported 3|
|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|Data History Supported 1|
|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|Data History Supported 2|
|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|Data History Supported 3|



Fields not described below MUST remain unchanged from version 1.


**Rate** **Type** **(2** **bits)**

This field is used to indicate if the actual reading advertises import or export values.


The Import value for a meter reading MUST indicate that the reading indicates a consumed amount.


The Export value for a meter reading MUST indicate that the reading indicates a produced amount.

This field MUST be encoded according to the Rate Types values defined in [26].

If the _Meter_ _Type_ field is set to Submeter (0x0B), this field MUST be set to Import (0x01).


**2.2.63.5** **Meter** **Table** **Current** **Data** **Report** **Command**


This command is used to report a number of time stamped values.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 314




<!-- PAGE 316 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.380: Meter Table Current Data Report Command, version

|Table 2.38 2 7|80: Meter T 6|Table Curre 5|ent Data R 4|Report Com 3|mmand, vers 2|sion 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|Command = METER_TBL_CURRENT_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Operating Status<br>Indication|Reserved|Reserved|Reserved|Reserved|Reserved|Rate Type|Rate Type|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|
|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|
|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|
|Current Meter Precision 1|Current Meter Precision 1|Current Meter Precision 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|Current Meter Scale 1|
|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|Current Value 1,1|
|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|Current Value 1,2|
|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|Current Value 1,3|
|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|Current Value 1,4|
|…|…|…|…|…|…|…|…|
|Current Meter Precision N|Current Meter Precision N|Current Meter Precision N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|Current Meter Scale N|
|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|Current Value N,1|
|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|Current Value N,2|
|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|Current Value N,3|
|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|Current Value N,4|



Fields not described below MUST remain unchanged from version 1.


**Operating** **Status** **Indication** **(1** **bit)**

This field is used to indicate that the reported meter data is measured while the meter is in an
operating status different from Normal (0x00) e.g. accuracy warning or clock not accurate.

The value 1 MUST indicate that the meter is operating in a status different from Normal


The value 0 MUST indicate that the meter is operating in Normal mode (Operating status=0x00).


**Rate** **Type** **(2** **bits)**

This field is used to indicate the type of parameters in the report. This field MUST be encoded
according to the Rate Types values defined in [26].

If the _Meter_ _Type_ field is set to Submeter (0x0B), this field MUST be set to Import (0x01).


**2.2.63.6** **Meter** **Table** **Historical** **Data** **Report** **Command**


This command is used to report a number of time stamped values.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 315




<!-- PAGE 317 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.381: Meter Table Historical Data Report Command, ver
|Table 2.38 sion 2 7|81: Meter T 6|Table Histo 5|orical Data 4|a Report C 3|Command, v 2|ver- 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|Command Class = COMMAND_CLASS_METER_TBL_MONITOR|
|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|Command = METER_TBL_HISTORICAL_DATA_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Operating Status<br>Indication|Reserved|Reserved|Reserved|Reserved|Reserved|Rate Type|Rate Type|
|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|Dataset 1|
|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|Dataset 2|
|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|Dataset 3|
|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|Historical Year 1|
|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|Historical Year 2|
|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|Historical Month|
|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|Historical Day|
|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|Historical Hour Local Time|
|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|Historical Minute Local Time|
|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|Historical Second Local Time|
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



Fields not described below MUST remain unchanged from version 1.


**Operating** **Status** **Indication** **(1** **bit)**

This field is used to indicate that the reported meter data is measured while the meter is in an
operating status different from Normal (0x00) e.g. accuracy warning or clock not accurate.

The value 1 MUST indicate that the meter is operating in a status different from Normal


The value 0 MUST indicate that the meter is operating in Normal mode (Operating status=0x00).


**Rate** **Type** **(2** **bits)**

This field is used to indicate the type of parameters in the report. This field MUST be encoded
according to the Rate Types values defined in [26].

If the _Meter_ _Type_ field is set to Submeter (0x0B), this field MUST be set to Import (0x01).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 316

---

<!-- PAGE 318 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.64** **Meter** **Table** **Monitor** **Command** **Class,** **version** **3**


The Meter Table Monitor Command Class, version 3 is used for advanced metering applications.
It allows reading historical and accumulated values in physical units from a water meter or other
metering device (gas, electric etc.) or electric sub-metering device and thereby enabling automatic
meter reading capabilities


**2.2.64.1** **Compatibility** **Considerations**


The Meter Table Monitor Command Class, version 3 is backwards compatible with the Meter Table
Monitor Command Class, version 2.

All commands and fields not mentioned in this version MUST remain unchanged from the Meter
Table Monitor Command Class, version 2.


The list of supported Meter Types, Meter scales and Meter dataset bitmasks is moved to [26]. Values
not defined in [26] are reserved and MUST NOT be used by a supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 317