<!-- PAGE 1019 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7** **Node** **Provisioning** **Command** **Class,** **version** **1**


The Node Provisioning Command Class is used to manage a list of unique nodes (Node Provisioning
List) in a Smart Start enabled controller or gateway.


**5.2.7.1** **Terminology**


Smart start allows a controller to include new nodes in a network (or keep them out) without user
interaction.


A Smart Start enabled controller or gateway maintains a **Node** **Provisioning** List or **Provisioning**
**List** (PL). The Provisioning List is a list of unique nodes and their additional associated meta data
necessary for performing their network inclusion and security bootstrapping.


A **Provisioning** **List** **entry** represents a node and its associated data. Provisioning List entries may
also be used for ignoring nodes.


A Z/IP Client or controller can read and edit the Provisioning List entries of a Z/IP Gateway or
controller using this Command Class.


**5.2.7.2** **Compatibility** **considerations**


CC:0078.01.00.22.001 This Command Class MAY be carried in Z/IP Packets or in Z-Wave frames. However, this Command
Class SHOULD only be used in Z/IP Packets.


CC:0078.01.00.21.001 A node supporting this Command Class MUST support at least 232 entries in its Node Provisioning
List.


**5.2.7.3** **Security** **considerations**


This Command Class allows a controlling node to include new nodes in the Z-Wave network and grant
them all the security keys.


CC:0078.01.00.41.001 A node supporting this Command Class MUST NOT support it in a Z-Wave network if its highest
Security Class is lower than S2 Access Control.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1018




<!-- PAGE 1020 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.4** **Node** **Provisioning** **Set** **Command**


This command is used to create or update an entry in the node provisioning list of a supporting node.


Table 5.134: Node Provisioning Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0078.01.01.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**DSK** **Length** **(5** **bits)**

CC:0078.01.01.11.002 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.01.11.003 This field MUST be set to 16.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being added or updated.


CC:0078.01.01.11.004 A receiving node MUST add a new entry in the provisioning list if it does not have any entry with
the advertised DSK value.


CC:0078.01.01.11.00D A receiving node MUST ignore a command attempting to create a new entry if the Provisioning List
is full.


CC:0078.01.01.11.005 A receiving node MUST update the corresponding entry in the provisioning list if it already has an
entry with the advertised DSK value.

CC:0078.01.01.11.006 The length of this field (in bytes) MUST be according to the DSK Length field value.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the node.

CC:0078.01.01.13.001 This field MAY contain zero, one or several extensions.


CC:0078.01.01.11.007 Each extension MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].


CC:0078.01.01.11.009 If the Bootstrapping mode Type (0x36) is omitted from this command, the Bootstrapping mode value
1 (Smart Start Mode) MUST be assumed by the receiving node when creating a new entry.


CC:0078.01.01.11.00B If the SmartStart Inclusion Setting Type (0x34) is omitted from this command, the Inclusion setting
value 0 (Pending) MUST be assumed by the receiving node when creating a new entry that has a
SmartStart Bootstrapping mode.


CC:0078.01.01.11.00A The Network Status Type (0x37) MUST NOT be carried in this command. The Network Status Type
(0x37) MUST be ignored if received in this command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1019




<!-- PAGE 1021 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.5** **Node** **Provisioning** **Delete** **Command**


This command is used to delete one or all entries in the node provisioning list of a supporting node. Already included nodes will stay in the Z-Wave network even if no more corresponding node provisioning
list entry is kept by the controller.


Table 5.135: Node Provisioning Delete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.02.11.001 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.02.11.002 This field MUST be set to 0 or 16.


CC:0078.01.02.11.003 The value 0 MUST indicate that the receiving node MUST delete all entries in its Node Provisioning
List.


CC:0078.01.02.11.004 The value 16 MUST indicate that the receiving node MUST delete the entry in its Node Provisioning
List that match the advertised value in the DSK field.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being deleted.


CC:0078.01.02.11.005 A receiving node MUST delete the corresponding entry from the Node Provisioning List if it has an
entry with the advertised DSK value.


CC:0078.01.02.11.006 A receiving node MUST ignore this command if it has no entry with the advertised DSK value.

CC:0078.01.02.11.007 The length of this field (in bytes) MUST be according to the DSK Length field value.

This field MUST be omitted if the DSK Length field is set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1020




<!-- PAGE 1022 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.6** **Node** **Provisioning** **Get** **Command**


This command is used to request the metadata information associated to an entry in the node Provisioning List of the receiving node.


CC:0078.01.05.11.001 The Node Provisioning Report Command MUST be returned in response to this command.


CC:0078.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0078.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.136: Node Provisioning Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No.** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.05.11.004 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.05.11.005 This field MUST be set to 16.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being requested.


CC:0078.01.05.11.006 A receiving node MUST return the corresponding DSK entry if it has an entry matching the requested
DSK in its Provisioning List.


CC:0078.01.05.11.007 A receiving node MUST return a report containing no DSK (DSK Length set to 0) if the requested
DSK value is not in its Provisioning List.

CC:0078.01.05.11.008 The length of this field (in bytes) MUST be according to the DSK Length field value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1021




<!-- PAGE 1023 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.7** **Node** **Provisioning** **Report** **Command**


This command is used to advertise the contents of an entry in the node Provisioning List of the
sending node.


Table 5.137: Node Provisioning Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|
|…|…|…|…|…|…|…|…|
|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.06.11.001 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.06.11.002 This field MUST be set to 0 or 16


CC:0078.01.06.11.003 The value 0 MUST indicate that the requested DSK is not present in the Provisioning List.


**DSK** **(N** **bytes)**

CC:0078.01.06.11.004 This field is used to advertise the DSK for the Provisioning List entry being advertised.

CC:0078.01.06.11.005 The length of this field (in bytes) MUST be according to the DSK Length field value. This field
MUST be omitted if the DSK Length field is set to 0.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the Provisioning List entry.

CC:0078.01.06.13.001 This field MAY contain several extensions.


CC:0078.01.06.11.006 Each extension Type, Length and Value MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].

CC:0078.01.06.13.002 A supporting node MAY set the critical flag to 0 even when advertising critical extensions.

CC:0078.01.06.11.007 If the DSK Length field is set to 0, this field MUST be omitted.

If the DSK Length field is not set to 0:


CC:0078.01.06.11.008 - A sending node MUST advertise the SmartStart Inclusion Setting extension (type 0x34)


CC:0078.01.06.11.009 - A sending node MUST advertise the Bootstrapping mode extension (type 0x36)


CC:0078.01.06.11.00B - A sending node MUST advertise the Network Status extension (type 0x37)


CC:0078.01.06.11.00A - A sending node MUST advertise all other extension data kept in the Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1022




<!-- PAGE 1024 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.8** **Node** **Provisioning** **List** **Iteration** **Get** **Command**


This command is used to read the entire the provisioning list of a supporting node.


CC:0078.01.03.11.001 The Node Provisioning List Iteration Report Command MUST be returned in response to this command unless it is to be ignored.


CC:0078.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:0078.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

CC:0078.01.03.11.004 A sending node MUST follow the frame flow in Section 5.2.7.11.1.


Table 5.138: Node Provisioning List Iteration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Remaining** **Counter** **(8** **bits)**

This field is used to iterate over the Provisioning List. The field indicates the remaining amount of
CC:0078.01.03.11.005 entries in the Provisioning List. This field MUST be in the range 0x01..0xFF.

CC:0078.01.03.11.006 This field MUST be set to 0xFF to start a new iteration. A supporting node MUST return the first
entry and the actual amount of remaining entries in the returned report, i.e. If the Provisioning list
has 3 elements the first response Remaining Count field MUST be set to 2.

CC:0078.01.03.11.007 A sending node MUST subsequently set this field to the returned value ”Remaining Count” value
received in the returned Report if the ”Remaining Count” value is higher than 0x00. A supporting
node MUST ignore this field if it is not set to the expected next iteration value.

CC:0078.01.03.11.008 This command MUST be ignored by a supporting node if this field is set to a value lower than 0xFF
and no iteration has been started.


Refer to Section 5.2.7.11.1.


**5.2.7.9** **Node** **Provisioning** **List** **Iteration** **Report** **Command**


This command is used to advertise the contents of an entry in the Provisioning List of the sending
node.


Table 5.139: Node Provisioning List Iteration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|
|Reserved|Reserved|Reserved|DSK Length N|DSK Length N|DSK Length N|DSK Length N|DSK Length N|
|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|
|…|…|…|…|…|…|…|…|
|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1023




<!-- PAGE 1025 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Remaining** **Count** **(8** **bits)**

The field MUST indicate the remaining amount of entries in the Provisioning List iteration. This field
CC:0078.01.04.11.001 MUST be in the range 0x00..0xFE.


**DSK** **Length** **(5** **bits)**

CC:0078.01.04.11.002 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.04.11.003 This field MUST be set to 0 or 16.


CC:0078.01.04.11.004 The value 0 MUST indicate that the Provisioning List of the sending node is empty or the Provisioning
List Entry has been deleted after the start of the iteration.


CC:0078.01.04.11.005 The value 16 MUST indicate that the sending node advertises the DSK of a Provisioning List entry.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the Provisioning List entry being advertised.

CC:0078.01.04.11.006 The length of this field (in bytes) MUST be according to the DSK Length field value. This field
MUST be omitted if the DSK Length field is set to 0.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the Provisioning List entry.

CC:0078.01.04.13.001 This field MAY contain several extensions.


CC:0078.01.04.11.007 Each extension Type, Length and Value MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].

CC:0078.01.04.13.002 A supporting node MAY set the critical flag to 0 even when advertising critical extensions.

CC:0078.01.04.11.008 If the DSK Length field is set to 0, this field MUST be omitted.

If the DSK Length field is not set to 0:


CC:0078.01.04.11.009 - A sending node MUST advertise the SmartStart Inclusion Setting extension (type 0x34)


CC:0078.01.04.11.00A - A sending node MUST advertise the Bootstrapping mode extension (type 0x36)


CC:0078.01.04.11.00C - A sending node MUST advertise the Network Status extension (type 0x37)


CC:0078.01.04.11.00B - A sending node MUST advertise all other extension data kept in the Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1024




<!-- PAGE 1026 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.10** **Meta** **Data** **Extension** **Format**


CC:0078.01.00.11.001 Each Meta Data extension MUST be parsed according to the following format:


Table 5.140: Meta Data Extension Format

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|critical|
|Length|Length|Length|Length|Length|Length|Length|Length|
|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|



**Meta** **Data** **Type** **(7** **bits)**

This field is used to advertise the type of the data contained in the corresponding extension.

CC:0078.01.00.11.002 For the list of defined valid extensions, refer to [28]. Values not defined in [28] are reserved and MUST
NOT be used by a sending node.


**Critical** **(1** **bit)**

This field is used to advertise the criticality of the extension.


CC:0078.01.00.11.003
A supporting node MUST discard and ignore the entire command if this flag is set to ‘1’ and the Meta
Data Type field advertises a value that the node does not support.


CC:0078.01.00.12.001 A controlling node which controls only (i.e. does not support this Command Class) SHOULD keep
the Provisioning List entry in its record even if this flag is set to ‘1’ and the node does not know what
the extension means.

If this flag is set to ‘0’ and the Meta Data Type field advertises a value that the receiving node does
CC:0078.01.00.11.004 not support, the actual extension MUST be ignored and left out the provisioning list entry.


CC:0078.01.00.11.005 In this case, a receiving node MUST continue processing of the encapsulation command after the
discarded extension.


**Length** **(8** **bits)**

CC:0078.01.00.11.006 This field MUST indicate the length of the corresponding Value field in bytes.


**Value** **(L** **bytes)**

CC:0078.01.00.11.007 This field MUST indicate the value of the Meta Data type being advertised in the extension.

The length of this field (in bytes) MUST be according to the corresponding Length field value .This
CC:0078.01.00.11.008 field MUST be omitted if the corresponding Length field is set to 0.

CC:0078.01.00.11.009 The encoding of this field MUST be interpreted with the Meta Data Type field as defined in [28].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1025




<!-- PAGE 1027 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.11** **Usage** **and** **Frame** **Flows**


**5.2.7.11.1** **Z/IP** **Client** **requesting** **the** **entire** **Node** **Provisioning** **list.**


The frame flow for Z/IP client requesting the entire Provisioning List of a supporting node is shown
in Figure 5.28.


Figure 5.28: Reading the entire Node Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1026