<!-- PAGE 821 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.2** **Multi** **Channel** **Command** **Class,** **version** **3** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class.


New implemenetations MUST use the _Multi Channel Command Class,_ _version 4_, or newer instead.


The Multi Channel command class is used to address one or more End Points in a Multi Channel

device.


Refer to Section 4.1.3 for an introduction to the Multi Channel concept.


**4.2.2.1** **Compatibility** **Considerations**


CC:0060.03.00.23.001 A Multi Channel device MAY implement from 1 to 127 End Points.


CC:0060.03.00.21.002 A Multi Channel device MUST implement all application functionality in End Points.


CC:0060.03.00.21.003 End Point 1 MUST implement the primary application functionality of the actual Multi Channel
device.


CC:0060.03.00.23.002 Additional End Points MAY implement an identical functionality; as an example, a power strip may
implement five End Points (one for each outlet) with identical functionality.


CC:0060.03.00.21.004 For backwards compatibility, the Root Device MUST mirror the application functionality of End Point
1.


CC:0060.03.00.23.003 Further, the Root Device MAY mirror the application functionalities of additional End Points. As an
example, Basic Off and On commands for the Root Device may control all outlets of a power strip
with five outlets.


CC:0060.03.00.21.005 With the exception of dynamic End Points, the Root Device MUST advertise all End Point functionality which is mirrored by the Root Device.


CC:0060.03.00.22.001 The Root Device SHOULD NOT advertise the application functionality of any dynamic End Point.



CC:0060.03.00.21.006


CC:0060.03.00.22.003



The Root Device of a Multi Channel device MUST only advertise application functionality that can be
reached via one or more End Points. However, if the node supports the following Command Classes,
they SHOULD only be supported and advertised by the Root Device:


 - Central Scene Command Class

 - Configuration Command Class


 - Anti-Theft Command Class


 - Anti-Theft Unlock Command Class


 - Clock Command Classes


 - Geographic Location Command Class



CC:0060.03.00.21.007 It MUST NOT be possible to limit the functionality, or enable non-compliant behavior of any End
Point in the device by sending a command to the Root Device.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 820




<!-- PAGE 822 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.2.1.1** **Node** **information** **Frame** **(NIF)**


CC:0060.03.00.21.001 A node supporting this Command Class MUST set the Optional Functionality bit in its NIF.


CC:0060.03.00.21.00C Multi Channel Root Devices MUST advertise their non-secure capabilities via the NIF.


CC:0060.03.00.21.00D Multi Channel End Points MUST advertise their non-secure capabilities via the Multi Channel Capability Report Command.


CC:0060.03.00.21.00E Security bootstrapped nodes MUST advertise their capabilities using security encapsulation (for both
Root Devices and End Points) via the S0 Security Commands Supported Report Command or the S2
Security 2 Commands Supported Report Command.


Secure End Point capabilities are therefore requested using the following encapsulation:


      - S0/S2 Encapsulation


      - Multi Channel Encapsulation


      - S0/S2 Commands Supported Get/Report Commands


**4.2.2.1.2** **Dynamic** **End** **Point** **considerations**


**DYNAMIC** **END** **POINTS** **HAVE** **BEEN** **OBSOLETED**


Dynamic End Points have been obsoleted. New implementation MUST use dynamic capabilities.


A node may add and/or remove End Points based on a user action, such as changing configuration parameters or the physical addition/removal of a module. When this happen,
the node SHOULD treat such behavior as dynamic capabilities [For details, refer to _Dy-_
_namic Capabilities and Node Discovery_ ] and notify the End Point modification capabilities
to the lifeline destinations.


CC:0060.03.00.23.004 An End Point MAY be dynamic. Dynamic End points are intended End Points able to change their
capabilities or that can be added and removed from a Multi Channel device.

CC:0060.03.00.22.002 When creating a new dynamic End Point, it SHOULD be assigned an End Point identifier which has
not been used recently to allow applications to discover the removal of a dynamic End Point.


CC:0060.03.00.21.009 When a dynamic End Point is removed, all other End Points MUST maintain their current End Point
identifiers.


CC:0060.03.00.23.005 A supporting device implementing dynamic End Points MAY advertise the creation, change or removal
of a dynamic End Point via the Root Device Lifeline association group by issuing a Multi Channel
Capability Report.


CC:0060.03.00.21.00A A node MUST NOT advertise changes to dynamic End Points via broadcast transmission. A receiving
node MUST ignore such broadcasted advertisements.


CC:0060.03.00.21.00B After advertising the removal, a removed dynamic End Point MUST ignore all commands.


**4.2.2.2** **Interoperability** **considerations**



CC:0060.03.00.53.001


CC:0060.03.00.51.001



A controlling node MAY use Multi Channel Encapsulation Command to communicate with Multi
Channel End Points in other nodes. If such a controlling node does not implement any End Points,
it MUST NOT advertise the Multi Channel Command Class in its Node Information Frame (NIF) or
S0/S2 Commands Supported Report Command.


An example of such device would be a controller or gateway which can control End Points in other
supporting nodes via commands from the Root Device of the gateway. Likewise, the Root Device of
the gateway may receive unsolicited commands from other nodes End Points.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 821




<!-- PAGE 823 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.2.3** **Multi** **Channel** **End** **Point** **Get** **Command**


This command is used to query the number of End Points implemented by the receiving node.


CC:0060.03.07.11.001 The Multi Channel End Point Report Command MUST be returned in response to this command.


CC:0060.03.07.51.001 This command MUST NOT be issued via multicast addressing.


CC:0060.03.07.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|Command = MULTI_CHANNEL_END_POINT_GET (0x07)|



**4.2.2.4** **Multi** **Channel** **End** **Point** **Report** **Command**


This command is used to advertise the number of End Points implemented by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|
|Dynamic|Identical|Res|Res|Res|Res|Res|Res|
|Res|End Points|End Points|End Points|End Points|End Points|End Points|End Points|



**Dynamic** **(1** **bit)**

This field is used to advertise if the node implements a dynamic number of End Points.


CC:0060.03.08.11.001 The value 1 MUST be used to indicate that the number of End Points is dynamic.


The value 0 MUST be used to indicate that the number of End Points is static.


**Identical** **(1** **bit)**

This field is used to advertise if all end points have identical capabilities


CC:0060.03.08.11.002
This bit MUST be set to 1 if all End Points advertise the same Generic and Specific Device Class and
support the same Command Classes.


CC:0060.03.08.11.003 This bit MUST be set to 0 if End Points do not advertise the same Device Class or Command Class

information.


**Res**

CC:0060.03.08.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**End** **Points** **(7** **bits)**

This field is used to advertise the number of End Points implemented by the sending node.

CC:0060.03.08.11.005 This field MUST be in the range 1..127.

CC:0060.03.08.11.006 If the sending node implements dynamic End Points, this field MUST advertise the number of End

CC:0060.03.08.13.001 Points currently instantiated by the node. A dynamic End Point MAY be assigned any End Point
identifier in the range 2..127.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 822




<!-- PAGE 824 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.2.5** **Multi** **Channel** **Capability** **Get** **Command**


This command is used to query the non-secure Command Class capabilities of an End Point.


CC:0060.03.09.11.001 The Multi Channel Capability Report Command MUST be returned in response to this command
unless it is to be ignored.


CC:0060.03.09.51.001 This command MUST NOT be issued via multicast addressing.


CC:0060.03.09.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


**Res**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|Command = MULTI_CHANNEL_CAPABILITY_GET (0x09)|
|Res|End Point|End Point|End Point|End Point|End Point|End Point|End Point|


CC:0060.03.09.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**End** **Point** **(7** **bits** )

CC:0060.03.09.11.004 This field MUST specify the End Point for which the capabilities MUST be returned.

CC:0060.03.09.11.005 If the specified End Point does not exist, this command MUST be ignored.

If the specified End Point represents a removed dynamic End Point, this command MUST be ignored.


**4.2.2.6** **Multi** **Channel** **Capability** **Report** **Command**


This command is used to advertise the Generic and Specific Device Class and the supported command
classes of an End Point.


CC:0060.03.0A.11.002 When advertising the removal of a dynamic End Point, this command MUST carry the following
values:


      - Dynamic MUST be set to 1

      - End Point MUST be set to the actual End Point identifier


      - Generic Device Class MUST be set to 0xFF (GENERIC_TYPE_NON_INTEROPERABLE)

      - Specific Device Class MUST be set to 0x00 (SPECIFIC_TYPE_NOT_USED)

CC:0060.03.0A.11.003 - The Command Class field MUST be omitted.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|Command = MULTI_CHANNEL_CAPABILITY_REPORT (0x0A)|
|Dynamic|End Point|End Point|End Point|End Point|End Point|End Point|End Point|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1|Command Class 1|Command Class 1|Command Class 1|Command Class 1|Command Class 1|Command Class 1|Command Class 1|
|…|…|…|…|…|…|…|…|
|Command Class N|Command Class N|Command Class N|Command Class N|Command Class N|Command Class N|Command Class N|Command Class N|



**Dynamic** **(1** **bit)**

This field is used to advertise if the advertised End Point is dynamic.

CC:0060.03.0A.11.001 This field MUST be set to 1 if this is a dynamic End Point.

This field MUST be set to 0 to indicate that this is a static End Point.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 823




<!-- PAGE 825 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**End** **Point** **(7** **bits)**

CC:0060.03.0A.11.004 This field MUST advertise the actual End Point for which the capabilities are advertised.


**Generic** **Device** **Class** **(8** **bits)**

CC:0060.03.0A.11.005 This field MUST carry the Generic Device Class of the advertised End Point. For a detailed description
of all available Generic Device Classes, refer to [34] and Section 7 for Z-Wave Plus nodes.

**Specific** **Device** **Class** **(8** **bits)**

CC:0060.03.0A.11.006 This field MUST carry the Specific Device Class of the advertised End Point. For a detailed description
of all available Specific Device Classes, refer to [34] and Section 7 for Z-Wave Plus nodes.


**Command** **Class** **(N** **bytes)**

This field is used to advertise the non-secure supported Command Classes by the actual End Point.

CC:0060.03.0A.11.007 This field MUST be omitted if the advertised End Point does not exist or have been removed. The
number of Command Class bytes MUST be determined from the length of the frame.

CC:0060.03.0A.11.009 This field MUST represent the capabilities of an End Point with no security encapsulation.


CC:0060.03.0A.11.008 The Multi Channel Command Class MUST NOT be advertised in this list.


CC:0060.03.0A.11.00A Non-secure End Point capabilities MUST also be supported securely and MUST also be advertised in
the S0/S2 Commands Supported Report Commands unless they are encapsulated outside Security or
Security themselves.


CC:0060.03.0A.11.00B Nodes supporting S0 MUST advertise S0 as supported for each End Point that can be addressed with
S0 encapsulation


CC:0060.03.0A.11.00C Nodes supporting S2 MUST support addressing every End Point with S2 encapsulation and MAY
explicitly list S2 in the non-secure End Point capabilities.


**4.2.2.7** **Multi** **Channel** **End** **Point** **Find** **Command**


This command is used to request End Points having a specific Generic or Specific Device Class in End
Points.


CC:0060.03.0B.11.001 The Multi Channel End Point Find Report Command MUST be returned in response to this command.


CC:0060.03.0B.51.001 This command MUST NOT be issued via multicast addressing.


CC:0060.03.0B.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|Command = MULTI_CHANNEL_END_POINT_FIND (0x0B)|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|



**Generic** **Device** **Class** **(8** **bits)**

CC:0060.03.0B.11.003 This field MUST indicate the receiving node to return the list of End Points having the specified
Generic Device Class.

CC:0060.03.0B.11.004 The value 0xFF MUST indicate that all existing End Points MUST be returned. If this field is set to
0xFF, the Specific Device Class field MUST also be set to 0xFF.

**Specific** **Device** **Class** **(8** **bits)**

CC:0060.03.0B.11.005 This field MUST indicate the receiving node to return the list of End Point having the specified
Specific Device Class.


CC:0060.03.0B.11.006


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 824




<!-- PAGE 826 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0xFF MUST indicate that the list of all End Points having the specified Generic Device
Class MUST be returned.


**4.2.2.8** **Multi** **Channel** **End** **Point** **Find** **Report** **Command**


This command is used to advertise End Points that implement a given combination of Generic and
Specific Device Classes.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|Command = MULTI_CHANNEL_END_POINT_FIND_REPORT (0x0C)|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Res|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|
|…|…|…|…|…|…|…|…|
|Res|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|



**Reports** **to** **Follow** **(8** **bits)**

This field is used if multiple Report Commands are necessary for returning all the requested End
Points.

CC:0060.03.0C.11.001 This field MUST advertise the number of Multi Channel End Point Find Report Command following
the actual frame.


**Generic** **Device** **Class** **(8** **bits)**

This field is used to advertise the Generic Device Class of all advertised End Points in this command.

CC:0060.03.0C.11.002 The value 0xFF MUST be advertised if this value was specified in the Multi Channel End Point Find
Command.

If 0xFF is advertised, the _Specific_ _Device_ _Class_ field MUST also advertise the value 0xFF.

CC:0060.03.0C.13.001 If the value 0xFF is advertised, the advertised End Points MAY implement different Generic and
Specific Device Classes.

**Specific** **Device** **Class** **(8** **bits)**

This field is used to advertise the Specific Device Class of all advertised End Points in this command.

CC:0060.03.0C.13.002 If the value 0xFF is advertised, the advertised End Points MAY implement different specific device
classes.

CC:0060.03.0C.11.004 This field MUST be set to 0xFF if the _Generic_ _Device_ _Class_ field is set to 0xFF.


**Res**

CC:0060.03.0C.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**End** **Point** **(N** ***** **7** **bits)**

This field is used to advertise the list of End Point identifier(s) that matches the advertised Generic
and Specific Device Class values.


CC:0060.03.0C.11.006
If no End Point matches the advertised Generic Device Class and/or Specific Device Class, the sending
node MUST set this field to 0x00 and this field’s size MUST be 7 bits (only 1 list entry).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 825




<!-- PAGE 827 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.2.9** **Multi** **Channel** **Command** **Encapsulation**


This command is used to encapsulate commands to or from a Multi Channel End Point.


CC:0060.03.0D.11.001 The Multi Channel Command Encapsulation Command MUST NOT carry Source End Point and
Destination End Point fields that are both zero.


CC:0060.03.0D.13.001 A receiving node MAY respond to a Multi Channel encapsulated command if the Destination End

CC:0060.03.0D.11.002 Point field specifies a single End Point. In that case, the response MUST be Multi Channel encapsulated.


CC:0060.03.0D.11.003 A receiving node MUST NOT respond to a Multi Channel encapsulated command if the Destination
End Point field specifies multiple End Points via bit mask addressing.


CC:0060.03.0D.11.004 A node MUST NOT return a Multi Channel Encapsulated command in response to a non-encapsulated
command.


**Res**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|Command = MULTI_CHANNEL_CMD_ENCAP (0x0D)|
|Res|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|
|Bit address|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|
|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|Command Class (1 or 2 bytes)|
|Command|Command|Command|Command|Command|Command|Command|Command|
|Parameter 1|Parameter 1|Parameter 1|Parameter 1|Parameter 1|Parameter 1|Parameter 1|Parameter 1|
|…|…|…|…|…|…|…|…|
|Parameter N|Parameter N|Parameter N|Parameter N|Parameter N|Parameter N|Parameter N|Parameter N|


CC:0060.03.0D.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Source** **End** **Point** **(7** **bits)**

This field is used to advertise the originating End Point. The Source End Point MUST be in the
range 0..127.


CC:0060.03.0D.11.007 The value 0 MUST indicate that the encapsulated command is issued by the Root Device.

Values in the range 1…127 MUST indicate the actual End Point identifier which issues the encapsulated
command.

CC:0060.03.0D.11.008 This field MUST be set to a different value than 0 if the _Destination_ _End_ _Point_ field is set to 0.


CC:0060.03.0D.11.009 A node returning a response to a Multi Channel encapsulated command MUST swap the Source and
Destination End Point identifiers in this command.

CC:0060.03.0D.11.00A This field MUST be set to 0 if a sending node does not implement Multi Channel End Points or if
the Root Device of the Multi Channel device is issuing a command.


**Bit** **address** **(1** **bit)**

This bit is used to advertise if the destination End Point is specified as a bit mask.

CC:0060.03.0D.11.00B The value 1 MUST indicate that the Destination End Point field is specified as a bit mask.

The value 0 MUST indicate that the Destination End Point field is specified as an End Point identifier.


**Destination** **End** **Point** **(7** **bits)**

This field is used to advertise the destination End Point.

CC:0060.03.0D.11.00C This field MUST be interpreted based on the “Bit address” value.

CC:0060.03.0D.11.00D If the Bit Address field is set to 0, the Destination End Point field MUST carry a single End Point
identifier value in the range 0..127.

CC:0060.03.0D.11.00E If the Bit Address field is set to 1, the Destination End Point MUST use the following encoding:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 826




<!-- PAGE 828 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - Bit 0 in the Destination End Point indicates if End Point 1 is a destination


      - Bit 1 in the Destination End Point indicates if End Point 2 is a destination


      - …


CC:0060.03.0D.11.00F The bit value 0 MUST be used to advertise that the corresponding End Point is not a destination.


The bit value 1 MUST be used to advertise that the corresponding End Point is a destination.


**Command** **Class** **(8** **bits** **or** **16** **bits)**

CC:0060.03.0D.11.011 This field MUST specify the Command Class identifier of the encapsulated Command. This field
MUST carry a normal Command Class (8 bits) or an Extended Command Class (16 bits)


**Command** **(8** **bits)**

CC:0060.03.0D.11.012 This field MUST specify the Command identifier of the encapsulated command.


**Parameter** **(N** **bytes)**

CC:0060.03.0D.11.010 This field MUST carry the payload of the encapsulated command. The length of this field MUST be
determined from the Z-Wave frame length.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 827

---

<!-- PAGE 829 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.3** **Multi** **Channel** **Command** **Class,** **version** **4**


The Multi Channel Command Class is used to address one or more End Points in a Multi Channel

device.


Refer to Section 4.1.3 for an introduction to the Multi Channel concept.


**4.2.3.1** **Compatibility** **Considerations**


CC:0060.04.00.21.001 Compatibility considerations requirements from version 3 MUST also be observed by a version 4
supporting node. Refer to Section 4.2.2.1 Compatibility considerations.


CC:0060.04.00.21.002 Multi Channel Command Class, version 4 is backwards compatible with Multi Channel Command
Class, version 3. Fields and commands not described in this version MUST remain unchanged from
version 3.


**AGGREGATED** **END** **POINTS** **HAVE** **BEEN** **DEPRECATED**


Aggregated End Points have been deprecated. It is RECOMMENDED to issue multiple
report back-to-back if data from several End Points at a precise time needs to be reported.


Additionally, it is RECOMMENDED to aggregate all sensors functionalities at the Root
device. i.e. accumulated readings for all End Points SHOULD be advertised via the Root
Device.


The Multi Channel Command Class, version 4 introduces Aggregated End Points. Aggregated End
Points are assigned End Point identifiers following immediately after the identifiers allocated to individual End Points. Thus:


      - Aggregated End Points are invisible to devices supporting Multi Channel Command Class,
version 3 or older.


      - Individual End Points are identical in version 3 and version 4.


      - A version 3 controlling node can discover and control individual End Points.


      - A version 4 controlling node can discover and control individual End Points and Aggregated
End Points.


**4.2.3.2** **Interoperability** **Considerations**


CC:0060.04.00.31.001 Interoperability considerations from version 3 MUST also apply in this version.


Refer to Section 4.2.2.2 Interoperability considerations


**4.2.3.2.1** **Aggregated** **End** **Point** **design** **principles**


CC:0060.04.00.31.002 An **Aggregated** **End** **Point** MUST implement a function which relates to multiple individual End
Points.


CC:0060.04.00.31.003 An Aggregated End Point MUST NOT forward commands to individual End Points. In other words,
communication to a number of individual End Points MUST be done via multiple singlecast commands
or via bit mask addressing.


CC:0060.04.00.31.004 A command issued to an Aggregated End Point MUST NOT cause any individual End Point to return
a command in response.

CC:0060.04.00.31.005 Aggregated End Point MUST be assigned End Point identifiers from a continuous range starting
immediately after the last individual End Point.


CC:0060.04.00.31.006 An Aggregated End Point MUST NOT support other Command Classes and types than the ones
explicitly listed in Table 4.2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 828




<!-- PAGE 830 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 4.2: Aggregated End Point Command Class support

|Command Class|Type|Measurement Mode|
|---|---|---|
|Meter|Electricity|Instant, Accumulated|
|Meter|Gas|Instant, Accumulated|
|Meter|Water|Instant, Accumulated|
|Multilevel Sensor|Power|Instant|
|Multilevel Sensor|Current<br>|Instant|
|Multilevel Sensor|Air fow|Instant|
|Multilevel Sensor|Tank Capacity|Instant|



**4.2.3.2.2** **Dynamic** **End** **Point** **considerations**


In the case a node implements both Dynamic and Aggregated End Points, the Aggregated End Points
identifiers will vary accordingly to the last active dynamic End Point. An illustration is given in
Figure 4.2.


Figure 4.2: Static, dynamic and aggregated End Point layout example


**4.2.3.3** **Multi** **Channel** **End** **Point** **Report** **Command**


This command is used to advertise the number of Multi Channel End Points and other relevant Multi

Channel attributes.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|Command = MULTI_CHANNEL_END_POINT_REPORT (0x08)|
|Dynamic|Identical|Res|Res|Res|Res|Res|Res|
|Res|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|
|Res|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|



CC:0060.04.08.11.001 Fields not described below MUST remain unchanged from version 3. Refer to Section 4.2.2.4 _Multi_
_Channel_ _End_ _Point_ _Report_ _Command_ .


**Res**

CC:0060.04.08.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Individual** **End** **Points** **(7** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 829




<!-- PAGE 831 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the number of individual End Points implemented by the sending node.

CC:0060.04.08.11.003 This field MUST be in the range 1..127.


**Aggregated** **End** **Points** **(7** **bits)**

CC:0060.04.08.11.004 If the sending node implements dynamic End Points, this field MUST advertise the number of End

CC:0060.04.08.13.001 Points currently instantiated by the node. A dynamic End Point MAY be assigned any End Point
identifier in the range 2..127.

CC:0060.04.08.11.005 The sum of the values advertised by this field and the _Aggregated_ _End_ _Points_ field MUST be in the
range 1..127.


**4.2.3.4** **Multi** **Channel** **Capability** **Get/Report** **Commands**


These commands are unchanged in version 4.


Aggregated End Points SHOULD reply to this command and to the S2/S0 Supported Get Commands.

Aggregated End Points SHOULD set the Generic and Specific Device Class field to an identical value
to one of the Individual End Point it aggregates.


The list of supported Application Command Classes at the highest security level MUST only comprise
these Command Classes:


      - Meter Command Class


      - Multilevel Sensor Command Class.


**4.2.3.5** **Multi** **Channel** **Capability** **Find** **Report** **Commands**


This command is unchanged in version 4.


Aggregated End Points MUST NOT be advertised in the list of End Points returned for any
Generic/Specific Device Type.


**4.2.3.6** **Multi** **Channel** **Aggregated** **Members** **Get** **Command**


This command is used to query the members of an Aggregated End Point.


CC:0060.04.0E.11.001 The Multi Channel Aggregated Members Report MUST be returned in response to this command.


CC:0060.04.0E.51.001 This command MUST NOT be issued via multicast addressing.


CC:0060.04.0E.11.002 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x0E)|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|



**Res**

CC:0060.04.0E.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Aggregated** **End** **Point** **(7** **bits)**


CC:0060.04.0E.11.004
This field MUST specify the Aggregated End Point identifier for which the aggregated members MUST
be returned.


CC:0060.04.0E.11.005 The value MUST be in the range of advertised Aggregated End Points. If the value does not indicate
valid aggregated End Point identifier, a receiving node MUST return a response with the _Number_ _of_
_Bit_ _Masks_ field set to zero.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 830




<!-- PAGE 832 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.3.7** **Multi** **Channel** **Aggregated** **Members** **Report** **Command**


This command is used to advertise the members of an Aggregated End Point.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|Command = MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0F)|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|
|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|
|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|Aggregated Members Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|Aggregated Members Bit Mask N|



**Res**

CC:0060.04.0F.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Aggregated** **End** **Point** **(7** **bits)**

This field is used to advertise the Aggregated End Point identifier for which the members are advertised
in this command.


**Number** **of** **Bit** **Masks** **(8** **bits)**

This field is used to advertise the length in bytes of the _Aggregated_ _Member_ _Bit_ _Mask_ field.

CC:0060.04.0F.11.002 The value 0 MUST indicate that the Aggregated Members Bit Mask field is MUST be omitted.

Values in the range 1..255 MUST indicate the length of the _Aggregated_ _Members_ _Bit_ _Mask_ field in
bytes.


**Aggregated** **Members** **Bit** **Mask** **(N** **bytes)**

This field is used to advertise the End Point members of the actual Aggregated End Point.

CC:0060.04.0F.11.003 The length of this field in bytes MUST be according to the _Number_ _of_ _Bit_ _Masks_ field value.

This field MUST be treated as a bit mask and MUST use the following encoding for advertising
members:


      - Bit 0 in Bit Mask 1 indicates if End Point 1 is a member


      - Bit 1 in Bit Mask 1 indicates if End Point 2 is a member


      - …


CC:0060.04.0F.11.004 The bit value 0 MUST be used to advertise that the corresponding End Point is not a member.


The bit value 1 MUST be used to advertise that the corresponding End Point is a member.

CC:0060.04.0F.11.005 The first byte of this field MUST represent End Points 1..8.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 831