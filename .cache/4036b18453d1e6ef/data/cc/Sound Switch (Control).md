<!-- PAGE 1122 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.16** **Sound** **Switch** **Command** **Class,** **version** **1**


**6.2.16.1** **Mandatory** **node** **interview**


CL:0079.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.21.


Figure 6.21: Sound Switch Command Class interview


**6.2.16.2** **Minimum** **end** **user** **functionalities**


CL:0079.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.16.2.1** **Configure** **the** **sound** **switch**


CL:0079.01.31.02.1 The end user MUST be able to configure the volume and default tone at the supporting node. When
the end user performs this action, the issued command MUST comply with Table 6.23.


Table 6.23: Sound Switch::Configure the sound switch

|Field|Value|
|---|---|
|Command|SOUND_SWITCH_CONFIGURATION_SET<br>|
|Volume<br>|User defned among 0x00..0x64 or 0xFF<br>|
|Default Tone identifer|User defned among supported or 0x00|



**6.2.16.2.2** **Play/stop** **a** **selected** **or** **default** **tone**


CL:0079.01.31.03.1 The end user MUST be able to play the default tone, play a selected tone or stop playing a tone.
When the end user performs this action, the issued command MUST comply with Table 6.24.

|Table Field|6.24: Sound Switch::Play/stop a selected or default tone Value|
|---|---|
|Field|Value|
|Command<br>|SOUND_SWITCH_TONE_PLAY_SET<br>|
|Tone identifer|User defned among supported tones, 0x00 and 0xFF.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1121




<!-- PAGE 1123 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.16.3** **Node** **properties**


CL:0079.01.42.01.1 Controller SHOULD allow the end user to see/access the following properties:

     - (Last known) configured volume

     - (Last known) configured default tone


     - List of supported tones and their duration


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1122




<!-- PAGE 1124 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.17** **Thermostat** **Mode** **Command** **Class,** **version** **1-3**


**6.2.17.1** **Mandatory** **interview**


CL:0040.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.22.


Figure 6.22: Thermostat Mode Command Class interview


**6.2.17.2** **Minimum** **end** **user** **functionalities**


CL:0040.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.17.2.1** **Change** **mode**


CL:0040.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.25.

|Field|Table 6.25: Thermostat Mode::Change mode Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_MODE_SET<br>|
|Mode|User defned among supported modes|



CL:0040.01.31.03.1 The end user MUST be able to select between all supported modes by the supporting node, even if
the controlling node does not know what a given mode represents.


**6.2.17.3** **Node** **properties**


CL:0040.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:


     - Last known mode


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1123