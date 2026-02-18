<!-- PAGE 393 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.84** **Scene** **Actuator** **Configuration** **Command** **Class,** **version** **1**


The Scene Actuator Configuration Command Class is used to configure scenes settings for a node
supporting an actuator Command Class, e.g. a multilevel switch, binary switch etc.


**2.2.84.1** **Compatibility** **Considerations**


A node supporting this Command Class MUST support 255 Scene IDs (Scene ID 1 to 255). The
Scene ID 0 MUST NOT be supported..


**2.2.84.2** **Scene** **Actuator** **Configuration** **Set** **Command**


This command is used to associate the specified scene ID to the defined actuator settings.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|
|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|Command = SCENE_ACTUATOR_CONF_SET (0x01)|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|
|Override|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Level|Level|Level|Level|Level|Level|Level|Level|



**Scene** **ID** **(8** **bits)**

This field is used to specify the Scene ID to be associated with the current actuator settings.

This field MUST be in the range 1..255.


**Dimming** **Duration** **(8** **bits)**

This field MUST specify the time it MUST take to reach the target level associated to the actual
Scene ID.


A receiving node always starts from current level. The dimming duration MUST be the same independently of the number of levels to be changed.

Supporting actuator nodes without duration capabilities MUST ignore this field.


Supporting actuator nodes with duration capabilities SHOULD respect the indicated duration to reach
the target level.

This field MUST be encoded according to Table 2.9.


**Override** **(1** **bit)**

This field is used to specify if the current actuator settings MUST be used as settings for the actual
Scene ID.

If this field is set to 0, the current actuator settings at the supporting node MUST be associated to
the actual Scene ID. In this case, the Level field MUST be ignored.

If this field is set to 1, the value indicated by the Level field MUST be associated to the actual Scene
ID.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Level** **(8** **bits)**

This field is used to specify the actuator setting that MUST be used as setting for the actual Scene ID.
This field MUST correspond and be interpreted as the Value field of the Basic Set Command. i.e. the
supporting node receiving a Scene Activation Set for the actual Scene ID specified in this command
MUST react as if it had received a Basic Set Command with the Value field set to the value indicated
by this field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 392




<!-- PAGE 394 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.84.3** **Scene** **Actuator** **Configuration** **Get** **Command**


This command is used to request the settings for a given scene identifier or for the scene currently
active.

The Scene Actuator Configuration Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|
|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|Command = SCENE_ACTUATOR_CONF_GET (0x02)|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|



**Scene** **ID** **(8** **bits)**

This field is used to specify the requested Scene ID settings.


Values in the range 1..255 MUST indicate that the receiving node MUST return settings associated
to the actual Scene ID..


The value 0 MUST indicate that the current active scene (if any).


**2.2.84.4** **Scene** **Actuator** **Configuration** **Report** **Command**


This command is used to advertise the settings associated to a scene identifier.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|Command Class = COMMAND_CLASS_SCENE_ACTUATOR_CONF|
|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|Command = SCENE_ACTUATOR_CONF_REPORT (0x03)|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Level|Level|Level|Level|Level|Level|Level|Level|
|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|



**Scene** **ID** **(8** **bits)**

This field is used to specify the actual Scene ID for which the settings are being advertised.


Values in the range 1..255 MUST indicate an actual Scene ID.


The value 0 MUST indicate that no scene is currently active at the sending node and no scene setting
is advertised in this command. In this case, the Level and Dimming Duration fields SHOULD be
ignored.


**Level** **(8** **bits)**

This field is used to advertise the actuator setting that MUST be used by the node when activating
the actual Scene ID.

The value advertised by the sending node MUST correspond to the format of the Value field when
returning a Basic Report Command.


**Dimming** **Duration** **(8** **bits)**

This field MUST specify the time it MUST take to reach the target level associated to the actual
Scene ID..

Supporting actuator nodes without duration capabilities MUST ignore this field and SHOULD set it
to 0x00.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 393




<!-- PAGE 395 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Supporting actuator nodes with duration capabilities SHOULD respect the indicated duration to reach
the target level.

This field MUST be encoded according to Table 2.485.


Table 2.485: Scene Actuator Configuration Report::Dimming Duration encoding

|Dimming Duration|Description|
|---|---|
|0x00|Instantly|
|0x01..0x7F|Dimming durations from 1 second (0x01) to 127 seconds (0x7F) in<br>1-second resolution.|
|0x80-0xFE|Specify dimming durations from 1 minute (0x80) to 127 minutes (0xFE)<br>in 1-minute resolution.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 394