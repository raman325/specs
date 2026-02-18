<!-- PAGE 434 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.90** **Schedule** **Entry** **Lock** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Schedule Command Class.


If implementing this command class, it is RECOMMENDED that the Schedule Command Class
is also implemented.


The Schedule Entry Lock Command Class provides Z-Wave devices the capability to exchange scheduling information. The Schedule Entry Lock Type Commands are for controlling the schedules of an
Entry Lock using schedule based user code Ids. The Entry Lock supports two types of schedules for
each user ID supported in the device. The two schedule types are a time-fenced weekly schedule and
a time-fenced one-time range schedule. When these schedules are configured and enabled, it allows
the specified user ID’s code to be active during the time intervals configured in the scheduling slots.


The Week Day schedule is a day-to-day schedule that will repeat weekly for the enabled user ID. A
single schedule slot cannot span days.


Example: A homeowner has a Secure Keypad Door Lock and a dog that needs walking three times
a week. The dog walker can be given access to the house using this schedule. The homeowner would
give the dog walker a keypad code that would be active M, W, F from 1pm - 2pm.

The Year Day schedule is an extended schedule that allows two points in time to be specified that is
beyond a daily schedule. A particular slot can span weeks, months or years. Once the end point is
reached that schedule slot is no longer valid because it is out of range.


Example: A homeowner is going away on vacation for two weeks. The homeowner could give the
neighbor a keypad code to the neighbor that would be active from April 2 [nd], 2008 to April 16 [th‘] 2008.
The code would be invalid after April 16th 2008.


**2.2.90.1** **Schedule** **Entry** **Lock** **Enable** **Set** **Command**


This command enables or disables schedules for a specified user code ID. It affects only the schedules
associated with the specific user ID.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|Command = SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x01)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|



**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored.


**Enabled** **(8** **bits)**


Table 2.500: Schedule Entry Lock Enable Set::Enabled encoding

|Value|Description|
|---|---|
|0x00|Schedule for the user identifed is disabled.<br>|
|0x01|Schedule for the user identifed is enabled.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 433




<!-- PAGE 435 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.90.2** **Schedule** **Entry** **Lock** **Enable** **All** **Set** **Command**


This command enables or disables all schedules for type Entry Lock.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|Command = SCHEDULE_ENTRY_LOCK_ENABLE_ALL_SET (0x02)|
|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|Enabled|



**Enabled** **(8** **bits)**


See description in Schedule Entry Lock Enable Set Command.


**2.2.90.3** **Schedule** **Entry** **Lock** **Supported** **Get** **Command**


This command is used to request the number of schedule slots each type of schedule the device supports
for every user.


The Schedule Entry Lock Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_GET (0x09)|



**2.2.90.4** **Schedule** **Entry** **Lock** **Supported** **Report** **Command**


This command is used to report the number of supported schedule slots an Entry Lock schedule device
supports for each user in the system. It lists how many schedule slots there are for Week Days type
and how many slots for the Year Day type.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|
|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|
|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|Number of slots Year Day|



**Number** **of** **Slots** **Week** **Day** **(8** **bits)**

A number from 0 - 255 that represents how many different schedule slots are supported each week for
every user in the system for type Week Day.


**Number** **of** **Slots** **Year** **Day** **(8** **bits)**

A number from 0 - 255 that represents how many different schedule slots are supported for every user
in the system for type Year Day.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 434




<!-- PAGE 436 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.90.5** **Schedule** **Entry** **Lock** **Week** **Day** **Schedule** **Set** **Command**


This command set or erase a weekday schedule for a identified user who already has valid user access
code.

When setting, the week day schedule is automatically enabled and the identified user if it is not
already. The start parameters of the time fence needs to occur prior to the stop parameters. When
erasing the schedule slot ID, the user code ID will continue to use week day type scheduling.


**Note:** Each user can only use one type of scheduling at a time.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_SET (0x03)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



**Set** **Action** **(8** **bits)**


Table 2.501: Schedule Entry Lock Week Day Schedule Set::Set
Action encoding

|Set Action|Description|
|---|---|
|0|Erase the schedule slot.<br>|
|1|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored.


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Week_ _Day_ _Supported_ .


**Day** **of** **Week** **(8** **bits)**


A value from 0 to 6 where 0 is Sunday.


**Start** **Hour** **(8** **bits)**


A value from 0 to 23 representing the starting hour of the time fence.


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Stop** **Hour** **(8** **bits)**


A value from 0 to 23 representing the stop hour of the time fence.


**Stop** **Minute** **(8** **bits)**


A value from 0 to 59 representing the stop minute of the time fence


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 435




<!-- PAGE 437 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.90.6** **Schedule** **Entry** **Lock** **Week** **Days** **Schedule** **Get** **Command**


This command gets a week day schedule slot for a identified user and specified schedule slot ID.


The Schedule Entry Lock Week Days Schedule Report Command MUST be returned in response to
this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_GET (0x04)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|



**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored.


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Week_ _Day_ _Supported_ .


**2.2.90.7** **Schedule** **Entry** **Lock** **Week** **Day** **Schedule** **Report** **Command**


This command returns week day schedule report for the requested schedule slot ID for identified user.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|Command = SCHEDULE_ENTRY_LOCK_WEEK_DAY_REPORT (0x05)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



Refer to the description under the Schedule Set Week Day Schedule.


**Note:** If a requested schedule slot is erased/empty, the time fields SHOULD be set to 0xFF.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 436




<!-- PAGE 438 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.90.8** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Set** **Command**


This command sets or erases a schedule slot for a identified user who already has valid user access
code. The year day schedule represents two days, any time apart, where the specified user ID’s code
is valid. When setting the schedule slot, the start parameters of the time fence needs to occur prior to
the stop parameters and the year day schedule is automatically enabled for the identified user. When
erasing, the user code does not change from year day scheduling.


**Note:** Each user can only use one type of scheduling at a time.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_SET (0x06)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



Set Action (8 bits)


Table 2.502: Schedule Entry Lock Year Day Schedule Set::Set Action Encoding

|Value|Description|
|---|---|
|0x00|Erase the schedule slot.<br>|
|0x01|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Year_ _Day_ _Supported_ .


**Start** **Year** **(8** **bits)**


A value from 0 to 99 that represents the 2 year in the century.


**Start** **Month** **(8** **bits)**


A value from 1 to 12 that represents the month in a year.


**Start** **Day** **(8** **bits)**


A value from 1 to 31 that represents the date of the month.


**Start** **Hour** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 437




<!-- PAGE 439 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A value from 0 to 23 representing the starting hour of the time fence.


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Stop** **Year** **(8** **bits)**


A value from 0 to 99 that represents the 2 year in the century.


**Stop** **Month** **(8** **bits)**


A value from 1 to 12 that represents the month in a year.


**Stop** **Day** **(8** **bits)**


A value from 1 to 31 that represents the date of the month.


**Stop** **Hour** **(8** **bits)**


A value from 0 to 23 representing the stop hour of the time fence.


**Stop** **Minute** **(8** **bits)**


A value from 0 to 59 representing the stop minute of the time fence


**2.2.90.9** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Get** **Command**


This command gets a year/day schedule slot for an identified user and specified schedule slot ID.


The Schedule Entry Lock Year Day Schedule Report Command MUST be returned in response to
this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_GET (0x07)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|



**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Year_ _Day_ _Supported_ .


**2.2.90.10** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Report** **Command**


This command returns year/day schedule report for the requested schedule slot ID for the identified

user.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 438




<!-- PAGE 440 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|Command = SCHEDULE_ENTRY_LOCK_YEAR_DAY_REPORT (0x08)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



Refer to the description under Schedule Set Year Day Schedule command.


**Note:** If a requested schedule slot is erased/empty the time fields SHOULD be set to 0xFF.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 439

---

<!-- PAGE 441 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.91** **Schedule** **Entry** **Lock** **Command** **Class,** **version** **2** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the Schedule Command Class.


If implementing this command class, it is RECOMMENDED that the Schedule Command Class
is also implemented.


The Schedule Entry Lock Command Class provides Z-Wave devices the capability to exchange scheduling information. The Schedule Entry Lock Type Commands are for controlling the schedules of an
Entry Lock using schedule based user code Ids. The Entry Lock supports two types of schedules for
each user ID supported in the device. The two schedule types are a time-fenced weekly schedule and
a time-fenced one-time range schedule. When these schedules are configured and enabled, it allows
the specified user ID’s code to be active during the time intervals configured in the scheduling slots.

In Version 2 local time is used instead of UTC time, and Time Offset commands are added.


The commands not mentioned here remain the same as in version 1.


**2.2.91.1** **Schedule** **Entry** **Lock** **Time** **Offset** **Get** **Command**


This command is used to request time zone offset and daylight savings parameters.

The Schedule Entry Lock Time Offset Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0B)|



**2.2.91.2** **Schedule** **Entry** **Lock** **Time** **Offset** **Set** **Command**


This command is used to set the current local TZO and DST offsets into an Entry Lock Device. Any
schedules that are already in the device before or after issuing the Schedule Entry Time Offset Set
command are now assumed to be programmed in the Local time set by this command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|
|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_GET (0x0D)|
|Sign TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|
|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|
|Sign Ofset<br>TZO|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|



**Sign** **TZO** **(1** **bit)**

Plus (0) or minus (1) sign to indicate a positive or negative offset from UTC.


**Hour** **TZO** **(7** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 440




<!-- PAGE 442 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Specify the number of hours that the originating time zone deviates from UTC. Refer to the DST
field regarding daylight savings handling.


**Minute** **TZO** **(7** **bits)**

Specify the number of minutes that the originating time zone deviates UTC. Refer to the DST field
regarding daylight savings handling.

**Sign** **Offset** **DST** **(1** **bit)**

Plus (0) or minus (1) sign to indicate a positive or negative offset from UTC.

**Minute** **Offset** **DST** **(7** **bits)**

This field MUST specify the number of minutes the time is to be adjusted when daylight savings mode
is enabled.


**2.2.91.3** **Schedule** **Entry** **Lock** **Time** **Offset** **Report** **Command**


This command is used to advertise the time zone offset and daylight savings parameters.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK|
|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|Command = SCHEDULE_ENTRY_LOCK_TIME_OFFSET_REPORT (0x0C)|
|Sign TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|
|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|
|Sign Ofset<br>TZO|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|



Refer to description under the Schedule Entry Lock Time Offset Set command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 441

---

<!-- PAGE 443 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.92** **Schedule** **Entry** **Lock** **Command** **Class,** **version** **3**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this command class, but it is RECOMMENDED that new implementations use the _Schedule_ _Entry_ _Lock_ _Command_ _Class,_ _version_ _4_ _[NEVER_ _CERTIFIED]_ .


The Schedule Entry Lock Command Class provides a scheduling type alongside the existing types
Week Day and Year Day. The new type is similar to Week Day functionality but provides a simpler implementation to repeat a time slot daily (selected days) and repeat those days weekly. The
commands not mentioned here remain the same as in Version 2.


**2.2.92.1** **Schedule** **Entry** **Type** **Supported** **Report** **Command**


This command is used to report the number of supported schedule slots an Entry Lock schedule device
supports for each user in the system. It lists how many schedule slots there are for Week Day, Year
Day, and Daily Repeating types.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|Command = SCHEDULE_ENTRY_TYPE_SUPPORTED_REPORT (0x0A)|
|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|Number of Slots Week Day|
|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|Number of Slots Year Day|
|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|Number of Slots Daily Repeating|



**Number** **of** **Slots** **Week** **Day** **(8** **bits)**

A number from 0 to 255 that represents how many different schedule slots are supported each week
for every user in the system for type Week Day.


**Number** **of** **Slots** **Year** **Day** **(8** **bits)**

A number from 0 to 255 that represents how many different schedule slots are supported for every
user in the system for type Year Day.


**Number** **of** **Slots** **Daily** **Repeating** **(8** **bits)**

A number from 0 to 255 that represents how many different schedule slots are supported for every
user in the system for type Daily Repeating Day.


**2.2.92.2** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Set** **Command**


This command is used to set or erase a daily repeating schedule for an identified user who already has
valid user access code.

When setting; the daily repeating schedule is automatically enabled for the identified user if it is not
already. The start parameters of the time fence needs to occur prior to the stop parameters. When
erasing the schedule slot ID, the user code ID will continue to use daily repeating type scheduling.


**Note:** Each user can only use one type of scheduling at a time.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 442




<!-- PAGE 444 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x10)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|
|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|



**Set** **Action** **(8** **bits)**

|ble 2.503: oding Value|Schedule Entry Lock Daily Repeating Set::Set Act Description|
|---|---|
|Value|Description|
|0x00|Erase the schedule slot.<br>|
|0x01|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to Number of Slots Daily Repeating Supported.


**Week** **Day** **Bitmask** **(8** **bits)**


A bitmask of the days of the week for this schedule entry is active.


Table 2.504: Schedule Entry Lock Daily Repeating Set::Week Day
Bitmask encoding

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Value**|Res|Sat|Fri|Thr|Wed|Tue|Mon|Sun|



The ‘Res’ bit is reserved and MUST be set to zero by a sending node. Reserved bits MUST be ignored
by a receiving node.


**Start** **Hour** **(8** **bits)**


A value from 0 to 23 representing the starting hour of the time fence.


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Duration** **Hour** **(8** **bits)**


A value from 0 to 23 representing how many hours the time fence will last. Duration hour will
be maxed at the documented capability of the specific device since this scheduling type is memory
conscious.


**Duration** **Minute** **(8** **bits)**


A value from 0 to 59 representing how many minutes the time fence will last past the Duration Hour
field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 443




<!-- PAGE 445 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.92.3** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Get** **Command**


This command is used to request a daily repeating schedule slot for a identified user and specified
schedule slot ID.


The Schedule Entry Lock Daily Repeating Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x0E)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|



**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Daily_ _Repeating_ _Supported_ .


**2.2.92.4** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Report** **Command**


This command is used to return the requested schedule slot ID for identified user.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|Command = SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT (0x0F)<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|Schedule Set ID|
|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|
|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|



Refer to the description under the Schedule Set Daily Repeating Schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 444

---

<!-- PAGE 446 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.93** **Schedule** **Entry** **Lock** **Command** **Class,** **version** **4** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class version has never been implemented and certified by a Z-Wave product. Therefore, this Command Class definition MAY be updated in a non-backwards compatible manner, or
even removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


The Schedule Entry Lock Command Class provides a scheduling type alongside the existing types
Week Day and Year Day. The new type is similar to Week Day functionality but provides a simpler implementation to repeat a time slot daily (selected days) and repeat those days weekly. The
commands not mentioned here remain the same as in Version 3.


The following commands are also introduced to address the extended range of credentials:


 - Extended Schedule Entry Lock Enable Set Command


 - Extended Schedule Entry Lock Week Day Schedule Set Command


 - Extended Schedule Entry Lock Week Day Schedule Get Command


 - Extended Schedule Entry Lock Week Day Schedule Report Command


 - Extended Schedule Entry Lock Year Day Schedule Set Command


 - Extended Schedule Entry Lock Year Day Schedule Get Command


 - Extended Schedule Entry Lock Year Day Schedule Report Command


 - Extended Schedule Entry Lock Daily Repeating Set Command


 - Extended Schedule Entry Lock Daily Repeating Get Command


 - Extended Schedule Entry Lock Daily Repeating Report Command


The Schedule Entry Command Class, version 4 is backwards compatible with _Schedule_ _Entry_ _Lock_
_Command_ _Class,_ _version_ _3_ .

The _Extended User Code Set Command_ permits to configure several credentials per user. The following
command has been extended to match the extended number of supported credentials:


 - _Schedule_ _Entry_ _Lock_ _Command_ _Class,_ _version_ _3_ .


**2.2.93.1** **Extended** **Schedule** **Entry** **Lock** **Enable** **Set** **Command**


This command enables or disables schedules for a specified user code ID. It affects only the schedules
associated with the specific user ID.








|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_ENABLE_SET (0x11)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Enabled|



**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command MUST be ignored.


**Enabled** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 445




<!-- PAGE 447 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.505: Schedule Entry Lock Enable Set::Enabled encoding

|Value|Description|
|---|---|
|0|Schedule for the user identifed is disabled.<br>|
|1|Schedule for the user identifed is enabled.|



**2.2.93.2** **Extended** **Schedule** **Entry** **Lock** **Week** **Day** **Schedule** **Set** **Command**


This command set or erase a weekday schedule for a identified user who already has valid user access
code.

When setting, the week day schedule is automatically enabled and the identified user if it is not
already. The start parameters of the time fence needs to occur prior to the stop parameters. When
erasing the schedule slot ID, the user code ID will continue to use week day type scheduling.


**Note:** Each user can only use one type of scheduling at a time.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_SET<br>(0x12)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



**Set** **Action** **(8** **bits)**


Table 2.506: Schedule Entry Lock Week Day Schedule Set::Set
Action encoding

|Set Action|Description|
|---|---|
|0|Erase the schedule slot.<br>|
|1|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored.


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Week_ _Day_ _Supported_ .


**Day** **of** **Week** **(8** **bits)**


A value from 0 to 6 where 0 is Sunday.


**Start** **Hour** **(8** **bits)**


A value from 0 to 23 representing the starting hour of the time fence.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 446




<!-- PAGE 448 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Stop** **Hour** **(8** **bits)**


A value from 0 to 23 representing the stop hour of the time fence.


**Stop** **Minute** **(8** **bits)**


A value from 0 to 59 representing the stop minute of the time fence


**2.2.93.3** **Extended** **Schedule** **Entry** **Lock** **Week** **Day** **Schedule** **Get** **Command**


This command gets a week day schedule slot for a identified user and specified schedule slot ID.


The Extended Schedule Entry Lock Week Days Schedule Report Command MUST be returned in
response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_GET<br>(0x13)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|


**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored.


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Week_ _Day_ _Supported_ .


**2.2.93.4** **Extended** **Schedule** **Entry** **Lock** **Week** **Day** **Schedule** **Report** **Command**


This command returns week day schedule report for the requested schedule slot ID for identified user.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_WEEK_DAY_SCHEDULE_RE-<br>PORT (0x14)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|Day of Week|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|


Refer to the description under the Schedule Set Week Day Schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 447




<!-- PAGE 449 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Note:** If a requested schedule slot is erased/empty, the time fields SHOULD be set to 0xFF.


**2.2.93.5** **Extended** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Set** **Command**


This command sets or erases a schedule slot for a identified user who already has valid user access
code. The year day schedule represents two days, any time apart, where the specified user ID’s code
is valid. When setting the schedule slot, the start parameters of the time fence needs to occur prior to
the stop parameters and the year day schedule is automatically enabled for the identified user. When
erasing, the user code does not change from year day scheduling.


**Note:** Each user can only use one type of scheduling at a time.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_SET<br>(0x15)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|



Set Action (8 bits)


Table 2.507: Schedule Entry Lock Year Day Schedule Set::Set Action Encoding

|Value|Description|
|---|---|
|0x00|Erase the schedule slot.<br>|
|0x01|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Year_ _Day_ _Supported_ .


**Start** **Year** **(8** **bits)**


A value from 0 to 99 that represents the 2 year in the century.


**Start** **Month** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 448




<!-- PAGE 450 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A value from 1 to 12 that represents the month in a year.


**Start** **Day** **(8** **bits)**


A value from 1 to 31 that represents the date of the month.


**Start** **Hour** **(8** **bits)**


A value from 0 to 23 representing the starting hour of the time fence.


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Stop** **Year** **(8** **bits)**


A value from 0 to 99 that represents the 2 year in the century.


**Stop** **Month** **(8** **bits)**


A value from 1 to 12 that represents the month in a year.


**Stop** **Day** **(8** **bits)**


A value from 1 to 31 that represents the date of the month.


**Stop** **Hour** **(8** **bits)**


A value from 0 to 23 representing the stop hour of the time fence.


**Stop** **Minute** **(8** **bits)**


A value from 0 to 59 representing the stop minute of the time fence


**2.2.93.6** **Extended** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Get** **Command**


This command gets a year/day schedule slot for an identified user and specified schedule slot ID.


The Extended Schedule Entry Lock Year Day Schedule Report Command MUST be returned in
response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_GET<br>(0x16)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|


**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Year_ _Day_ _Supported_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 449




<!-- PAGE 451 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.93.7** **Extended** **Schedule** **Entry** **Lock** **Year** **Day** **Schedule** **Report** **Command**


This command returns year/day schedule report for the requested schedule slot ID for the identified

user.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|Command = EXTENDED SCHEDULE_ENTRY_LOCK_YEAR_DAY_SCHEDULE_RE-<br>PORT (0x17)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|Start Year|
|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|Start Month|
|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|Start Day|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|Stop Year|
|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|Stop Month|
|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|Stop Day|
|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|Stop Hour|
|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|Stop Minute|


Refer to the description under Schedule Set Year Day Schedule command.


**Note:** If a requested schedule slot is erased/empty the time fields SHOULD be set to 0xFF.


**2.2.93.8** **Extended** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Set** **Command**


This command is used to set or erase a daily repeating schedule for an identified user who already has
valid user access code.

When setting; the daily repeating schedule is automatically enabled for the identified user if it is not
already. The start parameters of the time fence needs to occur prior to the stop parameters. When
erasing the schedule slot ID, the user code ID will continue to use daily repeating type scheduling.


**Note:** Each user can only use one type of scheduling at a time.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_SET (0x18)|
|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|Set Action<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|
|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|



**Set** **Action** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 450




<!-- PAGE 452 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|ble 2.508: oding Value|Schedule Entry Lock Daily Repeating Set::Set Act Description|
|---|---|
|Value|Description|
|0x00|Erase the schedule slot.<br>|
|0x01|Modify the schedule slot for the identifed user.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to Number of Slots Daily Repeating Supported.


**Week** **Day** **Bitmask** **(8** **bits)**


A bitmask of the days of the week for this schedule entry is active.


Table 2.509: Schedule Entry Lock Daily Repeating Set::Week Day
Bitmask encoding

|Bit|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|---|
|**Value**|Res|Sat|Fri|Thr|Wed|Tue|Mon|Sun|



The ‘Res’ bit is reserved and MUST be set to zero by a sending node. Reserved bits MUST be ignored
by a receiving node.


**Start** **Hour** **(8** **bits)**


A value from 0 to 23 representing the starting hour of the time fence.


**Start** **Minute** **(8** **bits)**


A value from 0 to 59 representing the starting minute of the time fence.


**Duration** **Hour** **(8** **bits)**


A value from 0 to 23 representing how many hours the time fence will last. Duration hour will
be maxed at the documented capability of the specific device since this scheduling type is memory
conscious.


**Duration** **Minute** **(8** **bits)**


A value from 0 to 59 representing how many minutes the time fence will last past the Duration Hour
field.


**2.2.93.9** **Extended** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Get** **Command**


This command is used to request a daily repeating schedule slot for a identified user and specified
schedule slot ID.


The Extended Schedule Entry Lock Daily Repeating Report Command MUST be returned in response
to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 451




<!-- PAGE 453 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_GET (0x19)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|


**User** **Identifier** **(16** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. If the user identifier is out of range, the command will be ignored


**Schedule** **Slot** **ID** **(8** **bits)**


A value from 1 to _Number_ _of_ _Slots_ _Daily_ _Repeating_ _Supported_ .


**2.2.93.10** **Extended** **Schedule** **Entry** **Lock** **Daily** **Repeating** **Report** **Command**


This command is used to return the requested schedule slot ID for identified user.





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|Command Class = COMMAND_CLASS_SCHEDULE_ENTRY_LOCK (0x4E)|
|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|Command = EXTENDED_SCHEDULE_ENTRY_LOCK_DAILY_REPEATING_REPORT<br>(0x1A)<br>|
|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|User Identifer (MSB)<br>|
|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|User Identifer (LSB)|
|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|Schedule Slot ID|
|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|Week Day Bitmask|
|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|Start Hour|
|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|Start Minute|
|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|Duration Hour|
|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|Duration Minute|


Refer to the description under the Schedule Set Daily Repeating Schedule.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 452