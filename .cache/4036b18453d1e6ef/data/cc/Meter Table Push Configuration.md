<!-- PAGE 319 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.65** **Meter** **Table** **Push** **Configuration** **Command** **Class,** **version** **1** **[OBSOLETED]**


The Meter Table Push Configuration Command Class is used to configure the meter to send a Current
Data Report at a given interval. The meter may be configured to return different data sets at different
intervals using both the primary and secondary push commands.


**2.2.65.1** **Meter** **Table** **Push** **Configuration** **Set** **Command**


This command is used to request the meter to send a Current Data Report at a given interval. The
meter may be configured to return different data sets at different intervals using both the primary
and secondary push commands.


Table 2.382: Meter Table Push Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|
|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|Command = METER_TBL_PUSH_CONFIGURATION_SET|
|Reserved|Reserved|Reserved|P/S|Operating Status Push Mode|Operating Status Push Mode|Operating Status Push Mode|Operating Status Push Mode|
|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|
|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|
|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|
|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|
|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|
|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|
|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|
|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|



**Operating** **Status** **Push** **Mode** **(4** **bits)**

This field is used to configure if the Meter Table Status Report Command (refer to Section 2.2.62.11)
participates in the Push Functionality


Table 2.383: Operating Status Push Mode

|i<br>Operating Status Push Mode Identifer|Description|
|---|---|
|0x00|Operating Status push disabled|
|0x01|Operating Status push based on Interval|
|0x02|Operating Status push based on Status Change|
|0x03|Operating Status push Based on Interval AND<br>status change|
|0x04-0x0F|Reserved|



**P/S** **(1** **bit)**


Table 2.384: P/S

|P/S|Description|
|---|---|
|0x00|Primary push confguration<br>|
|0x01|Secondary push confguration|



**Push** **Dataset** **(24** **bits)**


The Push Dataset parameter is use to indicate which parameters are requested to be pushed from the
meter. This field MUST be encoded according to the Meter Dataset defined in [26].


**Interval** **Months** **(8** **bits)**


Specify the number of months between pushing the push dataset.


**Interval** **Day** **(8** **bits)**


Specify the number of days between pushing the push dataset.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 318




<!-- PAGE 320 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Interval** **Hours** **(8** **bits)**


Specify the number of hours between pushing the push dataset.


**Interval** **Minute** **(8** **bits)**


Specify the number of minutes between pushing the push dataset.


**Push** **Node** **ID** **(8** **bits)**


Specify the node ID of the node to receive push dataset in the given interval.


**2.2.65.2** **Meter** **Table** **Push** **Configuration** **Get** **Command**


This command is used to request the meters push configuration

The Meter Table Push Configuration Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.385: Meter Table Push Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|
|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|Command = METER_TBL_PUSH_CONFIGURATION_GET|



**2.2.65.3** **Meter** **Table** **Push** **Configuration** **Report** **Command**


This command is used report the current Push Configuration


Table 2.386: Meter Table Push Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|Command Class = COMMAND_CLASS_METER_TBL_PUSH|
|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|Command = METER_TBL_PUSH_CONFIGURATION_REPORT|
|Reserved|Reserved|Reserved|P/S|Operating Status Push Mode|Operating Status Push Mode|Operating Status Push Mode|Operating Status Push Mode|
|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|Push Dataset 1|
|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|Push Dataset 2|
|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|Push Dataset 3|
|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|Interval Months|
|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|Interval Days|
|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|Interval Hours|
|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|Interval Minutes|
|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|Push Node ID|



Refer to Meter Table Push Configuration Set Command (Section 2.2.65.1) for detailed description of
the fields.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 319