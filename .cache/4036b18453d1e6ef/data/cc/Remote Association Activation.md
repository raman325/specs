<!-- PAGE 759 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.38** **Remote** **Association** **Activation** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT use this command class.


The Remote Association Activation Command Class is used to remote activations of Association
grouping identifiers in other nodes.


**Mandatory** **requirement:** Both ‘local’ and ‘remote’ node MUST implement the Association Command Class as illustrated below. In addition the ‘local’ node MUST implement the Remote Association
Configuration Command Class as ‘Supported’.

The Remote Association Activation Command Class and the Remote Association Configuration Command Class are additions to the functionality to the existing Association Command Class.


Figure 3.25: Remote Association Activation Command Class


The Remote Association Configuration Command Class enables a 1st node (any node) to configure a
2nd node (local node) to issue a Remote Association Activate Command to a 3rd node (remote node),
which instruct the 3rd node to activate one of its locally stored association group identifiers as defined
by the Association Command Class.


**3.2.38.1** **Remote** **Association** **Activate** **Command**


The Remote Association Activate Command is used to instruct a ’remote’ node to activate one of its
locally stored association group identifiers as defined by the Association Command Class. This will
subsequently generate a number of Commands being issued from the ‘remote node to the NodeIDs
associated to the grouping identifier.


Table 3.145: Remote Association Activate Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|Command Class = COMMAND_CLASS_REMOTE_ASSOCIATION_ACTIVATE|
|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|Command = REMOTE_ASSOCIATION_ACTIVATE<br>|
|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|Grouping identifer|



**Grouping** **identifier** **(8** **bits)**

This group identifier used to specify the grouping identifier on the remote node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 758