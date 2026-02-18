<!-- PAGE 65 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.6** **Anti-theft** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **OBSOLETED** New
implementations MUST use the _Anti-theft_ _Command_ _Class,_ _version_ _2_ _[DEPRECATED]_ or newer.


The Anti-theft Command Class is used to disable a subset of supported/controlled command classes in
a device if the device is being excluded and re-included into a Z-Wave network again. This command
class is typically used when installing a Z-Wave device in a public location such as a hotel room
or conference center. The command class allows the user to lock the device to the actual Z-Wave

network and to render it useless if it is removed from the local network without being unlocked.
Another application would be to protect service provider owned products from leaving the service
providers network before they are paid for.


Version 2 limits the Magic Code and Anti-theft Hint maximum bytes to 10. This makes it possible
to embed Anti-theft Command Class Version 2 in one Security Command Class and thereby avoid
splitting it.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 64

---

<!-- PAGE 66 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.7** **Anti-theft** **Command** **Class,** **version** **2** **[DEPRECATED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **DEPRECATED**


New implementations SHOULD use the _Anti-theft_ _Command_ _Class,_ _version_ _3_ .


The Anti-theft Command Class MUST NOT be supported unless the Device Class or Device Type
implemented by the device explicitly allows for support of the Anti-theft Command Class.


The Anti-theft Command Class is intended for devices operating in public locations such as hotel
rooms or a conference center. The purpose of the Anti-theft Command Class is to render a device
useless if it is removed from its actual network without being unlocked by the owner or a service
provider.


The Anti-theft Command Class is used to disable all command classes related to the actual application
functionality of a device if is it excluded and later included in another network. It does not matter
if the device implements a single resource addressed via the Root Device or a collection of resources
addressed via individual Multi Channel End Points Enabling anti-theft protection in a device MUST
NOT change any operation with respect to supported/controlled command classes as long as the
device stays in the actual network.


If a locked device is excluded, it MUST enter the protected state. When in the protected state, the
node information frame (NIF) MUST NOT advertise support of the protected command classes.The
NIF MUST however continue advertising support of the Anti-theft Command Class and all other
non-application specific command classes; just as when the device operates in its home network.


The device MUST NOT respond to application commands while in the protected state. A device
in protected state MUST NOT leave its protected state if it is re-included into its home network.
Another Anti-Theft Set command MUST be used to either disable locking or to clear the protected

state.

The following non-device specific command classes must not be protected by the anti-theft functionality (i.e. will always be available in the device regardless of protection state):

 - Manufacturer Specific Command Class


 - Version Command Class


 - Anti-theft Command Class


 - Security Command Class (optional)


Security encapsulated command classes are allowed to be protected. In that case they must be
removed from the _Security_ _Commands_ _Supported_ _Report_ _Command_ when in the protected state
in a foreign network.


The protection state may be updated by sending the set command with the correct magic code to the
device at any time and in any network. When the protection state is updated the device must return
to normal operation, regardless of whether the update is to disable or re-enable protection. However,
it is not possible to update protection state when device is excluded because it must be able to receive
a command.


The Anti-theft protection state must be preserved in the following situations:


 - Exclusion of a network


 - Reset to factory default

 - OTA update of firmware


If secure device, supports Anti-theft Command Class, Security Command Class needs to be supported
regardless of anti-theft protection state. A security enabled device MUST be able to join any secure
Z-Wave network regardless of its anti-theft protection state.


It is RECOMMENDED for a device that supports anti-theft protection to have physical mark that
indicates that this device is capable of being locked. It is further RECOMMENDED that the device is
capable of signaling via a LED or other means if the device refuses inclusion in a network because the


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 65




<!-- PAGE 67 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


device is locked to another network. Finally, the user guide and installation manual MUST advertise
support of anti-theft protection.


**2.2.7.1** **Anti-theft** **Set** **Command**


This command is used to enable/disable anti-theft protection in a device already included into a
Z-Wave Network by sending a magic code to device in question. The same magic code MUST be used
to disable anti-theft protection again. A new magic code may be used the next time to enable anti-theft
protection in the device, but only if protection is disabled at the time. A new device MUST have
anti-theft protection disabled. Enabling anti-theft protection in an already-enabled device restores it
to normal operation if it is in reduced functionality mode, but otherwise has no effect.


Table 2.34: Anti-theft Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|
|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|Command = ANTITHEFT_SET|
|Enable|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|
|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|
|…|…|…|…|…|…|…|…|
|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|
|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|
|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|
|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|
|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|
|…|…|…|…|…|…|…|…|
|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|



**Enable** **(1** **bit)**


The value MAY be 0 (Attempt to disable anti-theft protection in device) or 1 (Attempt to enable or
re-enable anti-theft protection in device). It is not necessary to first disable an exclude device having
protection enable; it can be re-enabled directly in a new network by using correct magic code again.


**Number** **of** **Magic** **Code** **bytes** **(7** **bits)**

Indicates the Number of Magic Code fields N used in bytes. Maximum number of Magic Code fields
MUST NOT exceed 10 bytes.


**Magic** **Code** **(N** **bytes)**

The Magic Code fields hold the code to enable/disable the Z-Wave device in question.


**Manufacturer** **ID** **(2** **bytes)**


The Manufacturer ID of the company’s product having a central role in the application requiring
anti-theft protection enabled. Device should report 0xFFFF if anti-theft protection is disabled.

Manufacturer identifiers can be found in [32].


**Number** **of** **Anti-theft** **Hint** **bytes** **(8** **bits)**

Indicates the Number of Anti-theft Hint fields N used in bytes. If length is 0 no Hint provided.
Maximum number of Anti-theft Hint fields MUST NOT exceed 10 bytes.


**Anti-theft** **Hint** **Byte** **(N** **bytes)**

Anti-theft Hint Bytes that may be used as an identifier or key value for retrieving the Magic Code. The
exact format and meaning of these Bytes is specific to the product or service that enabled anti-theft
protection on the device, as identified by the Manufacturer ID above. If it is necessary to render the
Hint Bytes for display, each byte should be interpreted as an unsigned integer value and represented
in hexadecimal.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 66




<!-- PAGE 68 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.7.2** **Anti-theft** **Get** **Command**


This command is used to get an Anti-theft Report Command showing status of the Z-Wave device in
question.


The Anti-theft Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.35: Anti-theft Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|
|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|Command = ANTITHEFT_GET|



**2.2.7.3** **Anti-theft** **Report** **Command**


This command is used to report status of the Z-Wave device in question.


Table 2.36: Anti-theft Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|Command Class = COMMAND_CLASS_ANTITHEFT|
|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|Command = ANTITHEFT_REPORT|
|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|
|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|
|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|
|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|Anti-theft Hint Number Bytes|
|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|Anti-theft Hint Byte 1|
|…|…|…|…|…|…|…|…|
|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|Anti-theft Hint Byte N|



**Anti-theft** **Protection** **Status** **(8** **bits)**

Anti-theft Protection Status specifies the actual status of Z-Wave device in question. Refer to the
table below with respect to defined status values.


Table 2.37: Anti-theft Protection Status

|Value|Anti -theft Protection Status|
|---|---|
|0x00|Reserved.|
|0x01|Anti-Theft Protection is currently DISABLED, and the Z-Wave Device<br>is fully functional.|
|0x02|Anti-Theft Protection is currently ENABLED, and the Z-Wave Device is<br>fully functional.|
|0x03|Anti-Theft Protection is currently ENABLED, and the Z-Wave Device<br>is NOT fully functional (i.e., the Device was excluded from a network<br>without disabling protection, and an ANTITHEFT_SET command with<br>the correct Magic Code has notyet been received in the current network).|
|0x04..0xFF|Reserved|



**Manufacturer** **ID** **(2** **bytes)**


The Manufacturer ID of the company’s product having a central role in the application requiring
anti-theft protection enabled. Device should report 0xFFFF if anti-theft protection is disabled.


**Number** **of** **Anti-theft** **Hint** **bytes** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 67




<!-- PAGE 69 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Indicates the Number of Anti-theft Hint fields N used in bytes. If length is 0 no Hint provided.
Maximum number of Anti-theft Hint fields MUST NOT exceed 10 bytes.


**Anti-theft** **Hint** **Byte** **(N** **bytes)**


Anti-theft Hint Bytes. See the Anti-Theft Set Command for more details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 68




<!-- PAGE 70 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.7.4** **Examples**


Following examples are for reference only.


**2.2.7.4.1** **Example** **of** **a** **non-secure** **Thermostat**


Below is shown an example of the Node Information Frame (NIF) content for a non-secure thermostat.
The first NIF shows a device having anti-theft protection disabled. The device may never been included
into a network or reside in a network or excluded from a network:


Table 2.38: Disabled Anti-theft Protection

Disabled anti-theft protection
Manufacturer Specific Command Class
Version Command Class

Anti-theft Command Class

Thermostat Operating State Command Class
Thermostat Mode Command Class

Association Command Class

Battery Command Class


The second NIF shows a device having anti-theft protection enabled. The device may be excluded
from network in which it was originally anti-theft protection enabled or re-included into a network.
This also applies in case device is re-included into the network, which device originally was anti-theft
protection enabled:


Table 2.39: Enabled Anti-theft Protection


Enabled anti-theft protection
Manufacturer Specific Command Class
Version Command Class

Anti-theft Command Class


**2.2.7.4.2** **Example** **of** **a** **security** **enabled** **Thermostat**


Below is shown an example of the Node Information Frame (NIF) content for a security enabled
thermostat. The first NIF shows a device having anti-theft protection disabled. The device may never
been included into a network or reside in a network or excluded from a network:


Table 2.40: Disabled Anti-theft Protection, example 2


Disabled anti-theft protection
Manufacturer Specific Command Class
Version Command Class

Security Command Class


Finally, the _Security_ _Commands_ _Supported_ _Report_ _Command_ reports support of the following command classes:


 - Anti-theft Command Class


 - Thermostat Operating State Command Class


 - Thermostat Mode Command Class


 - Association Command Class


 - Battery Command Class


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 69




<!-- PAGE 71 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The second NIF shows a device having anti-theft protection enabled. The device may be excluded
from network in which it was originally anti-theft protection enabled or re-included into a network.
This also applies in case device is re-included into the network, which device originally was anti-theft
protection enabled. The NIF is unchanged because all application oriented command classes are
security encapsulated except the default command classes:


Table 2.41: Enabled Anti-theft Protection, example 2


Enabled anti-theft protection
Manufacturer Specific Command Class
Version Command Class

Security Command Class


Finally, the Security Commands Supported Report Command reports support of at least the Anti-theft
Command Class to be able to disable anti-theft protection:


 - Anti-theft Command Class


The Anti-theft Command Class is supported securely making malicious attempts to enable anti-theft
protection very difficult.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 70

---

<!-- PAGE 72 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.8** **Anti-theft** **Command** **Class,** **version** **3**


This Command Class is used to lock (and possibly unlock) a node.


**2.2.8.1** **Compatibility** **Considerations**


**2.2.8.1.1** **Command** **Class** **dependencies**


A node supporting this Command Class MUST also support the _Anti-theft_ _Unlock_ _Command_ _Class,_
_version_ _1_ .


**2.2.8.1.2** **Lock/Unlock** **requirements**


The Anti-Theft Command Class is intended for devices operating in public locations such as hotel
rooms or a conference center. The purpose of the Anti-theft Command Class is to render a device
useless if it is removed from its actual network without being unlocked by the owner or a service
provider.


A node can be _locked_ (or protected) or _unlocked_ .


The unlocked state means that the node will operate normally in any Z-Wave network.


The locked state means that the node will restrict usage of most of its command classes after being
excluded from a network, so that it cannot be used by any controlling unit. The locked state MUST
persist after the following operations:


 - Network inclusion/exclusion


 - Factory reset to default.


 - Firmware upgrade


When a node is locked and either excluded from a network or factory reset to default, it will enter its **restricted** mode. In the restricted mode, the node will not grant access to its application
functionalities. The restricted mode MUST stop when the node is unlocked again.

When a node runs in the restricted mode, the NIF MUST adapt its content to reflect the currently
supported Command Classes. The following Command Classes MUST still be supported when a node
is running in restricted mode:


 - Anti-Theft Command Class


 - Anti-Theft Unlock Command Class

 - Manufacturer Specific Command Class


 - Version Command Class


 - Wake-Up Command Class


 - All Command Classes that MUST always be supported at the non-secure level, refer to List of
defined Z-Wave Command Classes (see “This Command Class MUST always be in the NIF if
supported”)


All other supported command classes SHOULD be removed in the restricted mode.


The locked state may be changed back to unlocked with this Command Class or the Anti-Theft Unlock
Command Class.


When in restricted mode, a node MUST still be able to enter learn mode and join or leave a Z-Wave
Network and support Z-Wave protocol operations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 71




<!-- PAGE 73 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.8.1.3** **Multi** **Channel** **Considerations**


Multi Channel End Points SHOULD NOT support Anti-theft Command Class.


**2.2.8.2** **Anti-Theft** **Set** **Command**


This command is used to lock or unlock a node.


Table 2.42: Anti-theft Set Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|
|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|Command = ANTITHEFT_SET (0x01)|
|State|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|Number of Magic Code bytes|
|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|Magic Code 1|
|…|…|…|…|…|…|…|…|
|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|Magic Code N|
|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|
|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|
|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|
|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|Anti-theft Hint|
|…|…|…|…|…|…|…|…|
|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|Anti-theft Hint M|
|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|
|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|Z-Wave Alliance locking entity ID (LSB)|



**State** **(1** **bit)**

This field MUST indicate the desired locked/unlocked state for the receiving node.


The value 0 MUST indicate that the supporting node MUST change its state to unlocked.


The value 1 MUST indicate that the supporting node MUST change its state to locked.

If the receiving node is currently locked and this field is set to 0 (unlock), the receiving node MUST
change its state to unlocked if the Magic Code field value matches the Magic Code value that was
used to lock the node.

If the receiving node is currently locked and this field is set to 1 (lock), the receiving node MUST
ignore this command.

If the receiving node is currently unlocked and this field is set to 0 (unlock), the receiving node MUST
ignore this command.

If the receiving node is currently unlocked and this field is set to 1 (lock), the receiving node MUST
change its state to lock and save the associated Magic code, Manufacturer ID, Anti-Theft Hint and
Z-Wave Alliance locking entity ID.


**Magic** **Code** **Length** **(7** **bit)**

This field MUST indicate the length (in byte) of the _Magic_ _Code_ field.

This field MUST be in the range 1..10.


**Magic** **Code** **(N** **bytes)**

This field contains the Magic Code used to lock or unlock the node.

The length of this field in byte MUST be according to the _Magic_ _Code_ _Length_ field.

The receiving node MUST change its state from locked to unlocked if and only if this field’s value
matches the Magic Code that was used to lock the node.


**Manufacturer** **ID** **(2** **bytes)**

This field describes the Z-Wave Manufacturer ID of the company’s product that has locked the node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 72




<!-- PAGE 74 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST be set to 0x00 by a sending node and ignored by a receiving node if the State field
is set to 0.

If a controlling node has a Z-Wave Manufacturer ID assigned, this field MUST be set to its assigned
Manufacturer ID in Z-Wave Plus Assigned Manufacturer IDs.

If a controlling node has no Z-Wave Manufacturer ID assigned, this field MUST be set to 0x00.


**Anti-theft** **Hint** **Length** **(8** **bits)**

This field MUST indicate the length (in byte) of the _Anti-Theft_ _Hint_ field.

This field MUST be in the range 0..10.


**Anti-theft** **Hint** **(N** **bytes)**

This field is used as an identifier or key value to help retriving the Magic Code.

The length of this field in byte MUST be according to the _Anti-Theft_ _Hint_ _Length_ field. This field
MUST be omitted if the _Anti-Theft_ _Hint_ _Length_ field is set to 0.

The format of this field is manufacturer/controlling node specific.


**Z-Wave** **Alliance** **locking** **entity** **ID** **(2** **bytes)**

This field MUST specify a unique identifier for the entity that has locked the node.

A supporting node MUST NOT change its state to locked if this field is omitted or set to 0x00.


A controlling node MUST NOT lock a device without having a valid Z-Wave Alliance locking entity
ID value.


Contact the Z-Wave Alliance to get an ID assigned. With this ID, the Z-Wave alliance will be able
to provide the following information:


 - Name of the organization


 - Contact Phone for unlock information


 - Optional website/url


 - Optional unlock support email address

This field MUST be set to 0x00 if the _state_ field is set to 0.

This field MUST NOT be set to 0x00 if the _state_ field is set to 1.


**2.2.8.3** **Anti-theft** **Get** **Command**


This command is used to request the locked/unlocked state of a supporting node.


The Anti-Theft Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.43: Anti-theft Get Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|
|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|Command = ANTITHEFT_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 73




<!-- PAGE 75 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.8.4** **Anti-Theft** **Report** **Command**


This command is used to advertise the lock/unlock state of a supporting node.


Table 2.44: Anti-theft Report Command, version 3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|Command Class = COMMAND_CLASS_ANTITHEFT (0x5D)|
|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|Command = ANTITHEFT_REPORT (0x03)|
|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|Anti-theft Protection Status|
|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|Manufacturer ID MSB|
|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|Manufacturer ID LSB|
|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|Anti-theft Hint Length|
|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|Anti-theft Hint 1|
|…|…|…|…|…|…|…|…|
|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|Anti-theft Hint N|
|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|
|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|Z-Wave Alliance locking entity ID (MSB)|



**Anti-theft** **Protection** **Status** **(8** **bits)**

Anti-theft Protection Status specifies the actual status of Z-Wave device in question. Refer to the
table below with respect to defined status values.


Table 2.45: Anti-theft Protection Status, version 3

|Value|Description|
|---|---|
|0x00|Reserved.|
|0x01|Anti-Theft Protection is currently disabled, the node is unlocked|
|0x02|Anti-Theft Protection is currently enabled, the node is locked.<br>However, it did not change network so it is fully functional.|
|0x03|Anti-Theft Protection is currently enabled, the node is locked.<br>The node was reset and/or changed network and runs in restricted mode.|
|0x04..0xFF|Reserved|



**Manufacturer** **ID** **(2** **bytes)**

This field describes the Z-Wave Manufacturer ID of the company’s product that has locked the node.

This field MUST be set to 0x00 if the _Anti-theft_ _Protection_ _Status_ field is set to 0x01.

If the _Anti-theft Protection Status_ field is set to 0x02 or 0x03 and a Z-Wave Manufacturer listed in [32]
has locked the node, this field will advertise the Manufacturer ID that was provided in the Anti-theft
Set Command.

If the _Anti-theft_ _Protection_ _Status_ field is set to 0x02 or 0x03 and an entity who’s not a Z-Wave
Manufacturer listed in [32] has locked the node, this field will be set to 0x00.


**Anti-theft** **Hint** **Length** **(8** **bits)**

This field MUST indicate the length (in byte) of the _Anti-Theft_ _Hint_ field.

This field MUST be in the range 0..10.

If the _Anti-theft_ _Protection_ _Status_ field is set to 0x01, a sending node MUST set this field to 0.

If the _Anti-theft_ _Protection_ _Status_ field is set to 0x02 or 0x03, a sending node MUST advertise the
length of the Anti-Theft Hint field that was used to lock the node.


**Anti-theft** **Hint** **(N** **bytes)**

This field is used as an identifier or key value to help retrieving the Magic Code.

The length of this field in byte MUST be according to the _Anti-Theft_ _Hint_ _Length_ field. This field
MUST be omitted if the _Anti-Theft_ _Hint_ _Length_ field is set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 74




<!-- PAGE 76 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A supporting node MUST advertise the value that was specified in the Anti-Theft Set Command
when it got locked.


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

This field MUST be set to 0x00 if the _Anti-theft_ _Protection_ _Status_ field is set to 0x01.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 75