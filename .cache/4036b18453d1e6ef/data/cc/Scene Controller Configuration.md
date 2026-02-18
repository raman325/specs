<!-- PAGE 396 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.85** **Scene** **Controller** **Configuration** **Command** **Class,** **version** **1**


The Scene Controller Configuration Command Class is used to configure nodes launching scenes using
their association groups


**2.2.85.1** **Compatibility** **Considerations**


A node supporting this Command Class MUST support 255 scene IDs (Scene ID 1 to 255). The Scene
ID 0 MUST NOT be supported..


A node supporting this Command Class MUST support the Association Command Class, version 1

or newer.


A node supporting this Command Class MUST issue Scene Activation Set Command via its association

groups.


**2.2.85.2** **Scene** **Controller** **Configuration** **Set** **Command**


This command is used to configure settings for a given physical item on the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|
|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|Command = SCENE_CONTROLLER_CONF_SET|
|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|



**Group** **ID** **(8** **bits)**

This field is used to specify an Association Group Identifier.

The grouping identifier is mapped into a physical item e.g. a push button on the device in question.
The grouping identifier values MUST be a sequence starting from 1. The Association Supported
Groupings Get Command may be used to request the number of groupings that a node supports.


A sending node SHOULD NOT specify Group ID 1 as it is reserved for the Lifeline association group.


**Scene** **ID** **(8** **bits)**

This field is used to specify the Scene ID that MUST be associated with the actual grouping identifier.


Values in the range 1..255 MUST indicate that the receiving node MUST associate the Scene ID and
Dimming Duration values to the actual Association Group ID. The supporting node MUST set the
Scene ID value indicated by this field in the Scene Activation Set Command when issuing it via the
actual Group ID.

The value 0 MUST indicate that the receiving node MUST disable an associated scene for the specified
Group ID.


**Dimming** **Duration** **(8** **bits)**

This field is used to specify what value the supporting node MUST set in the Dimming Duration field
of the Scene Activation Set Command when issuing it via the actual Group ID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 395




<!-- PAGE 397 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.85.3** **Scene** **Controller** **Configuration** **Get** **Command**


This command is used to request the settings for a given association grouping identifier or the active
settings.

The Scene Controller Configuration Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|
|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|Command = SCENE_CONTROLLER_CONF_GET|
|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|



**Group** **ID** **(8** **bits)**

This field is used to request scene settings configured for an actual Association Group Identifier.

Values in the range 1..255 MUST indicate the requested Group Identifier.

The value 0 MUST indicate that the receiving node MUST return the currently active Group Identifier
and Scene ID (last activated group/scene).

A node receiving a non-supported group or having no currently active Group Identifier SHOULD
return a report for Group ID 0.


**2.2.85.4** **Scene** **Controller** **Configuration** **Report** **Command**


This command is used to advertise the current scene controller settings.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|Command Class = COMMAND_CLASS_SCENE_CONTROLLER_CONF|
|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|Command = SCENE_CONTROLLER_CONF_REPORT|
|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|Group ID|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|



**Group** **ID** **(8** **bits)**

This field is used to advertise the actual Association Group Identifier for which the settings are being
advertised.


**Scene** **ID** **(8** **bits)**

This field is used to specify the Scene ID that is associated with the actual grouping identifier.

Value in the range 1..255 MUST indicate the actual Scene ID setting for the specified grouping
identifier.


The value 0 MUST indicate that the Group ID/Scene ID is disabled.


**Dimming** **Duration** **(8** **bits)**

This field is used to specify the Dimming Duration that is associated with the actual grouping identifier.

If the actual Group ID/Scene ID is disabled, a sending node SHOULD set this field to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 396