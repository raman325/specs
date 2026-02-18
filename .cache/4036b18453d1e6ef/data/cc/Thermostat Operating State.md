<!-- PAGE 498 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.111** **Thermostat** **Operating** **State** **Command** **Class,** **version** **1**


The Thermostat Operating State Command Class is used to obtain the operating state of the ther
mostat.


**2.2.111.1** **Thermostat** **Operating** **State** **Get** **Command**


This command is used to request the operating state.


The Thermostat Operating State Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|



**2.2.111.2** **Thermostat** **Operating** **State** **Report** **Command**


The Thermostat Operating State Report Command is used to report the operating state.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|
|Reserved|Reserved|Reserved|Reserved|Operating State|Operating State|Operating State|Operating State|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Operating** **State** **(4** **bits)**

The thermostat operating state identifier MUST comply with Table 138.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 497

---

<!-- PAGE 499 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.112** **Thermostat** **Operating** **State** **Command** **Class,** **version** **2**


The Thermostat Operating State Command Class is used to obtain the operating state of the thermostat as well as logged operating runtime times of thermostat.


**2.2.112.1** **Thermostat** **Operating** **State** **Get**


This command gets the operating state of the thermostat.


The Thermostat Operating State Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|Command = THERMOSTAT_OPERATING_STATE_GET|



**2.2.112.2** **Thermostat** **Operating** **State** **Report**


This command is used to report the operating state.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|Command = THERMOSTAT_OPERATING_STATE_REPORT|
|Operating State|Operating State|Operating State|Operating State|Operating State|Operating State|Operating State|Operating State|



**Operating** **State** **(8** **bits)**

The thermostat operating state identifier MUST be set according to Table 2.524.


Table 2.524: Thermostat Operating State Report version 2::Operating State encoding







|Operating State|Description|Version|
|---|---|---|
|0x00|Idle|1|
|0x01|Heating|1|
|0x02|Cooling|1|
|0x03|Fan Only|1|
|0x04|Pending Heat. Short cycle prevention feature used in heat pump<br>applications to protect the compressor.|1|
|0x05|Pending Cool.<br>Short cycle prevention feature used in heat pump<br>applications to protect the compressor.|1|
|0x06|Vent/Economizer|1|
|0x07|Aux Heating|2|
|0x08|2~~nd ~~Stage Heating|2|
|0x09|2~~nd ~~Stage Cooling|2|
|0x0A|2~~nd ~~Stage Aux Heat|2|
|0x0B|2~~nd ~~Stage Aux Heat|2|


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 498




<!-- PAGE 500 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.112.3** **Thermostat** **Operating** **State** **Logging** **Supported** **Get**


This command is used to request the operating state logging supported by the device.


The Thermostat Operating State Logging Supported Report Command MUST be returned in response
to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_SUPPORTED_GET|



**2.2.112.4** **Thermostat** **Operating** **State** **Logging** **Supported** **Report**


This command is used to report the operating state logging supported by the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|Command = THERMOSTAT_OPERATING_LOGGING_SUPPORTED_REPORT|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the operating state logging supported by the device.


 - Bit 0 in Bit Mask 1 is not allocated to any Operating State and MUST beset to zero.


 - Bit 1 in Bit Mask 1 indicates if Operating State = 1 (Heating) log is supported.


 - Bit 2 in Bit Mask 1 indicates if Operating State = 2 (Cooling) is supported.


 - …


If the Operating State log is supported the bit MUST be set to 1. If the Operating State log is not
supported the bit MUST be set to 0. It is only necessary to send the Bit Mask fields from 1 and up to
the one indicating the last supported operating state log. The number of Bit Mask fields transmitted
MUST be determined from the length field in the frame.


**2.2.112.5** **Thermostat** **Operating** **State** **Logging** **Get**


This command is used to request the operating state logging supported by the device.


The Thermostat Operating State Logging Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 499




<!-- PAGE 501 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|Command = THERMOSTAT_OPERATING_STATE_LOGGING_GET|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the operating state log types to be requested.


 - Bit 0 in Bit Mask 1 is not allocated to any Operating State and MUST be set to zero.


 - Bit 1 in Bit Mask 1 indicates if Operating State = 1 (Heating) log is supported.


 - Bit 2 in Bit Mask 1 indicates if Operating State = 2 (Cooling) is supported.


 - …


If the Operating State log is supported the bit MUST be set to 1. If the Operating State log is not
supported the bit MUST be set to 0. It is only necessary to send the Bit Mask fields from 1 and
up to the one indicating the last requested operating state log type. The number of Bit Mask fields
transmitted MUST be determined from the length field in the frame.


**2.2.112.6** **Thermostat** **Operating** **State** **Logging** **Report**


This command is used to report the operating state logged for requested operating states.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|Command Class = COMMAND_CLASS_THERMOSTAT_OPERATING_STATE|
|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|Command = THERMOSTAT_OPERATING_STATE_LOGGING_REPORT|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Reserved|Reserved|Reserved|Reserved|Operating State Log Type 1|Operating State Log Type 1|Operating State Log Type 1|Operating State Log Type 1|
|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|
|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|
|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|
|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|
|…|…|…|…|…|…|…|…|
|Reserved|Reserved|Reserved|Reserved|Operating State Log Type N|Operating State Log Type N|Operating State Log Type N|Operating State Log Type N|
|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|Usage Today (Hours)|
|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|Usage Today (Minutes)|
|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|Usage Yesterday (Hours)|
|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|Usage Yesterday (Minutes)|



**Reports** **to** **Follow** **(8** **bits)**


This value indicates how many report frames left before transferring all of the requested thermostat
operating state logs.


**Operating** **State** **Log** **Type** **(N** ***** **4** **bits)**


The Operating State Log Type indicates the operating state type to be requested.


**Usage** **Today** **Hours** **(8** **bits)**


The number of hours (00:24) the thermostat has been in the indicated operating state since 12:00 am
of the current day.


**Usage** **Today** **Minutes** **(8** **bits)**


The number of minutes (00-59) the thermostat has been in the indicated operating state since 12:00
am of the current day.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 500




<!-- PAGE 502 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Usage** **Yesterday** **Hours** **(8** **bits)**


The number of hours (00:24) the thermostat had been in the indicated operating state between 12:00
am and 11:59pm of the previous day.


**Usage** **Yesterday** **Hours** **(8** **bits)**


The number of minutes (00-59) the thermostat had been in the indicated operating state between
12:00 am and 11:59pm of the previous day.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 501