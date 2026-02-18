<!-- PAGE 173 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.34** **Controller** **Replication** **Command** **Class,** **version** **1**


The Controller Replication Command Class is used to copy scene and group data to another controlling
node. The Command Class may be used in conjunction with a controller shift or when including a
new controller to the network. It is OPTIONAL to use this command class during a controller shift
or when including a new controller to the network.


**2.2.34.1** **Transfer** **group** **command**


This command is used to replicate mappings between Group ID and Node ID.


Table 2.169: Transfer Group Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|
|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|Command = CTRL_REPLICATION_TRANSFER_GROUP|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|



**Sequence** **Number** **(8** **bits)**


Sequence Number of this particular command.


**Group** **ID** **(8** **bits)**


Group ID of the group that the node is member of.


**NodeID** **(8** **bits)**

NodeID that belongs to the specified group.


**2.2.34.2** **Transfer** **Group** **Name** **Command**


This command is used to replicate group names.


Table 2.170: Transfer Group Name Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|
|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|Command = CTRL_REPLICATION_TRANSFER_GROUP_NAME|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|
|Group Name 1|Group Name 1|Group Name 1|Group Name 1|Group Name 1|Group Name 1|Group Name 1|Group Name 1|
|…|…|…|…|…|…|…|…|
|Group Name N|Group Name N|Group Name N|Group Name N|Group Name N|Group Name N|Group Name N|Group Name N|



**Sequence** **Number** **(8** **bits)**


Sequence Number of this particular command.


**Group** **ID** **(8** **bits)**

Group ID associated with a specific group.


**Group** **Name** **(N** **bytes)**

The Group Name fields contain the assign group name in ASCII characters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 172




<!-- PAGE 174 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.34.3** **Transfer** **scene** **command**


This command is used to replicate mappings between Scene ID and Node ID.


Table 2.171: Transfer Scene Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|
|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|Command = CTRL_REPLICATION_TRANSFER_SCENE|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|
|Level|Level|Level|Level|Level|Level|Level|Level|



**Sequence** **Number** **(8** **bits)**


Sequence Number of this particular command.


**Scene** **ID** **(8** **bits)**

The scene ID is the parameter used to link together the different devices that takes part of a scene.


**Node** **ID** **(8** **bits)**


The Node ID for a device that is part of the scene.


**Level** **(8** **bits)**

The level is the parameter used for the specified scene.


**2.2.34.4** **Transfer** **Scene** **Name** **Command**


This command is used to replicate scene names.


Table 2.172: Transfer Scene Name Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|Command Class = COMMAND_CLASS_CONTROLLER_REPLICATION|
|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|Command = CTRL_REPLICATION_TRANSFER_SCENE_NAME|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Scene Name 1|Scene Name 1|Scene Name 1|Scene Name 1|Scene Name 1|Scene Name 1|Scene Name 1|Scene Name 1|
|…|…|…|…|…|…|…|…|
|Scene Name N|Scene Name N|Scene Name N|Scene Name N|Scene Name N|Scene Name N|Scene Name N|Scene Name N|



**Sequence** **Number** **(8** **bits)**


Sequence Number of this particular command.


**Scene** **ID** **(8** **bits)**

Scene ID associated with a specific scene.


**Scene** **Name** **(N** **bytes)**

The Scene Name fields contain the assign scene name in ASCII characters.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 173