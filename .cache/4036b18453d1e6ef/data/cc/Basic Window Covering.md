<!-- PAGE 114 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.16** **Basic** **Window** **Covering** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED**


New implementations MUST NOT support this command class.


New window covering device implementations SHOULD support the _Window_ _Covering_ _Command_
_Class,_ _version_ _1_ .


This section contains Commands that may be used to control a Basic Window Covering Command
Class.


**2.2.16.1** **Basic** **Window** **Covering** **Start** **Level** **Change** **Command**


This command is used to start moving drapes, shades, blinds in a given direction. The speed of the
movement is implementation specific.


Table 2.87: Basic Window Covering Start Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|
|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_START_LEVEL_CHANGE|
|Reserved|Open /<br>Close|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



**Open/Close** **(1** **bit)** If the Open/Close bit is set to 0 the window covering SHOULD open. If field
is set to 1 the window covering SHOULD close.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**2.2.16.2** **Basic** **Window** **Covering** **Stop** **Level** **Change** **Command**


This command is used to stop moving drapes, shades, blinds in a given direction.


Table 2.88: Basic Window Covering Stop Level Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|Command Class = COMMAND_CLASS_BASIC_WINDOW_COVERING|
|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|Command = BASIC_WINDOW_COVERING_STOP_LEVEL_CHANGE|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 113