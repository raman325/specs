<!-- PAGE 732 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33** **Multi** **Channel** **Association** **Command** **Class,** **version** **2** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class.


New implemenetations MUST use the _Association_ _Command_ _Class,_ _version_ _3_, or newer instead.


The Multi Channel Association Command Class is used to manage associations to Multi Channel End
Point destinations as well as to NodeID destinations.

An association group sends an unsolicited command to the configured destinations when triggered by
an event. The parameters of the command may be dynamic, e.g. the temperature of a sensor reading
or the light level for a dimmer.

A NodeID association identifies its destination by a NodeID.

An End Point association identifies its destination by a combination of a NodeID and an End Point.


Refer to Section 4 for an introduction to the Multi Channel concept.


**3.2.33.1** **Compatibility** **considerations**


The Multi Channel Association Command Class extends the functionality of the Association command
CC:008E.02.00.21.001 class. A device supporting this Command Class version MUST also support the (non-Multi Channel)
Association Command Class, version 2.


CC:008E.02.00.22.001 A controlling device SHOULD NOT create End Point associations to dynamic Multi Channel End
Points.


CC:008E.02.00.22.002 The Association Group Information (AGI) Command Class SHOULD be supported to enable automated discovery of association group properties.


CC:008E.02.00.21.002 The Association and Multi Channel Association Command Classes MUST access the same collection

of association groups. Further, the following applies:


CC:008E.02.00.21.003 The two command classes MUST advertise the total number of association groups.


CC:008E.02.00.21.004 The two command classes MUST advertise the total number of supported nodes for a given association

group.


CC:008E.02.00.21.005 Any advertised association group MUST support NodeID destinations as well as End Point destina
tions.


CC:008E.02.00.21.006 NodeID associations maintained via the Multi Channel Association Command Class MUST be iden
tical to NodeID associations maintained via the Association Command Class.



CC:008E.02.00.21.007


CC:008E.02.00.23.001



The Multi Channel Command Class specifies that, for backwards compatibility with non-Multi Channel devices, the Root Device of a Multi Channel device MUST mirror the functionality of End Point
1 and it MAY mirror the functionality of more End Points. This principle also applies to association
groups advertised by the Root Device.



CC:008E.02.00.22.003 Each association group advertised by the Root Device, except for association group 1, SHOULD
mirror an association group of an End Point.


CC:008E.02.00.22.004 If a Root Device association group mirrors an End Point association group, the Root Device SHOULD
map all Association commands for that group to the mirrored End Point association group.


Except for association group 1 (the Z-Wave Plus Lifeline), a Multi Channel aware controlling device
CC:008E.02.00.22.005 SHOULD ignore all Root Device association groups since they are just mirrored End Point association

groups.


CC:008E.02.00.21.008 The use of encapsulation MUST comply with Table 3.128.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 731




<!-- PAGE 733 -->

|Table 3.128: V2 Associations and ger Source -> Destination|the Transmission Association|ns they may Trig- Allowed Transmissions|
|---|---|---|
|Source -> Destination|Association<br>Type|Allowed Transmissions|
|NodeID -> NodeID (V2)|NodeID|Non-encapsulated|
|End Point -> NodeID (V2)|NodeID|Non-encapsulated|
|NodeID -> End Point (V2)|End Point|Encapsulated *) (src0, dst>0)|
|End Point -> End Point (V2)|End Point|Encapsulated (src>0, dst>0)|
|**REMOVED** NodeID -> Root Device|End Point|_None_ **)|



CC:008E.02.00.11.001


CC:008E.02.00.13.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 3.128: V2 Associations and the Transmissions they may Trig

*) The source End Point MAY be different than 0 if the associated group is an End Point group
mapped to the Root Device


**) Version 2 of this command class does not allow the destination End Point to be zero.


**3.2.33.2** **Z-Wave** **Plus** **considerations**


The Z-Wave Plus certification program mandates that Association group 1 is reserved for the Lifeline
association group. Group 1 MUST NOT be assigned to any other use than the Lifeline group. The
actual Device Type specifies a mandatory list of commands which the device must be able to send to
all lifeline group destinations. A manufacturer MAY add additional commands to the lifeline group.



CC:008E.02.00.12.001 End Points SHOULD NOT implement the Lifeline Association Group. End Points SHOULD report
that zero NodeIDs are supported for association group 1.

The Z-Wave Plus certification program mandates support for the Association Group Information
(AGI) Command Class if a device supports the Multi Channel Association Command Class.


**3.2.33.3** **Security** **considerations**


CC:008E.02.00.41.001 A node that is included securely MUST NOT accept Association commands unless the commands are
received via the highest security key assigned to the device.


CC:008E.02.00.41.002 A supporting node issuing commands via association groups MUST send those commands with its
highest granted Security Class.


CC:008E.02.00.42.001 A supporting node issuing Set or Report type commands via association groups SHOULD use Supervision encapsulation only if sending commands with S2 (or higher security) encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 732




<!-- PAGE 734 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.4** **Multi** **Channel** **Association** **Set** **Command**


This command is used to request that one or more destinations are added to a given association group.


CC:008E.02.01.13.001 The destinations MAY be a mix of NodeID destinations and End Point destinations.

CC:008E.02.01.12.001 The receiving node SHOULD add the specified destinations to the specified association group.


CC:008E.02.01.13.002 This command MAY be ignored if the association group is already full.


CC:008E.02.01.11.001 Routing end nodes MUST have return routes assigned to all association destinations.


Table 3.129: Multi Channel Association Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|
|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|
|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|
|Bit Address<br>1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|
|…|…|…|…|…|…|…|…|
|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|
|Bit Address<br>N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|



**Grouping** **Identifier** **(8** **bits)**

CC:008E.02.01.11.002 This field is used to specify the actual association group. Grouping Identifiers MUST be assigned in
a consecutive range starting from 1.

CC:008E.02.01.11.003 A node that receives an unsupported Grouping Identifier MUST ignore this command


**NodeID** **(M** **bytes)**

This field specifies a list of NodeID destinations that are to be added to the specified association group
as a NodeID association.

CC:008E.02.01.11.004 A NodeID association created via this field MUST be identical to a NodeID association created with
the (non-Multi Channel) Association Set command.


**Marker** **(8** **bits)**



CC:008E.02.01.11.005


CC:008E.02.01.13.003



This field is used to indicate the end of NodeID destinations and the start of End Point destinations.
The Marker field MUST be set to the value MULTI_CHANNEL_ASSOCIATION_SET_MARKER.
The field MAY be omitted if no End Point destinations are specified.


**Multi** **Channel** **NodeID** **(N** **bytes)**

The Multi Channel NodeID, Bit Address and End Point fields specify a list of End Points which are
to be added to the specified association group as an End Point association.



The complete identification of an End Point destination requires a NodeID as well as an End Point
CC:008E.02.01.13.004 identifier. This command MAY carry multiple copies of the same Multi Channel NodeID in combination with different End Point identifiers.


**Bit** **Address** **+** **End** **Point** **(N** **bytes)**

CC:008E.02.01.11.006 These fields MUST be processed in combination with the Multi Channel NodeID field.

CC:008E.02.01.12.005 The receiving node SHOULD treat the Bit Address flag and the End Point identifier as one scalar
value; thus creating only one association group entry. Using a single scalar value enables:


      - Better utilization of association group capacity


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 733




<!-- PAGE 735 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - Simple transmission of command for a multi-End Point destination

      - Well-defined removal of bit addressed End Points


Refer to the Multi Channel Command Class for the actual encoding of bit addressed End Points.


CC:008E.02.01.11.007 The 7-bit End Point value MUST be in the range 1..127.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 734




<!-- PAGE 736 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.5** **Multi** **Channel** **Association** **Get** **Command**


This command is used to request the current destinations of a given association group.


CC:008E.02.02.11.001 The Multi Channel Association Report Command MUST be returned in response to this command.


CC:008E.02.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:008E.02.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.130: Multi Channel Association Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|Command = MULTI_CHANNEL_ASSOCIATION_GET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**Grouping** **Identifier** **(8** **bits)**

CC:008E.02.02.11.004 This field is used to specify the actual association group. Grouping Identifiers MUST be assigned in
a consecutive range starting from 1.

CC:008E.02.02.12.001 A node that receives an unsupported Grouping Identifier SHOULD return information relating to
Grouping Identifier 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 735




<!-- PAGE 737 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.6** **Multi** **Channel** **Association** **Report** **Command**


This command is used to advertise the current destinations for a given association group.


Table 3.131: Multi Channel Association Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|Command = MULTI_CHANNEL_ASSOCIATION_REPORT<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|Nax Nodes Supported|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|
|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REPORT_MARKER|
|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|
|Bit Address<br>1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|
|…|…|…|…|…|…|…|…|
|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|
|Bit Address<br>N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|



**Grouping** **Identifier** **(8** **bits)**

CC:008E.02.03.11.001 This field is used to advertise the actual association group. Grouping Identifiers MUST be assigned
in a consecutive range starting from 1.


**Max** **Nodes** **Supported** **(8** **bits)**


The maximum number of destinations supported by the advertised association group. Each destination
CC:008E.02.03.13.001 MAY be a NodeID destination or an End Point destination.


**Reports** **to** **Follow** **(8** **bits)**


The entire list destinations of the advertised association group may be too long for one command.

CC:008E.02.03.11.002 This field MUST advertise how many report frames will follow this report.


**NodeID** **(M** **bytes)**

This field advertises a list of NodeID destinations of the advertised association group.


CC:008E.02.03.11.003
The list of NodeIDs MUST be empty if there are no NodeID destinations configured for the advertised
association group.


**Marker** **(8** **bits)**


Refer to description under the Multi Channel Association Set command.


**Multi** **Channel** **NodeID** **(N** **bytes)**

The Multi Channel NodeID, Bit Address and End Point fields specify a list of End Points which are
currently in the advertised association group.

The complete identification of an End Point requires a NodeID as well as an End Point identifier. The
CC:008E.02.03.13.002 Multi Channel Association Report command MAY carry multiple copies of the same Multi Channel
NodeID in combination with different End Point identifiers.

CC:008E.02.03.11.004 The list of Multi Channel NodeID and End Point identifiers MUST be empty if there are no End
Point destinations configured for the advertised association group.


**Bit** **address** **+** **End** **Point** **(N** **bytes)**

CC:008E.02.03.11.005 These fields MUST be processed in combination with the Multi Channel NodeID field.


Refer to the Multi Channel Command Class for the actual encoding of bit addressed End Points.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 736




<!-- PAGE 738 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.7** **Multi** **Channel** **Association** **Remove** **Command**


This command is used to remove NodeID and End Point destinations from a given association group.


CC:008E.02.04.11.001 This command MUST manipulate the same list of NodeID destinations as the Association Remove
Command.


Table 3.132: Multi Channel Association Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|
|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_REMOVE_MARKER|
|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|
|Bit Address<br>1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|
|…|…|…|…|…|…|…|…|
|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|
|Bit Address<br>N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|



**Grouping** **Identifier** **(8** **bits)**

This field is used to specify from which association group the specified destinations should be removed.

CC:008E.02.04.11.002 Grouping Identifiers MUST be assigned in a consecutive range starting from 1.

CC:008E.02.04.11.003 A receiving node MUST ignore an unsupported Grouping Identifier; except for the value 0.

CC:008E.02.04.11.004 This field MUST be interpreted in combination with the NodeID and End Point fields.


**(NodeID** **Destination)** **NodeID** **(M** **bytes)**


**(End** **Point** **Destination)** **Multi** **Channel** **NodeID** **(N** **bytes)**


**(End** **Point** **Destination)** **End** **Point** **(N** **bytes)**

These fields specify the destinations that are to be removed.

CC:008E.02.04.11.005 The Grouping Identifier and these fields MUST be interpreted as follows.

“NodeID Destinations” denote the NodeID fields.

“End Point destinations” denote the combined Multi Channel NodeID and End Point fields found
after the marker.

CC:008E.02.04.13.001 A receiving node MAY interpret the empty command (only Command Class and Command fields)
as an instruction to Remove all NodeID destinations and End Point destinations from all association

groups.

CC:008E.02.04.11.006 This field MUST be interpreted according to Table 3.133


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 737




<!-- PAGE 739 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 3.133: Multi Channel Association Remove, V2::Parameter
Interpretation









|Grouping<br>i<br>identifer|Number<br>of NodeID<br>Destinations|Number of<br>End Point<br>Destinations|Interpretation|
|---|---|---|---|
|> 0|> 0|(don’t care)|Remove NodeID destinations from associ-<br>ation group.<br>Then assess End Points (next line) – if any<br>specifed|
|> 0|(don’t care)|> 0 *)|Remove End Point destinations from asso-<br>ciation group *).|
|> 0|= 0|= 0|Remove all NodeID destinations and End<br>Point destinations from associationgroup.|
|= 0|> 0|(don’t care)|Remove NodeID destinations from all as-<br>sociation groups.<br>Then assess End Point destinations (next<br>line) – if any specifed|
|= 0|(don’t care)|> 0 *)|Remove End Point destinations from all<br>association groups *).|
|= 0|= 0|= 0|Remove all NodeID destinations and End<br>Point destinations from all association<br>groups.|


CC:008E.02.04.11.007 *) The receiving node MUST treat the Bit Address flag and the End Point identifier as one scalar

CC:008E.02.04.11.008 value. The receiving node MUST remove End Points if an exact match can be found, while it MAY
ignore the removal request if an exact match cannot be found; even though there may exist associations
for individual End Point destinations which are covered by the End Point bitmap address.


**Marker** **(8** **bits)**


Refer to the description in Section 3.2.33.4 in the Multi Channel Association Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 738




<!-- PAGE 740 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.7.1** **Examples**


Figure 3.17: Remove specified NodeID from Group 3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 739




<!-- PAGE 741 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.18: Remove Specified End Point from Group 3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 740




<!-- PAGE 742 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.19: Remove Bit Addressable End Points from Group 3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 741




<!-- PAGE 743 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.20: Remove Specified NodeID and End Point from Group 3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 742




<!-- PAGE 744 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.21: Remove all Associations from Group 3


Figure 3.22: Remove Specific NodeID from all Groups


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 743




<!-- PAGE 745 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 3.23: Remove Specific Multi Channel NodeID from all Groups


Figure 3.24: Remove all Associations from all Groups


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 744




<!-- PAGE 746 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.33.8** **Multi** **Channel** **Association** **Supported** **Groupings** **Get** **Command**


This command is used to request the number of association groups that this node supports.


CC:008E.02.05.11.001 The Multi Channel Association Supported Groupings Report Command MUST be returned in response to this command.


CC:008E.02.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:008E.02.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.134: Multi Channel Association Supported Groupings Get
Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|Command = MULTI_CHANNEL_ASSOCIATION_GROUPINGS_GET|



**3.2.33.9** **Multi** **Channel** **Association** **Supported** **Groupings** **Report** **Command**


This command is used to advertise the maximum number of association groups implemented by this
node.


Table 3.135: Multi Channel Association Supported Groupings Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|Command = MULTI_CHANNEL_ASSOCIATION_REMOVE|
|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|



**Supported** **Groupings** **(8** **bits)**

This field is used to advertise the number of association groups that this node supports.

CC:008E.02.06.11.001 Grouping Identifiers MUST be assigned in a consecutive range starting from 1.


CC:008E.02.06.11.002
The value advertised by this field MUST be the total number of supported association groups; whether
associations are managed via the Association Command Class or the Multi Channel Association
Command Class.


CC:008E.02.06.11.003 Each of these association groups MUST support NodeID destinations as well as End Point destinations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 745

---

<!-- PAGE 747 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.34** **Multi** **Channel** **Association** **Command** **Class,** **version** **3**


The Multi Channel Association Command Class is used to manage associations to Multi Channel End
Point destinations as well as to NodeID destinations.


The following sections specify commands which were extended or added in version 3.


**3.2.34.1** **Compatibility** **considerations**


The considerations of section Section 3.2.33.1 also apply to this version the following additions:


CC:008E.03.00.21.001 A device supporting this Command Class version MUST also


      - support the Multi Channel Association Command Class, version 2


      - support the (non-Multi Channel) Association Command Class, version 2


This version introduces support for the creation of an End Point Association to the Root Device of
another device, e.g. a gateway, by allowing the destination End Point 0 as a valid value.


This allows a gateway to create a single Lifeline association from a Multi Channel device and subsequently receive status messages or sensor reports from the Root Device as well as the End Points of
that device. Refer to section Section 3.2.34.2.


CC:008E.03.00.21.002 The use of Multi Channel encapsulation MUST comply with Table 3.136.


Table 3.136: V3 Associations and the Transmissions they may Trig
|Table 3.136: V3 Associations and ger Source -> Destination|the Transmission Association|ns they may Trig- Allowed Transmissions|
|---|---|---|
|Source -> Destination|Association<br>Type|Allowed Transmissions|
|NodeID -> NodeID (V2)|NodeID|Non-encapsulated|
|End Point -> NodeID (V2)|NodeID|Non-encapsulated|
|NodeID -> End Point (V2)|End Point|Encapsulated *) (src0, dst>0)|
|End Point -> End Point (V2)|End Point|Encapsulated (src>0, dst>0)|
|End Point -> Root Device (V3)|End Point|Encapsulated (src>0, dst=0)|
|Root Device -> Root Device (V3)|End Point|Non-encapsulated **) or En-<br>capsulated (src>0, dst=0)|



*) The source End Point MAY be different than 0 if the associated group is an End Point Group
mapped to the Root Device


**) Command must be sent non-encapsulated if both End Points are zero. However, the End Point
association from a Root Device Lifeline group to a Root Device also allows a source End Point to send
encapsulated commands to the Root Device Lifeline destination. Refer to Section 3.2.34.2.


**3.2.34.2** **Z-Wave** **Plus** **considerations**


The considerations of version 2 also apply to this version.


Version 3 adds support for creation of an End Point Association to the Root Device of another device,
e.g. a gateway.


CC:008E.03.00.11.001 A controlling device MUST verify that a device supports Multi Channel Association Command Class,
Version 3 before creating an End Point Association to the Root Device of another device.


Multi Channel End Points may implement functionality relevant to a Lifeline destination, e.g. individual meter reports from a power strip. Multi Channel encapsulation allows the Lifeline destination
to distinguish between apparently identical commands from different End Points.

As specified by the Multi Channel Command Class, a Root Device must not use Multi Channel
encapsulation when communicating to another Root Device, i.e. if both End Points are zero. It does


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 746




<!-- PAGE 748 -->

CC:008E.03.00.12.001


CC:008E.03.00.13.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


however still make sense to create an End Point Association from one Root Device to another Root

Device, e.g. a gateway.


Consider, as an example, a two-channel temperature sensor. By creating an End Point association
from the Lifeline Association Group to the Root Device of a gateway, the gateway may receive unsolicited Multi Channel encapsulated sensor reports from each of the sensor End Points as well as
non-encapsulated battery status messages from the sensor Root Device.


The Root Device of a Multi Channel device SHOULD implement support for the Multi Channel Association Command Class if any of the End Points provide association capabilities. If the Root Device
implements such support, the Root Device MAY forward Multi Channel encapsulated commands to
the association destination on behalf of End Points.



CC:008E.03.00.11.002 A NodeID association MUST NOT be created in response to a request for an End Point association
to the Root Device (destination End Point 0).



CC:008E.03.00.11.003


CC:008E.03.00.11.004



If a NodeID Association is created from the Root Device Lifeline Association Group, End Point
commands MUST NOT be transmitted via the Lifeline Association Group of the root device. All
commands originating from the Root Device (Tamper Alarm, Device Reset Locally, etc.) MUST be
sent non-encapsulated to the Lifeline destination.



CC:008E.03.00.11.005 If a NodeID association is created, two End Points MUST NOT forward identical commands (e.g.
Multilevel Sensor Report::Temperature) via the Lifeline group, as the lack of source End Point information will prevent a receiving application from distinguishing the individual commands from each
other.


CC:008E.03.00.11.006 If an End Point Association is created from the Lifeline group, End Points MUST send relevant Multi
Channel encapsulated commands to the Lifeline group destination.


CC:008E.03.00.13.002 A Multi Channel device MAY forward commands from multiple Multi Channel End Points to the
Lifeline group destination.


**3.2.34.3** **Security** **considerations**


The considerations of section Section 3.2.33.3 also apply to this version.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 747




<!-- PAGE 749 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.34.4** **Multi** **Channel** **Association** **Set** **Command**


This command is used to request that one or more destinations are added to a given association group.


CC:008E.03.01.13.001 The destinations MAY be a mix of NodeID destinations and End Point destinations.

CC:008E.03.01.12.001 The receiving node SHOULD add the specified destinations to the specified association group.


CC:008E.03.01.13.002 This command MAY be ignored if the association group is already full.


CC:008E.03.01.11.001 Routing end nodes MUST have return routes assigned to all association destinations.


Table 3.137: Multi Channel Association Set Command version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|Command Class = COMMAND_CLASS_MULTI_CHANNEL_ASSOCIATION|
|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|Command = MULTI_CHANNEL_ASSOCIATION_SET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|NodeID M|
|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|Marker = MULTI_CHANNEL_ASSOCIATION_SET_MARKER|
|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|Multi Channel NodeID 1|
|Bit Address<br>1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|End Point 1|
|…|…|…|…|…|…|…|…|
|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|Multi Channel NodeID N|
|Bit Address<br>N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|End Point N|



**Grouping** **Identifier** **(8** **bits)**

This field is used to specify the actual association group.

CC:008E.03.01.11.002 A node receiving an unsupported Grouping Identifier MUST ignore this command.


**NodeID** **(M** **bytes)**

The NodeID fields specify a list of NodeID destinations that are to be added to the specified association
group as a NodeID association.

CC:008E.03.01.11.003 A NodeID association created via this field MUST be identical to a NodeID association created with
the (non-Multi Channel) Association Set command.


**Marker** **(8** **bits)**

This field is used to indicate the end of NodeID destinations and the start of End Point destinations.

CC:008E.03.01.11.004
The Marker field MUST be set to the value MULTI_CHANNEL_ASSOCIATION_SET_MARKER.
The field MAY be omitted if no End Point destinations are specified.


**Multi** **Channel** **NodeID** **(N** **bytes)**

The Multi Channel NodeID, Bit Address and End Point fields specify a list of End Point destinations
which are to be added to the specified association group as an End Point association.

The complete identification of an End Point destination requires a NodeID as well as an End Point
CC:008E.03.01.13.003 identifier. This command MAY carry multiple copies of the same Multi Channel NodeID in combination with different End Point identifiers.


**Bit** **address** **+** **End** **Point** **(N** **bytes)**

CC:008E.03.01.11.005 These fields MUST be processed in combination with the Multi Channel NodeID field.

CC:008E.03.01.12.005 The receiving node SHOULD treat the Bit Address flag and the End Point identifier as one scalar
value; thus creating only one association group entry. Using a single scalar value enables:


      - Better utilization of association group capacity


      - Simple transmission of command for a multi-End Point destination


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 748




<!-- PAGE 750 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - Well-defined removal of bit addressed End Points


Refer to the Multi Channel Command Class for the actual encoding of bit addressed End Points.


CC:008E.03.01.11.006 The 7-bit End Point value MUST be in the range 0..127.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 749

---

<!-- PAGE 751 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.35** **Multi** **Channel** **Association** **Command** **Class,** **version** **4**


The Multi Channel Association Command Class version 4 introduces the capability to discover the
highest security class of a target when issuing controlling commands via association groups.


**3.2.35.1** **Compatibility** **Considerations**


CC:008E.04.00.21.001 If a node supports the version 4 of this Command Class and the Association Command Class, it
MUST support the Association Command Class, version 3 or newer.


**3.2.35.2** **Interoperability** **considerations**


CC:008E.04.00.31.001 A supporting node MUST respect the requirement defined in Section 3.2.5.2 Interoperability considerations


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 750

---

<!-- PAGE 752 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.36** **Multi** **Channel** **Association** **Command** **Class,** **version** **5**


The Multi Channel Association Command Class version 5 introduces the capability to discover the
highest security class of a target when issuing unsolicited supporting commands (Unsolicited Reports
and Notifications) via association groups.


**3.2.36.1** **Compatibility** **Considerations**


CC:008E.05.00.21.001 If a node supports the version 5 of this Command Class and the Association Command Class, it
MUST support the Association Command Class, version 4 or newer.


**3.2.36.2** **Interoperability** **considerations**


CC:008E.05.00.31.001 A supporting node MUST respect the requirement defined in Section 3.2.6.2 Interoperability considerations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 751