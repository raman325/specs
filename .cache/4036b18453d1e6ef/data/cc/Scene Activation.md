<!-- PAGE 392 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.83** **Scene** **Activation** **Command** **Class,** **version** **1**


The Scene Activation Command Class used for launching scenes in a number of actuator nodes e.g.
another scene-controlling unit, a multilevel switch, a binary switch etc.


**2.2.83.1** **Compatibility** **Considerations**


A node supporting this Command Class MUST also support the Scene Actuator Configuration Command Class.

This command class requires an initial configuration of the scenes to be launched by the Scene Actuator
Configuration Set.

Since a common identifier that is sent out, multicast addressing may be used. Multicast addressing
may eliminate the potential popping effect which could be the result if individual Set Commands were
send out to a large number of nodes distributed over a vast area. The multicast transmission MUST
be followed by individual singlecast transmissions to ensure all the nodes have received the command.


**2.2.83.2** **Scene** **Activation** **Set** **Command**


This command is used to activate the setting associated to the scene ID.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|Command Class = COMMAND_CLASS_SCENE_ACTIVATION|
|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|Command = SCENE_ACTIVATION_SET|
|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|Scene ID|
|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|Dimming Duration|



**Scene** **ID** **(8** **bits)**

This field is used to specify the Scene ID that the receiving node MUST activate

This field MUST be in the range 1..255.


**Dimming** **Duration** **(8** **bits)**

This field MUST specify the time that the transition from the current level to the target level (indicated
by the Scene ID) should take.

Supporting actuator nodes without duration capabilities MUST ignore this field.


Supporting actuator nodes with a duration capabilities SHOULD respect the indicated dimming
duration to reach the target level.

This field MUST be encoded according to Table 2.484.

|Value|Table 2.484: Scene Activation Set::Dimming Duration encoding Description|
|---|---|
|Value|Description|
|0x00|Instantly|
|0x01..0x7F|Obtain dimming durations from 1 second (0x01) to 127 seconds (0x7F) in 1-second<br>resolution|
|0x80..0xFE|Specify dimming durations from 1 minute (0x80) to 127 minutes (0xFE) in 1-minute<br>resolution.<br>|
|0xFF|Specify dimming duration confgured by the Scene Actuator Confguration Set and<br>Scene Controller Confguration Set Command depending on device used.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 391