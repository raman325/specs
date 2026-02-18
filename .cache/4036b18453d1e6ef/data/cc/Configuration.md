<!-- PAGE 153 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.30** **Configuration** **Command** **Class,** **version** **1**


The Configuration Command Class allows product specific configuration parameters to be changed.
One example could be the default dimming rate of a light dimmer.

**CC:0070.01.00.11.00** 12 Configuration parameters MUST be specified in the product documentation. Configuration parameters accessed via this command class MUST NOT replace similar commands provided by other existing
Command Classes.

CC:0070.01.00.12.001 A device MUST be able to operate with default factory configuration parameter values.

CC:0070.01.00.11.003 It is RECOMMENDED that configuration parameters can be manipulated via a local user interface.

CC:0070.01.00.12.002 It is RECOMMENDED that default factory configuration parameter values can be restored via a
local user interface.


**2.2.30.1** **Compatibility** **considerations**


**2.2.30.1.1** **“Default”** **flag**


Earlier text revisions of the Configuration Command Class, versions 1-3 presented conflicting interCC:0070.01.00.23.001 pretations of the default field. Controllers should be aware that nodes with version 3 or less MAY
reset all configuration parameters to default when receiving a Configuration Set or Configuration Bulk
Set Command with the Default bit set to 1.


CC:0070.01.00.22.001 A controller SHOULD probe a node in order to discover what behavior it implements. The following
steps are RECOMMENDED:

      - If the device is version 1- 2, scan the node for available configuration parameters. Else discover
the available parameters thanks to the Configuration Properties Get Command.


      - Determine how the default bit works if the node implements 2 or more parameters


**Step** **1:**

      - One at a time, issue a Configuration Set for a parameter number, and check whether the value
can be read back. Try each parameter for 1, 2 and 4 bytes sizes.


      - Store the discovered parameter list for future use.


**Step** **2:**

      - Choose 2 parameters and issue a Configuration Set with the default bit set to 1 for each parameter.

      - Read back both parameters value with a Configuration Get.


      Try to modify both parameters to non-default values (it is recommended to try the default value
± 1)

      - Send a Configuration Set for one of parameters with the default bit set to 1.


      - Read back both parameters and check whether one or both returned to the default value


**2.2.30.2** **Configuration** **Set** **Command**


The Configuration Set Command is used to set the value of a configuration parameter.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 152




<!-- PAGE 154 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.149: Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|
|Default|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|



**Parameter** **Number** **(8** **bits)**

CC:0070.01.04.13.001 This field is used to specify the actual configuration parameter. Parameter Numbers MAY be product

CC:0070.01.04.12.001 specific. Parameter Numbers SHOULD be assigned in a sequence starting from 1.


**Default** **(1** **bit)**

This field is used to specify if the default value is to be restored for the specified configuration
parameter.


CC:0070.01.04.11.001

The value 1 MUST indicate that default factory settings must be restored for the specified Parameter
CC:0070.01.04.11.002 Number. In this case, the Configuration Value field MUST be ignored and the receiving node MUST
reset the specified parameter and SHOULD NOT reset any other parameters.

CC:0070.01.04.11.003 The value 0 MUST indicate that the specified Parameter Number must assume the value specified by
the Configuration Value field.


**Reserved**

CC:0070.01.04.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Size** **(3** **bits)**

CC:0070.01.04.11.005 This field is used to specify the size of the actual parameter. The advertised size of a given parameter
MUST always be the same. The value of this field MUST comply with Table 2.150.

|Size|Table 2.150: Configuration Set::Size encoding Size of Value Field|
|---|---|
|Size|Size of Value Field|
|1|8 bit|
|2|16 bit|
|4|32 bit|



CC:0070.01.04.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Configuration** **Value** **(N** **bytes)**


CC:0070.01.04.11.007
This field carries the value to be assigned. The size of the field MUST comply with the size advertised
by the Size field.

CC:0070.01.04.11.008 The field MUST carry a signed value. The binary encoding of the signed value MUST comply with
Table 2.12. The field Value 1 MUST be the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 153




<!-- PAGE 155 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.30.3** **Configuration** **Get** **Command**


This command is used to query the value of a configuration parameter.

CC:0070.01.05.11.001 The Configuration Report Command MUST be returned in response to this command.


CC:0070.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0070.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.151: Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|Command = CONFIGURATION_GET|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|



**Parameter** **Number** **(8** **bits)**

CC:0070.01.05.13.001 This field is used to specify the requested configuration parameter. Parameter Numbers MAY be

CC:0070.01.05.12.001 product specific. Parameter Numbers SHOULD be assigned in a sequence starting from 1.


CC:0070.01.05.12.002 A node receiving this command for an unsupported parameter SHOULD return a Report advertising
the value of the first available parameter in the node.


**2.2.30.4** **Configuration** **Report** **Command**


This command is used to advertise the actual value of the advertised parameter.


Table 2.152: Configuration Report“ Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|Command = CONFIGURATION_REPORT|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|
|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|



Refer to the Configuration Set Command for parameter details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 154

---

<!-- PAGE 156 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.31** **Configuration** **Command** **Class,** **version** **2**


The Configuration Command Class allows product specific configuration parameters to be changed.
One example could be the default dimming rate of a light dimmer.

**CC:0070.02.00.11.00** 12 Configuration parameters MUST be specified in the product documentation. Configuration parameters accessed via this command class MUST NOT replace similar commands provided by other existing
Command Classes.

CC:0070.02.00.11.003 A device MUST be able to operate with default factory configuration parameter values.

CC:0070.02.00.12.001 It is RECOMMENDED that configuration parameters can be manipulated via a local user interface.

CC:0070.02.00.12.002 It is RECOMMENDED that default factory configuration parameter values can be restored via a
local user interface.


**2.2.31.1** **Compatibility** **considerations**


Configuration Command Class, version 2 extends the addressing space to 65.535 product specific
configuration parameters. Further, Configuration Command Class, version 2 makes it possible to set
multiple configuration parameters with one Command.


CC:0070.02.00.21.001
A device supporting Configuration Command Class, version 2 MUST support _Configuration Command_
_Class,_ _version_ _1_ .


**2.2.31.1.1** **“Default”** **flag**


Refer to Section 2.2.30.1.1.


**2.2.31.2** **Interoperability** **considerations**


Configuration Command Class, version 2 is backwards compatible with Configuration Command
Class, version 1.



CC:0070.02.00.31.001



Configuration Command Class, version 2 does not extend any existing commands of Configuration
Command Class, version 1. The 255 parameters that can be addressed by the Configuration Set
Command MUST be identical to the first 255 parameters that can be addressed by the (version 2)
Configuration Bulk Set Command.


**2.2.31.3** **Configuration** **Set** **Command**


This Command is used to set the value of a configuration parameter.


Table 2.153: Configuration Set Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|
|Default|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|



**Parameter** **Number** **(8** **bits)**



**CC:0070.02.04.1** 32 **.001** This field is used to specify the actual configuration parameter. Parameter Numbers MAY be product
specific. Parameter Numbers SHOULD be assigned in a sequence starting from 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 155




<!-- PAGE 157 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Default** **(1** **bit)**

This field is used to specify if the default value is to be restored for the specified configuration
parameter.


CC:0070.02.04.11.001

The value 1 MUST indicate that default factory settings must be restored for the specified Parameter
CC:0070.02.04.11.002 Number. In this case, the Configuration Value field MUST be ignored and the receiving node MUST
reset the specified parameter and SHOULD NOT reset any other parameters.

CC:0070.02.04.11.003 The value 0 MUST indicate that the specified Parameter Number must assume the value specified by
the Configuration Value field.


**Reserved**

CC:0070.02.04.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Size** **(3** **bits)**

CC:0070.02.04.11.005 This field is used to specify the size of the actual parameter. The advertised size of a given parameter
MUST always be the same. The value of this field MUST comply with Table 2.150.


CC:0070.02.04.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Configuration** **Value** **(N** **bytes)**


CC:0070.02.04.11.007
This field carries the value to be assigned. The size of the field MUST comply with the size advertised
by the Size field.

CC:0070.02.04.11.008 The field MUST carry a signed value. The binary encoding of the signed value MUST comply
withTable 10. The field Value 1 MUST be the most significant byte.


**2.2.31.4** **Configuration** **Bulk** **Set** **Command**


This command is used to set the value of one or more configuration parameters.


Table 2.154: Configuration Bulk Set Command





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|
|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|
|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|
|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|
|Default|Hand- shake<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|


**Parameter** **Offset** **(16** **bits)**

CC:0070.02.07.11.001 This field is used to specify the first parameter in a range of one or more parameters. The first byte
MUST carry the most significant byte of the 16 bit value.


**Number** **of** **Parameters** **(8** **bits)**

This field is used to specify the number (M) of configuration parameters contained in this command.

CC:0070.02.07.11.002 The value of this field MUST be in the range 1..255.


CC:0070.02.07.11.010


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 156




<!-- PAGE 158 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The advertised parameters MUST be in a consecutive range. For example, Parameter Offset set to 4
and Number of Parameters set to 3 MUST represent parameters number 4, 5 and 6.


CC:0070.02.07.11.011 A receiving node MUST ignore values for non-existing parameters


**Default** **(1** **bit)**

This field is used to specify if the default value is to be restored for the specified configuration
parameters.



CC:0070.02.07.11.003


CC:0070.02.07.11.004



The value 1 MUST indicate that default factory settings must be restored for the Parameter Numbers
defined by the Parameter Offset and Number of Parameters fields. In this case, the Configuration Value
field MUST be ignored and the receiving node MUST reset the specified parameters and SHOULD
NOT reset any other parameters.



CC:0070.02.07.11.005 The value 0 MUST indicate that the specified Parameter Numbers must assume the value specified
by the Configuration Value field.


**Handshake** **(1** **bit)**

This field is used to indicate if a Configuration Bulk Report Command is to be returned when the
specified configuration parameters have been stored in non-volatile memory.



CC:0070.02.07.11.006


CC:0070.02.07.11.007


CC:0070.02.07.11.008


CC:0070.02.07.11.009


CC:0070.02.07.12.001



If the Handshake bit is set to 1, a Configuration Bulk Report Command MUST be returned. The
command MUST echo all parameters found in this Configuration Bulk Set Command. A node returning a Configuration Bulk Report Command with the Handshake bit set MUST be ready to receive
another Configuration Bulk Set Command. If the Handshake bit is set, an originating node MUST
wait for the Configuration Bulk Report Command for at least one second. If not receiving a report,
the originating node SHOULD assume that the operation failed and resend the same Configuration
Bulk Set Command one more time.



CC:0070.02.07.11.00A If the Handshake bit is set to 0, a receiving node MUST NOT return a Configuration Bulk Report in

response.


**Reserved**

CC:0070.02.07.11.00B This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Size** **(3** **bits)**

This field is used to specify the size of the actual parameters. The advertised size of a given parameter
CC:0070.02.07.11.00C MUST always be the same. The value of this field MUST comply with Table 2.150.


CC:0070.02.07.11.00D All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Parameter** **-** **Configuration** **Value** **(M*N** **bytes)**

CC:0070.02.07.11.00E These fields carry the values to be assigned. Each field MUST have the same size. The size of each
field MUST comply with the size advertised by the Size field.

CC:0070.02.07.11.00F The field MUST carry a signed value. The binary encoding of the signed value MUST comply
withTable 10. The Value 1 field MUST be the most significant byte.


**2.2.31.5** **Configuration** **Bulk** **Get** **Command**


This command is used to query the value of one or more configuration parameters.

CC:0070.02.08.11.001 The Configuration Bulk Report Command MUST be returned in response to this command.


CC:0070.02.08.11.002 This command MUST NOT be issued via multicast addressing.


CC:0070.02.08.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 157




<!-- PAGE 159 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.155: Configuration Bulk Get Command





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|Command = CONFIGURATION_BULK_GET<br>|
|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|
|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|
|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|


**Parameter** **Offset** **(16** **bits)**

This field is used to specify the first parameter in a range of one or more parameters. The first byte
CC:0070.02.08.11.004 MUST carry the most significant byte of the 16 bit value.


CC:0070.02.08.12.001 Parameter Numbers SHOULD be assigned in a sequence starting from 1.


**Number** **of** **Parameters** **(8** **bits)**

This field is used to specify the number of requested configuration parameters.

CC:0070.02.08.11.005 The value of this field MUST be in the range 1..255.

CC:0070.02.08.11.006 The advertised parameters MUST be in a consecutive range. For example, Parameter Offset set to 4
and Number of Parameters set to 3 MUST represent parameters number 4, 5 and 6.


**2.2.31.6** **Configuration** **Bulk** **Report** **Command**


This command is used to advertise the actual value of one or more advertised parameters.


Table 2.156: Configuration Bulk Report Command





|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|Command = CONFIGURATION_BULK_REPORT<br>|
|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|
|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|
|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|
|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|
|Default|Hand- shake<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|


**Parameter** **Offset** **(16** **bits)**


CC:0070.02.09.11.001
This field is used to advertise the first parameter in a range of one or more parameters. The first byte
MUST carry the most significant byte of the 16 bit value.


**Number** **of** **Parameters** **(8** **bits)**

This field is used to advertise the number (M) of configuration parameters contained in this command.

CC:0070.02.09.11.002 The value of this field MUST be in the range 1..255.

CC:0070.02.09.11.012 The advertised parameters MUST be in a consecutive range. For example, Parameter Offset set to
4 and Number of Parameters set to 3 MUST represent parameters number 4, 5 and 6, regardless of
whether they exist at the sending node.


**Reports** **to** **follow** **(8** **bits)**


CC:0070.02.09.11.003


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 158




<!-- PAGE 160 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be used to advertise the number of reports left before all requested configuration
parameters values have been transferred.


CC:0070.02.09.11.004 The value 0 MUST indicate that this is the last report.

CC:0070.02.09.11.005 If the Handshake field is 1, this field MUST be set to 0.

CC:0070.02.09.11.006 The value of this field MUST be in the range 0..255.


**Default** **(1** **bit)**

CC:0070.02.09.11.007 This field MUST be used to advertise if all advertised configuration parameters have the factory
default value.

CC:0070.02.09.11.008 The value 1 MUST indicate that all advertised configuration parameters have the factory default
value.

CC:0070.02.09.11.009 The value 0 MUST indicate that one or more of the advertised configuration parameters do not have
the factory default value.


**Handshake** **(1** **bit)**

This field is used to indicate if this report is returned in response to a Configuration Bulk Set Command.



CC:0070.02.09.11.00A


CC:0070.02.09.11.00B


CC:0070.02.09.11.00C



The value 1 MUST indicate that all configuration parameters have been stored in non-volatile memory
and that the sending node is ready to receive another Configuration Bulk Set Command. Except for
the Reports to Follow field, all other fields MUST echo the values received in the Configuration Bulk
Set Command. The Reports to Follow field MUST be 0.



CC:0070.02.09.11.00D The value 0 MUST indicate that this report is returned in response to a Configuration Bulk Get
Command.


**Size** **(3** **bits)**

This field is used to advertise the size of the actual parameter. The advertised size of a given parameter
CC:0070.02.09.11.00E MUST always be the same. The value of this field MUST comply with Table 2.150.


CC:0070.02.09.11.00F All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Parameter** **-** **Configuration** **Value** **(M*N** **bytes)**

These fields carry the values advertised by the Parameter Offset and Number of Parameters fields.
CC:0070.02.09.11.010 Each field MUST have the same size. The size of each field MUST comply with the size advertised
by the Size field.

CC:0070.02.09.11.011 The field MUST carry a signed value. The binary encoding of the signed value MUST comply with
Table 2.12 Table 10. The Value 1 field MUST be the most significant byte.

CC:0070.02.09.12.001 A sending node SHOULD set this field to 0 for non-existing parameters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 159

---

<!-- PAGE 161 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.32** **Configuration** **Command** **Class,** **version** **3**


The Configuration Command Class, version 3 allows product specific configuration parameters to be
changed. Examples include the default dimming rate of a light dimmer and the endpoints of a window
covering device.

CC:0070.03.00.11.001 Configuration parameters accessed via this command class MUST NOT replace similar commands
provided by other existing application Command Classes.

CC:0070.03.00.11.002 Configuration parameter documentation MUST be provided in the product documentation.

CC:0070.03.00.12.001 Configuration parameter documentation SHOULD be provided via Z-Wave via this command class
version.

CC:0070.03.00.11.003 A device MUST be able to operate with default factory configuration parameter values.

CC:0070.03.00.12.002 It is RECOMMENDED that configuration parameters can be manipulated via a local user interface.

CC:0070.03.00.12.003 It is RECOMMENDED that default factory configuration parameter values can be restored via a
local user interface.


**2.2.32.1** **Compatibility** **considerations**


The following additions are made to the Configuration Command Class, version 3:

      - Configuration Name Get Command

      - Configuration Name Report Command

      - Configuration Info Get Command

      - Configuration Info Report Command

      - Configuration Properties Get Command

      - Configuration Properties Report Command


The purpose of the above commands is to allow a manufacturer to advertise information relating to
the use of a specific configuration parameter directly from the configuration interface. The advertised
information should be the same as can be found in the printed documentation.

It should be emphasized that, just like versions 1 and 2, the Configuration Command Class, version
3 is intended only for access to product specific configuration parameters. The access to parameter
information is only meant to facilitate access via Z-Wave to information which can also be found in
the printed documentation.

Configuration Command Class versions 1 and 2 explicitly require that the binary value of all configuration parameters are represented as signed values encoded as binary 2’s complement.

Configuration Command Class v3 allows for bit field, signed integer or unsigned integer representations
of each individual parameter.



CC:0070.03.00.21.001


CC:0070.03.00.21.002



A device supporting the Configuration Command Class v3 MUST respond to a Configuration Properties Get command. If a Configuration Properties Report command is not returned in response to
a Configuration Properties Get command, a controlling device MUST treat the parameter value as a
signed integer.

Configuration Command Class version 2 extended the possible parameter range from 1..255 to
1..65535. The first 255 parameters of the two ranges are identical. Parameters in the range 1..255 can
be addressed using either the Bulk Set/Get Commands or Set/Get Commands while parameters in
the range 256..65535 can only be addressed using the Bulk Set/Get Commands.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 160




<!-- PAGE 162 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.32.1.1** **“Default”** **flag**


Refer to Section 2.2.30.1.1.


**2.2.32.1.2** **Configuration** **Properties** **Report**


Earlier text revisions of the Configuration Command Class, version 3 did not explicitly specify that
CC:0070.03.00.21.003 the “Min Value”, “Max Value” and “Default Value” fields MUST be omitted if the advertised size is
0 in the Configuration Properties Report Command.



CC:0070.03.00.22.001


CC:0070.03.00.22.002



Controlling nodes SHOULD be aware that some legacy nodes supporting version 3 could by error
include the “Min Value”, “Max Value” and “Default Value” fields and set them to 0x00 with an
arbitrary size. If a controlling node receives a Report in which the “Next Parameter Number” field
seems to be set to 0x0000 when requesting parameter number 0, the controlling node SHOULD inspect
the last 2 bytes of the command frame in order to find out what is the Next Parameter Number.


**2.2.32.2** **Interoperability** **considerations**



CC:0070.03.00.32.001 It is RECOMMENDED that the name and information stored in a supporting device are in English.

CC:0070.03.00.32.002 It is RECOMMENDED that the last line of the information field presents an Internet URL which
points to updated information for the actual configuration parameter as well as other language variants.


**2.2.32.3** **Configuration** **Name** **Get** **Command**


This command is used to request the name of a configuration parameter.

CC:0070.0A.11.001 The Configuration Name Report Command MUST be returned in response to this command.


CC:0070.0A.11.002 This command MUST NOT be issued via multicast addressing.


CC:0070.0A.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.157: Configuration Name Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|Command = CONFIGURATION_NAME_GET|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|



**Parameter** **Number** **(16** **bits)**

This field is used to specify the requested configuration parameter.

CC:0070.03.0A.11.004 The first byte MUST carry the most significant byte of the 16 bit value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 161




<!-- PAGE 163 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.32.4** **Configuration** **Name** **Report** **Command**


This command is used to advertise the name of a parameter.


Table 2.158: Configuration Name Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|Command = CONFIGURATION_NAME_REPORT|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|
|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|
|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|
|…|…|…|…|…|…|…|…|
|Name N|Name N|Name N|Name N|Name N|Name N|Name N|Name N|



**Parameter** **Number** **(16** **bits)**

This field is used to advertise the actual configuration parameter.

CC:0070.03.0B.11.001 The first byte MUST carry the most significant byte of the 16 bit value.



CC:0070.03.0B.13.001


CC:0070.03.0B.12.001



If a non-existing parameter is specified in a Configuration Name Get Command, a receiving node
MAY return a zero-length Name field in the Configuration Name Report Command. The receiving
node SHOULD however return an error message e.g. “Unassigned parameter”.


Parameter numbers above 255 can only be addressed using the Bulk Set/Get Commands. Parameter
numbers in the range 1..255 can be addressed using either the Bulk Set/Get Commands or the Set/Get
Commands.


**Reports** **to** **follow** **(8** **bits)**

This field is used to advertise the number of reports left before all parts of the command have been
transferred.



CC:0070.03.0B.11.002 The value 0 MUST indicate that this is the last report.


**Name** **(N** **bytes)**

CC:0070.03.0B.12.002 This field is used to advertise the name of the parameter. It is RECOMMENDED that the Name
field advertises the name found in the documentation.

CC:0070.03.0B.11.003 The field MUST carry a byte string with no zero termination. The Name field MAY span multiple
reports. The number of Name bytes transmitted MUST be determined from the length field in the
frame.


CC:0070.03.0B.11.004 Bytes MUST be encoded in UTF-8 format.


CC:0070.03.0B.12.003 It is RECOMMENDED that the name stored in a supporting device is in English.


**2.2.32.5** **Configuration** **Info** **Get** **Command**


This command is used to request usage information for a configuration parameter.

CC:0070.03.0C.11.001 The Configuration Info Report Command MUST be returned in response to this command.


CC:0070.03.0C.11.002 This command MUST NOT be issued via multicast addressing.


CC:0070.03.0C.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 162




<!-- PAGE 164 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.159: Configuration Info Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|Command = CONFIGURATION_INFO_GET|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|



**Parameter** **Number** **(16** **bits)**

This field is used to specify the requested configuration parameter.

CC:0070.03.0C.11.004 The first byte MUST carry the most significant byte of the 16 bit value.


**2.2.32.6** **Configuration** **Info** **Report** **Command**


This command is used to advertise usage information for a configuration parameter.


Table 2.160: Configuration Info Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|Command = CONFIGURATION_INFO_REPORT|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|
|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|Reports to follow|
|Info 1|Info 1|Info 1|Info 1|Info 1|Info 1|Info 1|Info 1|
|…|…|…|…|…|…|…|…|
|Info N|Info N|Info N|Info N|Info N|Info N|Info N|Info N|



**Parameter** **Number** **(16** **bits)**

This field is used to advertise the actual configuration parameter.

CC:0070.03.0D.11.001 The first byte MUST carry the most significant byte of the 16 bit value.

CC:0070.03.0D.13.001 If a non-existing parameter is specified in a Configuration Info Get Command, a receiving node

CC:0070.03.0D.12.001 MAY return a zero-length Info field in the Configuration Info Report Command. The receiving node
SHOULD however return an error message, e.g. “Unassigned parameter”.


Parameter numbers above 255 can only be addressed using the Bulk Set/Get Commands. Parameter
numbers in the range 1..255 can be addressed using either the Bulk Set/Get Commands or the Set/Get
Commands


**Reports** **to** **follow** **(8** **bits)**

This field is used to advertise the number of reports left before all parts of the command have been
transferred.


CC:0070.03.0D.11.002 The value 0 MUST indicate that this is the last report.


**Info** **(N** **bytes)**

CC:0070.03.0D.12.002 This field is used to advertise the detailed information available for the parameter. It is RECOMMENDED that the Info field carries all information found in the documentation.

CC:0070.03.0D.11.003 The field MUST carry a byte string with no zero termination.

CC:0070.03.0D.11.004 The number of Info bytes transmitted MUST be determined from the length field in the frame.

CC:0070.03.0D.13.002 The Info field MAY span multiple reports. The number of Info bytes MAY be zero.


CC:0070.03.0D.11.005 Bytes MUST be encoded in UTF-8 format.


CC:0070.03.0D.12.003 It is RECOMMENDED that the information stored in a supporting device is in English.


CC:0070.03.0D.12.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 163




<!-- PAGE 165 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


It is RECOMMENDED that the last line of the information field presents an Internet URL which
points to updated information for the actual configuration parameter as well as other language variants.


**2.2.32.7** **Configuration** **Properties** **Get** **Command**


This command is used to request the properties of a configuration parameter.

The Configuration Properties Report Command MUST be returned in response to this command.

If a Configuration Properties Report command is not returned in response to a Configuration Properties Get command, a controlling device MUST treat the parameter value as a signed integer.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.161: Configuration Properties Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|Command = CONFIGURATION_PROPERTIES_GET|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|



**Parameter** **Number** **(16** **bits)**

This field is used to specify the requested configuration parameter.

CC:0070.03.0E.11.001 The first byte MUST carry the most significant byte of the 16 bit value.


CC:0070.03.0E.11.002

If a non-existing parameter is specified in this command, a receiving node MUST advertise zero values
CC:0070.03.0E.11.003 in the Format and Size fields. The Next Parameter Number field MUST advertise the next available
configuration parameter.

CC:0070.03.0E.12.001 It is RECOMMENDED that a controlling device initiates probing of supported configuration parameters by issuing this command for parameter number 0.


CC:0070.03.0E.12.002
If a Size field value of zero is returned, a controlling device SHOULD issue a Configuration Properties
Get Command for the parameter advertised in the Next Parameter Number field.


**2.2.32.8** **Configuration** **Properties** **Report** **Command**


This command is used to advertise the properties of a configuration parameter.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 164




<!-- PAGE 166 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.162: Configuration Properties Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|Parameter Number 2 (LSB)|
|Reserved|Reserved|Format|Format|Format|Size|Size|Size|
|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|
|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|
|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|
|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|
|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|



**Parameter** **Number** **(16** **bits)**

This field is used to advertise the actual configuration parameter.

CC:0070.03.0F.11.001 The first byte MUST carry the most significant byte of the 16 bit value.

CC:0070.03.0F.11.002 If this field advertises a non-existing parameter, a receiving node MUST advertise zero values in

CC:0070.03.0F.11.003 the Format and Size fields. The Next Parameter Number field MUST advertise the next available
configuration parameter.


Parameter numbers above 255 can only be addressed using the Bulk Set/Get Commands. Parameter
numbers in the range 1..255 can be addressed using either the Bulk Set/Get Commands or the Set/Get
Commands.


**Reserved**

CC:0070.03.0F.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Format** **(3** **bits)**

This field is used to advertise the format of the parameter.

CC:0070.03.0F.11.005 The value of this field MUST comply with Table 2.163.


Table 2.163: Configuration Properties Report::Format encoding

|Value|Parameter format and presentation|
|---|---|
|0x00|Signed Integer|
|0x01|Unsigned Integer|
|0x02|Enumerated (Radio buttons)<br>|
|0x03|Bit feld (Checkboxes)|



CC:0070.03.0F.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0070.03.0F.11.007 If the parameter format is “Unsigned integer”, normal binary integer encoding MUST be used.


CC:0070.03.0F.11.008 If the parameter format is “Signed integer”, the binary encoding MUST comply with Table 2.12.


CC:0070.03.0F.11.009 If the parameter format is “Enumerated”, the parameter MUST be treated as an unsigned integer.

CC:0070.03.0F.12.001 A graphical configuration tool SHOULD present this parameter as a series of radio buttons [21].

CC:0070.03.0F.11.00A If the parameter format is “Bit field” the parameter MUST be treated as a bit field where each
individual bit can be set or reset.


CC:0070.03.0F.12.002


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 165




<!-- PAGE 167 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A graphical configuration tool SHOULD present this parameter as a series of checkboxes [21].


**Size** **(3** **bits)**

This field is used to advertise the size of the actual parameter.


CC:0070.03.0F.11.00B
The advertised size MUST also apply to the fields “Min Value”, “Max Value”, “Default Value” carried
in this command.

CC:0070.03.0F.11.00C The value of this field MUST comply with Table 2.164.

|Size|Table 2.164: Configuration Properties Report::Size encoding Size of parameter|
|---|---|
|Size|Size of parameter<br>|
|0|0 bit (Unassigned parameter, Value felds omitted)|
|1|8 bit|
|2|16 bit|
|4|32 bit|



CC:0070.03.0F.11.00D All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Min** **Value** **(N** **bytes)**

CC:0070.03.0F.11.00E This field MUST advertise the minimum value that the actual parameter can assume.

CC:0070.03.0F.11.00F If the parameter is “Bit field”, this field MUST be set to 0.

CC:0070.03.0F.11.010 The size of the field MUST comply with the size advertised by the Size field. This field MUST be
omitted if the Size field is set to 0.

CC:0070.03.0F.11.011 The sign encoding MUST comply with the mode advertised by the Signed field.


**Max** **Value** **(N** **bytes)**

CC:0070.03.0F.11.012 This field MUST advertise the maximum value that the actual parameter can assume.

CC:0070.03.0F.11.013 If the parameter is “Bit field”, each individual supported bit MUST be set to ‘1’, while each
un-supported bit of MUST be set to ‘0’.

CC:0070.03.0F.12.003 A graphical configuration tool SHOULD NOT present checkboxes for un-supported bits.

CC:0070.03.0F.11.014 The size of the field MUST comply with the size advertised by the Size field. This field MUST be
omitted if the Size field is set to 0.

CC:0070.03.0F.11.015 The sign encoding MUST comply with the mode advertised by the Signed field.


**Default** **Value** **(N** **bytes)**

CC:0070.03.0F.11.016 This field MUST advertise the default value of the actual parameter.

CC:0070.03.0F.11.017 The size of the field MUST comply with the size advertised by the Size field. This field MUST be
omitted if the Size field is set to 0.

CC:0070.03.0F.11.018 The sign encoding MUST comply with the mode advertised by the Signed field.


**Next** **Parameter** **Number** **(16** **bits)**

Configuration parameter identifiers may be assigned in a non-sequential order.

CC:0070.03.0F.11.019 This field MUST advertise the next available configuration parameter.

The value 0x0000 MUST indicate that this is the last available configuration parameter.

CC:0070.03.0F.11.01A The first byte MUST carry the most significant byte of the 16 bit value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 166

---

<!-- PAGE 168 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.33** **Configuration** **Command** **Class,** **version** **4**


The Configuration Command Class, version 4 introduces the support of read-only parameters, parameters requiring network re-inclusion and advanced parameters as well as allows optional support for
Bulk Commands.

A read-only parameter can be accessed with Get commands but cannot be modified with Set Commands. A parameter requiring re-inclusion is typically a parameter altering the node capabilities,
which requires performing the inclusion again in order to have the controller to learn about the node
capabilities once more. A parameter may be advertised as “advanced” to indicate to the controlling
application that the actual parameter is intended only for advanced use, e.g. calibration.

The following commands are modified in version 4:

      - Configuration Set Command

      - Configuration Bulk Set Command

      - Configuration Properties Report Command


The following new command is introduced:

      - Configuration Default Reset Command


All commands not mentioned in this version remain unchanged from previous versions.


**2.2.33.1** **Compatibility** **considerations**


Configuration Command Class, version 4 is backwards compatible with the previous versions of Configuration Command Class.


CC:0070.04.00.21.001
A device supporting Configuration Command Class, version 4 MUST support Configuration Command
Class, version 3.


**2.2.33.1.1** **Multi** **Channel** **Consideration**


CC:0070.04.00.12.001 Multi Channel End Points SHOULD NOT support the Configuration Command Class.


**2.2.33.1.2** **“Default”** **flag**


Refer to Section 2.2.30.1.1.

CC:0070.04.00.21.002 From version 4 and onwards, a node MUST NOT reset all Configuration Parameters when receiving
a Set or Bulk Set Command with the default flag set to 1.


**2.2.33.1.3** **Configuration** **Properties** **Report**


Refer to Section 2.2.32.1.2.

The recommendation given in version 3 does not apply to version 4 supporting nodes as new fields
are appended at the end of the Configuration Properties Report Command in version 4.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 167




<!-- PAGE 169 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.33.1.4** **“Altering** **capabilities”** **flag**


Configuration parameters modifying a node’s and/or (non-dynamic) Multi Channel End Point capaCC:0070.04.00.21.003 bilities MUST be advertised as “Altering capabilities”.

CC:0070.04.00.21.004 When such a parameter is modified:


      A Z-Wave or Z-Wave Plus node MUST NOT advertise the new and/or Multi Channel End Point
capabilities before being excluded from its current network.


      - A Z-Wave Plus version 2 node MUST advertise its new capabilities immediately.


**2.2.33.1.5** **“Advanced”** **flag**


The difference between normal and advanced parameters lies on the controlling node side.

CC:0070.04.00.23.001 A parameter MAY be advertised as “advanced” in order to simplify the configuration of a node by
normally not showing such a parameter to the end user.


CC:0070.04.00.22.001 Advanced parameters SHOULD be presented to the user only when an [Advanced] option is selected
in the controller user interface.


**2.2.33.1.6** **Parameters** **value** **and** **network** **inclusion/exclusion**


CC:0070.04.00.21.005 From version 4 and onwards, a node MUST NOT modify or reset any configuration parameter when
being included or excluded of a Z-Wave network.

CC:0070.04.00.21.006 A node MUST reset all its configuration parameters if either:


      - It is manually reset to factory default

      - It receives a Configuration Default Reset Command.

CC:0070.04.00.21.007 A node MUST NOT reset all its configuration parameters in any other case.


**2.2.33.1.7** **Bulk** **commands** **support**


CC:0070.04.00.22.002 A node supporting Configuration Command Class, version 4 MAY elect to ignore the following Commands:

      - Configuration Bulk Set Command

      - Configuration Bulk Get Command

      - Configuration Bulk Report Command


CC:0070.04.00.21.008 If it is the case, the node MUST:


      - Return an Application Rejected Request Command when receiving one of the ignored commands
(if received without Supervision encapsulation)

      - Advertise that it ignores the Bulk Commands in the Configuration Properties Report


CC:0070.04.00.21.009 If Bulk Commands are supported, they MUST be supported for all parameters. If Bulk Commands
are ignored, they MUST be ignored for all parameters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 168




<!-- PAGE 170 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.33.2** **Configuration** **Set** **Command**


This command is used to set the value of a configuration parameter.


Table 2.165: Configuration Set Command, version 4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|Command = CONFIGURATION_SET|
|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|Parameter Number|
|Default|Reserved<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|Confguration Value 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|Confguration Value N|



CC:0070.04.04.11.001 A receiving node MUST ignore this command if the specified parameter is advertised as a Read-only
parameter.

All fields not specified below are unchanged from version 2 Configuration Set Command.


**Default** **(1** **bit)**

This field is used to specify if the default value is to be restored for the specified configuration
parameter.


CC:0070.04.04.11.002

The value 1 MUST indicate that default factory settings must be restored for the specified Parameter
CC:0070.04.04.11.003 Number. In this case, the Configuration value field MUST be ignored and any other parameters
MUST NOT be reset by a receiving node.

CC:0070.04.04.11.004 The value 0 MUST indicate that the specified Parameter Number MUST assume the value specified
by the Configuration Value field.

**Configuration** **Value** **(N** **bytes)**


CC:0070.04.04.11.005
This field carries the value to be assigned. The size of the field MUST comply with the size advertised
by the Size field.

CC:0070.04.04.11.006 The configuration value MUST be encoded according to the Format field advertised in the Configuration Properties Report Command for the parameter number.


**2.2.33.3** **Configuration** **Bulk** **Set** **Command**


This command is used to set the value of one or more configuration parameters.


Table 2.166: Configuration Bulk Set Command, version 4




|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|Command = CONFIGURATION_BULK_SET<br>|
|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|Parameter Ofset 1 (MSB)<br>|
|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|Parameter Ofset 2 (LSB)|
|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|Number of Parameters|
|Default|Hand- shake<br>|Reserved<br>|Reserved<br>|Reserved<br>|Size<br>|Size<br>|Size<br>|
|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|Parameter 1 - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|Parameter 1 - Confguration Value N (LSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|Parameter M - Confguration Value 1 (MSB)|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|Parameter M - Confguration Value N (LSB)|



CC:0070.04.07.11.001



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 169




<!-- PAGE 171 -->

CC:0070.04.07.11.002


CC:0070.04.07.11.003



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A receiving node MUST ignore this command for parameters that are advertised as Read-only pa
rameters.

All fields not specified below are unchanged from version 2 Configuration Bulk Set Command.


**Default** **(1** **bit)**

This field is used to specify if the default value is to be restored for the specified configuration
parameters.


The value 1 MUST indicate that default factory settings must be restored for all the Parameter Numbers defined by the Parameter Offset and Number of Parameters fields. In this case, the Configuration
Value field MUST be ignored and any other parameters MUST NOT be reset by a receiving node.



CC:0070.04.07.11.004 The value 0 MUST indicate that the specified Parameter Numbers MUST assume the value specified
by the Configuration Value field.

**Parameter** **-Configuration** **Value** **(M*N** **bytes)**

CC:0070.04.07.11.005 These fields carry the parameter values to be assigned. Each parameter value field MUST have the
same size. The size of each field MUST comply with the size advertised by the Size field.


CC:0070.04.07.11.006
The values MUST be encoded according to the Format field advertised in the Configuration Properties
Report Command for each parameter number.


**2.2.33.4** **Configuration** **Properties** **Report** **Command**


This command is used to advertise the properties of a configuration parameter.


Table 2.167: Configuration Properties Report Command, version












|Tab 4 7|ble 2.167: Co 6|onfiguratio 5|on Propert 4|ties Repor 3|rt Comma 2|and, version 1|0|
|---|---|---|---|---|---|---|---|
|**7**|**6**|**5**|**4**|**3**|**2**|**1**|**0**|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|Command = CONFIGURATION_PROPERTIES_REPORT|
|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|Parameter Number 1 (MSB)|
|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|Parameter Number 2 (MSB)|
|Altering<br>capabilities|Read-<br>only|Format|Format|Format|Size|Size|Size|
|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|Min Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|Min Value N (LSB)|
|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|Max Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|Max Value N (LSB)|
|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|Default Value 1 (MSB)|
|…|…|…|…|…|…|…|…|
|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|Default Value N (LSB)|
|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|Next Parameter Number 1 (MSB)|
|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|Next Parameter Number 2 (LSB)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|No Bulk<br>support|Ad-<br>vanced|



All fields not specified below are unchanged from version 3 Configuration Properties Report Command.


**Read-only** **(1** **bit)**

This field is used to indicate if the parameter is read-only.


CC:0070.04.0F.11.001 The value 1 MUST indicate that the advertised parameter is read-only.


CC:0070.04.0F.11.002 The value 0 MUST indicate that the advertised parameter is not read-only.


**Altering** **capabilities** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 170




<!-- PAGE 172 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate if the advertised parameter triggers a change in the node’s capabilities.


CC:0070.04.0F.11.003 The value 1 MUST indicate that the advertised parameter alters the node capabilities when being
changed.


CC:0070.04.0F.11.004 The value 0 MUST indicate that the advertised parameter does not alter the node capabilities when
being changed.

Refer to Section 2.2.33.1.4 “Altering capabilities” flag.


**Advanced** **(1** **bit)**

This field is used to indicate if the advertised parameter is to be presented in the “Advanced” parameter
section in the controller GUI.


CC:0070.04.0F.11.005 The value 1 MUST indicate that the advertised parameter is an Advanced parameter.


CC:0070.04.0F.11.006 The value 0 MUST indicate that the advertised parameter is not an Advanced parameter.


**No** **Bulk** **support** **(1** **bit)**

This field is used to advertise if the sending node supports Bulk Commands.


CC:0070.0F.11.007 The value 1 MUST indicate that the Bulk Commands will be ignored by the sending node.


CC:0070.0F.11.008 The value 0 MUST indicate that the Bulk Commands are supported by the sending node

CC:0070.0F.11.009 A sending node MUST always advertise the same value in this field, regardless of the parameter
number.


**2.2.33.5** **Configuration** **Default** **Reset** **Command**


This command is used to reset all configuration parameters to their default value.


Table 2.168: Configuration Default Reset Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|Command Class = COMMAND_CLASS_CONFIGURATION|
|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|Command = CONFIGURATION_DEFAULT_RESET|



CC:0070.04.01.11.001 A node receiving this command MUST reset all its Configuration Parameters to their default value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 171