<!-- PAGE 585 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3** **Association** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this Command Class.


New implemenetations MUST use the _Association_ _Command_ _Class,_ _version_ _2_, or newer instead.


The Association Command Class is used to manage associations to NodeID destinations. A NodeID
destination may be a simple device or the Root Device of a Multi Channel device.

An association group sends an unsolicited command to the configured destinations when triggered by
an event. The parameters of the command may be dynamic, e.g. the temperature of a sensor reading
or the light level for a dimmer.


**3.2.3.1** **Compatibility** **considerations**


CC:0085.01.00.22.001 The Association Group Information (AGI) Command Class SHOULD be supported to enable automated discovery of association group properties.


CC:0085.01.00.22.002 It is RECOMMENDED that a node which implements the Association Command Class also implements the Multi Channel Association Command Class for compatibility with End Point destinations.
For instance, a wall switch may be configured to control one specific outlet of a power strip if the wall
switch supports Multi Channel Association.


**3.2.3.2** **Z-Wave** **Plus** **considerations**



CC:0085.01.00.11.001


CC:0085.01.00.13.001



The Z-Wave Plus certification program mandates that association group 1 is reserved for the Lifeline
association group. Association group 1 MUST NOT be assigned to any other use than the Lifeline
group. The actual Device Type of a given product specifies mandatory commands which the device
must be able to send to a lifeline group destination. A manufacturer MAY add additional commands
to the Lifeline group.

The Z-Wave Plus certification program mandates support for the Association Group Information
(AGI) Command Class if a device supports the Association Command Class.

The Z-Wave Plus certification program recommends that a composite device is designed as a Multi
Channel device.


**3.2.3.3** **Security** **considerations**



CC:0085.01.00.41.001 A node that has been S0/S2 bootstrapped MUST NOT accept Association commands unless the
commands are received via the highest security key granted to the node during bootstrapping.


CC:0085.01.00.41.002 A supporting node issuing commands via association groups MUST send those commands with its
highest granted Security Class.


CC:0085.01.00.42.001 A supporting node issuing Set or Report type commands via association groups SHOULD use Supervision encapsulation only if sending commands with S2 (or higher security) encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 584




<!-- PAGE 586 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3.4** **Association** **Set** **Command**


This command is used to add destinations to a given association group.


CC:0085.01.01.12.001

The receiving node SHOULD add the specified NodeID destinations to the specified association group.
CC:0085.01.01.13.001 This command MAY be ignored if the association group is already full.


CC:0085.01.01.11.001 Routing end nodes MUST have return routes assigned to all association destinations.



CC:0085.01.01.51.001


CC:0085.01.01.51.002



Unless the association destination is a gateway, a controlling node MUST NOT create an association
if the association destination node does not support the controlling commands (Set/Get types) that
the actual association group will be sending. The AGI Command Class MUST be used to probe the
commands that a given association group will be sending.



CC:0085.01.01.52.001 A controlling node SHOULD NOT create an association if the source and destination nodes are
bootstrapped with different security levels.


Table 3.7: Association Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|Command = ASSOCIATION_SET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|



**Grouping** **Identifier** **(8** **bits)**

CC:0085.01.01.11.002 This field is used to specify the actual association group. Grouping Identifiers MUST be assigned in
a consecutive range starting from 1.

CC:0085.01.01.11.003 A receiving node MUST ignore an unsupported Grouping Identifier.


**NodeID** **(N** **bytes)**

This field specifies a list of NodeIDs that are to be added to the specified association group.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 585




<!-- PAGE 587 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3.5** **Association** **Get** **Command**


This command is used to request the current destinations of a given association group.


CC:0085.01.02.11.001 The Association Report Command MUST be returned in response to this command.


CC:0085.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0085.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.8: Association Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|Command = ASSOCIATION_GET<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|



**Grouping** **Identifier** **(8** **bits)**

CC:0085.01.02.11.004 This field is used to specify the actual association group. Grouping Identifiers MUST be assigned in
a consecutive range starting from 1.

CC:0085.01.02.12.001 A node that receives an unsupported Grouping Identifier SHOULD return information relating to
Grouping Identifier 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 586




<!-- PAGE 588 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3.6** **Association** **Report** **Command**


This command is used to advertise the current destinations of a given association group.


If the node supports the Multi Channel Association Command Class,


CC:0085.01.03.11.001 - the node MUST advertise the same Node ID destinations in this report as in the Multi Channel


      - Association Report Command


CC:0085.01.03.11.002 - the node MUST NOT advertise the NodeID of End Point destinations in this report.


Table 3.9: Association Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|Command = ASSOCIATION_REPORT<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|Max Nodes Supported|
|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|Reports to Follow|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|



**Grouping** **Identifier** **(8** **bits)**

CC:0085.01.03.11.003 This field is used to advertise the actual association group. Grouping Identifiers MUST be assigned
in a consecutive range starting from 1.


**Max** **Nodes** **Supported** **(8** **bits)**


CC:0085.01.03.13.001 The maximum number of destinations supported by the advertised association group. Each destination
MAY be a NodeID destination or an End Point destination (if the node supports the Multi Channel
Association Command Class).


**Reports** **to** **Follow** **(8** **bits)**


The entire list destinations of the advertised association group may be too long for one command.
CC:0085.01.03.11.004 This field MUST advertise how many report frames will follow this report.


**NodeID** **(N** **bytes)**

This field advertises a list of NodeID destinations of the advertised association group. The list of

CC:0085.01.03.11.005
NodeIDs MUST be empty if there are no NodeID destinations configured for the advertised association

group.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 587




<!-- PAGE 589 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3.7** **Association** **Remove** **Command**


This command is used to remove destinations from a given association group.


CC:0085.01.04.11.001 If the node supports the Multi Channel Association Command Class the node MUST NOT remove
End Point destinations in response to this command.


Table 3.10: Association Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|



**Grouping** **Identifier** **(8** **bits)**

This field is used to specify from which association group the specified NodeID destinations should be
removed.

CC:0085.01.04.11.002 Grouping Identifiers MUST be assigned in a consecutive range starting from 1.

CC:0085.01.04.11.003 This field MUST be interpreted in combination with the NodeID field.

CC:0085.01.04.11.004 A node that receives an unsupported Grouping Identifier MUST ignore this command.


**NodeID** **(N** **bytes)**

This field specifies a list of NodeID destinations that are to be removed from the specified association

group.

CC:0085.01.04.11.005 The Grouping Identifier and NodeID fields MUST be interpreted as indicated in Table 3.11.


Table 3.11: Association Remove, V1::Parameter Interpretation

|i<br>Grouping Identifer|Number of NodeIDs|Interpretation|
|---|---|---|
|> 0|> 0|Remove specifed NodeIDs from the specifed as-<br>sociation group (MANDATORY V1)<br>|
|> 0|= 0|Remove all NodeIDs from the specifed associa-<br>tion group (RECOMMENDED V1)|
|= 0|>= 0|(_Reserved_ V1)|



CC:0085.01.04.11.006 A sending node MUST NOT send reserved parameter combinations and a receiving node MUST
ignore reserved parameter combinations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 588




<!-- PAGE 590 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.3.8** **Association** **Supported** **Groupings** **Get** **Command**


This command is used to request the number of association groups that this node supports.


CC:0085.01.05.11.001 The Association Supported Groupings Report Command MUST be returned in response to this command.


CC:0085.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0085.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.12: Association Supported Groupings Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|Command = ASSOCIATION_GROUPINGS_GET|



**3.2.3.9** **Association** **Supported** **Groupings** **Report** **Command**


This command is used to advertise the maximum number of association groups implemented by this
node.


Table 3.13: Association Supported Groupings Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|Command = ASSOCIATION_GROUPINGS_REPORT|
|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|Supported Groupings|



**Supported** **Groupings** **(8** **bits)**

This field is used to advertise the number of association groups that this node supports.

CC:0085.01.06.11.001 Grouping Identifiers MUST be assigned in a consecutive range starting from 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 589

---

<!-- PAGE 591 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.4** **Association** **Command** **Class,** **version** **2**


The Association Command Class is used to manage associations to NodeID destinations. A NodeID
destination may be a simple device or the Root Device of a Multi Channel device.


The following sections specify commands which were extended or added in version 2.


**3.2.4.1** **Compatibility** **Considerations**


CC:0085.02.00.21.001 A device supporting this command class version MUST also support the Association Command Class,
version 1.


This version introduces        - New methods for the removal of associations via the Association Remove

Command       - New commands

      - Association Specific Group Get Command

      - Association Specific Group Report Command


The considerations of Section 3.2.3.1 also apply to this version.


**3.2.4.2** **Z-Wave** **Plus** **considerations**


The considerations of Section 3.2.3.2 also apply to this version.


**3.2.4.3** **Security** **considerations**


The considerations of Section 3.2.3.3 also apply to this version.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 590




<!-- PAGE 592 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.4.4** **Association** **Remove** **Command**


The Association Remove Command is used to remove NodeID destinations from a given association

group.


CC:0085.02.04.11.001 If the node supports the Multi Channel Association Command Class the node MUST NOT remove
End Point destinations in response to this command.


Table 3.14: Association Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|Command = ASSOCIATION_REMOVE<br>|
|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|Grouping Identifer|
|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|NodeID 1|
|…|…|…|…|…|…|…|…|
|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|NodeID N|



**Grouping** **identifier** **(8** **bits)**

This field is used to specify from which association group the specified NodeID destinations are to be
removed.

CC:0085.02.04.11.002 This field MUST be interpreted in combination with the NodeID field.

CC:0085.02.04.11.003 A node that receives an unsupported Grouping Identifier MUST ignore this command; with the
exception of Grouping Identifier 0, which MUST be accepted. Refer to Table 3.15.


**NodeID** **(N** **bytes)**

This field specifies a list of NodeID destinations that are to be removed. The Grouping Identifier and
CC:0085.02.04.11.004 NodeID fields MUST be interpreted as indicated in Table 3.15:


Table 3.15: Association Remove, V2::Parameter Interpretation

|i<br>Grouping Identifer|Number of NodeIDs|Interpretation|
|---|---|---|
|> 0|> 0|Remove destination NodeIDs from association<br>group (MANDATORY V1, MANDATORY V2)|
|> 0|= 0|Remove all destination NodeIDs from associa-<br>tion group (RECOMMENDED V1, MANDA-<br>TORY V2)|
|= 0|> 0|Remove destination NodeIDs from all associa-<br>tion groups (_Reserved_ V1, MANDATORY V2)|
|= 0|= 0|Remove all destination NodeIDs from all associ-<br>ation groups (_Reserved_ V1, MANDATORY V2)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 591




<!-- PAGE 593 -->

CC:0085.02.0B.12.001


CC:0085.02.0B.11.001


CC:0085.02.0B.12.002


CC:0085.02.0B.12.003



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.4.5** **Association** **Specific** **Group** **Get** **Command**


This command allows a portable controller to interactively create associations from a multi-button
device to a destination that is out of direct range.


It is OPTIONAL for a device to support this functionality. However, a receiving device MUST always
return the Association Specific Group Report Command in response to this command. If the device
does not support this functionality, a Group parameter value of 0 SHOULD be advertised in the
Association Specific Group Report Command that is returned in response to this command.


This functionality allows a supporting multi-button device to detect a key press and subsequently
advertise the identity of the key. The following sequence of events takes place:

 - The user activates a special identification sequence and pushes the button to be identified


 - The device issues a Node Information frame (NIF)


 - The NIF allows the portable controller to determine the NodeID of the multi-button device


 The portable controller issues an Association Specific Group Get Command to the multi-button
device


 The multi-button device returns an Association Specific Group Report Command that advertises
the association group that represents the most recently detected button


The Association Group Information (AGI) Command Class provides a centralized alternative for the
discovery of available association groups and the capabilities of these groups. A device supporting
this functionality SHOULD also support the Association Group Information (AGI) Command Class.



**CC:0085.02.0B.11.00** 23 This command MUST NOT be issued via multicast addressing. A receiving node MUST NOT return
a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the
broadcast NodeID and the Multi Channel multi-End Point destination are all considered multicast

addressing methods.


Table 3.16: Association Specific Group Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|Command = ASSOCIATION_SPECIFIC_GROUP_GET|



**Clarification** : Previous text revisions of this specification presented conflicting guidelines for the
Association Specific Group Get Command when received by non-supporting devices.

The values 0 and 1 were both suggested for the Group field of the Association Specific Group Report
CC:0085.02.0B.12.004 Command. It is RECOMMENDED that the value 0 is returned by non-supporting devices.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 592




<!-- PAGE 594 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.4.6** **Association** **Specific** **Group** **Report** **Command**


This command is used to advertise the association group that represents the most recently detected
button.


Table 3.17: Association Specific Group Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|Command Class = COMMAND_CLASS_ASSOCIATION|
|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|Command = ASSOCIATION_SPECIFIC_GROUP_REPORT|
|Group|Group|Group|Group|Group|Group|Group|Group|



**Group** **(8** **bits)**

This field is used to advertise the association group that represents the most recently detected button.

CC:0085.02.0C.11.001 The value of this field MUST be in the range 0..255.

CC:0085.02.0C.11.002 If a supporting device implements a multi-button device, the Group field MUST advertise an as
CC:0085.02.0C.12.001 sociation group which represents the most recently activated button. The actual association group
SHOULD be able to control an actuator device, e.g. via the Basic Command Class.


CC:0085.02.0C.12.002
This field SHOULD be set to 0 if the functionality is not supported or if the most recent button event
does not map to an association group.

**Clarification** : Previous text revisions of this specification presented conflicting guidelines for the
Association Specific Group Get Command when received by non-supporting devices.

CC:0085.02.0C.12.003 The values 0 and 1 were both suggested for the Group field of the Association Specific Group Report
Command. It is RECOMMENDED that the value 0 is returned by non-supporting devices.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 593

---

<!-- PAGE 595 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.5** **Association** **Command** **Class,** **version** **3**


The Association Command Class version 3 introduces the capability to discover the highest security
class of a target when issuing controlling commands via association groups.


**3.2.5.1** **Compatibility** **Considerations**


If a node supports the version 3 of this Command Class and the Multi Channel Association Command
CC:0085.03.00.21.001 Class, it MUST support the Multi Channel Association Command Class, version 4 or newer.


**3.2.5.2** **Interoperability** **considerations**


CC:0085.03.00.31.001 Any supporting node MUST learn the granted security classes of a destination before sending controlling commands to a destination via association groups.


Commands are marked as controlling or supporting in [25].


CC:0085.03.00.32.001 The following discovery is RECOMMENDED:


1. Request the NIF and read its contents, look for S2/Supervision and S0


2. If S2 is supported, for every granted S2 key starting from the highest:


a. Issue the S2 encrypted controlling command using Supervision Get encapsulation (and
Multi Channel encapsulation if End Point source or destination)


b. If receiving a Supervision Report, stop the discovery and use the current S2 Security Class
for controlling the target NodeID.


c. Else if no answer is returned (or S2 Nonce Reports), proceed with a lower granted S2 key.


3. If S0 is supported, try using S0:


a. If S2 was in the NIF :


i. Issue the S0 encrypted controlling command using Supervision Get encapsulation


ii. If receiving a Supervision Report, stop the discovery and use S0 as the Security Class
to control the target NodeID


b. If S2 was not in the NIF:


i. Issue a S0 encrypted S0 Security Command Supported Get command


ii. If receiving S0 encrypted S0 Security Command Supported Report command, stop the
discovery and use S0 for controlling the target NodeID


4. Settle for non-secure level if no Security Class was found. Supervision encapsulation MAY be
used non-securely only if it was in the NIF.


CC:0085.03.00.33.001 A supporting node MAY use another algorithm using the following assumptions:


CC:0085.03.00.31.002 - A controlling node MUST NOT associate Node A to a Node B destination that does not support
the Command Class that the Node A will be controlling.


CC:0085.03.00.31.003 - A controlling node MUST NOT associate Node A to a Node B destination if Node A was not
granted Node B’s highest Security Class.

_Role_ _Type_ _Specification_ provides recommended timeouts when waiting for responses to Get type commands.


Further, when issuing (supporting or controlling) commands via an association group:


CC:0085.03.00.31.004 - A supporting node MUST NOT use Supervision encapsulation if the destination does not support
the _Supervision_ _Command_ _Class,_ _version_ _1_ .


CC:0085.03.00.31.6  - A supporting node MUST use Supervision encapsulation if the destination supports the Supervision Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 594




<!-- PAGE 596 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:0085.03.00.31.5 - A supporting node MUST NOT use Multi Command encapsulation if the destination does not
support the Multi Command Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 595

---

<!-- PAGE 597 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.6** **Association** **Command** **Class,** **version** **4**


The Association Command Class version 4 introduces the capability to discover the highest security
class of a target when issuing unsolicited supporting commands (unsolicited Reports and Notifications)
via association groups.


**3.2.6.1** **Compatibility** **Considerations**


If a node supports the version 4 of this Command Class and the Multi Channel Association Command
CC:0085.04.00.21.001 Class, it MUST support the Multi Channel Association Command Class, version 5 or newer.


**3.2.6.2** **Interoperability** **considerations**


CC:0085.04.00.31.001 Any supporting node MUST learn the granted security classes of a destination before sending controlling or unsolicited supporting commands to a destination via association groups.


CC:0085.04.00.32.002 The learned security class SHOULD be saved in the device after a successful learn process to prevent
further learn process.


The discovery is considered to be failed if the destination node did not respond on any security class
nor non-securely.


CC:0085.04.00.31.007 If the discovery fails, the discovery MUST be marked as incomplete and the discovery SHOULD be

CC:0085.04.00.32.003 attempted later.


The supporting node is allowed to use the learned security class to send unsolicited supporting commands on a level lower that its own highest security class.


CC:0085.04.00.31.008 The learned security level can be used only to send unsolicited supporting commands or control
commands (Set, see Section 3.2.5.2). The supporting node MUST NOT reply on control commands
(with a Report on a Get command) on lower security class than its highest security class even if a
lower security class is used for sending unsolicited supporting commands.


Commands are marked as controlling or supporting in [25].


CC:0085.04.00.32.001 The discovery process is the same for the discovery of control commands (Set commands, see Section
3.2.5.2) and for unsolicited supporting commands.


The following discovery is RECOMMENDED:


1. If the destination node B previously used to send a command on the sender node A’s highest
level, node A MUST use this level for sending unsolicited supporting commands to node B


2. Request the NIF and read its contents, look for S2/Supervision and S0


3. If S2 is supported, for every granted S2 key starting from the highest:


a. Issue the S2 encrypted controlling or unsolicited supporting command using Supervision
Get encapsulation (and Multi Channel encapsulation if End Point source or destination).


b. If receiving a Supervision Report, stop the discovery and use the current S2 Security Class
for controlling or sending unsolicited supporting commands to the target NodeID.


c. Else if no answer is returned (or S2 Nonce Reports), proceed with a lower granted S2 key.


4. If S0 is supported, try using S0:


a. If S2 was in the NIF :


i. Issue the S0 encrypted controlling or unsolicited supporting command using Supervision Get encapsulation


ii. If receiving a Supervision Report, stop the discovery and use S0 as the Security Class
for controlling or sending unsolicited supporting commands to the target NodeID


b. If S2 was not in the NIF:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 596




<!-- PAGE 598 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


i. Issue a S0 encrypted S0 Security Command Supported Get command


ii. If receiving S0 encrypted S0 Security Command Supported Report command, stop the
discovery and use S0 for controlling or sending unsolicited supporting commands to
the target NodeID


5. Settle for non-secure level if no Security Class was found. Supervision encapsulation MAY be
used non-securely only if it was in the NIF.


CC:0085.04.00.33.001 A supporting node MAY use another algorithm using the following assumptions:


CC:0085.04.00.31.003 - A controlling node MUST NOT associate Node A to a Node B destination if Node A was not
granted Node B’s highest Security Class.

_Role_ _Type_ _Specification_ provides recommended timeouts when waiting for responses to Get type commands.


Further, when issuing (supporting or controlling) commands via an association group:


CC:0085.04.00.31.004 - A supporting node MUST NOT use Supervision encapsulation if the destination does not support
the _Supervision_ _Command_ _Class,_ _version_ _1_


CC:0085.04.00.31.006 - A supporting node MUST use Supervision encapsulation if the destination supports the Supervision Command Class


CC:0085.04.00.31.005 - A supporting node MUST NOT use Multi Command encapsulation if the destination does not
support the Multi Command Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 597