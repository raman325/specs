<!-- PAGE 599 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7** **Association** **Command** **Configuration** **Command** **Class,** **version** **1**


The Association Command Configuration Command Class defines the commands necessary for a 2nd
node to add and delete commands to NodeIDs in a group as defined in the Association Command
Class in a 1st node.


The device MUST implement the Association Command Class as ‘supported’

The Association Command Class and the Command Configuration Command Class MUST be linked
through the following dependencies:


 - Nodes added to an association through an Association Set or Association Composite Set MUST
be reported in Command Configuration Reports with the Command Class and command identifiers transmitted to the nodes.

 - Nodes added to an association through a Command Configuration Set MUST also be reported
in an Association Report and Association Composite Report

 - All commands associated to a grouping identifier/NodeID pair will be removed as a result of an
Association Remove. The related command records will be released

 - Command(s) associated to a grouping identifier/NodeID/endpoint pair will be removed as a
result of an Association Composite remove. The related command(s) record will be released.

The memory consumption of supporting full command sizes in all combinations of groupings identifiers
and Node IDs is very extensive; hence the command class supports a memory flexible implementation.


The Command Class allows a device to support a number of command records. A command record
consists of the grouping identifier, the Node ID and the command. The size of the command MAY
be restricted by the device through the Max command length field. The command MUST be the
complete command needed (I.e. All relevant encapsulations MUST be included in the command).


When no command records are free (all has been used), new commands MUST NOT be allocated to
Node IDs before one or more command records have been freed up (through the Association Remove
Command)

If the 2nd node runs out of free command records before it has finalized its command configurations, it
MUST accept that the application on the device has full control of the remaining Node IDs. Alternatively the 2nd node can abort the command configuration process. In this case it is RECOMMENDED
that the 2nd node free up the used command records in the aborted command configuration attempt.


A device can report the maximum number of command records, the number of free command records,
and the max command length supported through the Command Records Supported Report.


In order to support sharing knowledge of how a device controls nodes without using extensive memory
resources a Configurable Cmd field is supported. When configurable Cmd= 0x0 then a 2nd node can
only monitor the commands. It cannot control them.

The V/C field allows a device to decrease the memory utilization to a minimum. When a device
reports V/C=0x01, then the Command Configuration Set and Command Configuration Report MUST
always use command class identifier and command identifier equal to a Basic Set Command Records
Supported Get. This allows the device to only store the value field and thereby save memory resources.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 598




<!-- PAGE 600 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7.1** **Command** **Records** **Supported** **Get** **Command**


The Command Records Supported Get Command is used to request the number of free command
records available (grouping Identifier, Node ID, command), the maximum command records supported
in the device and information regarding the maximum command length supported in the device.


The maximum number of groupings the given node supports is available through the Association
Command Class.


The Command Records Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.18: Command Records Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|
|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|Command = COMMAND_RECORDS_SUPPORTED_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 599




<!-- PAGE 601 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7.2** **Command** **Records** **Supported** **Report** **Command**


The Command Records Supported Report Command used to report information regarding the Command records.


Table 3.19: Command Records Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|
|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|Command = COMMAND_RECORDS_SUPPORTED_REPORT|
|Max command length|Max command length|Max command length|Max command length|Max command length|Max command length|V/C|Conf. Cmd|
|Free Command records 1|Free Command records 1|Free Command records 1|Free Command records 1|Free Command records 1|Free Command records 1|Free Command records 1|Free Command records 1|
|Free Command records 2|Free Command records 2|Free Command records 2|Free Command records 2|Free Command records 2|Free Command records 2|Free Command records 2|Free Command records 2|
|Max Command records 1|Max Command records 1|Max Command records 1|Max Command records 1|Max Command records 1|Max Command records 1|Max Command records 1|Max Command records 1|
|Max Command records 2|Max Command records 2|Max Command records 2|Max Command records 2|Max Command records 2|Max Command records 2|Max Command records 2|Max Command records 2|



**Configurable** **Cmd** **(1** **bit)**

|Configurable Cmd|Table 3.20: Configurable Command bit Functionality|
|---|---|
|Confgurable Cmd|Functionality|
|0|The local application has full control of the commands associated with<br>the grouping.<br>The commands can be monitored from a 2nd network node.<br>|
|1|The specifc commands associated with the grouping can be controlled<br>and monitored from a 2nd network node.<br>This option includes also the level feld used by the command _Transfer_<br>_Scene_ in the_ Controller Replication Command Class_. In this case the level<br>value is transferred via the command _Basic Set_ in the _Basic Command_<br>_Class_.|



**V/C** **(1** **bit)**

|V/C|Table 3.21: V/C bit Functionality|
|---|---|
|V/C|Functionality|
|0|Command type. A Z-Wave command can be added to the node<br>|
|1|Value type. A Value feld is specifed for a Node ID using the command<br>_Basic Set_ in the _Basic Command Class_. Level feld originates from the<br>command _Transfer Scene_ in the _Controller Replication Command Class_.|



**Max** **command** **length** **(6** **bits)**

If Configurable Cmd is equal to 0x0, the field SHOULD return 0x0.

If Configurable Cmd is equal to 0x1 the field SHOULD return the maximum length of a command
which can be associated to a node in a grouping. The minimum max command length allowed is 0x03.


Example:


A product reports a Max command length = 0x03. In this case the product can be programmed with
a Multilevel Switch Set, but not a Switch Multilevel Start Level Change.


Multilevel Switch Set has a command length of 3


Multilevel Switch Start Level Change has a command length of 4


**Free** **Command** **Records** **(16** **bits)**

The field specifies the current number of free Command Records which can be configured in the device
through the Command Configuration Set Command.


**Max** **Command** **records** **(16** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 600




<!-- PAGE 602 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The field specifies the maximum number of Command Records which can be configured in the device
through the Command Configuration Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 601




<!-- PAGE 603 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7.3** **Command** **Configuration** **Set** **Command**


The Command Configuration Set Command used to specify which commands SHOULD be sent to
nodes within a given Grouping identifier.

Every Command Configuration Set will utilize one Command record from the pool of free Command
records.

If the device has no free command records when receiving the Command Configuration Set, the
command will be ignored.


The Application on the node may alter the commands when needed.


Table 3.22: Command Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|
|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|Command = COMMAND_CONFIGURATION_SET<br>|
|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|
|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|
|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|
|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|
|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|
|…|…|…|…|…|…|…|…|
|Command byte n|Command byte n|Command byte n|Command byte n|Command byte n|Command byte n|Command byte n|Command byte n|



**Grouping** **identifier** **(8** **bits)**

This grouping identifier used to specify how nodes are grouped together. The grouping identifier values
MUST be a sequence starting from 1. This field MAY be ignored in case the node only supports one

group.


**Node** **ID** **(8** **bits)**

This field contains the node ID within the grouping specified, that should receive the command.


**Command** **length** **(8** **bits)**

This field specifies the complete command length (including command class and command identifiers).

Example: Switch Multilevel Set 0x20. The command length field MUST be equal to 0x03.

**Command** **Class** **Identifier** **(8** **bits)**

This field contains the identifier of the command class which should be sent to the Node ID. In case
the Configurable Cmd field is equal to 0x0 is this field and the following ignored and can therefore be
omitted.

In case the device has reported V/C=0x1, the Command Class and Command Identifiers MUST be
equal to Basic Set command.

**Command** **identifier** **(8** **bits)**

This field contains the identifier of the Command, which should be sent to the specified Node ID. In
case the Configurable Cmd field is equal to 0x0 is this field ignored and can therefore be omitted.

In case the device has reported V/C=0x1, the Command Class and Command Identifiers MUST be
equal to Basic Set Command.


**Command** **byte** **(N** **bytes)**

These fields contain the command parameters, which should be sent to the Node ID. In case the
Configurable Cmd field is equal to 0x0 is these fields ignored and can therefore be omitted.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 602




<!-- PAGE 604 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7.4** **Command** **Configuration** **Get** **Command**


The Command Configuration Get Command is used to request the commands specified for to a Node
ID within a given Grouping identifier.

The Command Configuration Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.23: Command Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|
|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|Command = COMMAND_CONFIGURATION_GET<br>|
|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|



**Grouping** **identifier** **(8** **bits)**

This group identifier used to specify how nodes are grouped together. The group identifier values
MUST be a sequence starting from 1. This field MUST be ignored in case the node only supports one

group.


**Node** **ID** **(8** **bits)**

This field specifies the node ID within the grouping.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 603




<!-- PAGE 605 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.7.5** **Command** **Configuration** **Report** **Command**


The Command Configuration Report Command used to report the commands specified for a Node
ID within a given Grouping identifier.


Table 3.24: Command Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|Command Class =<br>COMMAND_CLASS_ASSOCIATION_COMMAND_CONFIGURATION|
|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|Command = COMMAND_CONFIGURATION_REPORT<br>|
|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|
|First|Reserved|Reserved|Reserved|Reports to follow|Reports to follow|Reports to follow|Reports to follow|
|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|Command length<br>|
|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|Command Class identifer<br>|
|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|Command identifer|
|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|Command byte 1|
|…|…|…|…|…|…|…|…|
|Command byte N|Command byte N|Command byte N|Command byte N|Command byte N|Command byte N|Command byte N|Command byte N|



**Grouping** **identifier** **(8** **bits)**

This group identifier identifies the group. The group identifier values MUST be a sequence starting
from 1.


**Node** **ID** **(8** **bits)**

This field contains the node ID as requested in the Association Command Get.


**Reports** **to** **follow** **(4** **bits)**


This value indicates how many report frames left before transferring the entire list of commands.


**First** **(1** **bit)**

This field indicates that this report is the first report relating to a Grouping identifier/Node ID pair


**Command** **length** **(8** **bits)**

This field specifies the complete command length (including command class and command identifiers).

Example: Multilevel Switch Set 0x20. The command length field MUST be equal to 0x03.

**Command** **Class** **Identifier** **(8** **bits)**

This field contains the identifier of the command class which is sent to the Node ID.

In case the device has reported V/C=0x1, the Command Class and Command Identifiers MUST be
equal to Basic Set command

**Command** **identifier** **(8** **bits)**

This field contains the identifier of the Command which is sent to the specified Node ID.

In case the device has reported V/C=0x1, the Command Class and Command Identifiers MUST be
equal to Basic Set Command


**Command** **byte** **(N** **bytes)**

These fields contain the command parameter which is sent to the Node ID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 604