<!-- PAGE 77 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.9** **Anti-theft** **Unlock** **Command** **Class,** **version** **1**


This Command Class is used to unlock a device that has been locked by the Anti-theft Command
Class. Controllers that do not lock devices still can control this command class in order to unlock

devices that have been locked by previous owners.


**2.2.9.1** **Compatibility** **Considerations**


A node supporting this Command Class MUST also support the Anti-Theft Command Class, version
3.


**2.2.9.1.1** **Multi** **Channel** **Considerations**


Multi Channel End Points SHOULD NOT support the Anti-Theft Unlock Command Class.


**2.2.9.2** **Anti-Theft** **Unlock** **State** **Get** **Command**


This command is used to request the locked/unlocked state of the node.


The Anti-Theft Unlock State Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.46: Anti-theft Unlock State Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|
|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_GET (0x01)|



**2.2.9.3** **Anti-Theft** **Unlock** **State** **Report** **Command**


This command is used to advertise the current locked/unlocked state of the node with some additional
information.


Table 2.47: Anti-theft Unlock State Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|
|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|Command = COMMAND_ANTITHEFT_UNLOCK_STATE_REPORT (0x02)|
|Reserved|Reserved|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Re-<br>stricted|State|
|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|
|…|…|…|…|…|…|…|…|
|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|
|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|Manufacturer ID (MSB)|
|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|Manufacturer ID (LSB)|
|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|
|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|



**State** **(1** **bit)**

This field MUST indicate the current locked/unlocked state of the device.


The value 0 MUST indicate that the supporting node is unlocked.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 76




<!-- PAGE 78 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 1 MUST indicate that the supporting node is locked.

The value 0x01 from the _Anti-theft_ _Protection_ _Status_ field from the Anti-theft Report Command
MUST be mapped to the value 0 for this field

The values 0x02 and 0x03 from the _Anti-theft_ _Protection_ _Status_ field from the Anti-theft Report
Command MUST be mapped to the value 1 for this field


**Restricted** **(1** **bit)**

This field MUST indicate if the node currently runs in restricted mode.


The value 0 MUST indicate that the supporting node is not restricted.


The value 1 MUST indicate that the supporting node is restricted.

This field MUST be set to 0 if the _State_ field is set to 0.

The values 0x01 and 0x02 from the _Anti-theft_ _Protection_ _Status_ field from the Anti-theft Report
Command MUST be mapped to the value 0 for this field

The value 0x03 from the _Anti-theft_ _Protection_ _Status_ field from the Anti-theft Report Command
MUST be mapped to the value 1 for this field


**Anti-theft** **Hint** **Length** **(4** **bits)**

This field MUST indicate the length (in byte) of the _Anti-Theft_ _Hint_ field.

This field MUST be in the range 0..10.

If the state field is set to 0, a sending node MUST set this field to 0.

If the state field is set to 1, a sending node MUST advertise the length of the Anti-Theft Hint field
that was used to lock the node.


**Anti-theft** **Hint** **(N** **bytes)**

This field is used as an identifier or key value to help retrieving the Magic Code.

The length of this field in byte MUST be according to the _Anti-Theft_ _Hint_ _Length_ field. This field
MUST be omitted if the Anti-Theft Hint Length field is set to 0.

A supporting node MUST advertise the value that was specified in the Anti-Theft Set Command
when it got locked.


**Manufacturer** **ID** **(2** **bytes)**

This field describes the Z-Wave Manufacturer ID of the company’s product that has locked the node.

This field MUST be set to 0x00 if the state field is set to 0.

If the state field is set to 1 and a Z-Wave Manufacturer listed in [32] has locked the node, this field
will advertise the Manufacturer ID that was provided in the Anti-theft Set Command.

If the state field is set to 1 and an entity who’s not a Z-Wave Manufacturer listed in [32] has locked
the node, this field will be set to 0x00.


**Z-Wave** **Alliance** **locking** **entity** **ID** **(2** **bytes)**

This field advertises a unique identifier for the entity that has locked the node. Anti-Theft Command
Class, list of assigned Locking Entity IDs registry contains the valid assigned IDs with additional
information about the entity.


Contact the Z-Wave Alliance to get an ID assigned. With this ID, the Z-Wave alliance will be able
to provide the following information:


 - Name of the organization


 - Contact phone for unlock information


 - Optional website/url


 - Optional unlock support email address


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 77




<!-- PAGE 79 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be set to 0x00 if the state field is set to 0.

If the state field is set to 1, this field MUST advertise the ID that was provided in the Anti-Theft Set
Command.


**2.2.9.4** **Anti-Theft** **Unlock** **Set** **Command**


This command is used to unlock a node that is currently locked.


A receiving node MUST ignore this command if its current state is unlocked.


Table 2.48: Anti-theft Unlock Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|Command Class = COMMAND_CLASS_ANTITHEFT_UNLOCK (0x7E)|
|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|Command = COMMAND_ANTITHEFT_UNLOCK_SET (0x03)|
|Reserved|Reserved|Reserved|Reserved|Magic code length|Magic code length|Magic code length|Magic code length|
|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|
|…|…|…|…|…|…|…|…|
|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|



**Magic** **Code** **Length** **(4** **bits)**

This field MUST indicate the length in byte of the Magic Code field.

This field MUST be in the range 1..10


**Magic** **Code** **(N** **bytes)**

This field contains the Magic Code used to unlock the node.

The length of this field in byte MUST be according to the Magic Code Length field.

The receiving node MUST change its state to unlocked (and exit restricted mode) if this field’s value
matches the Magic Code that was used to lock the node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 78