<!-- PAGE 467 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.100** **Sound** **Switch** **Command** **Class,** **version** **1**


The Sound Switch Command Class is used to manage nodes with a speaker or sound notification
capability. It can be used for a doorbell, alarm clock, siren or any device issuing sound notifications.


**2.2.100.1** **Terminology**


A **Sound** **Switch** is a sound notification device with pre-recorded tones. A tone can be a short sound
effect as well as an entire song. The **volume** setting can be configured and the node will subsequently
play tones using the configured volume for any tone. A **default** **tone** can also be configured, allowing
the Sound Switch to play same sound when controlled by a node without the ability to select between

tones.


A Sound Switch node advertises a **name** and **duration** for each tone. This information is used to
guide an end-user in its tone selection and helps controlling nodes to know when the tone is finished
playing.


**2.2.100.2** **Compatibility** **Considerations**


The Sound Switch Command Class is an actuator control Command Class. Refer to Section 2.1.6.


CC:0079.01.00.21.001 A node supporting this Command Class MUST support at least 1 tone.

CC:0079.01.00.21.002 The implemented tone identifier values MUST be in a sequence starting from 1, i.e. a node supporting
10 tones MUST accept Tone Identifiers in the range 1..10.


**2.2.100.3** **Sound** **Switch** **Tones** **Number** **Get** **Command**


This command is used to request the number of tones supported by the receiving node.


CC:0079.01.01.11.001 The Sound Switch Tones Number Report Command MUST be returned in response to this command.


CC:0079.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0079.01.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|Command = SOUND_SWITCH_TONES_NUMBER_GET (0x01)|



**2.2.100.4** **Sound** **Switch** **Tones** **Number** **Report** **Command**


This command is used to advertise the number of tones supported by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|Command = SOUND_SWITCH_TONES_NUMBER_REPORT (0x02)|
|Supported Tones|Supported Tones|Supported Tones|Supported Tones|Supported Tones|Supported Tones|Supported Tones|Supported Tones|



**Supported** **Tones** **(8** **bits)**

CC:0079.01.02.11.001 This field MUST be set to the total amount of supported tones.

CC:0079.01.02.11.003 This field MUST be in the range 1..254.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 466




<!-- PAGE 468 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.100.5** **Sound** **Switch** **Tone** **Info** **Get** **Command**


This command is used to query the information associated to a tone at a supporting node.


CC:0079.01.03.11.001 The Sound Switch Tone Info Report Command MUST be returned in response to this command.


CC:0079.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:0079.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|Command = SOUND_SWITCH_TONE_INFO_GET (0x03)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|



**Tone** **Identifier** **(8** **bits)**

This field is used to specify the requested Tone Identifier.

CC:0079.01.03.11.004 The implemented tone identifier values MUST be in a sequence starting from 1, i.e. a node supporting
10 tones MUST accept Tone Identifiers in the range 1..10.

CC:0079.01.03.11.005 A sending node MUST specify a Tone Identifier that is supported by a receiving node, i.e. in the
range 1..{Total number of supported tones}.

CC:0079.01.03.11.006 A node receiving this command for an unsupported Tone Identifier or for Tone Identifier 0x00 MUST
return a zero duration and a zero length name.


**2.2.100.6** **Sound** **Switch** **Tone** **Info** **Report** **Command**


This command is used to advertise the information associated to a tone at a supporting node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|Command = SOUND_SWITCH_TONE_INFO_REPORT (0x04)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|
|Tone Duration 1|Tone Duration 1|Tone Duration 1|Tone Duration 1|Tone Duration 1|Tone Duration 1|Tone Duration 1|Tone Duration 1|
|Tone Duration 2|Tone Duration 2|Tone Duration 2|Tone Duration 2|Tone Duration 2|Tone Duration 2|Tone Duration 2|Tone Duration 2|
|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|Name Length|
|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|
|…|…|…|…|…|…|…|…|
|Name N|Name N|Name N|Name N|Name N|Name N|Name N|Name N|



**Tone** **Identifier** **(8** **bits)**

This field is used to advertise the Tone Identifier for which the associated information is being advertised.


**Tone** **Duration** **(16** **bits)**

This field is used to advertise duration of the Tone Identifier.

CC:0079.01.04.11.001 This field MUST indicate the time in seconds it takes to play the actual Tone Identifier.

CC:0079.01.04.11.002 This field MUST be set to 0 if the Tone Identifier is set to 0x00 or a value higher than the total
number of supported tones advertised in the Sound Switch Tones Number Report Command.


**Name** **Length** **(8** **bits)**

This field indicates the length in bytes of the Name field.


CC:0079.01.04.11.003


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 467




<!-- PAGE 469 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be in the range 1..255 if the Tone Identifier is supported.

CC:0079.01.04.11.004 This field MUST be set to 0 if the Tone Identifier is set to 0x00 or a value higher than the total
number of supported tones advertised in the Sound Switch Tones Number Report Command.


**Name** **(N** **bytes)**

This field is used to indicate the assigned name or label for the actual Tone Identifier.

CC:0079.01.04.11.005 The length of this field in bytes MUST comply with the advertised value in the Name Length field.
This field MUST be omitted if the Name Length field is set to 0.

CC:0079.01.04.11.006 The field MUST be formatted as a byte array with no zero termination.


CC:0079.01.04.11.007 The characters MUST be encoded in UTF-8 format.


**2.2.100.7** **Sound** **Switch** **Configuration** **Set** **Command**


This command is used to set the configuration for playing tones at the supporting node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|Command = SOUND_SWITCH_CONFIGURATION_SET (0x05)|
|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|
|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|



**Volume** **(8** **bits)**

This field is used to specify the volume at which the node will play tones.

The encoding of the Volume field MUST be according to Table 2.516.


Table 2.516: Sound Switch Configuration Set::Volume encoding

|Value|Description|
|---|---|
|0 (0x00)|This value MUST indicate an Of/Mute volume setting (0%)|
|1..100 (0x01..0x64)|These values MUST indicate the actual volume setting from respectively<br>1% to 100%.<br>A supporting node MAY implement fewer than 100 hardware level. In<br>this case, mapping of hardware levels MUST be monotonous, i.e. a higher<br>value MUST be mapped to either the same or a higher hardware level|
|255 (0xFF)|This value MUST indicate to restore most recent non-zero volume setting.<br>This value MUST be ignored if the current volume is not zero (0x00).<br>This value MAY be used to set the Default Tone Identifer and do not<br>modify the volume setting|



CC:0079.01.05.11.005 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.

**Default** **Tone** **Identifier** **(8** **bits)**

This field is used to specify the Default Tone. This Tone will be played if receiving the Sound Switch
Tone Play Set Command for an unsupported value or for the 0xFF value.


CC:0079.01.05.11.006 The value 0x00 MUST indicate that the receiving node MUST NOT update its current default tone
and the command is sent to configure the volume only.


CC:0079.01.05.11.007 Values in the range 1..{Total number of supported tones} MUST indicate that the receiving node
MUST use the specified Identifier as Default Tone.


Values higher than the Total number of supported tones advertised in the Sound Switch Tones Number
CC:0079.01.05.11.008 Report Command MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 468




<!-- PAGE 470 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.100.8** **Sound** **Switch** **Configuration** **Get** **Command**


This command is used to request the current configuration for playing tones at the supporting node.

CC:0079.01.06.11.001 The Sound Switch Configuration Report Command MUST be returned in response to this command.


CC:0079.01.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:0079.01.06.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|Command = SOUND_SWITCH_CONFIGURATION_GET (0x06)|



**2.2.100.9** **Sound** **Switch** **Configuration** **Report** **Command**


This command is used to advertise the current configuration for playing tones at the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|Command = SOUND_SWITCH_CONFIGURATION_REPORT (0x07)|
|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|Volume<br>|
|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|Default Tone Identifer|



**Volume** **(8** **bits)**

This field is used to advertise the current volume setting at the sending node.

CC:0079.01.07.11.001 This field MUST be in the range 0..100. Values in the range 0..100 MUST indicate the current volume
percentage.

**Default** **Tone** **Identifier** **(8** **bits)**

This field is used to advertise the current configured Default Tone. This Tone Identifier will be played
if receiving a Sound Switch Tone Play Set Command for an unsupported value or for the 0xFF value.

CC:0079.01.07.11.002 This field MUST be in the range 1..{Total number of supported Tones}.


**2.2.100.10** **Sound** **Switch** **Tone** **Play** **Set** **Command**


This command is used to instruct a supporting node to play (or stop playing) a tone.

CC:0079.01.08.11.001 The supporting node MUST play the specified tone immediately when receiving this command.

CC:0079.01.08.11.002 A node already playing a tone MUST interrupt the current tone and start playing the tone specified
in this command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|



**Tone** **Identifier** **(8** **bits)**

CC:0079.01.08.11.003 This field is used to specify the tone that the receiving node MUST play.

CC:0079.01.08.11.004 This field MUST be encoded according to Table 2.517.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 469




<!-- PAGE 471 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.517: Sound Switch Tone Play Set::Tone Identifier encoding

|Value|Description|
|---|---|
|0x00|No Tone MUST be played.<br>A supporting node MUST stop playing any tone when receiving this value.<br>|
|0x01..0xFE|A supporting node MUST play the specifed Tone identifer using the<br>confgured volume setting.<br>A node receiving a non-supported Tone Identifer (higher than the To-<br>tal number of supported tones) MUST play the default tone using the<br>confgured volume setting.<br>|
|0xFF|The supporting node MUST play the default tone using the confgured<br>volume setting.|



**2.2.100.11** **Sound** **Switch** **Tone** **Play** **Get** **Command**


This command is used to request the current tone being played by the receiving node.


CC:0079.01.09.11.001 The Sound Switch Tone Play Report Command MUST be returned in response to this command.


CC:0079.01.09.11.002 This command MUST NOT be issued via multicast addressing.


CC:0079.01.09.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|Command = SOUND_SWITCH_TONE_PLAY_GET (0x09)|



**2.2.100.12** **Sound** **Switch** **Tone** **Play** **Report** **Command**


This command is used to advertise the current tone being played by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|



**Tone** **Identifier** **(8** **bits)**


CC:0079.01.0A.11.001
This field MUST indicate which tone is currently being played by the sending node. This field MUST
be in the range 0..{Total number of supported tones}.


CC:0079.01.0A.11.002 The value 0 MUST indicate that no Tone is currently being played.

This field MUST be set to 0x00 by a sending node if the configured volume is 0x00 (muted).


CC:0079.01.0A.11.003 Values in the range 1..{Total number of supported tones} MUST indicate the Tone that is currently
being played.


CC:0079.01.0A.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 470

---

<!-- PAGE 472 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.101** **Sound** **Switch** **Command** **Class,** **version** **2**


The Sound Switch Command Class is used to manage nodes with a speaker or sound notification
capability. It can be used for a doorbell, alarm clock, siren or any device issuing sound notifications.


**2.2.101.1** **Compatibility** **Considerations**


The Sound Switch Command Class is backwards compatible with the Sound Switch Command Class,

version 1.

CC:0079.02.00.21.001 All Commands and fields not mentioned in this version MUST remain unchanged from the Sound
Switch Command Class, version 1.


This version extends the following commands to allow a controlling node to modify the volume setting
only for a single Tone Play Set Command:


      - Sound Switch Tone Play Set Command


      - Sound Switch Tone Play Report Command


**2.2.101.2** **Sound** **Switch** **Tone** **Play** **Set** **Command**


This command is used to instruct a supporting node to play (or stop playing) a tone.

CC:0079.02.08.11.001 The supporting node MUST play the specified tone immediately when receiving this command.

CC:0079.02.08.11.002 A node already playing a tone MUST interrupt the current tone and start playing the tone specified
in this command.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|Command = SOUND_SWITCH_TONE_PLAY_SET (0x08)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|
|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|



CC:0079.02.08.11.003 All fields not described below MUST remain unchanged from version 1.


**Play** **Command** **Tone** **Volume** **(8** **bits)**

This field is used to configure the volume for the actual Play Command.

CC:0079.02.08.11.005 The volume setting configured with the Sound Switch Configuration Set Command MUST remain

CC:0079.02.08.11.006 unchanged by this command and this field MUST be used for the volume of the actual tone that will
start playing.

CC:0079.02.08.11.007 This field MUST be set to 0x00 and ignored by a receiving node if the Tone identifier field is set to
0x00.

CC:0079.02.08.11.008 The encoding of this field MUST be according to Table 2.518.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 471




<!-- PAGE 473 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Table 2.518: encoding Value|Sound Switch Tone Play Set::Play Command Volume Description|
|---|---|
|Value|Description<br>|
|0 (0x00)|This value MUST indicate to use the confgured volume at the node<br>(Sound Switch Confguration Set Command).|
|1..100 (0x01..0x64)|These values MUST indicate the actual volume setting from respec-<br>tively 1% to 100% to use for the Play Set Command<br>This value SHOULD be used for critical applications (e.g. security<br>alarm) where it is important to have the sound played even when<br>the device is muted.|
|255 (0xFF)|This value MUST indicate to use most recent non-zero volume set-<br>ting if the current volume is muted (0x00).<br>If the current confgured volume is not muted (>0x00), this value<br>MUST indicate to use the confgured current volume at the node<br>(Sound Switch Confguration Set Command)<br>This value SHOULD be used only for critical application (e.g. se-<br>curity alarm) where it is important to have the sound played even<br>when the device is muted.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.101.3** **Sound** **Switch** **Tone** **Play** **Report** **Command**


This command is used to advertise the current tone being played by the sending node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|Command Class = COMMAND_CLASS_SOUND_SWITCH|
|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|Command = SOUND_SWITCH_TONE_PLAY_REPORT (0x0A)<br>|
|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|Tone Identifer|
|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|Play Command Tone Volume|



All fields not described below MUST remain unchanged from version 1.


**Play** **Command** **Tone** **Volume** **(8** **bits)**

CC:0079.02.0A.11.001 This field MUST advertise the actual playing volume represented with the value from 0x00 …0x64 (0
… 100%). The values 0x00 and 0x64 MUST represent mute and maximum volume, respectively.

This field MUST be set to 0x00 if the Tone Identifier field is set to 0x00.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 472