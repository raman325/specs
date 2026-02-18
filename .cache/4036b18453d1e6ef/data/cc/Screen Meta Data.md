<!-- PAGE 457 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.96** **Screen** **Meta** **Data** **Command** **Class,** **version** **1**


The Screen Meta Data Command Class is used to streaming data containing user related information
to a screen located on a device in a Z-Wave network. The screen can request single or multiple data
packets. The device having the data containing user related information to the screen can also initiate
the data streaming.


In order not to congest the Z-Wave network, large data transfers MUST leave transmit opportunities
for other nodes in the network. If sending a command longer than two frames, a node MUST implement
a delay between every transmitted frame. The minimum required time delay and number of frames
before a delay must be inserted depends on the actual bit rate.


 - 40 kbit/s: At least 35 ms if sending more than 2 frames back-to-back


 - 100 kbit/s: At least 15 ms if sending more than 2 frames back-to-back


**2.2.96.1** **Screen** **Meta** **Data** **Get** **Command**


This command is used to request the Screen Meta Data Report Command. The Screen Meta Data
Get Command is used as handshake to avoid buffer overflow in the receiving node. The Screen Meta
Data Get Command will optionally be able to request multiple Screen Meta Data Report Commands
to improve the effective bandwidth.


The Screen Meta Data Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|
|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|Command = SCREEN_MD_GET|
|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|Number of Reports|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Number** **of** **Reports** **(8** **bits)**


Number of Screen Meta Data Report Commands to be received without requesting each Screen Meta
Data Report Command (1..255). Be aware of overflow when requesting multiple reports.


**NodeID** **(8** **bits)**

The NodeID (1..232) specifies the device to receive the requested reports. In case NodeID is equal to
0x00, the information is requested by the source NodeID of the Screen Meta Data Get Command.


**2.2.96.2** **Screen** **Meta** **Data** **Report** **Command**


This command is used to send data to the device hosting the screen.


The size of the payload SHOULD NOT be bigger than 48 bytes. It is possible to write characters to
multiple lines in the same frame.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 456




<!-- PAGE 458 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|
|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|
|More Data|Reserved|Screen Settings|Screen Settings|Screen Settings|Character Encoding|Character Encoding|Character Encoding|
|Line Settings A|Line Settings A|Line Settings A|Clear A|Line Number A|Line Number A|Line Number A|Line Number A|
|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|
|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|
|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|
|…|…|…|…|…|…|…|…|
|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|
|…|…|…|…|…|…|…|…|
|Line Settings B|Line Settings B|Line Settings B|Clear B|Line Number B|Line Number B|Line Number B|Line Number B|
|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|
|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|
|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|
|…|…|…|…|…|…|…|…|
|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|



**More** **Data** **(1** **bit)**


The more data bit indicates if additional reports are expected before the whole data streaming is
completed. If the more data bit is set to 1 then additional reports are expected and the opposite if 0.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Screen** **Settings** **(3** **bits)**

This field MUST comply with Table 2.511:


Table 2.511: Screen Meta Data Report::Screen Settings encoding

|Screen Settings|Description|
|---|---|
|0|Whole screen is cleared before lines are written.|
|1|Current content on screen is scrolled one line down.|
|2|Current content on screen is scrolled one line up.|
|7|Do not change the current content on the screen.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Character** **Encoding** **(3** **bits)**

This field MUST comply with Table 2.512:


Table 2.512: Screen Meta Data Report::Character Encoding encoding

|Character<br>Encoding|Description|
|---|---|
|0|Using standard ASCII codes, see _ASCII Codes_ (values 128-255 are ignored)|
|1|Using standard ASCII codes and OEM Extended ASCII codes, see_ ASCII Codes_|
|2|Unicode UTF-16<br>|
|3|Using standard ASCII codes and Player codes, see _ASCII Codes_ (undefned<br>values are ignored)|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Note:** Devices supporting Unicode UTF-16 characters are described by a 2 byte long decimal


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 457




<!-- PAGE 459 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


representation. The first byte is the most significant byte. E.g. if there is one Unicode character in
the set frame the char 1 will be MSB and char 2 will be LSB of the Unicode character.


**Line** **Settings** **(3** **bits)**

This field MUST comply with Table 2.513:

|Line Settings|Table 2.513: Screen Meta Data Report::Line Settings encoding Description|
|---|---|
|Line Settings|Description|
|0|Characters are written in selected font|
|1|Characters are written as highlighted|
|2|Characters are written using a larger font compared to line settings equal to 0|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Clear** **(1** **bit)**

Determine if the characters are written directly or line is cleared first.


Table 2.514: Screen Meta Data Report::Clear encoding

|Clear|Description|
|---|---|
|0|Characters are written directly|
|1|Line is cleared before characters are written.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Line** **Number** **(4** **bits)**

The line number field indicates the line to write the characters to counting from zero (0..15).


**Character** **Position** **(8** **bits)**

The character position field indicates where on the line to write the characters counting from zero
(0..255). The character position may be larger than the display size in case the line buffer is bigger
(See the Screen Attributes Report Command).


**Number** **of** **Characters** **(8** **bits)**

The number of characters field indicates how many characters to be written on the screen for the
specified line number, counting from 1.


**Character** **(N** **bytes)**

The character fields hold the string to output in specified character representation. Characters will
be ignored in case there is no room left in the line buffer.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 458

---

<!-- PAGE 460 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.97** **Screen** **Meta** **Data** **Command** **Class,** **version** **2**


The Screen Meta Data Command Class, version 2 introduces a Screen Timeout bit. The support for
the Screen Timeout bit may be advertised by the Screen Attribute Command Class, version 2.


Details not mentioned remain the same as in version 1.


**2.2.97.1** **Screen** **Meta** **Data** **Report** **Command**


This command is used to transfer data to the device hosting the screen. The size of the payload
MUST NOT be bigger than 48 bytes. It is possible to write characters to multiple lines in the same
frame.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|Command Class = COMMAND_CLASS_SCREEN_MD|
|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|Command SCREEN_MD_REPORT|
|More Data|Extended<br>Setup|Screen Settings|Screen Settings|Screen Settings|Character Encoding|Character Encoding|Character Encoding|
|Line Settings A|Line Settings A|Line Settings A|Clear A|Line Number A|Line Number A|Line Number A|Line Number A|
|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|Character Position A|
|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|Number of Characters A|
|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|Character 1,A|
|…|…|…|…|…|…|…|…|
|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|Character N,A|
|…|…|…|…|…|…|…|…|
|Line Settings B|Line Settings B|Line Settings B|Clear B|Line Number B|Line Number B|Line Number B|Line Number B|
|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|Character Position B|
|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|Number of Characters B|
|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|Character 1,B|
|…|…|…|…|…|…|…|…|
|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|Character N,B|



**More** **Data** **(1** **bit)**


The more data bit indicates if additional reports are expected before the whole data streaming is
completed. If the more data bit is set to 1 then additional reports are expected and the opposite if 0.


**Extended** **Setup** **(1** **bit)**

If set to true, the last byte of the payload defines an extended setup.


**Screen** **Settings** **(3** **bits)**

The screen settings identifier MUST be encoded according to Table 2.511.


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Character** **Encoding** **(3** **bits)**

The Character Encoding identifier MUST be encoded according to Table 2.512.


**Note:** Devices supporting Unicode UTF-16 characters are described by a 2 byte long decimal
representation. The first byte is the most significant byte. E.g. if there is one Unicode character in
the set frame the char 1 will be MSB and char 2 will be LSB of the Unicode character.


All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 459