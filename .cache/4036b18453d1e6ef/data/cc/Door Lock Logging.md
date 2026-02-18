<!-- PAGE 202 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.40** **Door** **Lock** **Logging** **Command** **Class,** **version** **1**


This Door Lock Logging Command Class provides an audit trail in an access control application.
Each time an event takes place at the door lock, the system logs the user’s ID, date, time etc.


**2.2.40.1** **Door** **Lock** **Logging** **Records** **Supported** **Get** **Command**


This command is used to request the number of records that the audit trail supports.


The Door Lock Logging Records Supported Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.213: Door Lock Logging Records Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|
|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_GET|



**2.2.40.2** **Door** **Lock** **Logging** **Records** **Supported** **Report** **Command**


This command is used to report the maximum number of reports the audit trail supports.


Table 2.214: Door Lock Logging Records Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|
|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|Command = DOOR_LOCK_LOGGING_RECORDS_SUPPORTED_REPORT|
|Max records stored|Max records stored|Max records stored|Max records stored|Max records stored|Max records stored|Max records stored|Max records stored|



**Max** **records** **stored** **(8** **bits)**


The number of records the audit trail supports stored in a queue.


**2.2.40.3** **Door** **Lock** **Logging** **Record** **Get** **Command**


This command is used to request the audit trail.


The Door Lock Logging Record Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.215: Door Lock Logging Record Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|
|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|Command = RECORD_GET|
|Record number|Record number|Record number|Record number|Record number|Record number|Record number|Record number|



**Record** **number** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 201




<!-- PAGE 203 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Record number field indicates the record to be requested.


A value 0 - _Max_ _records_ stored is acceptable with a value of 0 being the most recent entry. When
requesting with a value of 0, the report will contain the record number so the latest record is known.


**2.2.40.4** **Door** **Lock** **Logging** **Record** **Report** **Command**


This command returns records from the audit trail.

To provide flexibility the user associated with the record may be identified by one of two methods:
the user identifier or the user code.


Table 2.216: Door Lock Logging Record Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|Command Class = COMMAND_CLASS_DOOR_LOCK_LOGGING|
|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|Command = RECORD_REPORT|
|Record number|Record number|Record number|Record number|Record number|Record number|Record number|Record number|
|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|Timestamp - Year 1|
|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|Timestamp - Year 2|
|Timestamp - Month|Timestamp - Month|Timestamp - Month|Timestamp - Month|Timestamp - Month|Timestamp - Month|Timestamp - Month|Timestamp - Month|
|Timestamp - Day|Timestamp - Day|Timestamp - Day|Timestamp - Day|Timestamp - Day|Timestamp - Day|Timestamp - Day|Timestamp - Day|
|Record status|Record status|Record status|Timestamp - Hour Local Time|Timestamp - Hour Local Time|Timestamp - Hour Local Time|Timestamp - Hour Local Time|Timestamp - Hour Local Time|
|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|Timestamp - Minute Local Time|
|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|Timestamp - Second Local Time|
|Event Type<br>|Event Type<br>|Event Type<br>|Event Type<br>|Event Type<br>|Event Type<br>|Event Type<br>|Event Type<br>|
|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|User Identifer|
|User Code Length|User Code Length|User Code Length|User Code Length|User Code Length|User Code Length|User Code Length|User Code Length|
|USER_CODE 1|USER_CODE 1|USER_CODE 1|USER_CODE 1|USER_CODE 1|USER_CODE 1|USER_CODE 1|USER_CODE 1|
|…|…|…|…|…|…|…|…|
|USER_CODE N|USER_CODE N|USER_CODE N|USER_CODE N|USER_CODE N|USER_CODE N|USER_CODE N|USER_CODE N|



**Record** **number** **(8** **bits)**


Record number requested (1- 255).


**Timestamp** **-** **Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Timestamp** **-** **Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December).


**-**
**Timestamp** **Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Record** **status** **(3-bits)**

The Record Status field is used to indicate if legal data is stored in the record.


Table 2.217: Record Status Field

|Record State|Description|
|---|---|
|0|Requested record is empty.|
|1|Requested record holds legal data.|



**Timestamp** **-** **Hour** **Local** **Time** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00-23) in local time.


**Timestamp** **-** **Minute** **Local** **Time** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00-59) in local
time.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 202




<!-- PAGE 204 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Timestamp** **-** **Second** **Local** **Time** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00-59) in local time. The value
60 used to keep UTC from wandering away is not supported.


Note: If RTC (Real Time Clock) all values in Time Stamp record SHOULD be set to 0. Most recent
Record MUST be stored under Record Number 1.

**User** **Identifier** **(8** **bits)**

The User Identifier is used to recognize the user identity. A valid User Identifier MUST be a value
starting from 1 to the maximum number of users supported by the device; refer to the User Code
Command Class. A User Identifier of 0 is acceptable when the record does not need to identify a user
or if the User Code is provided in this report.


**User** **Code** **Length** **(8** **bits)**

The User Code Length field indicates the number of bytes used to hold the User Code. A length of 0
is acceptable when the record does not need to identify a User Code or when the User Identifier field
is non-zero.


**USER_CODE** **(N** **bytes)**

These fields contain the user code. Minimum code length is 4 and maximum 10 ASCII digits. For
further details about the user code, refer to the User Code Command Class.


**Event** **Type** **(8** **bits)**

This field MUST be encoded according to Table 2.218.


Table 2.218: Door Lock Logging Record Report::Event Type en
|Table 2. coding Event Type|.218: Door Lock Logging Record Report::Event Type en- Description|
|---|---|
|Event Type|Description<br>|
|1|Lock Command: Keypad access code verifed lock command<br>|
|2|Unlock Command: Keypad access code verifed unlock command|
|3|Lock Command: Keypad lock button pressed|
|4|Unlock command: Keypad unlock button pressed|
|5|Lock Command: Keypad access code out of schedule|
|6|Unlock Command: Keypad access code out of schedule|
|7|Keypad illegal access code entered|
|8|Key or latch operation locked (manual)|
|9|Key or latch operation unlocked (manual)|
|10|Auto lock operation|
|11|Auto unlock operation<br>|
|12|Lock Command: Z-Wave access code verifed<br>|
|13|Unlock Command: Z-Wave access code verifed|
|14|Lock Command: Z-Wave (no code)|
|15|Unlock Command: Z-Wave (no code)|
|16|Lock Command: Z-Wave access code out of schedule|
|17|Unlock Command Z-Wave access code out of schedule|
|18|Z-Wave illegal access code entered|
|19|Key or latch operation locked (manual)|
|20|Key or latch operation unlocked (manual)|
|21|Lock secured|
|22|Lock unsecured|
|23|User code added|
|24|User code deleted|
|25|All user codes deleted|
|26|Admin code changed|
|27|User code changed|
|28|Lock reset<br>|
|29|Confguration changed|



continues on next page


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 203




<!-- PAGE 205 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Event Type|Table 2.218 – continued from previous page Description|
|---|---|
|Event Type|Description|
|30|Low battery|
|31|New Battery installed|



Not all events types are supported and it is up to manufacturer to decide which ones are to be
supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 204