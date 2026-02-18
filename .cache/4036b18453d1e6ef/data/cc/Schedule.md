<!-- PAGE 398 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.86** **Schedule** **Command** **Class,** **version** **1**


The Schedule Command Class allows scheduling the execution of commands for a given duration in
a supporting device. It is a generic Command Class that may be used to schedule commands of any
other Command Class.


**2.2.86.1** **Terminology**


A **schedule** or **regular schedule** is a delayed execution of one or more commands for a given duration.
The commands used in a schedule are typically “Set” type commands, affecting actuating resources
or states.

A schedule is first **created** or **set**, meaning that an available **Schedule** **ID** is used and has been
assigned a set of commands, a starting time and a duration.


A schedule can be **removed**, meaning that a previously set Schedule ID is freed and the assigned
commands, starting time and duration are erased.

A schedule is **active** during the configured duration after its starting time.

When a schedule is active, the states affected by the schedule commands are temporarily changed.

When a schedule becomes inactive, the states affected by the schedule commands are restored to their
previous values.


Several schedules can overlap and be active simultaneously.


Supporting nodes can optionally support **enabling** and **disabling** schedules. By default, a schedule
is enabled when being created. When a schedule is disabled, it will never become active, even if the
start time condition is met. It allows a controlling node to quickly enable/disable schedules without
erasing the schedules configuration from the supporting nodes.


When all schedules are inactive, the supporting node is said to be operating in **Normal** **Mode** .
Regardless of whether any schedule is active, Normal Mode’s states are permanently affected by
**direct** **commands** (issued without Schedule encapsulation). State changes triggered by schedules do
not affect Normal Mode.


Figure 2.24: Simple daily schedules (example)


Direct commands affecting the states of a currently active schedule will cause those states to go back
to normal mode and the corresponding normal mode states/values to be permanently changed.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 397




<!-- PAGE 399 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 2.25: Receiving a direct command during daily schedules (example)


There are 2 types of special schedules.


If a **Fall Back Schedule** is created, it takes over the role of the Normal Mode. The Fall Back Schedule
is activated when all other schedules are inactive. Fall Back Schedule is used to define default settings
or states for the normal mode


If an **Override** **Schedule** is created, it **suspends** all other schedules. An override schedule may have
a start time or start immediately. An override schedule may have a duration, run until stopped or
run until another regular schedule starts. An example is given in the figure below


Figure 2.26: Daily schedules and an “Advance” Override Schedule (example)


An overview of the Schedule types and priorities is given in Table 2.486.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 398




<!-- PAGE 400 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.486: Schedule CC terminology and priority








|Priority|Term|Description|
|---|---|---|
|(highest)|Direct command|Afects device state immediately.<br>Permanently afects Normal Mode.|
|(higher)|Override Schedule<br>(Schedule ID = 0xFF)|All other schedules are suspended as long as<br>the override schedule is active.<br>|
|(normal)|Regular Schedule(s)<br>(Schedule<br>ID<br>in<br>[1..Supported<br>number of schedules])|One or more schedules defning intended be-<br>havior.|
|(lower)|Fall Back Schedule<br>(Schedule ID = 0xFE)|Fall Back Schedule becomes active when no<br>other schedule is currently active.<br>If the Fall Back Schedule is defned, Normal<br>Mode is never reached, unless receiving direct<br>commands.|
|(lowest)|Normal Mode|No schedules are currently active.|



**2.2.86.2** **Interoperability** **Considerations**


CC:0053.01.00.31.001 A schedule causes a temporary state change that only applies to the duration of the schedule. The
state value(s) of the Normal Mode MUST NOT be affected by any command executed as part of a
schedule.


CC:0053.01.00.31.002
The state value(s) of the Normal Mode MUST be restored when the affecting Schedule become inactive.


Schedules are set with a start time, which requires the supporting node to be aware of the current date
CC:0053.01.00.32.001 and/or time. It is RECOMMENDED to support the Clock Command Class or the Time Command
Class in order to allow a controlling node to verify or configure correct date/time settings at the
supporting node.


**2.2.86.2.1** **Override** **Schedule**


CC:0053.01.00.31.003 When the Override Schedule is active, all regular schedules MUST be suspended.


CC:0053.01.00.31.004 When the Override Schedule ends, all suspended schedules MUST resume the state they would have
had if the Override Schedule had not been activated.


CC:0053.01.00.32.002 If the Override Schedule is created with a duration type not set to Override, a receiving node SHOULD
respect the specified duration for the Override Schedule.

CC:0053.01.00.31.005 A supporting node MUST respect the specified duration for all regular schedules.


**2.2.86.2.2** **Fall** **Back** **Schedule**


CC:0053.01.00.31.006 If no Fall Back Schedule is set, a supporting node MUST return to Normal Mode when no schedule
is currently active.


CC:0053.01.00.31.007 If a Fall Back Schedule is set, a supporting node MUST:


      - Activate the Fall Back Schedule when no other schedule is active.


      - De-activate the Fall Back Schedule if any other schedule becomes active.

      - Direct commands state changes MUST be active until the start of a new schedule affecting the
same state values.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 399




<!-- PAGE 401 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.86.2.3** **Multi** **Channel** **considerations**


A Multi Channel device may support different schedule types and command classes for each Multi
Channel End Point. An example is a central heating boiler with a thermostat for room heating and
another thermostat for water heating. Each system may implement regular weekday+time schedules
as well as an override schedule for manual intervention.


CC:0053.01.00.32.003 In any case, it is RECOMMENDED that multi-function devices support the Multi Channel Command
Class, so that each End Point supports its own scheduling functionality.


**2.2.86.3** **Schedule** **Supported** **Get** **Command**


This command is used to query the schedule functionalities supported by a node.


CC:0053.01.01.11.001 The Schedule Supported Report Command MUST be returned in response to this command.


CC:0053.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0053.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|



**2.2.86.4** **Schedule** **Supported** **Report** **Command**


This command is used to advertise the schedule functionalities supported by a node.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|
|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|
|Support<br>Enable/Disable|Fallback<br>Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|
|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|
|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command 1|Supported<br>Command 1|
|…|…|…|…|…|…|…|…|
|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command N|Supported<br>Command N|
|Override<br>Support|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|


**Number** **of** **Supported** **Schedule** **IDs** **(8** **bits)**

CC:0053.01.02.11.001 This field MUST advertise the number of regular Schedule IDs supported by the node.


CC:0053.01.02.11.002 The implemented Schedule IDs MUST be in the range 1..[Number of Supported Schedule IDs]. i.e. a
node supporting 10 regular schedules MUST accept Schedule ID values in the range 1..10.


CC:0053.01.02.13.001 The following special Schedule IDs MAY also be supported by a device:


      - Schedule ID = 0xFF (Override Schedule)


      - Schedule ID = 0xFE (Fall Back schedule)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 400




<!-- PAGE 402 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:0053.01.02.11.003 Special Schedule IDs MUST NOT be included in the number advertised in this field.


**Start** **Time** **Support** **(6** **bits)**

This field is used to advertise the start time options supported for regular schedules by a node.


CC:0053.01.02.11.004 Regular schedules MUST support the advertised start time options.


CC:0053.01.02.12.001 The Override Schedule SHOULD support the advertised start time options.

CC:0053.01.02.11.005 This field MUST be treated as a bitmask and MUST be encoded according to Table 2.487.

|Bit|Table 2.487: Start Time Support encoding Indicates support for|Version|
|---|---|---|
|Bit|Indicates support for|Version|
|0|Start now. Refer to Section 2.2.86.5.|1|
|1|Start Hour and Minute. Refer to Section 2.2.86.6.|1|
|2|Calendar time. Refer to Section 2.2.86.7.|1|
|3|Weekdays. Refer to Section 2.2.86.8.|1|
|4..5|Reserved|N/A|



Each bit indicates the support for a given Start Time option.


CC:0053.01.02.11.006 The value 1 MUST indicate that the node supports the corresponding start time option.


CC:0053.01.02.11.007 The value 0 MUST indicate that the node does not support the corresponding start time option.

While support is advertised as a bitmask, the actual functionality is triggered by different combinations of Schedule Set start time fields. The following subsections outline the mandatory supported
combinations when advertising support for the corresponding option.


**2.2.86.5** **Start** **Time** **Option:** **Start** **Now**


The start now option is used to make a configured schedule start immediately (upon reception of the
Schedule Set Command).


CC:0053.01.02.11.008 A node that supports the start now option, MUST support the creation of a schedule starting immediately when all start time fields are left unspecified.


**2.2.86.6** **Start** **Time** **Option:** **Hour** **and** **Minute**


The start hour and minute option is used to make a schedule start at a specified time of the day.


CC:0053.01.02.11.009
If Start Hour and Start Minute are specified, node supporting this option MUST activate the schedule
at the specified start time.


CC:0053.01.02.11.00A A node supporting the _Hour_ _and_ _Minute_ start option MUST support the creation of a schedule with
the following start time fields’ combination:


      - Every day @ Hour:Minute


(YYMMDD = 0xFF, 0x00, 0x00, Weekdays = 0x00, HH:MM = **Hour:Minute** )


CC:0053.01.02.11.00B A node that also supports the _Weekdays_ start option MUST support the creation of a schedule with
the following start time fields’ combination:


      - Same weekday(s) every week @ Hour:Minute


(YYMMDD = 0xFF, 0x00, 0x00, Weekdays = **weekdays**, HH:MM = **Hour:Minute** )


CC:0053.01.02.11.00C A node that also supports the _Calendar_ _Time_ start option MUST support the creation of a schedule
with the following start time fields’ combination:


      - Same day every month @ Hour:Minute


(YYMMDD = 0xFF, 0x00, **day**, Weekdays = 0x00, HH:MM = **Hour:Minute** )


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 401




<!-- PAGE 403 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - Same day every year @ Hour:Minute


(YYMMDD = 0xFF, **month**, **day**, Weekdays = 0x00, HH:MM = **Hour:Minute** )

      - One specific date in a specific year @ Hour:Minute


(YYMMDD = **year**, **month**, **day**, Weekdays = 0x00, HH:MM = **Hour:Minute** )


**2.2.86.7** **Start** **Time** **Option:** **Calendar** **Time**


The calendar time option is used to make a schedule start at a specified date.

CC:0053.01.02.11.00D If Start Year, Start Month and Start Day are specified, node supporting this option MUST activate
the schedule at the specified date(s).


CC:0053.01.02.11.00E A node that supports the _Calendar_ Time option MUST support the creation of a schedule with the
following start time fields’ combination:


      - Same day every month @ 00:00


(YYMMDD = 0xFF, 0x00, **day**, Weekdays = 0x00, HH:MM = 0x1F, 0x3F)


      - Same day every year @ 00:00


(YYMMDD = 0xFF, **month**, **day**, Weekdays = 0x00, HH:MM = 0x1F, 0x3F)

      - One specific date in a specific year @ 00:00


(YYMMDD = **year**, **month**, **day**, Weekdays = 0x00, HH:MM = 0x1F, 0x3F)


**2.2.86.8** **Start** **Time** **Option:** **Weekday**


The start weekday option is used to make a schedule start at on specified weekdays.

CC:0053.01.02.11.00F If weekdays are specified, node supporting this option MUST activate the schedule on the specified
weekdays.


A node that supports the _Weekdays_ option MUST support the creation of a schedule with the following
start time fields’ combination:


      - Same weekday(s) every week @ 00:00


(YYMMDD = 0xFF, 0x00, 0x00, Weekdays = **weekdays**, HH:MM = 0x1F, 0x3F)


**Fall** **Back** **Support** **(1** **bit)**


This bit is used to advertise the support of the Fall Back Schedule (Schedule ID = 0xFE).


CC:0053.01.02.11.011 The bit MUST be set to 1 if the node supports the Fall Back Schedule.


CC:0053.01.02.11.012 The bit MUST be set to 0 if the node does not support the Fall Back Schedule.


**Support** **Enable/Disable** **(1** **bit)**


This bit is used to advertise the support for enabling/disabling set/used schedules via the Schedule
State Set Command.


CC:0053.01.02.11.013 The bit MUST be set to 0 if the node supports enabling/disabling schedules.


CC:0053.01.02.11.014 The bit MUST be set to 1 if the node does not support enabling/disabling schedules.


CC:0053.01.02.11.015 A node that does not support enabling/disabling schedules MUST consider every set/used schedule
ID as enabled.


**Number** **of** **supported** **CC** **(8** **bits)**

CC:0053.01.02.11.016 This field MUST advertise the number of supported Command Classes advertised in this command
with the Supported CC and Supported Command fields.


CC:0053.01.02.11.017


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 402




<!-- PAGE 404 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0xFF MUST be used if all the command classes supported by the node are also supported
for scheduling. If this field is set to 0xFF:


CC:0053.01.02.11.018 - This command MUST NOT carry any Command Class entries (Supported CC and Supported
Command fields).

CC:0053.01.02.11.019 - The node MUST support “Get” as well as “Set” commands. (i.e. Supported Commands fields
set to 0x00)


**Supported** **CC** **(N** ***** **8** **bits)**

This field is used to advertise the list of Command Classes that can be scheduled by the node.

CC:0053.01.02.11.01A The length of this field MUST be according to the Number of supported CC field value.

CC:0053.01.02.11.01B A sending node MUST support every Command Class advertised in this field.

CC:0053.01.02.12.002 A sending node SHOULD NOT advertise the Supervision Command Class in this field.


CC:0053.01.02.11.01C A sending node MUST NOT advertise the following encapsulation Command Classes:


      - S0/S2 Command Class


      - Transport Service Command Class


      - Multi Channel Command Class


      - Multi Command Command Class


**Supported** **Command** **(N** ***** **2** **bits)**

CC:0053.01.02.11.01D This field MUST advertise the supported commands for the actual command class entry. This field
MUST comply with Table 2.488.

|Value|Table 2.488: Supported Command Description|Version|
|---|---|---|
|Value|Description|Version|
|0x00|Both Set and Get Commands are supported|1|
|0x01|Only Set Commands are supported|1|
|0x02|Only Get Commands are supported|1|
|0x03|Reserved|N/A|



CC:0053.01.02.11.01E Certain command classes commands do not contain the string “Set” or “Get” in their name. Nodes
MUST consider all commands mandating to return a response to be of type “Get” and all other
commands to be of type “Set”.

CC:0053.01.02.11.01F The length of this field MUST be according to the Number of supported CC field value.


**Override** **Support** **(1** **bit)**

This field is used to advertise support for the Override Schedule (Schedule ID = 0xFF).


CC:0053.01.02.11.020 This bit MUST be set to 1 if the node supports the Override Schedule.


CC:0053.01.02.11.021 This bit MUST be set to 0 if the node does not support the Override Schedule.


**Supported** **Override** **Types** **(7** **bits)**

This field is used to advertise the supported Override Schedule duration types.


CC:0053.01.02.11.022 A receiving node MUST ignore this bit mask if the Override Schedule is not supported by the sending
node.

CC:0053.01.02.11.023 This field MUST be treated as a bitmask and MUST be encoded according to Table 2.489.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 403




<!-- PAGE 405 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.489: Schedule Supported Report::Supported Override
Types encoding







|Bit|Name|Description|Version|
|---|---|---|---|
|0|Advance|The override schedule MUST run until the start of<br>the next regular schedule.|1|
|1|Run forever|The override schedule MUST run until the schedule<br>is removed.|1|
|2..6|Reserved|Reserved|N/A|


**2.2.86.9** **Schedule** **Set** **Command**


This command is used to create a new schedule or modify an existing schedule.


This command MUST enable the schedule if a new schedule is created.


This command MUST NOT change the enabled/disabled state of existing schedules.


If the receiving node supports S0 or S2 Command Class, it MUST NOT process the schedule creation
if any of the scheduled command classes is not supported at the security level of the received Schedule
Set Command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Reserved|Reserved|Reserved|Reserved|Start Month|Start Month|Start Month|Start Month|
|Reserved|Reserved|Reserved|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|
|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



**Reserved**

CC:0053.01.03.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Schedule** **ID** **(8** **bits)**

This field is used to indicate which Schedule ID is being set.


CC:0053.01.03.11.005 Values in the range 1..[Number of supported Schedule] MUST indicate regular Schedule IDs


CC:0053.01.03.11.006 The value 0xFE MUST indicate the Fall Back Schedule.


CC:0053.01.03.11.007 The value 0xFF MUST indicate the Override Schedule.

CC:0053.01.03.11.008 A receiving node MUST ignore this command if a non-supported Schedule ID is specified.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 404




<!-- PAGE 406 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If this field is set to 0xFF:

CC:0053.01.03.12.001 - The sending node SHOULD set the start time fields to the Start Now pattern.


CC:0053.01.03.11.009 - The receiving node MUST respond immediately to an Override Schedule .

If this field is set to 0xFE:

CC:0053.01.03.12.002 - The sending node SHOULD set the start time fields and duration fields to 0x00.

CC:0053.01.03.11.00A - The receiving node MUST ignore the start time fields and duration fields


**2.2.86.9.1** **Start** **Time** **fields**


The schedule start time is defined by the following fields:


      - Start Year


      - Start Month


      - Start Day of Month


      - Start Weekday


      - Start Hour


      - Start Minute

CC:0053.01.03.11.00B A receiving node MUST support the start time fields combinations indicated in Section 2.2.86.5, Section 2.2.86.6, Section 2.2.86.7 and Section 2.2.86.8 if the corresponding start time option is supported.

CC:0053.01.03.11.00C If none of the start time fields are specified, the schedule MUST start immediately if the start now

CC:0053.01.03.11.00D option is supported. In this case, the schedule MUST NOT be activated again at a later time unless
receiving another Schedule Set Command.


**Start** **Year** **(8** **bits)**

CC:0053.01.03.11.00E This field is used to set the year for which the schedule is to start. This field MUST be in the range
0..99 or set to 0xFF.


CC:0053.01.03.11.00F Values in the range 0..99 MUST indicate the actual year last 2 digits. A node MUST accept a value
lower than the current year to allow schedules starting in the next century.

CC:0053.01.03.11.010 The value 0xFF MUST be used to indicate that the start year is unspecified.


CC:0053.01.03.11.011
This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the Calendar time start time option in the Schedule Supported Report Command.


**Start** **Month** **(4** **bits)**


CC:0053.01.03.11.012
This field is used to set the month for which the schedule is to start. This field MUST be in the range
0..12.


CC:0053.01.03.11.013 Values in the range 1..12 MUST indicate the actual start month.

CC:0053.01.03.11.014 The value 0x00 MUST be used to indicate that the start month is unspecified.


CC:0053.01.03.11.015
This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the Calendar time start time option in the Schedule Supported Report Command.


**Start** **Day** **of** **Month** **(5** **bits)**

CC:0053.01.03.11.016 This field is used to set the day of month for which the schedule is to start. This field MUST be in
the range 0..31.

CC:0053.01.03.11.017 Values in the range 1..31 MUST indicate the actual start day of the month. If the specified value does

CC:0053.01.03.13.001 not exist in the actual Year/Month tuple (28/29/30 day month), a receiving node MAY ignore this
command.

CC:0053.01.03.11.018 The value 0x00 MUST be used to indicate that the day of the month is unspecified.


CC:0053.01.03.11.019


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 405




<!-- PAGE 407 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the Calendar time start time option in the Schedule Supported Report Command.


**Start** **Weekday** **(7** **bits)**

CC:0053.01.03.11.01A This field is used to set one or more weekdays for which the schedule is to start. This field MUST be
treated a as bitmask and MUST be encoded according to Table 2.490.


Table 2.490: Weekday bitmask encoding

|Bit|Description|Version|
|---|---|---|
|0|Monday|1|
|1|Tuesday|1|
|2|Wednesday|1|
|3|Thursday|1|
|4|Friday|1|
|5|Saturday|1|
|6|Sunday|1|



CC:0053.01.03.11.01B The value 1 MUST indicate that the specified Schedule ID MUST start on the corresponding day.

CC:0053.01.03.11.01C The value 0 MUST indicate that the specified Schedule ID MUST NOT start on the corresponding
day.

CC:0053.01.03.11.01D If any of the Start Year, Start Month or Start Day of Month field is specified, this field MUST be set
to 0x00 by a sending node and MUST be ignored by a receiving node.


CC:0053.01.03.11.01E
This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the Weekday start time option in the Schedule Supported Report Command.


**Start** **Hour** **(5** **bits)**

CC:0053.01.03.11.01F This field is used to set the hour for which the schedule is to start. This field MUST be in the range
0..23 or set to 0x1F.


CC:0053.01.03.11.020 Values in the range 0..23 MUST indicate the start hour of the day.

CC:0053.01.03.11.021 The value 0x1F (31) MUST be used to indicate that the start hour is unspecified.


CC:0053.01.03.11.022
This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the hour and minute start time option in the Schedule Supported Report Command.


**Start** **Minute** **(6** **bits)**


CC:0053.01.03.11.023
This field is used to set the minute for which the schedule is to start. This field MUST be in the range
0..59 or set to 0x3F.


CC:0053.01.03.11.024 Values in the range 0..59 MUST indicate the starting minute of the schedule.

CC:0053.01.03.11.025 The value 0x3F (63) MUST be used to indicate that the start minute is unspecified.


CC:0053.01.03.11.026
This field MUST be ignored and treated as unspecified by a receiving node advertising no support for
the hour and minute start time option in the Schedule Supported Report Command.


**2.2.86.9.2** **Duration** **fields**


The schedule duration is defined by the following fields:


      - Duration Type


      - Duration


**Duration** **Type** **(3** **bits)**


CC:0053.01.03.11.027
This field is used to indicate how to interpret the duration field. This field MUST be encoded according
to Table 2.491.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 406




<!-- PAGE 408 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.491: Duration Type encoding






|Value|Description|Version|
|---|---|---|
|0x00|The duration feld is expressed in Minutes.<br>|1|
|0x01|The duration feld is expressed in Hours.<br>|1|
|0x02|The duration feld is expressed in Days.<br>|1|
|0x03|Override: The duration feld is indicating the Override Type.<br>This value MUST NOT be used if the Schedule ID feld is not set to<br>0xFF|1|



CC:0053.01.03.11.029 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Duration** **(16** **bits)**

CC:0053.01.03.11.02A This field is used to specify the duration of the schedule being set. The Duration Type field MUST
be inspected before interpreting this field.

CC:0053.01.03.11.02B If the Duration Type field is not set to Override (0x03), this field MUST indicate the duration of the
actual schedule. The Duration Type field indicates the unit of this field.


CC:0053.01.03.11.02C
If the Duration Type field is set to Override (0x03), the LSB of this field MUST be encoded according
to Table 2.492 and the MSB of this field MUST be set to 0x00.


Table 2.492: Override Types duration







|Name|Duration value (LSB)|Description|Version|
|---|---|---|---|
|Advance||The override schedule MUST run until the<br>start of the next regular schedule..|1|
|Run forever|0x02|The override schedule MUST run until it is<br>removed.|1|
|Reserved|0x03..0x07|Reserved|N/A|


**2.2.86.9.3** **Command** **and** **other** **fields**


**Reports** **to** **Follow** **(8** **bits)**

CC:0053.01.03.11.02F This field MUST be used if multiple Schedule Set commands are used to define a single schedule.


CC:0053.01.03.11.030 The value MUST indicate the remaining number of Schedule Set Commands. The header bytes
(Schedule ID, Start time, Duration, etc.) MUST be the same for all Schedule Set Commands.


**Number** **of** **Cmd** **to** **Follow** **(8** **bits)**

This field is used to advertise the number of command blocks (Cmd Length/Cmd Byte fields units)
included within the actual Schedule Set Command (represented by P in the command structure).

CC:0053.01.03.11.031 Each command block MUST comprise the Cmd Length and Cmd Byte fields.



CC:0053.01.03.11.032


CC:0053.01.03.11.033



If the list of scheduled commands and their payload is longer than the maximum available Z-Wave
MAC frame size, multiple Schedule Set commands MUST be used to send the complete list of scheduled commands. In this case, this field MUST advertise how many commands are included in the
actual/current Schedule Set Command.


**Cmd** **Length** **(8** **bits)**

This field is used to indicate the length in byte of the corresponding Cmd Byte field.


**Cmd** **Byte** **(N** **bytes)**

This field is used to set the commands to be executed during the actual Schedule.



CC:0053.01.03.11.034
This field MUST carry a complete command including Command Class identifier, Command identifier
and the required parameter bytes.


CC:0053.01.03.11.035


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 407




<!-- PAGE 409 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The length of each Cmd Byte entry MUST be according to the corresponding Cmd Length field entry.

CC:0053.01.03.11.036 The number of Cmd Byte entries MUST be according to the Number of Cmd to Follow field.


CC:0053.01.03.11.037 If a schedule includes commands mandating to return a response, responses MUST be returned to the
node that has set the schedule.



CC:0053.01.03.12.003


CC:0053.01.03.11.038



A receiving node SHOULD ignore the entire Schedule Set Command if this field carries a command
not advertised as supported for scheduling in the Schedule Supported Report Command. In any
case, the receiving node MUST NOT accept commands non-supported for scheduling as part of the
Schedule.



CC:0053.01.03.12.004 A controlling node SHOULD avoid creating conflicting schedules and a supporting node SHOULD
discard a new conflicting schedule, even if the conflict is with a temporarily disabled schedule.


**2.2.86.10** **Schedule** **Get** **Command**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|



**Schedule** **ID** **(8** **bits)**

CC:0053.01.04.11.004 This field MUST carry the requested Schedule ID.


**2.2.86.11** **Schedule** **Report** **Command**


This command is used to report the configuration for a specific schedule.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Active_ID|Active_ID|Active_ID|Active_ID|Start Month|Start Month|Start Month|Start Month|
|Reserved|Reserved|Reserved|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|
|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|
|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



Fields not described below are described in the Schedule Set Command; refer to Section 2.2.86.9.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 408




<!-- PAGE 410 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Schedule** **ID** **(8** **bits)**

This field is used to indicate the advertised Schedule ID.


CC:0053.01.05.11.001 If this command is advertising an unused or unsupported Schedule ID, all parameters until Number
of Cmd to Follow MUST be set to 0x00. The Cmd Length and Cmd Byte fields MUST be omitted.


**Active_ID** **(4** **bits)**

CC:0053.01.05.11.002 This field is used to advertise the status for the requested Schedule ID. This field MUST be encoded
according to Table 2.494.


**Duration** **(16** **bits)**

This field is used to advertise either the configured duration for a schedule or how much time is left
before the schedule becomes inactive.

CC:0053.01.05.11.003 The Duration Type, Start Time and Schedule ID fields MUST be inspected before interpreting this
field. This field MUST advertise a value according to Table 2.493.


Table 2.493: Duration field usage








|Duration Type|Schedule ID|Start Time|Advertised duration|
|---|---|---|---|
|Time<br>(0x00..0x02)|Regular|Specifed start time|Confgured duration|
|Time<br>(0x00..0x02)|Regular of Override|Start now|Remaining time<br>|
|Override (0x03)|Override (0xFF)|Start now|Confgured<br>override<br>type<br>(Table 2.492)|



**2.2.86.12** **Schedule** **Remove** **Command**


This command is used to request the removal of one or all Schedules in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|



**Schedule** **ID** **(8** **bits)**

This field is used to indicate the schedule that is to be removed/erased.

CC:0053.01.06.11.001 If this field is set to 0x00, all configured schedules MUST be removed.

CC:0053.01.06.11.002 If this field is set to 0xFE, the Fall Back Schedule MUST be removed (if defined).

CC:0053.01.06.11.003 If this field is set to 0xFF, the Override Schedule MUST be removed (if defined).

CC:0053.01.06.11.004 If this field is in the range 0x01..[Number of supported Schedules], the receiving node MUST remove
the corresponding schedule.


**2.2.86.13** **Schedule** **State** **Set** **Command**


This command is used to enable or disable a schedule.


CC:0053.01.07.11.001 This command MUST be ignored by a node advertising no support for Enabling/Disabling schedules
in the Schedule Supported Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 409




<!-- PAGE 411 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|



**Schedule** **ID** **(8** **bits)**

This field is used to indicate the schedule that is to be enabled or disabled.


CC:0053.01.07.11.002 The value 0x00 MUST cause the receiving node to change the state for all schedules, except for the
Override Schedule.


CC:0053.01.07.11.003 Values in the range 0x01..[number of supported schedules] and 0xFE MUST indicate the actual schedule ID which state is to be updated.


CC:0053.01.07.11.004 The value 0xFF MUST be ignored by a receiving node. Override schedules cannot be enabled/disabled
and may only be removed using the Schedule Remove Command.


**Schedule** **state** **(8** **bits)**

This field is used to indicate the new state of one or more schedules.


CC:0053.01.07.11.005 The value 0xFF MUST indicate that the actual schedule MUST be enabled.


CC:0053.01.07.11.006 The value 0x00 MUST indicate that the actual schedule MUST be disabled.


CC:0053.01.07.11.007 Disabling a schedule MUST NOT cause the schedule settings to be permanently removed. Schedules
may be permanently removed via the Schedule Remove Command.


CC:0053.01.07.11.008 If a schedule is enabled, the receiving node MUST assess if the actual schedule should have been active
and activate it accordingly.


CC:0053.01.07.11.009 If a schedule is disabled while being active, the receiving node MUST treat the disabling operation as
if the schedule ended.


**2.2.86.14** **Schedule** **State** **Get** **Command**


This command is used to request the status of all schedules supported by a node.


CC:0053.01.08.11.001 The Schedule State Report Command MUST be returned in response to this command.


CC:0053.01.08.11.002 This command MUST NOT be issued via multicast addressing.


CC:0053.01.08.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|



**2.2.86.15** **Schedule** **State** **Report** **Command**


This command is used to advertise the status of all schedules supported by a device.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 410




<!-- PAGE 412 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|
|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Override|
|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 1|Active_ID 1|Active_ID 1|Active_ID 1|
|…|…|…|…|…|…|…|…|
|Active_ID N|Active_ID N|Active_ID N|Active_ID N|Active_ID N-1|Active_ID N-1|Active_ID N-1|Active_ID N-1|



**Number** **of** **Supported** **Schedule** **ID** **(8** **bits)**


CC:0053.01.09.11.001
This field is used to advertise the number of supported regular schedule IDs. This field’s value MUST
be the same as the value advertised in the Schedule Supported Report Command.


**Override** **(1** **bit)**

CC:0053.01.09.11.002 This field MUST be used to advertise the status of the Override Schedule (ID = 0xFF).


CC:0053.01.09.11.003 If the Override Schedule is active, this bit MUST be set to 1.


CC:0053.01.09.11.004 If the Override Schedule is inactive, this bit MUST be set to 0.


**Reports** **to** **Follow** **(7** **bits)**

The length of the Active_ID field may be larger than the maximum available Z-Wave MAC frame
size.

CC:0053.01.09.11.005 This field MUST be used to advertise the number of commands following this command in order to
advertise the status of all Schedules IDs.


CC:0053.01.09.12.001 A controlling node SHOULD use this value to detect missing reports.


**Active_ID** **(N** ***** **4** **bits)**

This field is used to advertise the status for each supported schedule ID. Four bits units are used for
each Schedule ID to indicate the status. It means that:


      - Bits 0 to 3 in Active_ID byte 1 represent Schedule ID = 1


      - Bits 4 to 7 in Active_ID byte 1 represent Schedule ID = 2


      - Bits 0 to 3 in Active_ID byte 2 represent Schedule ID = 3


      - …

CC:0053.01.09.11.006 The size of this field MUST be the smallest number of bytes needed to advertise the number of
supported Schedule IDs advertised in this command.


CC:0053.01.09.11.007
If several Reports are returned (using the Reports to follow field), the first Report advertises Schedule
ID 1 to Schedule ID N and the subsequent report MUST be interpreted as representing Schedule ID
starting from N+1.


CC:0053.01.09.11.008 Each 4 bits unit MUST be encoded according to Table 2.494.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 411




<!-- PAGE 413 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.494: Active_ID encoding







CC:0053.01.09.12.002

















CC:0053.01.09.12.003









CC:0053.01.09.12.004




|Hex|Description|Detailed description|Version|
|---|---|---|---|
|0x00|Not used|The Schedule ID is not used. (not set/confgured) or<br>unsupported|1|
|0x01|[DEPRECATED]<br>Override + Not used|[DEPRECATED]<br>A sending node SHOULD NOT use this status. It<br>is RECOMMENDED to use 0x00 instead. A receiv-<br>ing node MUST interpret this status as Active_ID =<br>0x00 (and the override feld set to 1 for the Schedule<br>State Report Command).|1|
|0x02|Not Active|The Schedule ID is used, enabled and currently not<br>active.|1|
|0x03|Active|The Schedule ID is used, enabled and currently ac-<br>tive.|1|
|0x04|Disabled|The Schedule ID is used and disabled.|1|
|0x05|Override + Active|The Schedule ID is used, enabled and should cur-<br>rently be active but it is suspended by the Override<br>Schedule<br>The override feld MUST be set to 1 when using this<br>status in the Schedule State Report Command.|1|
|0x06|[DEPRECATED]<br>Override + Not Active|[DEPRECATED]<br>A sending node SHOULD NOT use this status. It<br>is RECOMMENDED to use 0x02 instead. A receiv-<br>ing node MUST interpret this status as Active_ID =<br>0x02 (and the override feld set to 1 for the Schedule<br>State Report Command.|1|
|0x07|[DEPRECATED]<br>Override + Disabled|[DEPRECATED]<br>A sending node SHOULD NOT use this status. It<br>is RECOMMENDED to use 0x04 instead. A receiv-<br>ing node MUST interpret this status as Active_ID =<br>0x04 (and the override feld set to 1 for the Schedule<br>State Report Command).|1|



CC:0053.01.09.11.00D All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 412

---

<!-- PAGE 414 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.87** **Schedule** **Command** **Class,** **version** **2**


The Schedule Command Class version 2 allows scheduling the execution of commands for a given
duration in a supporting node. It is a generic command class that may be used to schedule commands
from any other Command Class.


**2.2.87.1** **Compatibility** **Considerations**


The Schedule Command Class, version 2 is backwards compatible with version 1.


CC:0053.02.00.21.001 A node supporting the Schedule Command Class, version 2 MUST also support version 1.


Schedule Command Class, version 2 introduces the following:


      - Schedule ID Blocks

      - Clarification on using Schedule Command Class with Security

All commands or fields not described in this version remain unchanged from version 1.


**2.2.87.1.1** **Schedule** **ID** **Blocks**


In Schedule Command Class version 1, all Schedule IDs have to support the same Start Time Options,
Override Types and supported commands.


The Schedule ID Blocks allows a node to implement several Schedule ID pools sharing the same
scheduling functionalities.


CC:0053.02.00.21.002 Each Schedule ID Block MUST have its own range of Schedule ID’s. The ID for each Block MUST
be in the range 1..[Number of Supported Schedule IDs].


CC:0053.02.00.21.003 Schedule ID Block = 1 is the default Block. A version 1 node MUST be assumed to be using Schedule
ID block 1.


**2.2.87.1.2** **Schedule** **Command** **Class** **with** **Security**


The Schedule Command Class may be implemented by secure devices. Depending on the type of
device, a given Command Class may be supported only via secure communication or via secure as
well as unsecure communication.


The following command class categories may be considered:


      - **Always** **unsecure** :


Examples of command classes which are always supported via unsecure communication          as well as via secure communication if the device is securely included (e.g Z-Wave Plus
Info Command Class).


      - **Migrate** **to** **secure** :


Examples of command classes which are supported via unsecure communication if the
device is not securely included            - but **only** **via** **secure** communication if the device is
securely included. (e.g. Multilevel Switch or Association Command Class)


      - **Secure** **only** :


Examples of command classes which are supported **only** **via** **secure** communication. (e.g.
Door Lock Command Class)

CC:0053.02.00.21.004 To reflect the above mentioned dynamic support scenarios, a device MUST advertise the supported
Command Classes for scheduling in a way that matches the current secure/non-secure supported
Command Class lists found in the NIF and S0/S2 Commands Supported Report Commands.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 413




<!-- PAGE 415 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Clarification is added to the Schedule Supported Report Command and Schedule Set Command for
proper reporting and configuration of unsecure and secure command classes scheduling.


CC:0053.02.00.22.001 It is RECOMMENDED to support the Schedule Command Class only at the highest security level in
order to avoid dynamic listing.


**2.2.87.2** **Schedule** **Supported** **Get** **Command**


This command is used to query the properties of a node.


CC:0053.02.01.11.001 The Schedule Supported Report Command MUST be returned in response to this command.


CC:0053.02.01.11.002 If the receiving node supports S0 or S2 Command Class and this command is issued via non-secure
communication, the receiving node MUST advertise Command Classes that can be scheduled but also
supported at the received security level.


CC:0053.02.01.11.003 This command MUST NOT be issued via multicast addressing.


CC:0053.02.01.11.004 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|Command = SCHEDULE_SUPPORTED_GET|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



**Schedule** **ID** **Block** **(1** **byte)**

This field is used to request a particular Schedule ID Block.

CC:0053.02.01.11.005 If this field is set to 0x00, the receiving node MUST return the default Schedule ID Block (ID = 1).


CC:0053.02.01.11.006
A node receiving a version 1 Schedule Supported Get Command (without the Schedule ID Block field)
MUST return a response for the default Schedule ID Block (ID = 1).


CC:0053.02.01.12.001 A node receiving a non-supported Schedule ID Block SHOULD return a report for the default Schedule
ID Block.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 414




<!-- PAGE 416 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.87.3** **Schedule** **Supported** **Report** **Command**


This command is used to advertise the scheduling functionalities supported by a node for a given
Schedule ID Block.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|
|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|
|Support<br>Enable/Disable|Fallback<br>Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|
|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|
|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command 1|Supported<br>Command 1|
|…|…|…|…|…|…|…|…|
|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command N|Supported<br>Command N|
|Override<br>Support|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|


Fields not described below remain unchanged from version 1.

All fields contained in this command advertise the scheduling supported functionalities for the actual
Schedule ID Block.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to indicate the actual Schedule ID Block for which the supported scheduling functionalities are advertised.

CC:0053.02.02.12.001 The advertised supported functionalities SHOULD be different for every Schedule ID Block.


**Number** **of** **Schedule** **ID** **Blocks** **(8** **bits)**

CC:0053.02.02.11.001 This field MUST advertise the total number of Schedule ID blocks supported by the node.

CC:0053.02.02.11.002 This field MUST be in the range 1..255.


CC:0053.02.02.11.003 The implemented Schedule ID Blocks MUST be in the range 1..[Number of Supported Schedule ID
Blocks]. i.e. a node supporting 10 Schedules ID Blocks MUST accept Schedule ID Blocks values in
the range 1..10.


**2.2.87.4** **Schedule** **Set** **Command**


This command is used to create a new schedule or modify an existing schedule.


CC:0053.02.03.11.001 This command MUST enable the schedule if a new schedule is created.


CC:0053.02.03.11.002 This command MUST NOT change the enabled/disabled state of existing schedules


CC:0053.02.03.11.003 If the receiving node supports S0 or S2 Command Class, it MUST NOT process the schedule creation
if any of the scheduled command classes is not supported at the security level of the received Schedule
Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 415




<!-- PAGE 417 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Reserved|Reserved|Reserved|Reserved|Start Month|Start Month|Start Month|Start Month|
|Reserved|Reserved|Reserved|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|
|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



Fields not described below remain unchanged from version 1.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the Schedule ID Block in which the specified Schedule ID is being set.

CC:0053.02.03.11.004 A node receiving a version 1 Schedule Set Command (with the Schedule ID Block field set to 0x00)
MUST assume the default Schedule ID Block (ID = 0x01).


**2.2.87.5** **Schedule** **Get** **Command**


This command is used to request the configuration for a specific schedule ID.


CC:0053.02.04.11.001 The Schedule Report Command MUST be returned in response to this command.


CC:0053.02.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0053.02.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



Fields not described below remain unchanged from version 1.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the requested Schedule ID Block.

CC:0053.02.04.11.004 A node receiving a version 1 Schedule Get Command (without the Schedule ID Block field) MUST
return a response for the default Schedule ID Block (ID = 1).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 416




<!-- PAGE 418 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.87.6** **Schedule** **Report** **Command**


This command is used to advertise the configuration for a specific schedule.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Active_ID|Active_ID|Active_ID|Active_ID|Start Month|Start Month|Start Month|Start Month|
|Reserved|Reserved|Reserved|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|
|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|
|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



Fields not described below remain unchanged from version 1.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the advertised Schedule ID Block.


**2.2.87.7** **Schedule** **Remove** **Command**


This command is used to request the removal of one or all Schedules in a device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|Command = SCHEDULE_REMOVE|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



**Schedule** **ID** **(8** **bits)**

This field is used to indicate the schedule that is to be removed.

CC:0053.02.06.11.001 If this field is set to 0x00, all schedules within the Schedule ID Block MUST be removed.

CC:0053.02.06.11.002 If this field is set to 0xFE, the Fall Back Schedule MUST be removed (if defined for the Schedule ID
Block).

CC:0053.02.06.11.003 If this field is set to 0xFF, the Override Schedule MUST be removed (if defined for the Schedule ID
Block).

CC:0053.02.06.11.004 If this field is in the range 0x01..[Number of supported Schedules], the receiving node MUST remove
the corresponding schedule in the Schedule ID Block.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 417




<!-- PAGE 419 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to indicate the Schedule ID Block in which a schedule is being removed.

CC:0053.02.06.11.005 A node receiving a version 1 Schedule Set Command (without the Schedule ID Block field) MUST
assume the default Schedule ID Block (ID = 0x01).


CC:0053.02.06.11.006 A node receiving this command with **Schedule ID = 0x00** and **Schedule ID Block = 0x00** MUST
remove all Schedule IDs in all Schedule ID Blocks


CC:0053.02.06.11.007 A node receiving this command with **Schedule** **ID** **=** **0x00** and **Schedule** **ID** **Block** **�0x00** MUST
remove all Schedule IDs from the specified Schedule ID Block.


CC:0053.02.06.11.008 A node receiving this command with **Schedule** **ID** **�0x00** and **Schedule** **ID** **Block** **=** **0x00** MUST
ignore the command


**2.2.87.8** **Schedule** **State** **Set** **Command**


This command is used to enable or disable one or more schedules.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|Command = SCHEDULE_STATE_SET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|Schedule State|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



Fields not described below remain unchanged from version 1.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the Schedule ID Block in which one or more schedule are being enabled
or disabled.


CC:0053.02.07.11.001 This command MUST be ignored by a node advertising no support for Enabling/Disabling schedules
in the Schedule Supported Report Command for the given Schedule ID Block.

CC:0053.02.07.11.002 A node receiving a version 1 Schedule Set Command (without the Schedule ID Block field) MUST
assume the default Schedule ID Block (ID = 0x01).


CC:0053.02.07.11.003 A node receiving this command with **Schedule ID = 0x00** and **Schedule ID Block = 0x00** MUST
enable/disable all Schedule IDs from all Schedule ID Blocks.


CC:0053.02.07.11.004 A node receiving this command with **Schedule** **ID** **=** **0x00** and **Schedule** **ID** **Block** **�0x00** MUST
enable/disable all Schedule IDs from the specified Schedule ID Block.


CC:0053.02.07.11.005 A node receiving this command with **Schedule** **ID** **�0x00** and **Schedule** **ID** **Block** **=** **0x00** MUST
ignore the command.


**2.2.87.9** **Schedule** **State** **Get** **Command**


This command is used to request the status of all schedules within a Schedule ID Block supported by
a node.


CC:0053.02.08.11.001 The Schedule State Report Command MUST be returned in response to this command.


CC:0053.02.08.11.002 This command MUST NOT be issued via multicast addressing.


CC:0053.02.08.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 418




<!-- PAGE 420 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|Command = SCHEDULE_STATE_GET|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



**Schedule** **ID** **Block** **(8** **bits)**

This field is used to request a particular Schedule ID Block.


CC:0053.02.08.11.004
A node receiving a version 1 Schedule Supported Get Command (without the Schedule ID Block field)
MUST return a response for the default Schedule ID Block (ID = 1).


**2.2.87.10** **Schedule** **State** **Report** **Command**


This command is used to advertise the status of all schedules supported by a device in a given Schedule
ID block.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|Command = SCHEDULE_STATE_REPORT|
|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Override|
|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 1|Active_ID 1|Active_ID 1|Active_ID 1|
|…|…|…|…|…|…|…|…|
|Active_ID N|Active_ID N|Active_ID N|Active_ID N|Active_ID N-1|Active_ID N-1|Active_ID N-1|Active_ID N-1|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



Fields not described below remain unchanged from version 1.


**Number** **of** **Supported** **Schedule** **ID** **(8** **bits)**

CC:0053.02.09.11.001 This field is used to advertise the number of supported regular schedule IDs for the actual Schedule
ID Block. This field’s value MUST be the same as the value advertised in the Schedule Supported
Report Command.


**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the Schedule ID Block in which all schedule states are advertised.

CC:0053.02.09.11.002 If several Reports are returned (using the Reports to Follow field), this field MUST be present in
every Report.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 419

---

<!-- PAGE 421 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.88** **Schedule** **Command** **Class,** **version** **3**


The Schedule Command Class, version 3 allows scheduling the execution of commands for a given
duration in a supporting node. It is a generic command class that may be used to schedule commands
of any other Command Class.


**2.2.88.1** **Terminology**


The Schedule Command Class version 3 introduces new terminology, complementing the terminology
introduced in The Schedule Command Class version 1:


Regular schedules may be triggered repeatedly by two mechanisms.

From version 1, a **Repeating Schedule** can be created by setting parts of the start time to unspecified
values, e.g. if month is unspecified, the schedule can start the first day of each month.


From version 3, **Recurrence** settings may specify additional periodical triggers, e.g. every second
day measured from the most recent trigger of the regular schedule.


**2.2.88.2** **Compatibility** **Considerations**


The Schedule Command Class, version 3 is backwards compatible with version 2.


CC:0053.03.00.21.001 A node supporting the Schedule Command Class, version 3 MUST also support version 2.


The Schedule Command Class version 3 introduces the “Recurring Mode” start mode and “Time from
now” start time option.


The “Time from now” start time option allows to set a schedule to start a after a given time from the
reception of the command.

The “Recurring Mode” start mode allows to set a schedule to restart repeatedly at fixed intervals
since the last activation, e.g. every second day or every 6 months since the last activation.


The Active_ID advertised in the Schedule Report Command of versions 1 and 2 is now overloaded
with the Recurrence Offset field. A new AID_RO_CTL flag in the Schedule Get Command controls
which value is actually returned.

All commands or fields not described in this version remain unchanged from version 2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 420




<!-- PAGE 422 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.88.3** **Schedule** **Supported** **Report** **Command**


This command is used to advertise the scheduling functionalities supported by a node.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|
|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|
|Support<br>Enable/Disable|Fallback<br>Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|
|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|
|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command 1|Supported<br>Command 1|
|…|…|…|…|…|…|…|…|
|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command N|Supported<br>Command N|
|Override<br>Support|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|


Fields not described below remain unchanged from version 2.


**Start** **Time** **Support** **(6** **bits)**

This field is used to advertise the start time options supported by the sending node.


CC:0053.03.02.11.001 Regular schedules MUST support the advertised start time options.


CC:0053.03.02.12.001 The Override Schedule SHOULD support the advertised start time options.


CC:0053.03.02.11.002 The Override Schedule MUST NOT support the Recurring Mode.

CC:0053.03.02.11.003 This field MUST be treated as a bitmask and MUST be encoded according to Table 2.495.

|Category|Bit|Table 2.495: Start Time Support Indicates support for|Version|
|---|---|---|---|
|Category|Bit|Indicates support for|Version|
|Start Time option|0|Start now. Refer to Section 2.2.86.5.|1|
|Start Time option|1|Start Hour and Minute. Refer to Section 2.2.86.6.|1|
|Start Time option|2|Calendar time. Refer to Section 2.2.86.7.|1|
|Start Time option|3|Weekdays. Refer to Section 2.2.86.8.|1|
|Start Time option|4|Time from now. Refer to Section 2.2.88.3.1.|3|
|Start Time mode|5|Recurring Mode. Refer to Section 2.2.88.3.2.|3|



Each bit indicates the support for a given Start Time option or mode.


CC:0053.03.02.11.004 The value 1 MUST indicate that the node supports the corresponding start time option/mode.


CC:0053.03.02.11.005 The value 0 MUST indicate that the node does not support the corresponding start time option/mode.

While support is advertised as a bitmap, the actual functionality is triggered by different combinations of Schedule Set start time fields. The following subsections outline the mandatory supported
combinations when advertising support for the corresponding option.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 421




<!-- PAGE 423 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.88.3.1** **Start** **Time** **Option:** **Start** **from** **now**


The start now option is used to make a configured schedule start after the indicated time has elapsed
from the reception of the Schedule Set Command.

CC:0053.03.02.11.006 The _Start_ _from_ _now_ option MUST cause a schedule to be activated at the specified relative time
measured from the reception of the _Schedule_ _Set_ Command and run for the specified duration.


CC:0053.03.02.11.007 A node supporting the _Time_ _from_ _now_ option MUST support the creation of a schedule with the
following start time fields’ combination:


Relative = ‘1’ and


YYMMDD = 0xFF, 0x00, **Days**, Weekdays = 0x00, HH:MM = **Hours:Minutes**


CC:0053.03.02.11.008 A receiving node MUST ignore all combinations which do not comply with the one above if the
Relative flag is set.


CC:0053.03.02.11.009 A node supporting this option is NOT REQUIRED to support the Start hour and Minute option or
Calendar time option even though it MUST be able to read the start day, start hour and start minutes
fields when using this option.


**2.2.88.3.2** **Start** **Time** **Mode:** **Recurring** **Mode**


This mode is used to trigger a schedule repeatedly at fixed intervals. When using this mode, a
schedule will start at the specified start time and will restart after a given time has elapsed since the
last activation.

The recurring mode is configured with the Recurrence Offset and Recurrence Mode fields of the
Schedule Set Command.


CC:0053.03.02.11.00A A node supporting the Recurring Mode MUST support at least one start time option.


**2.2.88.4** **Schedule** **Set** **Command**


This command is used to create a new schedule or modify an existing schedule


CC:0053.03.03.11.001 This command MUST enable the schedule if a new schedule is created.


CC:0053.03.03.11.002 This command MUST NOT change the enabled/disabled state of existing schedules.


CC:0053.03.03.11.003 If the receiving node supports S0 or S2 Command Class, it MUST NOT process the schedule creation
if any of the scheduled command classes is not supported at the security level of the received Schedule
Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 422




<!-- PAGE 424 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|Command = COMMAND_SCHEDULE_SET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|
|Recurrence Ofset|Recurrence Ofset|Recurrence Ofset|Recurrence Ofset|Start Month|Start Month|Start Month|Start Month|
|Reserved|Recurrence Mode|Recurrence Mode|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Relative|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|
|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



Fields not described below remain unchanged from version 2.


**Reserved**

CC:0053.03.03.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.88.4.1** **Recurrence** **fields**


The recurrence settings of a schedule are set by the following fields:


      - **Recurrence** **Mode**

      - **Recurrence** **Offset**

CC:0053.03.03.11.005 These fields MUST be ignored by a node advertising no support for the Recurring Mode start time
mode in the Schedule Supported Report Command.


**Recurrence** **mode** **(2** **bits)**

This field is used to specify the unit of the Recurrence Offset field.

This field MUST comply with Table 2.496.

|Value|Table 2.496: Recurrence Mode encoding Description|Version|
|---|---|---|
|Value|Description<br>|Version|
|0x00|The recurrence Ofset is expressed in Hours.<br>|3|
|0x01|The recurrence Ofset is expressed in Days.<br>|3|
|0x02|The recurrence Ofset is expressed in Weekd|3|



CC:0053.03.03.11.007 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

CC:0053.03.03.11.008 This field MUST be ignored if the Recurrence Offset field is set to 0.

**Recurrence** **Offset** **(4** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 423




<!-- PAGE 425 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to specify the interval at which the recurring schedule will be triggered.

CC:0053.03.03.11.009 This field MUST be encoded according to Table 2.497 and MUST be interpreted together with the
Recurrence Mode field.


|Offset|Table 2.497: Recurrence Offset encoding Description|
|---|---|
|Ofset|Description|
|0|Recurrence Disabled|
|1..15|Repeat every 1..15 hour, day or week.<br>The unit (hour, day, or week) is indicated by the Recurrence Mode feld.|



CC:0053.03.03.11.00A


CC:0053.03.03.11.00B


CC:0053.03.03.11.00C



When a schedule starts due to its start time options, it MUST restart the current recurrence timer.
It means that a schedule MUST start every time the start time condition is met and the recurrence
offset MUST trigger the schedule to restart based on the last time it started.



CC:0053.03.03.11.00D For example, a schedule set to start on the 1st of each month with a 2 day recurrence offset MUST
start on the 1 [st], 3 [rd], 5 [th], …, 27 [th], 29 [th], 31 [st] and will start again the next month on the 1 [st], 3 [rd], etc.


CC:0053.03.03.11.00E A receiving node MUST accept a schedule set to start in the past if recurrence is enabled. In this case,
the recurrence MUST trigger the schedule to restart based on the time it should have been started
last.


**2.2.88.4.2** **Start** **time** **fields**


The Schedule start time is defined by the following fields:


      - Start Year


      - Start Month


      - Start Day of Month


      - Start Weekday


      - Start Hour


      - Start Minute


      - Relative

CC:0053.03.03.11.00F A receiving node MUST support the start time fields combinations indicated in sections Section
2.2.86.5, Section 2.2.86.6, Section 2.2.86.7, Section 2.2.86.8 and Section 2.2.88.3.1 if the corresponding
start time option is supported.

CC:0053.03.03.11.010 If none of the start time fields are specified, the schedule MUST start immediately if the start now

CC:0053.03.03.11.011 option is supported. In this case, the schedule MUST NOT be activated again at a later time unless
receiving another Schedule Set Command.


**Relative** **(1** **bit)**

This field is used to indicate if the schedule start time is using the start from now start option.



CC:0053.03.03.11.012


CC:0053.03.03.11.013


CC:0053.03.03.11.014



The value 1 MUST indicate that the start time fields MUST be interpreted as the time left before
the schedule starts. In this case, the start time fields MUST be set and interpreted as indicated in
Section 2.2.88.3.1 and the schedule MUST NOT be activated again at a later time unless receiving
another Schedule Set Command.



CC:0053.03.03.11.015 The value 0 MUST indicate that the start time fields MUST be interpreted as an absolute start time
for the schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 424




<!-- PAGE 426 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.88.5** **Schedule** **Get** **Command**


This command is used to request the configuration for a specific schedule ID.


CC:0053.03.04.11.001 The Schedule Report Command MUST be returned in response to this command.


CC:0053.03.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0053.03.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|Command = COMMAND_SCHEDULE_GET|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|AID_RO_CTL|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



Fields not described below remain unchanged from version 2.

**Active_ID** **/** **Recurrence** **Offset** **control** **(AID_RO_CTL)** **(1** **bit)**

This field is used to request either the Active_ID or the Recurrence Offset value in the Schedule
Report Command which is returned in response to this command.


CC:0053.03.04.11.004 A receiving node MUST return a Schedule Report Command advertising the Active_ID of the Schedule if this field is set to 0.


CC:0053.03.04.11.005
A receiving node MUST return a Schedule Report Command advertising the Recurrence Offset of the
schedule if this field is set to 1.


**2.2.88.6** **Schedule** **Report** **Command**


The Schedule Report Command is used to advertise the configuration for a specific schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 425




<!-- PAGE 427 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024







|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|Command = COMMAND_SCHEDULE_REPORT|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Start Month|Start Month|Start Month|Start Month|
|AID_RO_CTL|AID_RO_CTL|AID_RO_CTL|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|
|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|
|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|Report to Follow|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|


Fields not described below remain unchanged from version 2.

**Active_ID/Recurrence** **Offset** **(AID_RO)** **(4** **bits)**

This field is used to advertise the Active_ID or the Recurrence Offset of the advertised schedule.

CC:0053.03.05.11.001 If this field carries the Active_ID value, this field MUST be encoded according to Table 2.494.

CC:0053.03.05.11.002 If this field carries the Recurrence Offset, this field MUST be encoded according to Table 2.497 and
MUST be interpreted together with the Recurrence Mode field.

**Active_ID** **/** **Recurrence** **Offset** **control** **(AID_RO_CTL)** **(1** **bit)**

This field is used to indicate whether the Active_ID or the Recurrence Offset value is advertised in
the command.

CC:0053.03.05.11.003 The value 0 MUST indicate that the Active_ID/Recurrence Offset (AID_RO) field carried the Active_ID value.

CC:0053.03.05.11.004 The value 1 MUST indicate that the Active_ID/Recurrence Offset (AID_RO) field carried the Recurrence Offset value.


**Recurrence** **mode** **(2** **bits)**

This field is used to specify the Recurrence Offset unit.

CC:0053.03.05.11.005 This field MUST be ignored if the AID_RO_CTL field is set to 0.

CC:0053.03.05.11.006 This field MUST comply with Table 2.496 if the AID_RO_CTL field is set to 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 426

---

<!-- PAGE 428 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.89** **Schedule** **Command** **Class,** **version** **4**


The Schedule Command Class, version 4 allows supporting nodes to advertise the list of commands
they support for scheduling.


**2.2.89.1** **Compatibility** **Considerations**


The Schedule Command Class version 4 introduces the possibility to advertise the list of command
supported for scheduling and explicitly allows scheduling extended command classes. The following
commands are introduced:


      - Schedule Supported Commands Get Command


      - Schedule Supported Commands Report Command


The following functionalities become obsoleted:

      - Redundant values in the Active_ID field encoding

      - The Report to Follow field.


A supporting node no longer needs to be able to parse and handle several commands in order to set or
report schedules or schedules states. Supporting nodes MUST use the Transport Service Command
Class, version 2 in order to transmit long Z-Wave payloads.


CC:0053.04.00.21.001 A node supporting the Schedule Command Class, version 4 MUST also support version 3. Commands
and fields not mentioned in this version MUST remain unchanged from version 3.


**2.2.89.2** **Schedule** **Supported** **Report** **Command**


This command is used to advertise the scheduling properties of a device.









|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|Command = SCHEDULE_SUPPORTED_REPORT|
|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|Number of Supported Schedule IDs|
|Support<br>Enable/Disable|Fallback<br>Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|Start Time Support|
|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|Number of Supported CC|
|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|Supported CC 1|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command 1|Supported<br>Command 1|
|…|…|…|…|…|…|…|…|
|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|Supported CC N|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Supported<br>Command N|Supported<br>Command N|
|Override<br>Support|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|Supported Override Types|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|Number of Supported Schedule Blocks|


All fields not described below remain unchanged from version 3.


**Supported** **Command** **(N** ***** **2** **bits)**

CC:0053.04.02.11.001 This field MUST advertise the supported commands for the command class entry. This field MUST
comply with Table 2.498.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 427




<!-- PAGE 429 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Value|Table 2.498: Schedule Supported Report version 4::Supported Command Description|Version|
|---|---|---|
|Value|Description|Version|
|0x00|All Commands within the Command Class are supported.|1|
|0x01|Only Set Commands are supported.|1|
|0x02|Only Get Commands are supported.|1|
|0x03|Custom list of commands are supported.|4|



CC:0053.04.02.11.002 Certain command classes commands do not contain the string “Set” or “Get” in their name. Nodes
MUST consider all commands mandating to return a response to be of type “Get” and all other
commands to be of type “Set”.

CC:0053.04.02.11.003 The length of this field in bytes MUST be according to the Number of supported CC field value.


CC:0053.04.02.11.004 A supporting node MUST NOT advertise the 0x03 value if the list of supported command can be
advertised with the other values.


CC:0053.04.02.52.001 If a sending node advertises 0x03 for a given Schedule ID Block and Command Class, a controlling node
SHOULD retrieve the exact list of supported commands using the Schedule Supported Commands
Get Command.


**2.2.89.3** **Schedule** **Supported** **Commands** **Get** **Command**


This command is used to query the list of commands that can be scheduled within for a given command
class and Schedule ID Block.


CC:0053.04.0A.11.001 The Schedule Supported Commands Report Command MUST be returned in response to this command.


CC:0053.04.0A.51.001 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressCC:0053.04.0A.11.002 ing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|Command = SCHEDULE_SUPPORTED_COMMANDS_GET (0x0A)|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



**Schedule** **ID** **Block** **(8** **bits)**

This field is used to request a particular Schedule ID Block.

If a non-supported Schedule ID Block is specified, a receiving node SHOULD return a response for
CC:0053.04.0A.12.001 the Schedule ID block 1.


**2.2.89.4** **Schedule** **Supported** **Commands** **Report** **Command**


This command is used to advertise the list of commands that can be scheduled within a given Schedule
ID Block


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 428




<!-- PAGE 430 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|Command = SCHEDULE_SUPPORTED_COMMANDS_REPORT (0x08)|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Command Class List Length|Command Class List Length|Command Class List Length|Command Class List Length|Command Class List Length|Command Class List Length|Command Class List Length|Command Class List Length|
|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|
|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|Supported Command List Length 1|
|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|Supported Command 1 - 1|
|…|…|…|…|…|…|…|…|
|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|Supported Command 1 - K|
|…|…|…|…|…|…|…|…|
|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|Command Class N (1 or 2 bytes)|
|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|Supported Command List Length N|
|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|Supported Command N - 1|
|…|…|…|…|…|…|…|…|
|Supported Command N - K|Supported Command N - K|Supported Command N - K|Supported Command N - K|Supported Command N - K|Supported Command N - K|Supported Command N - K|Supported Command N - K|



**Schedule** **ID** **Block** **(8** **bits)**

This field is used to specify the requested Schedule ID Block.


**Command** **Class** **List** **Length** **(8** **bit)**

This field is used to advertise the number of command classes contained in the command.


CC:0053.04.0B.11.001
This field MUST be set to the number of Command Class entries present in this command (represented
by N in the command structure).


**Command** **Class** **(8** **or** **16** **bits)**

CC:0053.04.0B.13.001 This field is used to indicate the command class to which the advertised commands belong. This field
MAY carry extended Command Classes


**Supported** **Command** **List** **Length** **(8** **bits)**

This field is used to advertise how many commands are advertised in the current Command Class’
list.

CC:0053.04.0B.11.002 This field MUST be set to the number of Supported Commands present in the current Command
Class entry (represented by K in the command structure).


**Supported** **Command** **(K** **bytes)**

This field is used to advertise the list of commands for the given Command Class entry that can be
scheduled for the actual Schedule ID Block.

CC:0053.04.0B.11.003 The length of this field in bytes MUST be according to the corresponding Supported Command List
Length field value.


**2.2.89.5** **Schedule** **Set** **Command**


This command is used to create a new schedule or modify an existing schedule.


CC:0053.04.03.11.001 This command MUST enable the schedule if a new schedule is created.


CC:0053.04.03.11.002 This command MUST NOT change the enabled/disabled state of existing schedules


CC:0053.04.03.11.003 If the receiving node supports S0 or S2 Command Class, it MUST NOT process the schedule creation
if any of the scheduled command classes is not supported at the security level of the received Schedule
Set Command.


CC:0053.04.03.11.004 A controlling node using previous versions may try to schedule unsupported commands. In this case,
a receiving node MUST ignore the Schedule Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 429




<!-- PAGE 431 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|Command = SCHEDULE_SET (0x03)|
|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|Schedule ID|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|Start Year<br>|
|Recurrence Ofset|Recurrence Ofset|Recurrence Ofset|Recurrence Ofset|Start Month|Start Month|Start Month|Start Month|
|Reserved|Recurrence Mode|Recurrence Mode|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Relative|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|Duration Byte 1 MSB|
|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|Duration Byte 2 LSB|
|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|



Fields not described below remain unchanged from version 3.


**Reports** **to** **Follow** **(8** **bits)** **[OBSOLETED]**

CC:0053.04.03.11.005 This field has been OBSOLETED: a sending node MUST use the Transport Service Command Class
in order to set a schedule containing commands payload too large to fit in the Z-Wave MAC frame
size.

CC:0053.04.03.11.006 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.89.6** **Schedule** **Report** **Command**


The Schedule Report Command is used to advertise the configuration for a specific schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 430




<!-- PAGE 432 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024







|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|Command = SCHEDULE_REPORT (0x05)|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Active_ID /<br>Recurrence Ofset<br>(AID_RO)|Start Month|Start Month|Start Month|Start Month|
|AID_RO_CTL|AID_RO_CTL|AID_RO_CTL|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|Start Day of Month|
|Reserved|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|Start Weekday|
|Duration Type|Duration Type|Duration Type|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Reserved|Reserved|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|Duration Byte 1|
|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|Duration Byte 2|
|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|Report to Follow [OBSOLETED]|
|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|Number of Cmd to Follow|
|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|Cmd Length 1|
|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|Cmd Byte 1 - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|Cmd Byte 1 - N|
|…|…|…|…|…|…|…|…|
|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|Cmd Length P|
|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|Cmd Byte P - 1|
|…|…|…|…|…|…|…|…|
|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|Cmd Byte P - N|


Fields not described below remain unchanged from version 3.

**Active_ID/Recurrence** **Offset** **(4** **bits)**

This field is used to advertise the Active_ID or the Recurrence Offset of the advertised schedule.

CC:0053.04.05.11.001 If this field carries the Active_ID value, this field MUST be encoded according to Table 2.499.

CC:0053.04.05.11.002 If this field carries the Recurrence Offset, this field MUST be encoded according to Table 2.497 and
MUST be interpreted together with the Recurrence Mode field.


**Reports** **to** **Follow** **(8** **bits)** **[OBSOLETED]**

CC:0053.04.05.11.003 This field has been OBSOLETED: a sending node MUST use the Transport Service Command Class
in order to report a schedule containing commands payload too large to fit in the Z-Wave MAC frame
size.

CC:0053.04.05.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.89.7** **Schedule** **State** **Report** **Command**


This command is used to advertise the status of all schedules supported by the specified schedule
block.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|Command Class = COMMAND_CLASS_SCHEDULE|
|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|Command = SCHEDULE_STATE_REPORT (0x09)|
|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|Number of Supported Schedule ID|
|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Reports to Follow [OBSOLETED]|Override|
|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 2|Active_ID 1|Active_ID 1|Active_ID 1|Active_ID 1|
|…|…|…|…|…|…|…|…|
|Active_ID N|Active_ID N|Active_ID N|Active_ID N|Active_ID N-1|Active_ID N-1|Active_ID N-1|Active_ID N-1|
|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|Schedule ID Block|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 431




<!-- PAGE 433 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Fields not described below remain unchanged from version 3.


**Reports** **to** **Follow** **(7** **bits)** **[OBSOLETED]**

CC:0053.04.09.11.001 This field has been OBSOLETED: a sending node MUST use the Transport Service Command Class
in order to advertise an Active_ID field too large to fit in the Z-Wave MAC frame size.

CC:0053.04.09.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Active_ID** **(N** ***** **4** **bits)**

CC:0053.04.09.11.003 The _Active_ID_ field MUST be used to advertise the status for each supported schedule ID. Four bits
are used for each Schedule ID to indicate the status. This means that :


      - Bits 0 to 3 in Active_ID byte 1 represent Schedule ID = 1,.


      - Bits 4 to 7 in Active_ID byte 1 represent Schedule ID = 2


      - Bits 0 to 3 in Active_ID byte 2 represent Schedule ID = 3


      - …

CC:0053.04.09.11.004 The size of this field MUST be the smallest number of bytes needed to advertise the number of
supported Schedule IDs advertised in this command.


CC:0053.04.09.11.005 Each 4 bits unit MUST be encoded according to Table 2.499.


Table 2.499: Active_ID encoding, version 4







CC:0053.04.09.11.006







CC:0053.04.09.11.008









CC:0053.04.09.11.009


|Hex|Description|Detailed description|Version|
|---|---|---|---|
|0x00|Not used|The Schedule ID is not used (not set/confgured)<br>or unsupported|1|
|0x01|[OBSOLETED]<br>Override + Not used|[OBSOLETED]<br>A sending node MUST NOT use this status and<br>MUST use 0x00 instead (and the override feld<br>set to 1 for the Schedule State Report Com-<br>mand).|4|
|0x02|Not Active|The Schedule ID is used, enabled and currently<br>not active.|1|
|0x03|Active|The Schedule ID is used, enabled and currently<br>active.|1|
|0x05|Override + Active|The Schedule ID is used, enabled and should<br>currently be active but it is suspended by the<br>Override Schedule<br>The override feld MUST be set to 1 when using<br>this status in the Schedule State Report Com-<br>mand|1|
|0x06|[OBSOLETED]<br>Override + Not Active|[OBSOLETED]<br>A sending node MUST NOT use this status and<br>MUST use 0x02 instead. (and the override feld<br>set to 1 for the Schedule State Report Com-<br>mand).|4|
|0x07|[OBSOLETED]<br>Override + Disabled|[OBSOLETED]<br>A sending node MUST NOT use this status and<br>MUST use 0x04 instead. (and the override feld<br>set to 1 for the Schedule State Report Com-<br>mand).|4|



CC:0053.04.09.11.00A All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 432