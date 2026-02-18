<!-- PAGE 53 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **2.2 Command Class** **Definitions**


**2.2.1** **Alarm** **Command** **Class,** **version** **1** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **DEPRECATED**


A device MAY implement this Command Class version, but it is RECOMMENDED that new
implementations comply with Notification Command Class, version 8


CC:0071.01.00.12.001


The Alarm Command Class allows applications to report alarm or service conditions. Since these
CC:0071.01.00.11.001 parameters are not standardized across devices the alarms/service parameters MUST be described in
the user manual (or an installer manual).


**2.2.1.1** **Interoperability** **considerations**


The Alarm Command Class has been superseded by the Notification Command Class. Refer to most
recent version of Notification Command Class.


**2.2.1.2** **Alarm** **Get** **Command**


This command is used to get the value of an alarm.


CC:0071.01.04.11.001 The Alarm Report Command MUST be returned in response to this command if the alarm type is
supported.


CC:0071.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.14: Alarm Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|
|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|



**Alarm** **Type** **(8** **bits)**

The Alarm Type field specifies which alarm is being requested. The alarm types are specific for each
application.


**2.2.1.3** **Alarm** **Report** **Command**


This command is used to report the type and level of an alarm.


Table 2.15: Alarm Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|
|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|
|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|



**Alarm** **Type** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 52




<!-- PAGE 54 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Refer to explanation under the _Alarm_ _Get_ _Command_ .


**Alarm** **Level** **(8** **bits)**

The alarm level is application specific.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 53

---

<!-- PAGE 55 -->

CC:0071.02.00.12.001


CC:0071.02.06.11.001


CC:0071.02.06.11.002


CC:0071.02.06.12.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.2** **Alarm** **Command** **Class,** **version** **2** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **DEPRECATED** A
device MAY implement this Command Class version, but it is RECOMMENDED that new implementations comply with Notification Command Class, version 8


The Alarm Command Class is intended for Z-Wave enabled devices capable of reporting alarm reports.


Version 2 of the Alarm Command Class is improved with the following functionalities:

 - Alarm Types defined by the Z-Wave Alliance


 - Interview process of supported Alarm Types


The commands not described in this version remain unchanged from _Alarm_ _Command_ _Class,_ _version_
_1_ _[DEPRECATED]_ .


**2.2.2.1** **Interoperability** **considerations**


The interoperability considerations from version 1 also apply for this version. Refer to Section 2.2.1.1.


**2.2.2.2** **Alarm** **Set** **Command**


This command is used to set the activity of the Z-Wave Alarm Type and Status.


Table 2.16: Alarm Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|Command = ALARM_SET|
|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|
|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|



**Z-Wave** **Alarm** **Type** **(8** **bits)**


Refer to Section 2.2.1.3 Alarm Report Command


**Z-Wave** **Alarm** **Status** **(8** **bits)**

This field is used to set the state of the Alarm Type. The value 0x00 will deactivate the alarm and
0xFF will activate the alarm i.e. unsolicited Alarm Report Command will be transmitted to the
node(s) defined in the Node field(s) when triggered by an event. Any other value is reserved for future

use.


**Note** : The factory default state MUST be described in the product manual. All Z-Wave enabled
devices MUST be able to operate based on factory default settings i.e. an end-user MUST NOT be
forced to set-up the states of the device in order to operate. The factory default state of the Z-Wave
Alarm Status SHOULD be enabled.



CC:0071.02.06.11.003 Products that do not allow deactivation of a specific Alarm Type, MUST respond to a Alarm Configuration Set deactivating the Alarm Type in question by returning an Application Rejected Request
Command of the Application Status Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 54




<!-- PAGE 56 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.2.3** **Alarm** **Get** **Command**


The Alarm Get Command is used to request the alarm state for a specific alarm type announced as
supported through the Alarm Type Supported Report Command.


CC:0071.02.04.11.001 The Alarm Report Command MUST be returned in response to this command if the alarm type is
supported.


CC:0071.02.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.02.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.17: Alarm Get Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|Command = ALARM_GET|
|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|
|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|



**Alarm** **Type** **(8** **bits)**



CC:0071.02.04.11.004



This field refers to the Alarm Type of Alarm Command Class (Version 1) i.e. the application specific
Alarm Type which is not defined by the Z-Wave Alliance. If the ‘V1 Alarm’ field is set to ‘0’ as reported
via the Alarm Type Supported Report Command, this field MUST be set to ‘0’ when requesting the
report.


**Z-Wave** **Alarm** **Type** **(8** **bits)**



CC:0071.02.04.11.005 The Z-Wave Alarm Type field MUST contain the Alarm Type identifier described in Alarm Report
Command. This parameter refers to the Alarm Types defined by the Z-Wave Alliance.


CC:0071.02.04.11.006 A node receiving a non-supported Z-Wave Alarm Type MUST ignore the command. A controlling

CC:0071.02.04.12.001 node SHOULD interview the device for supported Alarm Types by means of Alarm Type Supported
Get Command prior to Alarm Get.


**2.2.2.4** **Alarm** **Report** **Command**


This command is used by the application to report the alarm state.


Table 2.18: Alarm Report Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|Command = ALARM_REPORT|
|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|Alarm Type|
|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|Alarm Level|
|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|Zensor Net Source Node ID|
|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|Z-Wave Alarm Status|
|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|Z-Wave Alarm Type|
|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|Z-Wave Alarm Event|
|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|Number of Event Parameters|
|Event Parameter 1|Event Parameter 1|Event Parameter 1|Event Parameter 1|Event Parameter 1|Event Parameter 1|Event Parameter 1|Event Parameter 1|
|…|…|…|…|…|…|…|…|
|Event Parameter N|Event Parameter N|Event Parameter N|Event Parameter N|Event Parameter N|Event Parameter N|Event Parameter N|Event Parameter N|



**Alarm** **Type** **(8** **bits)**


Refer to Section 2.2.2.4 Alarm Report Command


**Alarm** **Level** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 55




<!-- PAGE 57 -->

CC:0071.02.05.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Refer to Section 2.2.2.4 Alarm Report Command


**Zensor** **Net** **Source** **Node** **ID** **(8** **bits)**


Specify the Zensor Net Source Node ID, which detected the alarm condition. In Zensor Net it is
not possible to determine the Source Node ID due to the broadcast forwarded frame is without this
information on protocol level. If the device is not based on Zensor Net this field MUST be set to ‘0’.


**Z-Wave** **Alarm** **Status** **(8** **bits)**


Refer to Section 2.2.2.2 Alarm Set Command


**Number** **of** **Event** **Parameters** **(8** **bits)**

Indicates the Number of Event Parameters fields used in bytes.


**Z-Wave** **Alarm** **Type** **(8** **bits),** **Z-Wave** **Alarm** **Event** **(8** **bits)** **and** **Event** **Parameters** **(N**
**Byte)**




[36] specifies the Alarm Types and its subordinate parameters defined by the Z-Wave Alliance. The
CC:0071.02.05.11.002 fields that do not contain any definition of the Z-Wave Alarm Type MUST be set to ‘0’ in the Alarm
Report Command.

CC:0071.02.05.11.003 The device MUST advertise support of the Command Class which is included for the specific Alarm
Type. Example: for Smoke Alarm, Smoke Detected the Node Naming and Location Command Class
MUST be advertised as supported in the Node Information Frame.

Alarm Type = 0xFF is used by the Alarm Get Command to retrieve the first alarm detection from
the list of pending alarms.


Example: a device supports the Z-Wave Alarm Types: Smoke, CO2 and Heat. The Heat Alarm is
active e.g. overheat has been detected. When the device receives Alarm Get, Z-Wave Alarm Type
(0xFF), it must return Alarm Report, Z-Wave Alarm Type (0x04), Z-Wave Alarm Event (0x01/0x02)
and the accompanied parameters.


**2.2.2.5** **Alarm** **Type** **Supported** **Get** **Command**


This command is used to request the supported alarm types.


CC:0071.02.07.11.001 The Alarm Type Supported Report Command MUST be returned in response to an Alarm Type
Supported Get command.


CC:0071.02.07.11.002 This command MUST NOT be issued via multicast addressing.


CC:0071.02.07.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.19: Alarm Type Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|Command = ALARM_TYPE_SUPPORTED_GET|



**2.2.2.6** **Alarm** **Type** **Supported** **Report** **Command**


This command is used to advertise the supported alarm types in the application.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 56




<!-- PAGE 58 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.20: Alarm Type Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|Command Class = COMMAND_CLASS_ALARM|
|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|Command = ALARM_TYPE_SUPPORTED_REPORT|
|V1 Alarm|Reserved|Reserved|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**V1** **Alarm** **(1** **bit)**

0 = the device implements only Notification CC V2 (or newer) Notification Type(s).

1 = the device implements Notification CC V2 Notification Types as well as proprietary Alarm CC
V1 Alarm Types and Alarm Levels.


**Reserved**

CC:0071.02.08.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Bit** **Masks** **(5** **bits)**

Indicates the Number of Bit Masks fields used in bytes.


**Bit** **Mask** **(N** **Bytes)**

The Bit Mask fields describe the supported **Z-Wave** **Alarm** Types by the device.


CC:0071.02.08.11.002 - Bit 0 in Bit Mask 1 is not allocated to any Z-Wave Alarm Type and MUST therefore be set to

zero.


      - Bit 1 in Bit Mask 1 indicates if Z-Wave Alarm Type = 1 (Smoke) is supported.


      - Bit 2 in Bit Mask 1 indicates if Z-Wave Alarm Type = 2 (CO) is supported.


      - Bit 3 in Bit Mask 1 indicates if Z-Wave Alarm Type = 3 (CO2) is supported


      - …


CC:0071.02.08.11.003 If the Z-Wave Alarm Type is supported the corresponding bit MUST be set to 1. If the Z-Wave Alarm
Type is not supported the corresponding bit MUST be set to 0.


CC:0071.02.08.11.004
Z-Wave Alarm Type = 0xFF (Return first Alarm on supported list) MUST NOT be advertised in the
Bit Masks.

CC:0071.02.08.11.005 The number of Bit Mask fields MUST match the value advertised in the Number of Bit Masks field.

Note that the mapping of bit 1 to Alarm Type =1 differs from the support mapping used by the
Multilevel Sensor Command Class. The Multilevel Sensor Command Class maps bit 0 to Sensor Type
= 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 57