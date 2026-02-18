<!-- PAGE 1028 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8** **Powerlevel** **Command** **Class,** **version** **1**


The Powerlevel Command Class defines RF transmit power controlling Commands useful when installing or testing a network. The Commands makes it possible for supporting controllers to set/get
the RF transmit power level of a node and test specific links between nodes with a specific RF transmit
power level.


**NOTE:** **This** **Command** **Class** **is** **only** **used** **in** **an** **installation** **or** **test** **situation.**


**5.2.8.1** **Powerlevel** **Set** **Command**


This command is used to set the power level indicator value, which should be used by the node when
transmitting RF, and the timeout for this power level indicator value before returning the power level
defined by the application.


Table 5.141: Powerlevel Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Power** **level** **(8** **bits)**

CC:0073.01.01.11.001 This field indicates the power level value that the receiving node MUST set. However, a supporting
node MAY decide not to change its actual Tx configuration. In any case, the value received in this
Command MUST be returned in a _Powerlevel_ _Report_ _Command_ in response to a Powerlevel Get
Command as if the power setting was accepted for the indicated duration.

CC:0073.01.01.11.002 This field MUST be encoded according to Table 5.142.

|Value|Table 5.142: Powerlevel Set::Power level encoding Description|
|---|---|
|Value|Description|
|0x00|NormalPower|
|0x01|minus1dBm|
|0x02|minus2dBm|
|0x03|minus3dBm|
|0x04|minus4dBm|
|0x05|minus5dBm|
|0x06|minus6dBm|
|0x07|minus7dBm|
|0x08|minus8dBm|
|0x09|minus9dBm|



CC:0073.01.01.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


Timeout value is ignored if Power level is set to normalPower.


**Timeout** **(8** **bits)**


The time in seconds the node should keep the Power level before resetting to normalPower level. It
is fundamental, that the timeout IS implemented and followed by the application, for keeping the
network consistent. Valid values are 1-255 resulting in timeouts from 1 second to 255 seconds.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1027




<!-- PAGE 1029 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.2** **Powerlevel** **Get** **Command**


This command is used to request the current power level value.


CC:0073.01.02.11.001 The Powerlevel Report Command MUST be returned in response to this command.


CC:0073.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0073.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.143: Powerlevel Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1028




<!-- PAGE 1030 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.3** **Powerlevel** **Report** **Command**


This command is used to advertise the current power level.


Table 5.144: Powerlevel Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Power** **level** **(8** **bits)**

This value is the current power level indicator value in effect on the node.

CC:0073.01.03.11.001 This field MUST be encoded according to Table 5.142.


If the returned value is normalPower, the timeout value is ignored.


**Timeout** **(8** **bits)**


The time in seconds the node has back at Power level before resetting to normal Power level.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1029




<!-- PAGE 1031 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.4** **Powerlevel** **Test** **Node** **Set** **Command**


This command is used to instruct the destination node to transmit a number of test frames to the
specified NodeID with the RF power level specified. After the test frame transmissions the RF power
level is reset to normal and the result (number of acknowledged test frames) is saved for subsequent
read-back. The result of the test may be requested with a Powerlevel Test Node Get Command.


CC:0073.01.04.12.001 A receiving node SHOULD return an unsolicited Powerlevel Test Node Report Command when it
completed the Powerlevel test initiated by this command.


Table 5.145: Powerlevel Test Node Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|
|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|
|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|



**Test** **NodeID** **(8** **bits)**


The test NodeID that should receive the test frames.


A power level test will not work with a test NodeID which is either a sleeping or FLiRS node. A
CC:0073.01.04.12.002 controller SHOULD NOT initiate a powerlevel test towards sleeping or FLiRS nodes.


**Power** **level** **(8** **bits)**


The power level indicator value to use in the test frame transmission.

CC:0073.01.04.11.001 This field MUST be encoded according to Table 5.142.


**Test** **frame** **count** **(16** **bits)**

The Test frame count field contains the number of test frames to transmit to the Test NodeID. The
first byte is the most significant byte. Valid Test frame count range is 1..65535.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1030




<!-- PAGE 1032 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.5** **Powerlevel** **Test** **Node** **Get** **Command**


This command is used to request the result of the latest Powerlevel Test.


CC:0073.01.05.11.001 The Powerlevel Test Node Report Command MUST be returned in response to this command.


CC:0073.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0073.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.146: Powerlevel Test Node Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1031




<!-- PAGE 1033 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.6** **Powerlevel** **Test** **Node** **Report** **Command**


This command is used to report the latest result of a test frame transmission started by the Powerlevel
Test Node Set Command.


Table 5.147: Powerlevel Test Node Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|
|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|
|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|
|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|
|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|



**Test** **NodeID** **(8** **bits)**

This field advertises the NodeID of the node, which is or has been under test.

CC:0073.01.06.11.001 If a test has been performed, this field MUST reflect the NodeID used in the last test initiated with
the Powerlevel Test Node Set Command.

CC:0073.01.06.11.002 If no test has been performed, this field MUST be set to 0. In this case, the Status of operation and

CC:0073.01.06.13.001 Test frame acknowledged count fields MAY be ignored.


CC:0073.01.06.13.002 It is OPTIONAL to save the last Powerlevel test result in the NVM. If a node saves the last Powerlevel

CC:0073.01.06.13.003 test result in the volatile memory, it MAY set this field to 0 after going to sleep or losing power.


**Status** **of** **operation** **(8** **bits)**

This field indicates the result of the last test initiated with the Powerlevel Test Node Set Command.
CC:0073.01.06.11.003 It MUST be encoded according to Table 5.148.


Table 5.148: Powerlevel Test Node Report::Status of Operation
Encoding

|Value|Description|
|---|---|
|0x00|Test Failed<br>No frame was returned during the test|
|0x01|Test Success<br>At least 1 frame was returned during the test|
|0x02|Test in Progress<br>The test is still ongoing|



CC:0073.01.06.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0073.01.06.13.004 A controller MAY return ”Test Failed” for a non-existing NodeID without carrying the test. However,

CC:0073.01.06.11.005 it MUST return ”Test in Progress” if carrying the test even if it knows that the test will fail.


**Test** **frame** **acknowledged** **count** **(16** **bits)**

This field indicates the number of test frames transmitted, which the Test NodeID has acknowledged.
The first byte is the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1032