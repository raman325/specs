<!-- PAGE 63 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.5** **All** **Switch** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED** New implementations
MUST NOT support this Command Class. Controlling nodes MUST use S2 Multicast mechanism
in order to achieve the All On and All Off functionality


The All Switch Command Class is used to switch all devices on or off. Devices may be excluded/included from the all on/all off functionality. The application determines which devices there are
included in the all on/all off functionality as default.


**2.2.5.1** **All** **Switch** **Set** **Command**


This command is used to instruct a device if it is included or excluded from the all on/all off functionality.


Table 2.28: All Switch Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|
|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|Command = SWITCH_ALL_SET|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Mode** **(8** **bits)**

The mode field used to set the all on/all off functionality of the device.


Table 2.29: All Switch Set Command Modes

|Mode|Description|
|---|---|
|0x00|Indicate that the switch is excluded from the all on/all of functionality.|
|0x01|Indicate that the switch is excluded from the all on functionality but not<br>all of.<br>|
|0x02|Indicate that the switch is excluded from the all of functionality but not<br>all on.|
|0x03..0xFE|Reserved<br>|
|0xFF|Indicates that the switch is included in the all on/all of functionality.|



**2.2.5.2** **All** **Switch** **Get** **Command**


This command is used to ask a device if it is included or excluded from the all on/all off functionality.


The All Switch Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.30: All Switch Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|
|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|Command = SWITCH_ALL_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 62




<!-- PAGE 64 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.5.3** **All** **Switch** **Report** **Command**


This command is used to report if the device is included or excluded from the all on/all off functionality.


Table 2.31: All Switch Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|
|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|Command = SWITCH_ALL_REPORT|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Mode** **(8** **bits)**


Refer to the _All_ _Switch_ _Set_ _Command_ .


**2.2.5.4** **All** **Switch** **On** **Command**


This command is used to inform a switch that it SHOULD be turned on. A receiving device MUST
NOT react to this command if the actual operation has been prohibited via the Switch All Set
command. Like the Basic Set On command, this command MUST cause the device to restore the
most recent (non-zero) level.


Table 2.32: All Switch On Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|
|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|Command = SWITCH_ALL_ON|



**2.2.5.5** **All** **Switch** **Off** **Command**


This command is used to inform a switch that it SHOULD be turned off. A receiving device MUST
NOT react to this command if the actual operation has been prohibited via the Switch All Set
command.


Table 2.33: All Switch Off Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|Command Class = COMMAND_CLASS_SWITCH_ALL|
|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|Command = SWITCH_ALL_OFF|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 63