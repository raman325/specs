<!-- PAGE 760 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.39** **Remote** **Association** **Configuration** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT use this command class.


The Remote Association Configuration Command Class is used to configuration of the Remote Association Activation Command Class.


**Mandatory** **requirement:** Both ‘local’ and ‘remote’ node MUST implement the Association Command Class as ‘supported’. In addition the ‘local’ node MUST implement the Remote Association
Configuration Command Class as ‘supported’ and the node used to make the configuration (‘any node’
in the description below) MUST implement it as ‘controlled’.

The Remote Association Configuration Command Class is an addition to the functionality of the
existing Association Command Class.


Figure 3.26: Remote Association Configuration Command Class


The Remote Association Configuration Command Class enables a 1st node (Any node) to configure
a 2nd node (Local node) to issue a Remote Association Activate Command to a 3rd node (Remote
node), which instructs the 3rd node to activate one of its locally stored association group identifiers
as defined by its Association Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 759




<!-- PAGE 761 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.39.1** **Remote** **Association** **Configuration** **Set** **Command**


The Remote Association Configuration Set Command links two nodes’ ‘Association Command Class’
defined grouping identifiers together. It allows one node (local node) to use its grouping identifiers to
control a second node’s (remote node) grouping identifiers, using the Remote Association Activation
Command Class.


Table 3.146: Remote Association Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|
|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_SET<br>|
|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|
|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|
|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|



**Local** **Grouping** **identifier** **(8** **bits)**

Like in the Association Command Class, the Local Grouping identifier is used to specify the grouping
identifier on the local node.

A Local grouping identifier = 0x0 will erase all links between local and remote grouping identifiers.


**Remote** **NodeID** **(8** **bits)**


This NodeID used to specify the Node, which should receive the Remote Association Activate Command.

A NodeID = 0x0 will remove a link between the specified local grouping identifier and a remote
grouping identifier.

**Remote** **Grouping** **identifier** **(8** **bits)**

This group identifier used to specify the grouping identifier on the remote node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 760




<!-- PAGE 762 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.39.2** **Remote** **Association** **Configuration** **Get** **Command**


The Remote Association Configuration Get Command is used to request the link between a Local
Grouping identifier and a Remote Grouping identifier on a node.

The Remote Association Configuration Report Command MUST be returned in response to this
command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.147: Remote Association Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|
|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_GET<br>|
|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|



**Local** **Grouping** **identifier** **(8** **bits)**

Like in the Association Command Class, the Local Grouping identifier is used to specify the grouping
identifier on the local node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 761




<!-- PAGE 763 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.39.3** **Remote** **Association** **Configuration** **Report** **Command**


The Remote Association Configuration Report Command returns the remote NodeID and the grouping
identifier.


Table 3.148: Remote Association Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION|
|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|Command = REMOTE_ASSOCIATION_CONFIGURATION_REPORT<br>|
|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|Local Grouping identifer|
|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|Remote NodeID<br>|
|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|Remote Grouping identifer|



**Local** **Grouping** **identifier** **(8** **bits)**

This group identifier used to specify the grouping identifier on the local node


**Remote** **NodeID** **(8** **bits)**


This NodeID used to specify the remote node that the Remote Association Activate Command is sent
to. If no link is established between the Local Grouping Identifier and a Remote Grouping Identifier,
the Remote NodeID will return zero (0x0)

**Remote** **Grouping** **identifier** **(8** **bits)**

This Remote grouping identifier used to specify the grouping identifier on the remote node that should
be activated.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 762