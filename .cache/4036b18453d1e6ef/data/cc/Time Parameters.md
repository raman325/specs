<!-- PAGE 774 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.42** **Time** **Parameters** **Command** **Class,** **version** **1**


The Time Parameters Command Class is used to set date and time in a device hosting this facility.
In case the clock is updated via an external source such as SAT, internet, Rugby/Frankfurt source,
omit this command class. Time zone offset and daylight savings may be set in the Time Command
Class if necessary. The data formats are based on the International Standard ISO 8601.


**3.2.42.1** **Time** **Parameters** **Set** **Command**


This command is used to set current date and time in Universal Time (UTC). Be aware that the
communication overhead may be significant in case routing is necessary.


Table 3.156: Time Parameters Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|
|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|Command = TIME_PARAMETERS_SET|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|
|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|
|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|



**Year** **(16** **bits)**

Specify the year in the usual Gregorian calendar. The first byte (Year 1) is the most significant byte.


**Month** **(8** **bits)**


Specify the month of the year between 01 (January) and 12 (December).


**Day** **(8** **bits)**


Specify the day of the month between 01 and 31.


**Hour** **UTC** **(8** **bits)**


Specify the number of complete hours that have passed since midnight (00..23) in UTC.


**Minute** **UTC** **(8** **bits)**


Specify the number of complete minutes that have passed since the start of the hour (00..59) in UTC.
Minutes are measured in Universal Time (UTC).


**Second** **UTC** **(8** **bits)**


Specify the number of complete seconds since the start of the minute (00..59) in UTC. Seconds are
measured in Universal Time (UTC).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 773




<!-- PAGE 775 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.42.2** **Time** **Parameters** **Get** **Command**


This command is used to request date and time parameters.


The Time Parameters Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.157: Time Parameters Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|
|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|Command = TIME_PARAMETERS_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 774




<!-- PAGE 776 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.42.3** **Time** **Parameters** **Report** **Command**


This command is used to advertise date and time.


Table 3.158: Time Parameters Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|Command Class = COMMAND_CLASS_TIME_PARAMETERS|
|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|Command = TIME_PARAMETERS_REPORT|
|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|Year 1|
|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|Year 2|
|Month|Month|Month|Month|Month|Month|Month|Month|
|Day|Day|Day|Day|Day|Day|Day|Day|
|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|Hour UTC|
|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|Minute UTC|
|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|Second UTC|



Refer to description under the Time Parameters Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 775