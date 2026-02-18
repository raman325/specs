<!-- PAGE 216 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43** **Generic** **Schedule** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


The Generic Schedule Command Class is used to define schedules.

Schedules defined in this command class are essentially time ranges or intervals. Each schedule is
associated to a Schedule ID.

The Schedules defined in this Command Class can be used in other Command Classes, e.g. to schedule
when user credentials are valid or when to apply a particular configuration.


**2.2.43.1** **Terminology**


**Schedules** are composed by one or more **Time** **Range(s)** . A time range is a composed of one or
several **scheduling** **parameters**, such as weekdays, day of the month, hour of the day, etc.

Time ranges are defined individually with scheduling parameters. For example, it could be Time
Range 1 representing weekdays during work hours and Time Range 2 representing public holidays at
fixed dates. (e.g. 25th of December and 31st of October)


A schedule can then be set **including** or **excluding** each of its composing time ranges. Schedule ID
1 could include weekdays work hours (Time Range 1) and exclude public holidays (Time Range 2). It
means that Schedule 1 must be active only on weekdays work hours when it is not a public holiday.

At least one of the included Time Ranges conditions must be fulfilled and none of the excluded Time
Ranges must be fulfilled for a Schedule to be active.


**2.2.43.2** **Interoperability** **considerations**


This Command Class relies on time and date synchronization between controlling and supporting
nodes.


Nodes supporting this command class should also have correct time or date settings depending on
their capabilities. Supporting nodes may support the Clock Command Class for this purpose. The
Time Command Class may also be used for reading the current date and time at the supporting node.


**2.2.43.3** **Generic** **Schedule** **Capabilities** **Get** **Command**


This command is used to request the scheduling capabilities of a supporting node.


The Generic Schedule Capabilities Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.233: Generic Schedule Capabilities Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|Command = GENERIC_SCHEDULE_CAPABILITIES_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 215




<!-- PAGE 217 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.4** **Generic** **Schedule** **Capabilities** **Report** **Command**


This command is used to advertise the number of supported Schedule Slot IDs for each Schedule
Type/User Identifier by the sending node.


Table 2.234: Generic Schedule Capabilities Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|Command = GENERIC_SCHEDULE_CAPABILITIES_REPORT|
|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|Number of supported Schedule IDs (MSB)|
|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|Number of supported Schedule IDs (LSB)|
|Res|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|Number of supported Time Range IDs (MSB)|
|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|Number of supported Time Range IDs (LSB)|
|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|Number of supported Time Ranges per Schedule|
|Reserved|Reserved|Reserved|Reserved|Reserved|Week- days|Date|Hour & Minute|



**Number** **of** **supported** **Schedule** **IDs** **(16** **bits)**

This field is used to indicate how many Schedule IDs are supported by a supporting node.

This field MUST be in the range 1..65535.


**Number** **of** **supported** **Time** **Range** **IDs** **(15** **bits)**

This field is used to indicate how many Time Ranges IDs are supported by a supporting node.

This field MUST be in the range 1.. 32767.


The number of supported Time Ranges IDs should be equal or greater than the ( _Number_ _of_ _supported_
_Schedule_ _IDs_ ) x ( _Number_ _of_ _supported_ _Time_ _Ranges_ _per_ _Schedule_ )


**Number** **of** **supported** **Time** **Ranges** **per** **Schedule** **(8** **bits)**

This field is used to indicate how many time ranges can be used as part of 1 schedule.

This field MUST be in the range 1..255.


**Weekdays** **(1** **bit)**

This field is used to indicate if the supporting node can accept weekdays in the time ranges.


The value 0 MUST indicate that weekdays are not supported in time ranges and will be ignored.


The value 1 MUST indicate that weekdays are supported in time ranges.


**Date** **(1** **bit)**

This field is used to indicate if the supporting node can accept years, month and day parameters in
the time ranges.


The value 0 MUST indicate that start/stop dates are not supported in time ranges and will be ignored.


The value 1 MUST indicate that start/stop dates are supported in time ranges.


**Hour** **&** **Minute** **(1** **bit)**

This field is used to indicate if the supporting node can accept start and stop hours/minutes in the
time ranges.


The value 0 MUST indicate that start/stop hours/minutes are not supported in time ranges and will
be ignored.


The value 1 MUST indicate that start/stop hours/minutes are supported in time ranges.


A supporting node MUST advertise support for at least 1 scheduling parameter (Weekdays, Date,
Hour & Minute).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 216




<!-- PAGE 218 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.5** **Generic** **Schedule** **Time** **Range** **Set** **Command**


This command is used to configure a Time Range for a supporting node.

A Time Range MUST be active when all the conditions indicated in its configuration are fulfilled.
Some examples are provided in Section 2.2.43.5.1.


Table 2.235: Generic Schedule Time Range Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|Command = GENERIC_SCHEDULE_TIME_RANGE_SET|
|Res|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|
|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|
|In use|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|
|In use|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|
|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|
|In use|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|
|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|
|In use|Reserved|Reserved|Reserved|Start Month|Start Month|Start Month|Start Month|
|In use|Reserved|Reserved|Reserved|Stop Month|Stop Month|Stop Month|Stop Month|
|In use|Reserved|Reserved|Start Day|Start Day|Start Day|Start Day|Start Day|
|In use|Reserved|Reserved|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|In use|Reserved|Reserved|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|In use|Reserved|Reserved|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|In use|Res|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|In use|Res|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|
|In use|Reserved|Reserved|Daily Start Hour|Daily Start Hour|Daily Start Hour|Daily Start Hour|Daily Start Hour|
|In use|Reserved|Reserved|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|
|In use|Res|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|
|In use|Res|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|



**Res** **/** **Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Time** **Range** **ID** **(15** **bits)**

This field is used to indicate which Time Range ID to use for the Time Range being set.

This field MUST be in the range 0..[Number of supported Time Range IDs].

The value 0 MUST indicate that the supporting node MUST erase all configured Time Ranges. In
this case, all other fields MUST be set to 0 and ignored by a receiving node.


Values in the range 1..[Number of supported Time Range IDs] MUST indicate the actual Time Range
ID to configure.

If a non-supported Time Range ID is specified in this command, a receiving node MUST ignore the
command.


**In** **use** **(15** **x** **1** **bit)**

This field is used to indicate if the corresponding scheduling parameter must be used in the Time
Range being set.

This field MUST apply to the scheduling parameter being part of the same byte. E.g. the “in use”
field part of the byte comprising the _Weekday_ _bitmask_ field MUST indicate if the _Weekday_ _bitmask_
parameter MUST be used and applied to the current Time Range.

The value 0 MUST indicate that the corresponding field is set to 0 and MUST be ignored.

The value 1 MUST indicate that the corresponding field is set to a valid value and MUST be applied
for the actual Time Range ID.

All “in use” fields set to 0 MUST indicate to erase a Time Range configuration.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 217




<!-- PAGE 219 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Weekday** **bitmask** **(7** **bits)**

This field is used to indicate on which days the actual Time Range ID MUST be active.

This field MUST be treated as a bitmask and encoded according to Table 2.236.


Table 2.236: Generic Schedule Set::Weekday bitmask encoding

|Bit #|Weekday|
|---|---|
|Bit 0|Sunday|
|Bit 1|Monday|
|Bit 2|Tuesday|
|Bit 3|Wednesday|
|Bit 4|Thursday|
|Bit 5|Friday|
|Bit 6|Saturday|



If the corresponding _In_ _use_ field is set to 1:


 - The value 0 MUST indicate that the Time Range MUST NOT be active during the corresponding
weekday.


 - The value 1 MUST indicate that the Time Range MUST be active during the corresponding
weekday.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST be active regardless of the current
weekday.

A supporting node MUST ignore this field if it advertises no support for the weekday scheduling
parameter in the Generic Schedule Capabilities Report Command


**Start** **Year** **(15** **bits)**

This field is used to indicate the start year for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. This field MUST be encoded
using unsigned representation.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Stop** **Year** **(15** **bits)**

This field is used to indicate the stop year for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. This field MUST be encoded
using unsigned representation.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Start** **Month** **(4** **bits)**

This field is used to indicate the start month for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. The values 1..12 MUST represent
respectively January..December.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Stop** **Month** **(4** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 218




<!-- PAGE 220 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate the stop month for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. The values 1..12 MUST represent
respectively January..December.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Start** **Day** **(5** **bits)**

This field is used to indicate the start day of the month for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. The field MUST be in the range
1..31.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Stop** **Day** **(5** **bits)**

This field is used to indicate the stop day of the month for the actual Time Range ID.

If the corresponding _In_ _use_ field is set to 1, the fields MUST indicate that the Time Range ID MUST
be use this field as parameter. Refer to Section 2.2.43.5.1 for details. The field MUST be in the range
1..31.

If the corresponding _In_ _use_ field is set to 0, the Time Range MUST ignore this parameter.

A supporting node MUST ignore this field if it advertises no support for the Date scheduling parameters in the Generic Schedule Capabilities Report Command


**Start** **Hour** **/Stop** **Hour** **(5** **bits)** **&** **Start** **Minute** **/** **Stop** **Minute** **(6** **bits)**

These fields are used to indicate from and until which times the actual Time Range ID MUST be
active.

If the corresponding _In_ _use_ field is set to 1:

 - The _Start_ _Hour_ _/_ _Stop_ _Hour_ fields MUST be in the range 0..23.

 - The _Start_ _Minute_ _/_ _Stop_ _Minute_ fields MUST be in the range 0..59.

If the corresponding In use field is set to 0, the corresponding field MUST be ignored by the Time
Range.

A supporting node MUST ignore this field if it advertises no support for the Hour & Minute scheduling
parameter in the Generic Schedule Capabilities Report Command


**Daily** **Start** **Hour** **/Stop** **Hour** **(5** **bits)** **&** **Daily** **Start** **Minute** **/** **Stop** **Minute** **(6** **bits)**

These fields are used to indicate in which time range the actual Time Range ID MUST be active.

If the corresponding _In_ _use_ field is set to 1:


 The fields MUST indicate that the Time Range ID MUST be active daily between the 2 specified
hour and minutes times. (e.g. from the 08:00 to 16:30)

 - The Start Hour / Stop Hour fields MUST be in the range 0..23.

 - The Start Minute / Stop Minute fields MUST be in the range 0..59.

If the corresponding _In_ _use_ field is set to 0, the corresponding field MUST be ignored by the Time
Range.

A supporting node MUST ignore this field if it advertises no support for the Hour & Minute scheduling
parameter in the Generic Schedule Capabilities Report Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 219




<!-- PAGE 221 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.5.1** **Time** **Range** **parameters** **and** **rules**


Time Ranges MUST be active when all their scheduling parameters are matching the conditions. We
define the parameter groups shown in Table 2.237.


Table 2.237: Generic Schedule Set Command::Parameter groups

|Parameter Group|Fields|
|---|---|
|Daily Start time|Daily Start Hour<br>Daily Start Minute|
|Daily Stop time|Daily Stop Hour<br>Daily Stop Minute|
|Start Datetime|Start Year<br>Start Month<br>Start Day<br>Start Hour<br>Start Minute|
|Stop Datetime|Stop Year<br>Stop Month<br>Stop Day<br>Stop Hour<br>Stop Minute|
|Weekday|Weekday bitmask|



**2.2.43.5.2** **All** **parameters** **specified**


If all Scheduling parameters are specified in a TimeRange, the Time Range MUST be active when
the following condition is fulfilled:


 - Daily Start Time <= Current time < Daily Stop Time


 - Start Datetime <= Current datetime <= Stop Datetime


 - Current weekday in (weekday bitmask)


For example, if Daily Start Time is set to 08:30, Daily Stop Time is set to 17:00, Start Datetime is
set to 10th of January 2019 at 12:00, Stop Datetime is set to 5th of February 2019 at 12:00, Weekday
bitmask is set to Monday to Friday, then the Time Range will be active:


 - On the 10th of January 2019 from 12:00 to 17:00


 - On subsequent weekdays until the 4th of February 2019, between 08:30 and 17:00


 - On the 5th of February 2019 from 08:30 to 12:00


**2.2.43.5.3** **Some** **parameters** **undefined** **in** **parameter** **groups**


If some of the parameters within a group are undefined, they are to be interpreted as wildcard and
excluded from the comparison for the parameter group. For example, if Start Datetime has no Start
Year and Start Month defined, but only Start Day set to 15, the time range MUST start on the 15th
of every month also regardless of the year.


If Start Day is set to 15 and Stop Minute is set to 30, then the Time Range MUST be active every
hour during 30 minutes from the 15th until the end of each month.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 220




<!-- PAGE 222 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.5.4** **All** **parameters** **missing** **from** **a** **parameter** **group**


If all fields are undefined (not in use) for a parameter group, the corresponding parameter group
MUST NOT be used for the Time Range activation. For example, if none of the Stop Datetime
parameters are defined, then the Time Range MUST be active when:


 - Daily Start Time <= Current time < Daily Stop Time


 - Start Datetime <= Current datetime


 - Current weekday in (weekday bitmask)


**2.2.43.6** **Generic** **Schedule** **Time** **Range** **Get** **Command**


This command is used to request the configuration of a Time Range ID for a supporting node.


The Generic Schedule Time Range Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.238: Generic Schedule Time Range Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|Command = GENERIC_SCHEDULE_TIME_RANGE_GET|
|Res|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|
|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|



**Time** **Range** **ID** **(16** **bits)**

This field is used to specify the requested Time Range ID.

The first byte MUST carry the most significant byte of the 15 bits.

A supporting node MUST return this value in the _Time_ _Range_ _ID_ field in the returned Generic
Schedule Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 221




<!-- PAGE 223 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.7** **Generic** **Schedule** **Time** **Range** **Report** **Command**


This command is used to advertise the configuration of a Time Range ID for a supporting node.


Table 2.239: Generic Schedule Time Range Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|Command = GENERIC_SCHEDULE_TIME_RANGE_REPORT|
|Res|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|
|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|Time Range ID 2 (LSB)|
|In use|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|Weekday bitmask|
|In use|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|Start Year (MSB)|
|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|Start Year (LSB)|
|In use|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|Stop Year (MSB)|
|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|Stop Year (LSB)|
|In use|Reserved|Reserved|Reserved|Start Month|Start Month|Start Month|Start Month|
|In use|Reserved|Reserved|Reserved|Stop Month|Stop Month|Stop Month|Stop Month|
|In use|Reserved|Reserved|Start Day|Start Day|Start Day|Start Day|Start Day|
|In use|Reserved|Reserved|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|In use|Reserved|Reserved|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|In use|Reserved|Reserved|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|In use|Res|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|In use|Res|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|
|In use|Reserved|Reserved|Daily Start Hour|Daily Start Hour|Daily Start Hour|Daily Start Hour|Daily Start Hour|
|In use|Reserved|Reserved|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|Daily Stop Hour|
|In use|Res|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|Daily Start Minute|
|In use|Res|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|Daily Stop Minute|
|Res|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|
|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|Next Time Range ID|



Fields not described below MUST remain identical to the description in Section 2.2.43.5 Generic
Schedule Time Range Set Command.


**Res** **/** **Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Time** **Range** **ID** **(15** **bits)**

This field is used to indicate which Time Range ID configuration is being advertised.

If this field is set to a non-supported or non-configured Time Range ID, all scheduling parameters
fields MUST be set to 0.


**Next** **Time** **Range** **ID** **(15** **bits)**

This field is used to indicate the next non-empty Time Range ID.

This field MUST indicate the next non-empty Time Range ID. The value 0 MUST indicate that there
is no following Time Range ID configured at the receiving node.

Non-empty Time Range slot ID means that at least 1 _In_ _use_ flag is set to 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 222




<!-- PAGE 224 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.8** **Generic** **Schedule** **Set** **Command**


This command is used to configure a Schedule for a supporting node.


A schedule MUST be active when:


 - At least one of the included Time Ranges is active


 - None of the excluded Time Ranges are active.


Refer to Section 2.2.43.8.1 for details.


Table 2.240: Generic Schedule Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|Command = GENERIC_SCHEDULE_SET|
|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|
|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|
|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|
|Include/ exclude|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|
|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|
|…|…|…|…|…|…|…|…|
|Include/ exclude|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|
|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|



**Res** **/** **Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Schedule** **ID** **(16** **bits)**

This field is used to indicate which Schedule slot ID to use for the schedule being set.

This field MUST be in the range 0..[Number of supported Schedule IDs].

The value 0 MUST indicate that the supporting node MUST erase all configured schedules. In this
case, the _Number_ _of_ _Time_ _Range_ _IDs_ field MUST be set to 0 by a sending node.


Values in the range 1..[Number of supported Schedule IDs] MUST indicate the actual Schedule ID to
configure.

If a non-supported Schedule ID is specified in this command, a receiving node MUST ignore the
command.


**Number** **of** **Time** **Range** **IDs** **(8** **bits)**

This field is used to indicate the number of Time Range IDs included as part of the Schedule.

This field MUST be in the range 0..[Number of supported Time Range IDs per Schedule].


A supporting node MUST ignore this command if it is set to a value higher than the reported _Number_
_of_ _supported_ _Time_ _Ranges_ _per_ _Schedule_ field in the Generic Schedule Capabilities Report Command

The number of _Include/exclude_ and _Time_ _Range_ _ID_ field blocks in this command MUST be according
to this field.


**Include/exclude** **(N** **x** **1** **bit)**

This field is used to indicate if the Schedule ID must include or exclude the corresponding Time Range
ID.


The value 0 MUST indicate that the corresponding Time Range is excluded and the schedule MUST
be active outside of the Time Range.


The value 1 MUST indicate that the corresponding Time Range is included and the schedule MUST
be active during the defined Time Range.


**Time** **Range** **ID** **(N** **x** **15** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 223




<!-- PAGE 225 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate which Time Range ID MUST be part of the Schedule ID.

Undefined Time Range IDs (all zeroed out) may be part of Schedules.


**2.2.43.8.1** **Schedules** **and** **Time** **Ranges** **examples**


**2.2.43.8.2** **Example** **1**


 - Time Range 1 is from 24th to 26th of December


 - Time Range 2 is from 17:00 to 08:00 every day


 - Time Range 3 is weekend days.


If a schedule is set to:


 - Include Time Range 1


 - Exclude Time Range 2


 - Include Time Range 3


Then it MUST be active:


 - every week-end from 08:00 to 17:00


 - on the 24th,25th and 26th of December from 08:00 to 17:00 regardless of the current weekday.


**2.2.43.8.3** **Example** **2**


 - Time Range 3 is undefined (all unused value).


If a schedule is set to:


 - Include Time Range 1


 - Include Time Range 2


 - Include Time Range 3


Then the schedule MUST be active at all times.


**2.2.43.8.4** **Example** **3**


 - Time Range 3 is undefined (all unused value).


If a schedule is set to:


 - Include Time Range 1


 - Exclude Time Range 2


 - Exclude Time Range 3


Then the schedule MUST never be active.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 224




<!-- PAGE 226 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.43.8.5** **Example** **4**


 - Time Range 1 has no start time and finishes on the 30th of June


 - Time Range 2 is from 08:00 to 17:00 on week days


 - Time Range 3 is 10:00 to 15:00 on weekend days


If a schedule is set to:


 - Include Time Range 1


 - Include Time Range 2


 - Include Time Range 3


Then the schedule MUST be active:


 - All the time from the 1st of January until the 30th of June


 - From 08:00 to 17:00 on weekdays between the 1st of July and the 31st of December every year


 - From 10:00 to 15:00 on weekends between the 1st of July and the 31st of December every year


**2.2.43.9** **Generic** **Schedule** **Get** **Command**


This command is used to request the configuration of a Schedule ID for a supporting node.


The Generic Schedule Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.241: Generic Schedule Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|Command = GENERIC_SCHEDULE_GET|
|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|
|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|



**Schedule** **ID** **(16** **bits)**

This field is used to specify the requested Schedule ID.

The first byte MUST carry the most significant byte of the 16 bits.

A supporting node MUST return this value in the _Schedule_ _ID_ field in the returned Generic Schedule
Report Command.


**2.2.43.10** **Generic** **Schedule** **Report** **Command**


This command is used to advertise the contents of a Schedule for a supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 225




<!-- PAGE 227 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.242: Generic Schedule Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|Command Class = COMMAND_CLASS_GENERIC_SCHEDULE|
|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|Command = GENERIC_SCHEDULE_REPORT|
|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|Schedule ID 1 (MSB)|
|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|Schedule ID 2 (LSB)|
|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|Number of Time Range IDs|
|Include/ exclude|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|Time Range ID 1 (MSB)|
|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|Time Range ID 1 (LSB)|
|…|…|…|…|…|…|…|…|
|Include/ exclude|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|Time Range ID N (MSB)|
|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|Time Range ID N (LSB)|
|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|Next Schedule ID 1 (MSB)|
|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|Next Schedule ID 2 (LSB)|



Fields not described below MUST remain identical to the description in Section 2.2.43.10.


**Res** **/** **Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Schedule** **ID** **(16** **bits)**

This field is used to indicate which Schedule ID configuration is being advertised.

If this field is set to a non-supported or non-configured Schedule ID, all the _Number_ _of_ _Time_ _Range_
_IDs_ field MUST be set to 0.


**Number** **of** **Time** **Range** **IDs** **(8** **bits)**

This field is used to indicate the number of Time Range IDs included as part of the Schedule.

This field MUST be in the range 0..[Number of supported Time Range IDs per Schedule].

The number of _Include/exclude_ and _Time_ _Range_ _ID_ field blocks in this command MUST be according
to this field.


**Include/exclude** **(N** **x** **1** **bit)**

This field is used to indicate if the Schedule ID must include or exclude the corresponding Time Range
ID.


The value 0 MUST indicate that the corresponding Time Range is excluded and the schedule MUST
be active outside of the Time Range.


The value 1 MUST indicate that the corresponding Time Range is included and the schedule MUST
be active during the defined Time Range.


**Time** **Range** **ID** **(N** **x** **15** **bits)**

This field is used to indicate which Time Range ID MUST be part of the Schedule ID.

Undefined Time Range IDs (all zeroed out) may be part of Schedules.


**Next** **Schedule** **ID** **(16** **bits)**

This field is used to indicate the next non-empty Schedule ID.

This field MUST indicate the next non-empty Schedule slot ID. The value 0 MUST indicate that there
is no following Schedule Slot ID configured at the supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 226




<!-- PAGE 228 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.44** **Geographic** **LocationCommand** **Class,** **version** **1**


The Geographic Location Command Class is used to read latitude and longitude from another device.
The latitude and longitude may also be set according to the geographic location in question. Date and
geographic location may be used to calculate sunrise and sunset for e.g. automatic lighting control.


**2.2.44.1** **Multi** **Channel** **Considerations**


Multi Channel End Points SHOULD NOT support the Geographic Location Command Class.


**2.2.44.2** **Geographic** **Location** **Set** **Command**


This command is used to set latitude and longitude.


Table 2.243: Geographic Location Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|
|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|Command = GEOGRAPHIC_LOCATION_SET|
|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|
|Long. Sign|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|
|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|
|Lat. Sign|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|



**Longitude** **(16** **bits)**


The longitude determines one’s location on the earth’s surface, East or West of the Greenwich Meridian. The Greenwich Meridian is located at the Greenwich observatory, in Greenwich, England to be
the geographic point for where East and West meet. Therefore, Greenwich Meridian is indicated as 0°
longitude. Longitude values for points East of the Meridian are always positive, while points West of
the Meridian are always negative. Valid ranges are for degrees (from -180 to 180) and minutes (0-59).
Other values will be interpreted as 0.


**Latitude** **(16** **bits)**


The latitude determines one’s location on the earth’s surface, North or South of the Equator. Latitude
is measured between -90° South, and +90° North of the Equator point (0°). Valid ranges are for degrees
(from -90 to 90) and minutes (0-59). Other values will be interpreted as 0.


**2.2.44.3** **Geographic** **Location** **Get** **Command**


This command is used to request latitude and longitude from a device.


The Geographic Location Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.244: Geographic Location Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|
|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|Command = GEOGRAPHIC_LOCATION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 227




<!-- PAGE 229 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.44.4** **Geographic** **Location** **Report** **Command**


This command returns latitude and longitude from a device in a Z-Wave network.


Table 2.245: Geographic Location Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|Command Class = COMMAND_CLASS_GEOGRAPHIC_LOCATION|
|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|Command = GEOGRAPHIC_LOCATION_REPORT|
|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|Longitude Degrees|
|Long. Sign|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|Longitude Minutes|
|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|Latitude Degrees|
|Lat. Sign|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|Latitude Minutes|



Refer to description under the _Geographic_ _Location_ _Set_ _Command_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 228