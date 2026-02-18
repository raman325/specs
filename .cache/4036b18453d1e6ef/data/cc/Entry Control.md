<!-- PAGE 208 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42** **Entry** **Control** **Command** **Class,** **version** **1**


The Entry Control Command Class defines a method for advertising user input to a central Entry
Control application and for the discovery of capabilities. User input may be button presses, RFID
tags or other means.


It is RECOMMENDED that this command class is only supported via secure communication. This
recommendation may be raised to a stronger requirement at the Device Class or Device Type level.


The Entry Control Command Class provides the following commands:


 - Key Supported Get/Report  - Used by the controller to request which ASCII keys are present
on the Entry Control device.


 - Event Supported Get/Report  - Used by the controller to request which Event Types are supported by the Entry Control device.

 - Configuration Set/Get/Report  - Used by the controller to configure the Entry Control device

 - Notification Command  - Used by the Entry Control device to notify the controller of inputs.


**2.2.42.1** **Interoperability** **Considerations**


It is RECOMMENDED that an Entry Control input device that implements the Entry Control Command Class also implements the Indicator Command Class, version 2.


If implementing the Indicator Command Class, version 2, it is RECOMMENDED that all indicator
resources are addressable via the Indicator Command Class, version 2.


The input device MAY implement local control of indicator resources. If the Indicator Command
Class, version 2 is supported, the first received Indicator Set command MUST disable all local control
of indicator resources – except for interface feedback functionality like a short beep on each button

press.


Transmissions may fail due to central control application fault or due to RF jamming. It is RECOMMENDED that an Entry Control input device provides local user feedback if the transmission of
notifications to the central control application fails.

If the device only features light indicators, it is RECOMMENDED that all light flashes at 2Hz for at
least 5 seconds to indicate transmission error.


If the device features a buzzer, it is RECOMMENDED that the buzzer generates sound pulses at a
rate of 2Hz for at least 5 seconds to indicate transmission error.


If implementing the indicator Command Class, version 2, in devices based on Role Type RSEN
(using Wake Up Command Class), the control of indicators must be synchronized with the Wake Up
Notification. The controller must therefore wait for the Wake Up Notification, before it can control
the indictors. The device implementing the indicator Command Class must therefore send the Wake
Up Notification after sending the Entry Control Notification Command, in case the device expects to
be controlled.


**2.2.42.2** **Security** **Considerations**


An attacker could theoretically determine the length of manually entered user credentials even if they
are transmitted via encryption. It is therefore MANDATORY to add padding bytes to ASCII strings
so that all transferred ASCII strings are structured as one or more blocks of 16 characters. The
ASCII code 0xFF MUST be reserved for padding purposes and it MUST NOT be used for any other

purposes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 207




<!-- PAGE 209 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.3** **Handling** **user** **supplied** **data**


The Entry Control device must cache the user input before sending the full entry in one Notification
Frame. A user input MUST therefore have a termination, which MAY be determined by:


 - The Key Cache Size is exceeded


 - The Key Cache Timeout is exceeded


 - A Command Button is pressed


 - User data is received by other means, e.g. from an RFID tag


**Key** **Cached** **Size:**

The Key Cached Size is configured to specify the number of user inputs before the Notification Frame
is sent. After sending the Notification Frame the cache must be cleared and subsequent user inputs
MUST be considered a new entry.

The Key Cached Size May be configured to 1, in which case a Notification Frame is send for each user
input.

It is RECOMMENDED to have a default Key Cached Size of 4, in which case the Notification Frame
will be send after 4 entries.


**Key** **Timeout:**

The Key Timeout is configured to specify the maximum time between user inputs. If the time between
user inputs exceeds the Timeout, the cached user inputs will be send in a Notification Frame. After
sending the Notification Frame the cache must be cleared and subsequent user inputs MUST be
considered a new entry.


**Based** **on** **Command** **Button:**


A user input may be terminated by the user pressing on of the Command Buttons like ENTER or
ARM_ALL. The cached entry will be sent in a Notification Frame immediately after the user presses
the Command Button. After sending the Notification Frame the cache must be cleared and subsequent
user inputs MUST be considered a new entry.


**Based** **on** **RFID:**


When presenting an RFID tag, the ID will be read from the tag, and this terminates the user input.
So the cached ID ‘s from the RFID tag data can immediately be sent in a Notification Frame. After
sending the Notification Frame the cache must be cleared and subsequent user inputs MUST be
considered a new entry.


Presenting an RFID tag may also terminate an ongoing user input. For instance, a user may enter
four characters and subsequently present an RFID tag. In that case, the four entries must first be
sent in one Notification Frame, and subsequently the ID ‘s from the RFID tag data is sent in a second
Notification Frame.


**2.2.42.4** **Handling** **Incorrect** **Entry**


A user may do an incorrect entry e.g. the credential is 1234 but the user enters 1734. In this case
the terminal may provide a “delete” option, to allow the user to fix or re-enter the credential. If a
“delete” option is not provided, the invalid code must first be send, followed by a new (correct) entry.


The terminal must not assume that the receiving controller does error handling like
1+7+Delete+2+3+4 = 1234.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 208




<!-- PAGE 210 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.5** **Entry** **Control** **Notification** **Command**


This command is used to advertise user input.


Depending on the Event Type, this command MAY carry manually entered user credentials.


Table 2.223: Entry Control Notification Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|Command = ENTRY_CONTROL_NOTIFICATION (0x01)|
|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|Sequence Number|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Data Type|Data Type|
|Event Type|Event Type|Event Type|Event Type|Event Type|Event Type|Event Type|Event Type|
|Event Data Length|Event Data Length|Event Data Length|Event Data Length|Event Data Length|Event Data Length|Event Data Length|Event Data Length|
|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|Event Data 1 (optional)|
|…|…|…|…|…|…|…|…|
|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|Event Data N (optional)|



**Sequence** **Number** **(8** **bit)**


The sequence number MUST be incremented each time a new command of this type is issued.


The value MUST be in the range 0..255. The initial value MAY be any value in the range 0..255.


A receiving device MUST use the Sequence Number to detect and ignore duplicates.


**Reserved**

This field MUST be set to 0 by a sending device and MUST be ignored by a receiving device.


**Data** **Type** **(2** **bits)**

This field is used to advertise the type of data (if any) that is appended to this command.

|Data|Col2|Table 2.224: Entry Control Notification::Event Data Type Description|
|---|---|---|
|**Data**<br>**Type**|**Data**<br>**Type**|**Description**|
|0x00|NA|No data included|
|0x01|RAW|1 to 32 bytes of arbitrary binary data|
|0x02|ASC|II<br>1 to 32 ASCII encoded characters. ASCII codes MUST be in the value range<br>0x00-0xF7.<br>The string MUST be padded with the value 0xFF to ft 16 byte blocks when sent in<br>a notifcation.|
|0x03|MD5|16 byte binary data encoded as a MD5 hash value.|



All other values are reserved and MUST NOT be used by a sending device. Reserved values MUST
be ignored by a receiving device.

**Event** **Type** **(4** **bit)** This field is used to advertise the actual Event Type.

The field MUST be encoded according to Section 2.2.42.13.


**Event** **Data** **Length** **(8** **bit)**

This field MUST advertise the length of the Event Data field in bytes.


The value MUST be in the range 0..32.

If no data bytes are included, this field MUST be set to 0.


**Event** **Data** **(n** **bytes)**

This field is used to carry data related to the event, e.g. received from an RFID tag.

The length of this field MUST comply with the length advertised by the Event Data Length field.

The format of this field MUST comply with the data format advertised by the Data Type field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 209




<!-- PAGE 211 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.6** **Entry** **Control** **Key** **Supported** **Get** **Command**


This command is used to query the keys that a device implements for entry of user credentials.


The Entry Control Key Supported Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.225: Entry Control Key Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|Command = ENTRY_CONTROL_KEY_SUPPORTED_GET (0x02)|



**2.2.42.7** **Entry** **Control** **Key** **Supported** **Report** **Command**


This command is used to advertise the keys that a device implements for entry of user credentials.


A management interface may determine the available keys for credential entry from this command.


The range of available Command Keys may be determined via the Entry Control Event Supported
Report Command.


Table 2.226: Entry Control Key Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|Command = ENTRY_CONTROL_KEY_SUPPORTED_REPORT (0x03)|
|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|Key Supported Bit Mask Length|
|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|Key Supported Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|Key Supported Bit Mask N|



**Key** **Supported** **Bit** **Mask** **Length**

This field is used to advertise the number of Key Supported Bit Mask Bytes to follow.


Only the Key Supported Bit Mask bytes until the last supported ASCII key SHOULD be included.


**Key** **Supported** **Bit** **Mask** **(Variable** **length)**

This field is used to advertise the keys that a device implements for entry of user credentials.

The Key Supported Bit Mask field MUST advertise ASCII codes that represent the supported keys.


 - Bit 0 in Bit Mask 1 indicates that the supporting device may issue ASCII code 0


 - Bit 1 in Bit Mask 1 indicates that the supporting device may issue ASCII code 1


 - …


 - Bit 7 in Bit Mask 16 indicates that the supporting device may issue ASCII code 127


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 210




<!-- PAGE 212 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.8** **Entry** **Control** **Event** **Supported** **Get** **Command**


This command is used to request the supported Events of a device.


The Entry Control Event Supported Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.227: Entry Control Event Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_GET (0x04)|



**2.2.42.9** **Entry** **Control** **Event** **Supported** **Report** **Command**


Table 2.228: Entry Control Event Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|Command = ENTRY_CONTROL_EVENT_SUPPORTED_REPORT (0x05)|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Data Type Supported Bit Mask<br>Length|Data Type Supported Bit Mask<br>Length|
|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|Data Type Supported Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|Data Type Supported Bit Mask M|
|Reserved|Reserved|Reserved|Event Supported Bit Mask Length|Event Supported Bit Mask Length|Event Supported Bit Mask Length|Event Supported Bit Mask Length|Event Supported Bit Mask Length|
|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|Event Type Supported Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|Event Type Supported Bit Mask N|
|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|Key Cached Size supported Minimum|
|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|Key Cached Size supported Maximum|
|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|Key Cached Timeout supported Minimum|
|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|Key Cached Timeout supported Maximum|



**Data** **Type** **Supported** **Bit** **Mask** **Length** **(2** **bits)**

This field is used to advertise the number of Data Type Supported Bit Mask Bytes to follow.


**Reserved**

This field MUST be set to 0 by a sending device and MUST be ignored by a receiving device.


**Data** **Type** **Supported** **Bit** **Mask** **(Variable** **length)**

This field is used to advertise the supported Data Types.


 - Bit 0 in Bit Mask 1 indicates if Data Type 0 is supported


 - Bit 1 in Bit Mask 1 indicates if Data Type 1 is supported


 - …

For the definition of Data Type IDs, refer to Table 2.224.


**Event** **Type** **Supported** **Bit** **Mask** **Length** **(1** **byte)**

This field is used to advertise the number of Event Type Supported Bit Mask Bytes to follow.


**Event** **Type** **Supported** **Bit** **Mask** **(variable** **length)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 211




<!-- PAGE 213 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the supported Event Type.


 - Bit 0 in Bit Mask 1 indicates if Event Type 0 is supported


 - Bit 1 in Bit Mask 1 indicates if Event Type 1 is supported


 - …

For the definition of Event Type IDs, refer to Table 2.232.


**Key** **Cached** **Size** **Supported** **Minimum**

The minimum configurable number of key entries before the CACHED_KEYS notification is sent.


Refer to Section 2.2.42.10.


**Key** **Cached** **Size** **Supported** **Maximum**

The maximum configurable number of key entries before the CACHED_KEYS notification is sent.


Refer to Section 2.2.42.10.


**Key** **Cached** **Timeout** **Supported** **Minimum**

The minimum configurable timeout before the CACHED_KEYS notification is sent.


Refer to Section 2.2.42.10.


**Key** **Cached** **Timeout** **Supported** **Maximum**

The maximum configurable timeout before the CACHED_KEYS notification is sent.


Refer to Section 2.2.42.10.


**2.2.42.10** **Entry** **Control** **Configuration** **Set** **Command**


This command is used to configure Event Type specific parameters.


Table 2.229: Entry Control Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|Command = ENTRY_CONTROL_CONFIGURATION_SET (0x06)|
|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|
|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|



**Key** **Cache** **Size** **(1** **byte)** This field specifies the number of characters the key cache MUST store
before sending data to the central control application. Data MUST be sent when the number of
characters in the cache matches or exceeds the value of this field.

The value MUST be in the range 1..32. The default value of this field SHOULD be 4.

In deployments where characters are entered first and a command button is pressed subsequently, it
is RECOMMENDED that this field is set to 32 and that the Key Cache Timeout is set to 2 seconds.


**Key** **Cache** **Timeout** **(1** **byte)**

This field specifies the number of seconds the key cache MUST wait for additional characters before
sending data to the central control application. Data MUST be sent if a Key Cache Timeout occurs.


The Key Cache Timeout MUST be measured from the most recent reception of a character.


The value SHOULD be in the range 1..10 seconds. The default value SHOULD be 2 seconds.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 212




<!-- PAGE 214 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.11** **Entry** **Control** **Configuration** **Get** **Command**


This command is used to request the operational mode of a device.

The Entry Control Configuration Report command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.230: Entry Control Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|Command = ENTRY_CONTROL_CONFIGURATION_GET (0x07)|



**2.2.42.12** **Entry** **Control** **Configuration** **Report** **Command**


This command is used to advertise the current operational mode of a device.


Table 2.231: Entry Control Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|Command Class = COMMAND_CLASS_ENTRY_CONTROL (0x6F)|
|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|Command = ENTRY_CONTROL_CONFIGURATION_REPORT (0x08)|
|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|Key Cache Size|
|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|Key Cache Timeout|



**Key** **Cache** **Size** **(1** **byte)**

Refer to Section 2.2.42.10 Entry Control Configuration Set Command.


**Key** **Cache** **Timeout** **(1** **byte)**

Refer to Section 2.2.42.10 Entry Control Configuration Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 213




<!-- PAGE 215 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.42.13** **Event** **Types**


The Event Types MUST be encoded according to Table 2.232.



Table 2.232: Event Types






|Event Type|Col2|Recommended Button<br>Label|Event Data (optional)|
|---|---|---|---|
|0x00|CACHING|-|-|
|0x01|CACHED_KEYS|-|ASCII bytes|
|0x02|ENTER|Enter|ASCII bytes|
|0x03|DISARM_ALL|Disarm|ASCII bytes|
|0x04|ARM_ALL|Arm|ASCII bytes|
|0x05|ARM_AWAY|Away|ASCII bytes|
|0x06|ARM_HOME|Home|ASCII bytes|
|0x07|EXIT_DELAY|Arm_Delay|ASCII bytes|
|0x08|ARM_1|Arm zone 1|ASCII bytes|
|0x09|ARM_2|Arm zone 2|ASCII bytes|
|0x0A|ARM_3|Arm zone 3|ASCII bytes|
|0x0B|ARM_4|Arm zone 4|ASCII bytes|
|0x0C|ARM_5|Arm zone 5|ASCII bytes|
|0x0D|ARM_6|Arm zone 6|ASCII bytes|
|0x0E|RFID|-|As advertised by the Data Type<br>feld|
|0x0F|BELL|-|-|
|0x10|FIRE|Fire|-|
|0x11|POLICE|Police|-|
|0x12|ALERT_PANIC|-|-|
|0x13|ALERT_MEDI-<br>CAL|-|-|
|0x14|GATE_OPEN|Open, Up. ‘O’ or similar|ASCII bytes|
|0x15|GATE_CLOSE|Close, Down, ‘C’ or similar|ASCII bytes|
|0x16|LOCK|-|ASCII bytes|
|0x17|UNLOCK|-|ASCII bytes|
|0x18|TEST|Test|ASCII bytes|
|0x19|CANCEL|Cancel|ASCII bytes|



All other values are reserved and MUST NOT be used by a sending device. Reserved values MUST
be ignored by a receiving device.


**Event** **Type** **CACHING**


The CACHING Event Type is used to indicate to the central controller that the user has started
entering credentials, and that caching is initiated. This allows the central controller to change the
indications on the Entry Control device through the indicator Command Class, or to change the status
of the central controller user interface.

If Key Cached Size it set to 1, the CACHING event notification MUST NOT be sent. Instead each
individual credential byte MUST be sent in its own CACHED_KEYS event notification.


**Event** **Type** **CACHED_KEYS**

The CACHED_KEYS Event Type is used to send user inputs in a Notification Frame. The
CACHED_KEYS is sent when the user input is terminated by one of the following reasons:


 - The Key Cache Size is exceeded


 - The Key Cache Timeout is exceeded


 - A command button is pressed


 - User data is received by other means, e.g. from an RFID tag


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 214