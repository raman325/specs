<!-- PAGE 764 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.40** **Time** **Command** **Class,** **version** **1**


The Time Command Class, version1 is used to read date and time from a supporting node in a Z-Wave
network.


**3.2.40.1** **Compatibility** **considerations**


Notice that the former Time Command Class version 1 (Revision 4 of this document) is discontinued
and replaced by a new one.


**3.2.40.1.1** **Node** **Information** **Frame** **(NIF)**


CC:008A.01.00.21.001 A supporting node MUST always advertise the Time Command Class in its NIF, regardless of the
security bootstrapping outcome. This allows other nodes bootstrapped on any security level to request
the current time from a supporting node.


**3.2.40.2** **Interoperability** **considerations**


Nodes supporting this Command Class are time servers for other nodes in a Z-Wave network. Other
nodes can learn the current date and time by querying nodes supporting this Command Class.


CC:008A.01.00.32.001 For nodes based on an end node Role Type, it is RECOMMENDED to support a dedicated Association
Group which issues the Time Get Command and/or the Date Get Command.


CC:008A.01.00.32.002 Controlling nodes SHOULD automatically associate such association groups to a node supporting the
Time Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 763




<!-- PAGE 765 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.40.3** **Time** **Get** **Command**


This command is used to request the current time from a supporting node.


CC:008A.01.01.11.001 The Time Report Command MUST be returned in response to this command.


CC:008A.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:008A.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.149: Time Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|Command = TIME_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 764




<!-- PAGE 766 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.40.4** **Time** **Report** **Command**


This command is used to report the current time.


Table 3.150: Time Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|Command = TIME_REPORT|
|RTC failure|Reserved|Reserved|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|Hour Local Time|
|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|Minute Local Time|
|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|Second Local Time|



**RTC** **failure** **(1** **bit)**


CC:008A.01.02.11.001 Many RTC chips have a stop bit indicating if the oscillator has been stopped. The RTC failure bit
MUST be set to 1 in order to indicate to the receiving node that the RTC has been stopped and that
the advertised time might be inaccurate.


CC:008A.01.02.11.002 If the sending node does not support this feature or if the oscillator has not been stopped, it MUST
set this field to 0.

CC:008A.01.02.11.003 If the receiving node does not support this feature, it MUST ignore this field.


**Reserved**

CC:008A.01.02.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Hour** **Local** **Time** **(8** **bits)**

This field is used to indicate the number of complete hours that have passed since midnight in local
time.

CC:008A.01.02.11.005 This field MUST be in the range 0..23.


**Minute** **Local** **Time** **(8** **bits)**

This field is used to indicate the number of complete minutes that have passed since the start of the
hour in local time.

CC:008A.01.02.11.006 This field MUST be in the range 0..59.


**Second** **Local** **Time** **(8** **bits)**

This field is used to indicate the number of complete seconds that have passed since the start of the
minute in local time.

CC:008A.01.02.11.007 This field MUST be in the range 0..59.


Note: the time synchronization between nodes may vary by a few seconds due to delays introduced
by the wireless communication.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 765




<!-- PAGE 767 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.40.5** **Date** **Get** **Command**


This command is used to request the current date adjusted according to the local time zone and
Daylight Saving Time from a supporting node.


CC:008A.01.03.11.001 The Date Report Command MUST be returned in response to this command.


CC:008A.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:008A.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.151: Date Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|Command = DATE_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 766




<!-- PAGE 768 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.40.6** **Date** **Report** **Command**


This command is used to advertise the current date adjusted according to the local time zone and
Daylight Saving Time.


Table 3.152: Date Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|Command = DATE_REPORT|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|



**Year** **(16** **bits)**


CC:008A.01.04.11.001
This field MUST specify the current year using the Gregorian calendar. The first byte (Year 1) MUST
be the most significant byte.


For example, Year1 = 0x07 and Year2 = 0xD7 MUST indicate year 2007


**Month** **(8** **bits)**

CC:008A.01.04.11.002 This field MUST specify the current month of the year.

CC:008A.01.04.11.003 This field MUST be in the range 1..12 (representing respectively January…December).


**Day** **(8** **bits)**

CC:008A.01.04.11.004 This field MUST specify current the day of the month.

CC:008A.01.04.11.005 This field MUST be in the range 1..31.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 767

---

<!-- PAGE 769 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.41** **Time** **Command** **Class,** **version** **2**


The Time Command Class, version 2 is used to read date and time from a supporting node in a
Z-Wave network.


**3.2.41.1** **Compatibility** **considerations**


The Time Command Class, version 2 is backwards compatible with the Time Command Class, version

1.

The Time Command Class, version 2 enables reading and setting Time Zone Offset and Daylight
Saving Time parameters. The data formats are based on the International Standard ISO 8601.


CC:008A.02.00.21.001 Commands not described in this version MUST remain unchanged from version 1.


**3.2.41.1.1** **Node** **Information** **Frame** **(NIF)**


CC:008A.02.00.21.002 A supporting node MUST always advertise the Time Command Class in its NIF, regardless of the
security bootstrapping outcome.


This allows other nodes bootstrapped on any security level to request the current time from a supporting node.


**3.2.41.2** **Interoperability** **considerations**


Nodes supporting this Command Class are time servers for other nodes in a Z-Wave network. Other
nodes can learn the current date and time by querying nodes supporting this Command Class.


CC:008A.02.00.32.001 For nodes based on an end node Role Type, it is RECOMMENDED to support a dedicated Association
Group which issues the Time Get Command, the Date Get Command and/or the Time Offset Get
Command.


CC:008A.02.00.32.002 Controlling nodes SHOULD automatically associate such association groups to a node supporting the
Time Command Class, version 2.


The purpose of this Command Class is to read the current date and time information from supporting
CC:008A.02.00.33.001 nodes. Hence, supporting nodes MAY ignore the Time Offset Set Command introduced in version 2 if
they rely on another source to retrieve the Time Zone Offset and Daylight Saving Time information.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 768




<!-- PAGE 770 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.41.3** **Time** **Offset** **Get** **Command**


This command is used to request the Time Zone Offset (TZO) and Daylight Savings Time (DST)
parameters from a supporting node.

CC:008A.02.06.11.001 The Time Offset Report Command MUST be returned in response to this command.


CC:008A.02.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:008A.02.06.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.153: Time Offset Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|Command = TIME_OFFSET_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 769




<!-- PAGE 771 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.41.4** **Time** **Offset** **Set** **Command**


This command is used to set Time Zone Offset (TZO) and Daylight Savings Time (DST) at the
supporting node.


CC:008A.02.05.13.001 This command MAY be ignored by a supporting node if it relies on another source to retrieve the
TZO/DST information.


CC:008A.02.05.12.001 This command SHOULD be ignored if it is not received at the highest granted security level.


Table 3.154: Time Offset Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|Command = TIME_OFFSET_SET|
|Sign TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|
|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|
|Sign Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|
|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|
|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|
|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|
|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|
|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|
|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|



**Sign** **TZO** **(1** **bit)**

This field is used to indicate the sign (plus or minus) to apply to the Hour TZO and Minute TZO
fields.

CC:008A.02.05.11.001 The value 0 MUST indicate the Plus sign (positive offset from UTC)

CC:008A.02.05.11.002 The value 1 MUST indicate the Minus sign (negative offset from UTC)


**Hour** **TZO** **(7** **bits)**

This field is used to indicate the number of hours that the originating time zone deviates from UTC.

CC:008A.02.05.12.002 This field SHOULD be in the range 0..14.


**Minute** **TZO** **(7** **bits)**

This field is used to indicate the number of minutes that the originating time zone deviates UTC.

CC:008A.02.05.11.003 This field MUST be in the range 0..59.

**Sign** **Offset** **DST** **(1** **bit)**

This field is used to indicate the sign (plus or minus) for the Minute Offset DST field to apply to the
current time while in the Daylight Saving Time.

CC:008A.02.05.11.004 The value 0 MUST indicate the Plus sign (positive offset from current time),

CC:008A.02.05.11.005 The value 1 MUST indicate the Minus sign (negative offset from current time).

**Minute** **Offset** **DST** **(7** **bits)**

CC:008A.02.05.11.006 This field MUST indicate the number of minutes by which the current time is to be adjusted when
Daylight Saving Time starts.


**Month** **Start** **DST** **(8** **bits)**

CC:008A.02.05.11.007 This field MUST indicate the month of the year when Daylight Saving Time starts.

CC:008A.02.05.11.008 This field MUST be in the range 1..12 (representing respectively January…December).


**Day** **Start** **DST** **(8** **bits)**

CC:008A.02.05.11.009 This field MUST indicate the day of the month when Daylight Saving Time starts.

CC:008A.02.05.11.00A This field MUST be in the range 1..31.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 770




<!-- PAGE 772 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Hour** **Start** **DST** **(8** **bits)**

CC:008A.02.05.11.00B This field MUST indicate the hour of the day when Daylight Saving Time starts.

CC:008A.02.05.11.00C This field MUST be in the range 0..23.


**Month** **End** **DST** **(8** **bits)**

CC:008A.02.05.11.00D This field MUST indicate the month of the year when Daylight Saving Time ends.

CC:008A.02.05.11.00E This field MUST be in the range 1..12 (representing respectively January…December).


**Day** **End** **DST** **(8** **bits)**

CC:008A.02.05.11.00F This field MUST indicate the day of the month when Daylight Saving Time ends.

CC:008A.02.05.11.010 This field MUST be in the range 1..31


**Hour** **End** **DST** **(8** **bits)**

CC:008A.02.05.11.011 This field MUST indicate the hour of the day when Daylight Saving Time ends.

CC:008A.02.05.11.012 This field MUST be in the range 0..23.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 771




<!-- PAGE 773 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.41.5** **Time** **Offset** **Report** **Command**


This command is used to advertise the Time Zone Offset (TZO) and Daylight Savings Time (DST)
parameters.


Table 3.155: Time Offset Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|Command Class = COMMAND_CLASS_TIME|
|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|Command = TIME_OFFSET_REPORT|
|Sign TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|Hour TZO|
|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|Minute TZO<br><br>|
|Sign Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|Minute Ofset DST|
|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|Month Start DST|
|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|Day Start DST|
|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|Hour Start DST|
|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|Month End DST|
|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|Day End DST|
|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|Hour End DST|



For fields’ description, refer to Section 3.2.41.4 Time Offset Set Command.

CC:008A.02.02.11.001 A sending node MUST comply with fields’ description from Section 3.2.41.4 Time Offset Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 772