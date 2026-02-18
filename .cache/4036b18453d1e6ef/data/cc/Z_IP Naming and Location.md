<!-- PAGE 803 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49** **Z/IP** **Naming** **and** **Location** **Command** **Class,** **version** **1**


The Z/IP Naming and Location Command Class is used to manage the Name and a Location text
strings of a Z/IP resource.


**3.2.49.1** **Compatibility** **Considerations**


A Z/IP resource is identified by an IPv6 address and an End Point ID. Capable Z/IP nodes SHOULD
store the naming and location information locally in non-volatile storage. In addition, a Z/IP Resource
Directory (RD) MAY store the naming and location of all Z/IP Resources; also sleeping resources.
The Z/IP RD manages node properties retrieved from actual nodes as well as extended information
which is not always available in classic Z-Wave nodes.


Information managed by the Z/IP RD may be announced to Z/IP Clients via service discovery mechanisms such as mDNS.

Commands defined in this command class MUST be encapsulated in Z/IP Packets.


A client modifying the name and/or location information MUST ensure that the combined length of
the Z/IP Name and Z/IP Location is 62 bytes or less in order to comply with DNS-SD limitations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 802




<!-- PAGE 804 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.2** **Z/IP** **Name** **Set** **Command**


This command is used to set the name of a Z/IP Resource.


Table 3.181: Z/IP Name Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|Command = ZIP_NAMING_NAME_SET|
|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|
|…|…|…|…|…|…|…|…|
|Name N|Name N|Name N|Name N|Name N|Name N|Name N|Name N|



**Name** **(N** **bytes)**

This field is used to specify the Name portion of the resource name.


The combined Name and Location strings MUST NOT be longer than 62 bytes.


The Name String MUST be UTF-8 encoded. Since a UTF-8 character may require two or more bytes,
the maximum length of a name string depends on the composition of the string.


The Name String MUST NOT contain any appended termination characters. The number of bytes
MUST be determined from the command length.


The name MUST NOT contain the dot (also known as period) character “.”.


The escape sequence “\.” (backslash followed by dot) MAY be used for encoding the dot character.


A user interface SHOULD allow users to enter names that contain dot characters.


If a dot character is entered, the user interface MUST replace the dot character with the escape
sequence “\.”before issuing this command.


The name MUST NOT contain the underscore character “_”.


The name MUST NOT end with the dash character “-”.


Node names MUST be case insensitive.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 803




<!-- PAGE 805 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.3** **Z/IP** **Name** **Get** **Command**


This command is used to request the name from a Z/IP Resource


The Z/IP Name Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.182: Z/IP Name Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|Command = ZIP_NAMING_NAME_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 804




<!-- PAGE 806 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.4** **Z/IP** **Name** **Report** **Command**


This command is used to advertise the name of a Z/IP Resource.


Table 3.183: Z/IP Name Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|Command = ZIP_NAMING_NAME_REPORT|
|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|Name 1|
|…|…|…|…|…|…|…|…|
|Name N|Name N|Name N|Name N|Name N|Name N|Name N|Name N|



**Name** **(N** **bytes)** Refer to Section 3.2.49.2 Z/IP Name Set Command.


It may be attractive to use dots in names. The escape sequence “\.” (backslash followed by dot) MAY
be used for encoding the dot character in names.


A receiving device SHOULD display the escape sequence “\.” as “.” in user interfaces facing end users.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 805




<!-- PAGE 807 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.5** **Z/IP** **Location** **Set** **Command**


This command is used to set the location of a Z/IP Resource.


Table 3.184: Z/IP Location Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|Command = ZIP_NAMING_LOCATION_SET|
|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|
|…|…|…|…|…|…|…|…|
|Location N|Location N|Location N|Location N|Location N|Location N|Location N|Location N|



**Location** **(N** **bytes)**

This field is used to specify the Location portion of the resource name.


The combined Name and Location strings MUST NOT be longer than 62 bytes.


The Location string MUST be UTF-8 encoded. Since a UTF-8 character may require two or more
bytes, the maximum length of a location string depends on the composition of the string.


The Location string MUST NOT contain any appended termination characters. The number of bytes
MUST be determined from the message length.


The location string MAY contain the dot (also known as the period) character “.”.


A user interface MUST NOT replace the dot character with the escape sequence “\.”before issuing
this Command.


The location string MUST NOT contain the underscore character “_”.


Each location sub-string (separated by the dot character “.”) MUST NOT end with the dash character
“-”.


Node locations MUST be case insensitive.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 806




<!-- PAGE 808 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.6** **Z/IP** **Location** **Get** **Command**


This command is used to request the location from a Z/IP Resource


The Z/IP Location Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 3.185: Z/IP Location Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|Command = ZIP_NAMING_LOCATION_GET|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 807




<!-- PAGE 809 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**3.2.49.7** **Z/IP** **Location** **Report** **Command**


This command is used to advertise the location of a Z/IP Resource.


Table 3.186: Z/IP Location Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|Command Class = COMMAND_CLASS_ZIP_NAMING|
|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|Command = ZIP_NAMING_LOCATION_REPORT|
|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|Location 1|
|…|…|…|…|…|…|…|…|
|Location N|Location N|Location N|Location N|Location N|Location N|Location N|Location N|



**Location** **(N** **bytes)**


Refer to Section 3.2.49.5 Z/IP Location Set Command.


The escape sequence “\.” (backslash followed by dot) MAY be used for encoding the dot character in
locations.


A receiving node SHOULD display the escape sequence “\.” as “.” in user interfaces facing end users.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 808