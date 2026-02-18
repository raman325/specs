<!-- PAGE 233 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.46** **HRV** **Control** **Command** **Class,** **version** **1**


The Heat Recovery Ventilation (HRV) Control Command Class is introducing control of Heat Recovery
Ventilation systems via the Z-Wave interface.


**2.2.46.1** **HRV** **Mode** **Set** **Command**


This command is used to set the desired mode in the device.


Table 2.252: HRV Mode Set

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|Command = HRV_CONTROL_MODE_SET|
|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|Mode|



**Mode** **(5** **bits)**

The mode identifier MAY be set to the following values:

|Mode|Table 2.253: Name|HRV Mode Description|
|---|---|---|
|Mode|Name<br>|Description<br>|
|0|Of|The HRV system is in the of state, frost protec-<br>tion can occur.|
|1|Demand / Automatic|The HRV system is controlled based on sensor<br>input.|
|2|Schedule|The HRV system is controlled based on pre-<br>defned input from the factory and/or user/in-<br>staller.|
|3|Energy Savings Mode|The HRV system will be put into a reduced heat<br>/ ventilation mode.|
|4|Manual|The HRV system is in manual mode.<br>The command HRV Manual Control Set may be<br>used to manually control the device.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.46.2** **HRV** **Mode** **Get** **Command**


This command is used to request the current mode from the device.


The HRV Mode Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.254: HRV Mode Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|Command = HRV_CONTROL_MODE_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 232




<!-- PAGE 234 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.46.3** **HRV** **Mode** **Report** **Command**


The HRV Mode Report Command is used to report the mode from the device.


Table 2.255: HRV Mode Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|Command = HRV_CONTROL_MODE_REPORT|
|Reserved|Reserved|Reserved|Mode|Mode|Mode|Mode|Mode|



**Mode** **(8** **bits)**


Refer to description under the Section 2.2.46.1 HRV Mode Set command.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.46.4** **HRV** **Bypass** **Set** **Command**


This command is used to set the bypass mode when the ventilation system is set to manual mode. If
the system is not in manual mode while receiving this command it MUST be ignored.


Table 2.256: HRV Bypass Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|Command = HRV_CONTROL_BYPASS_SET|
|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|



**Bypass** **(8** **bits)**


The value MAY be 0x00 (close) or 0xFF (open).

Furthermore, the field MAY carry a percentage value between 1 to 99 (0x01 - 0x63). If the ventilation
system supports modulated bypass, the percentage value will represent the aperture of the bypass. If
the system does not support the full range of aperture steps, the values SHOULD be mapped linearly
over the entire scale.


If ventilation system does support modulated bypass the values from 1 to 99 MUST be interpreted as
fully open.


The value 254 (0xFE) MAY be used to set the bypass into automatic mode.


**2.2.46.5** **HRV** **Bypass** **Get** **Command**


This command is used to request the current bypass setting.


The HRV Bypass Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.257: HRV Bypass Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|Command = HRV_CONTROL_BYPASS_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 233




<!-- PAGE 235 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.46.6** **HRV** **Bypass** **Report** **Command**


This command is used to report the current bypass parameters.


Table 2.258: HRV Bypass Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|Command = HRV_CONTROL_BYPASS_REPORT|
|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|Bypass|



**Bypass** **(8** **bits)**


See description in Section 2.2.46.4 HRV Bypass Set command.


**2.2.46.7** **HRV** **Ventilation** **Rate** **Set** **Command**


This command is used to set the ventilation rate when the ventilation system is set to manual mode.
If the system is not in manual mode while receiving this command it MUST be ignored.


Table 2.259: HRV Ventilation Rate Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|
|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|



**Ventilation** **Rate** **(8** **bits)**

The value MAY be 0x00 (off) or 0xFF (on).

The field MAY carry a percentage value between 1 to 99 (0x01 - 0x63). A ventilation system MAY
map the values 1..99 to less than 99 steps.


**2.2.46.8** **HRV** **Ventilation** **Rate** **Get** **Command**


This command is used to request the current ventilation rate setting.


The HRV Ventilation Rate Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.260: HRV Ventilation Rate Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|Command = HRV_CONTROL_VENTILATION_RATE_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 234




<!-- PAGE 236 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.46.9** **HRV** **Ventilation** **Rate** **Report** **Command**


This command is used to report the current ventilation rate setting.


Table 2.261: HRV Ventilation Rate Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|Command = HRV_CONTROL_VENTILATION_RATE_SET|
|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|Ventilation Rate|



**Ventilation** **Rate** **(8** **bits)**


See description under Section 2.2.46.7 HRV Ventilation Rate Set Command.


**2.2.46.10** **HRV** **Mode** **Supported** **Get** **Command**


This command is used to request the supported modes from the device.


The HRV Mode Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.262: HRV Mode Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|Command = HRV_CONTROL_MODE_SUPPORTED_GET|



**2.2.46.11** **HRV** **Mode** **Supported** **Report** **Command**


This command is used to report the supported modes from the device.


Table 2.263: HRV Mode Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|Command Class = COMMAND_CLASS_HRV_CONTROL|
|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|Command = HRV_CONTROL_MODE_SUPPORTED_REPORT|
|Reserved|Reserved|Reserved|Reserved|Manual Control Supported|Manual Control Supported|Manual Control Supported|Manual Control Supported|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Manual** **Control** **Supported** **(3** **bits)**


The manual control supported bits describes the supported manual control modes of the ventilation
system. The mode is supported if the bit is 1. If the bit is 0, the mode is not supported.


The bits are mapped to the following controls:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 235




<!-- PAGE 237 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Bit|Table 2.264: HRV Manual Control Support Name|
|---|---|
|Bit|Name|
|0|Bypass Open / Close|
|1|Bypass Auto|
|2|Modulated Bypass|
|3|Ventilation Rate|



E.g. a ventilation system supporting only open and close would report Manual Control Supported =
0x01.


**Bit** **Mask** **(N** **bytes)**

The Bit Mask fields describe the supported modes by the device.

 - Bit 0 in Bit Mask 1 field indicates if Mode = 0 (Off) is supported.

 - Bit 1 in Bit Mask 1 field indicates if Mode = 1 (Demand / Automatic) is supported.


 - …


If the Mode is supported the bit MUST be set to 1. If the Mode is not supported the bit MUST be
set to 0. It is only necessary to send the Bit Mask fields from 1 and up to the one indicating the last
supported mode. The number of Bit Mask fields transmitted MUST be determined from the length
field in the frame.


All available modes are given in Section 2.2.46.1 HRV Mode Set.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 236