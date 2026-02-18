<!-- PAGE 833 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.4** **Multi** **Command** **Command** **Class,** **version** **1**


The Multi Command Command Class is used to bundle multiple commands in one encapsulation
Command. This command class may be used to limit the number of transmissions and to extend
battery lifetime.


**4.2.4.1** **Interoperability** **considerations**


**The** **“Answer-as-asked”** **requirement** **for** **Multi** **Command** **Encapsulation** **com-**
**mands** **carrying** **Get** **type** **commands** **has** **been** **OBSOLETED.**


This allows for a simple parser design in end devices, enables battery power savings and
supports the deployment of gateways with a part of the application logic placed in the
cloud.


Refer to section Section 4.2.4.2 for updated requirements text.


Older implementations may expect Get type commands to be answered with the same encapsulation.
CC:008F.01.00.31.001 However, responding nodes MUST NOT return answers with the same encapsulation if the destination
does not advertise the Multi Command Command Class as supported.


CC:008F.01.00.32.001 Supporting nodes SHOULD NOT return an answer Multi Command encapsulated if returning a single
command and SHOULD NOT return individually Multi Command encapsulated response commands.


**4.2.4.2** **Compatibility** **considerations**


**4.2.4.2.1** **Multi** **Command** **Support**


CC:008F.01.00.21.001 A node supporting this Command Class MUST be able to receive Multi Command Encapsulated
commands.


CC:008F.01.00.21.002 A supporting node MUST support the Multi Command Encapsulation of all command classes advertised as supported (for the received Security Class) except for command classes that are encapsulated
outside Multi Command. Refer to the encapsulation order defined in section Section 4.1.3.5.


CC:008F.01.00.21.003 A supporting node MUST respond to an encapsulated command requiring an answer to be returned,
e.g. a Get type Command.


CC:008F.01.00.21.004 A responding node MUST NOT return Multi Command encapsulated commands in response to encapsulated requests if the sender does not support the Multi Command Command Class.


**4.2.4.2.2** **Multi** **Command** **Control**


A node controls the Multi Command Command Class if it sends Multi Command Encapsulated
commands to supporting nodes.


CC:008F.01.00.23.001 It means that a node MAY issue unsolicited Multi Command Encapsulated commands without advertising support for the Multi Command Command Class.


CC:008F.01.00.51.001 A controlling node MUST verify that the destination supports Multi Command in its NIF before
using Multi Command Encapsulation or be explicitly enabled by another controller node to use Multi
Command encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 832




<!-- PAGE 834 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.4.2.3** **Node** **Information** **Frame** **(NIF)**


CC:008F.01.00.21.005 A supporting node MUST always advertise the Multi Command Command Class in its NIF, regardless
of the security bootstrapping outcome.


This allows other nodes bootstrapped on any security level to know that they can use the Multi
Command encapsulation with the supporting node.


**4.2.4.3** **Multi** **Command** **Encapsulated** **Command**


The Multi Command Encapsulated Command used to contain multiple Commands.


CC:008F.01.01.11.001 The encapsulated Commands MUST be executed in the order they are received. In case Get type
Commands in a Multi Command Encapsulated Command are received by a device, the Report type
Commands MUST be returned in the same order as the Get type Commands were received.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|Command Class = COMMAND_CLASS_MULTI_CHANNEL|
|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|Command = MULTI_CMD_ENCAP (0x01)|
|Number of Commands|Number of Commands|Number of Commands|Number of Commands|Number of Commands|Number of Commands|Number of Commands|Number of Commands|
|Command Length 1|Command Length 1|Command Length 1|Command Length 1|Command Length 1|Command Length 1|Command Length 1|Command Length 1|
|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|Command Class 1 (1 or 2 bytes)|
|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|Command 1|
|Data 1,1|Data 1,1|Data 1,1|Data 1,1|Data 1,1|Data 1,1|Data 1,1|Data 1,1|
|…|…|…|…|…|…|…|…|
|Data 1,N|Data 1,N|Data 1,N|Data 1,N|Data 1,N|Data 1,N|Data 1,N|Data 1,N|
|…|…|…|…|…|…|…|…|
|Command Length X|Command Length X|Command Length X|Command Length X|Command Length X|Command Length X|Command Length X|Command Length X|
|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|Command Class X (1 or 2 bytes)|
|Command X|Command X|Command X|Command X|Command X|Command X|Command X|Command X|
|Data X,1|Data X,1|Data X,1|Data X,1|Data X,1|Data X,1|Data X,1|Data X,1|
|…|…|…|…|…|…|…|…|
|Data X,N|Data X,N|Data X,N|Data X,N|Data X,N|Data X,N|Data X,N|Data X,N|



**Number** **of** **Commands** **(8** **bits)**

CC:008F.01.01.11.002 This field MUST specify the number of encapsulated commands.

CC:008F.01.01.12.001 This field SHOULD be set to a value greater than 1.

CC:008F.01.01.11.003 Each block carrying an encapsulated command MUST comprise the following fields:


      - Command length


      - Command Class


      - Command


      - Data


CC:008F.01.01.11.004 A supporting node MUST accept and execute all encapsulated commands contained in this command.


A supporting node MUST NOT discard any encapsulated command based on the number of commands
encapsulated in the command.


**Command** **Length** **(8** **bits)**

CC:008F.01.01.11.005 This field MUST specify the number of bytes occupied by the Command Class, Command and the
Data fields in the actual command block.


**Command** **Class** **(8** **bits** **or** **16** **bits)**

CC:008F.01.01.11.006 This field MUST specify the Command Class identifier of the encapsulated command. This field
MUST carry a normal Command Class (8 bits) or an Extended Command Class (16 bits).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 833




<!-- PAGE 835 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Command** **(8** **bits)**

CC:008F.01.01.11.007 This field MUST specify the Command identifier of the encapsulated Command.


**Data** **(N** **bytes)**

CC:008F.01.01.11.008 This field MUST carry the payload of the encapsulated command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 834