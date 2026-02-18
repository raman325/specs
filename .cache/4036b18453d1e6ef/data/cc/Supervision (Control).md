<!-- PAGE 1160 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.5** **Supervision** **Command** **Class,** **version** **1**


**6.4.5.1** **Mandatory** **node** **interview**


There is no mandatory node interview for a node controlling this Command Class.


**6.4.5.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.5.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.5.4** **Additional** **Control** **Requirements**


CL:006C.01.51.01.1 A node issuing Supervision Get Commands MUST declare the Supervision Command Class as controlled during certification.


CL:006C.01.51.02.1 Any node issuing Supervision Get Commands MUST comply with the following:

     - The Session ID field MUST be incremented each time a new unique Supervision Get Command
is issued.


     - A sending node MAY use the same Session ID for a multicast and singlecast follow-up carrying
the same encapsulated command. A sending node MAY also use the same Session ID for all
destinations of singlecast follow-up commands.

It has been found that some nodes issue Wake Up Notifications using the same Supervision SessionID
CL:006C.01.52.01.1 every time. A controlling node SHOULD accept Wake Up Notifications even if they use the same
SessionID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1159




<!-- PAGE 1161 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **7 Device Type v2 Specification** **7.1 Introduction**


This document describes the requirement associated to the Z-Wave Plus v2 compliant Device Types. It
contains a list of requirements applying for all Z-Wave Plus v2 compliant nodes as well as requirements
specifics to each defined Device Type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1160




<!-- PAGE 1162 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **7.2 Common Z-Wave Plus v2 Device Type Requirements**


**7.2.1** **How** **to** **detect** **Z-Wave** **Plus** **v2** **compliant** **nodes**


DT:00.11.0001.1 A Z-Wave Plus v2 node MUST advertise version 0x02 in the Z-Wave Plus Version field of the Z-Wave
Plus Info Report. Multi Channel End Points MUST advertise the same version number in their
Z-Wave Plus Info Report


DT:00.11.0002.1 A Z-Wave Plus v2 node MUST set the Optional Functionality bit to 1 in its NIF. For the NIF’s
description, refer to Section 2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1161




<!-- PAGE 1163 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.2** **Command** **Classes** **Support** **Requirements**


DT:00.11.0003.1 A Z-Wave Plus v2 node MUST support the command classes listed in the following sections. When a
version number is indicated, the node MUST support or control the indicated version or a newer one.


**7.2.2.1** **Root** **Device** **level**


DT:00.11.0004.1 All Root Devices or nodes MUST support:


     - Association, version 2


     - Association Group Information


     - Device Reset Locally


     - Firmware Update Meta Data, version 5


     - Indicator, version 3

     - Manufacturer Specific


     - Multi Channel Association, version 3


     - Powerlevel


     - Security 2


     - Supervision


     - Transport Service, version 2


     - Version, version 2


     - Z-Wave Plus Info, version 2


**7.2.2.2** **End** **Point** **level**


DT:00.11.0005.1 All Multi Channel End Points MUST support:


     - Association, version 2


     - Association Group Information


     - Multi Channel Association, version 3


     - Supervision


     - Z-Wave Plus Info, version 2


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1162




<!-- PAGE 1164 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.3** **Identify**


DT:00.11.0006.2 A Z-Wave Plus v2 node MUST support an Identify indicator (Indicator ID 0x50) which can be used
for an Identify function.


DT:00.12.0004.1 The node is RECOMMENDED to use a visible LED for an identify function if it has an LED. If the
node is itself a light source, e.g. a light bulb, this MAY be used in place of a dedicated LED.


DT:00.11.0007.1 The Root Device of a node MUST support the Indicator Command Class, version 3 or newer and
support the Indicator ID 0x50 (Identify) and Properties ID 0x03, 0x04 and 0x05.


DT:00.13.0001.1 Multi Channel devices MAY support an Identify indicator on End Points, if the corresponding End
Point has its own LED or light source.


DT:00.11.0008.1 If a Multi Channel device only implements a single indicator for the entire device, the End Points
MUST NOT support the Identify Indicator, while the Root Device MUST support the Identify Indi
cator.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1163




<!-- PAGE 1165 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.4** **Dynamic** **Capabilities** **and** **Node** **Discovery**


DT:00.11.0009.1 A controller MUST have a menu or method for an (advanced) end user to request the controller to
perform a capability discovery for a given node (i.e. to perform a complete commissioning interview)


DT:00.13.0002.1 Nodes (and their End Points) MAY change capabilities based on a user action, such as changing
configuration parameters or the physical addition/removal of a module.


DT:00.11.000A.1 End Point changing capabilities based on a user action MUST NOT be advertised as Dynamic End
Points.

DT:00.13.0003.1 If supporting Configuration Command Class, nodes MAY issue a Configuration Report advertising a
dynamic capabilities parameter value change in order to let the lifeline destination(s) know that some
capabilities have changed.


DT:00.11.000B.1 However, a controlling node MUST NOT perform the node interview unless instructed to do so by
the end user.

DT:00.11.000C.1 The configuration of Command Classes that are available before and after a capability change MUST
remain unchanged. For instance, the Lifeline Association Group destination and Wake Up destination
MUST stay identical when a node changes capabilities.


DT:00.11.000D.1 A node MUST stay compliant and observe Z-Wave Plus v2 Device Type requirements when and after
changing capabilities. A node MAY change its Device Type when altering its capabilities.


DT:00.11.000E.1 A node being able to change between a secure only Device Type (S2 Access Control) and a regular
S2 Device Type MUST observe the S2 Access Control Device Type requirements (3.6.8.2.1) even if
configured to be a regular Device Type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1164




<!-- PAGE 1166 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.5** **Controller** **Functionalities**


A controller plays an important role in a Z-Wave network because this device hosts important functionality to create, maintain and configure the network and the home automation application. The
following sections describe important rules to ensure that a controller is capable of fulfilling this
important role.


**7.2.5.1** **Interoperability**


DT:00.11.0011.1 To ensure interoperability, a controller MUST comply with the following requirements:


1. It is not acceptable to block interoperability by any means.

2. It is not acceptable to prevent inclusion of certified devices into a system or force exclusion of
non- preferred devices after inclusion.


3. Devices from non-preferred manufacturers MAY be placed in a special section of the user interface; this section should be referred to as “Additional Z-Wave Ecosystem Devices”. Additionally,
it is acceptable to inform the user, upon inclusion of non-preferred devices that the device being
included is not part of the vendors preferred ecosystem, and that control and support of the
device by the vendor may be limited.


a. It is not permitted to display additional pop-ups, ask for pin codes or implement any other
blocking or discouraging behavior for inclusion or control of non-preferred devices. b. The
Z-Wave Alliance recommends wording as follows. “You are about to include a Z-Wave compatible
device that is not promoted by ‘service provider name’ for use in this application. While the
device will work as expected the device may or may not support all of the features of the ‘service
provider name’ recommended device.”


**7.2.5.2** **Minimal** **Control** **Functionality**


DT:00.11.0012.1 If a controller product supports short range wireless non-Z-Wave technology smarthome products (e.g.
light bulbs, thermostats, door locks and the like) and Z-Wave technology products, it MUST, at a
minimum, control the following Command Classes:


     - Door Lock Command Class


     - Binary Switch Command Class


     - Multilevel Switch Command Class


     - Thermostat Mode Command Class


     - Thermostat Setpoint Command Class


It is acceptable to provide additional controlling functionalities for nodes from a preferred manufacturer as long as the controller provides the minimal required control functionalities for all nodes. Refer
to Section 6 for Command Class control requirements.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1165




<!-- PAGE 1167 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.6** **Command** **Class** **Support** **Specific** **Requirements**


Certain rules must be fulfilled depending on which command classes are supported. The following
subsections detail the requirements of special command classes. Details about individual Command
Classes can be found in Section 2, Section 3, Section 4 and Section 5.


**7.2.6.1** **Anti-theft** **Command** **Class**


DT:00.11.002A.1 If the Anti-Theft Command Class is supported, it MUST be version 3 or newer.


**7.2.6.2** **Application** **Status** **Command** **Class**


DT:00.11.0015.1 If a node is temporarily not capable to service a Get or Set Command request, it MUST support
the Application Status Command Class and return an Application Busy Report Command to the
initiator of the Get or Set.


DT:00.13.0004.1 If a node is always capable of servicing the Get and Set requests, it is OPTIONAL to support the
Application Status Command Class.


**7.2.6.3** **Association** **requirements**


**7.2.6.3.1** **Mandatory** **groups**


DT:00.11.0016.1 The Root Device and End Points of a Z-Wave Plus v2 node MUST advertise the Association Groups
indicated in Table 7.1 as a minimum.



Table 7.1: Z-Wave Plus v2 minimum required AGI table







|Group<br>identi<br>-<br>i<br>fer|i<br>Profle (2 bytes)|Command Class & Command<br>list (N bytes)|Group name (UTF -8) (M<br>bytes)|
|---|---|---|---|
|1|General:Lifeline|Refer to Section 7.2.6.3.2|Lifeline|


DT:00.11.0017.1 A Node or Root Device MUST advertise a “Max Nodes Supported” value of 1 or more for the Lifeline
Association group in the Association Report and Multi Channel Association Report Commands.


DT:00.12.0006.1 It is RECOMMENDED to support 5 lifeline destinations.


DT:00.11.0018.1 End Points MUST advertise a “Max Nodes Supported” of 0 for the Lifeline Group and MUST report
their Lifeline Commands via the Root Device’s Lifeline Group when an End Point Association is
established for the Lifeline Group. (Refer to Multi Channel Association Command Class)


**7.2.6.3.2** **Lifeline** **reports**


DT:00.11.0019.1 A Z-Wave Plus v2 node MUST issue all the commands defined in [23] via the Lifeline Association
Group to reflect its state changes if the corresponding command is supported by the node.

DT:00.12.0001.1 Report or Notification Commands SHOULD NOT be issued while performing a transitions from
a Command Class state to another, but only when the supporting node has reached a final state.
Intermediate transition state values SHOULD be advertised only if a long transition takes place (e.g.
transition longer than 1 minute)

DT:00.12.0002.1 Any other Command Class state or configuration relevant to the control of the node or relevant for
GUI information SHOULD be reported via the Lifeline when changed.


DT:00.11.001A.1 If the state change was triggered by other means than a Z-Wave Command, a node MUST issue the
corresponding Report/Notification Command immediately to the lifeline destination(s).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1166




<!-- PAGE 1168 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the state change was triggered by a Z-Wave Command:

DT:00.12.0003.1 - A node SHOULD NOT issue any Report/Notification Commands via the Lifeline if the actual
lifeline destination issued the Set Command.

DT:00.11.001B.1 - A node MUST NOT issue any Report/Notification Command after a Command received via
Multicast/broadcast addressing.

DT:00.11.002D.1 - A node MUST issue a Report/Notification Command after a Command received via Singlecast
using Multi Channel multi-endpoint bit addressing.

DT:00.11.001C.1 - Unless the lifeline destination issued the command, a node MUST issue a Report/Notification
Command after a command was received using singlecast addressing (including Multi Channel
multi-End Point destination) via the Lifeline.


DT:00.11.001D.1 If a node has more than one lifeline destination, it MUST issue a Report/Notification Command
after a command was received using singlecast addressing (including Multi Channel multi-End
Point destination) via the Lifeline.

An example of the expected frame flow is shown in Figure 7.1.


Figure 7.1: Lifeline status reports frame flow after multicast (example)


**7.2.6.4** **Configuration** **Command** **Class**


DT:00.11.001E.1 If the Configuration Command Class is implemented, it MUST NOT replace any existing Command
Class functionality.

DT:00.11.001F.1 If the Configuration Command Class is supported, it MUST be version 4 as a minimum.


**7.2.6.5** **Firmware** **Update** **Meta** **Data** **Command** **Class**


DT:00.11.0020.1 The configuration of Command Classes that are available before and after a firmware update MUST
remain unchanged. For instance, the Lifeline Association Group destination, Wake Up destination
and any command class setting MUST stay identical before and after performing a firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1167




<!-- PAGE 1169 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.6.5.1** **SmartStart** **QR** **Code** **accuracy**


DT:00.11.0032.1 A node undergoing a firmware update MAY have inaccurate data in its QR Code TLVs. An OTA
Firmware Update MUST NOT lead to a loss of functionality that is indicated as supported in the QR
Code.

DT:00.13.0005.1 The following TLVs MAY be inaccurate after a firmware update:


     - The Product Type


     - The ProductID

DT:00.11.0033.1 The following information MUST remain accurate after a firmware update:


     - The DSK


     - The requested keys (for non-SmartStart S2 inclusions)


     - UUID16 TLV


DT:00.12.0005.1 The Supported Protocols TLV MAY become inaccurate. The Supported Protocol SHOULD only
be inaccurate if more Protocols are supported than what the QR Code’s Supported Protocols TLV
indicates


**7.2.6.6** **Wake** **Up** **Command** **Class**


DT:00.11.0021.1 If the node supports the Wake Up Command Class, the node MUST support manual Wake Up
triggered by a user activation.


**7.2.6.7** **Multi** **Channel** **support**


DT:00.11.0022.1 Actuator functionalities MUST reside in individual Multi Channel End Points according to the list of
actuator Device Types.


DT:00.11.0023.1 Multi Channel devices MUST support the Multi Channel Command Class, version 4 or newer


DT:00.11.0024.1 A node supporting the Multi Channel Command Class MUST issue commands to the Lifeline destination from all of its End Points if an End Point Association has been established on the Root Device

Lifeline association group.


DT:00.11.0025.1 A command issued to the Lifeline destination from a Multi Channel End Point MUST be Multi

Channel encapsulated if an End Point Association has been established.


**7.2.6.8** **Security** **2** **Command** **Class**


**7.2.6.8.1** **S2** **bootstrapping** **and** **functionalities**


DT:00.21.0001.1 After network inclusion, a node MUST consider S2 Bootstrapping as started after receiving the S2
KEX Get Command.


DT:00.21.0002.1 If a node times out waiting for security bootstrapping after network inclusion, it MUST NOT consider
that bootstrapping failed and MUST consider that it was included non-securely.


DT:00.23.0001.1 If S2 bootstrapping started and did not complete successfully, a supporting node MAY remove support
of its implemented command classes until re-included. Refer to Section 2 regarding NIF contents
depending on network inclusion and security bootstrapping.


DT:00.21.0003.1 A node supporting S2 MUST consider any Security Class lower than its highest granted Security Class
as unsecure communication. Certain command classes, such as Transport Service or Z-Wave Plus Info,
must always be supported non-securely and present in the NIF if they are supported by a node. In


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1168




<!-- PAGE 1170 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


this case, non-secure support requirements are specified in each individual command class definition.
A list of these special Command Classes is also available in [25] under “Additional Comments”.


DT:00.21.0004.1 By default, a node supporting S2 MUST support its Command Classes only at the highest granted
Security Class. If no Security Class was granted, the node MUST support all its Command Class
using non-secure communication. This does not apply to S2 Access Control nodes, which MAY (or
sometimes MUST) remove support for some Command Classes if a particular Security Class has not
been granted.


**7.2.6.8.2** **S2** **Security** **Classes** **requirements**


_Security_ _2_ _(S2)_ _Command_ _Class,_ _version_ _1_ defines several Security Classes.


DT:00.21.0005.1 A Z-Wave Plus v2 node MUST request either S2 Access Control or S2 Authenticated as its highest
key.


DT:00.21.0006.1 An S2 supporting node MUST comply with the requirements indicated in the subsection below (Section
7.2.6.8.3 or Section 7.2.6.8.4) associated to its highest requested Security Class during S2 bootstrapping.


DT:00.21.0007.1 Nodes requesting the S0 Security Class MUST also comply with requirement indicated in 3.6.8.3.


DT:00.21.0008.1 A Multi Channel Root Device and all its End Points MUST share the same highest S2 Security Class.


**7.2.6.8.3** **S2** **Access** **Control** **Security** **Class**


The S2 Access Control Class is the most trusted class and is intended for home access control devices

such as door locks, garage door openers or central controllers.


DT:00.21.0009.1 A node requesting the S2 Access Control Security Class MUST carry a representation of its DSK on
itself and/or make it visible on its UI at any time when Learn Mode is enabled. Refer to Section
7.2.6.8.6 for DSK format and representation.


DT:00.21.000A.1 A node based on a controlling Device Type (4.3) requesting S2 Access Control Security Class MUST
request S2 Authenticated and S2 Unauthenticated Security Classes when being S2 bootstrapped.


DT:00.23.0002.1 A node based on a controlling Device Type (4.3) requesting the S2 Access Control Security Class
MAY decide to not support a set of its implemented Command Classes if it has not been granted a
certain Security Class during S2 bootstrapping.


DT:00.23.0003.1 A node based on a supporting Device Type (4.2) requesting S2 Access Control Security Class MAY
request any other Security Class for control purposes.


DT:00.21.000B.1 A node based on a supporting Device Type (4.2) MUST support its Command Classes depending on
Security bootstrapping as follows:


DT:00.21.000C.1 - If security bootstrapped, it MUST support its Command Classes only if the highest granted key
is S0 or S2 Access Control Security Class. It MUST NOT support its Command Classes at all
if its highest granted Security Class is any other class than S0 or S2 Access Control.


DT:00.21.000D.1 - If it timed out waiting for security bootstrapping or S0/S2 bootstrapping failed, it MUST NOT
support its Command Classes non-securely.


DT:00.21.000E.1 - The above two requirements MUST NOT apply for Command Classes that MUST always be in
the NIF (refer to Section 7.2.6.8.1 and [25]).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1169




<!-- PAGE 1171 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.6.8.4** **S2** **Authenticated** **Security** **Class**


The S2 Authenticated Class is the 2nd most trusted class and is intended for secure applications in
home control deployments.


DT:00.21.000F.1 A node requesting the S2 Authenticated Security Class MUST carry a representation of its DSK on
itself and/or make it visible on its UI at any time when Learn Mode is enabled. Refer to Section
7.2.6.8.6 for DSK format and representation.


**7.2.6.8.5** **S0** **Security** **Class** **requirements**


The S0 Class is used for backwards compatibility with S0 supporting nodes.


DT:00.21.0011.1 An S2 node MUST NOT request the S0 Security Class if it does not support the Security 0 Command
Class. An S2 node MUST NOT request the S0 Security Class without requesting an S2 Security Class.


DT:00.22.0001.1 Nodes with controlling capabilities and controllers SHOULD request the S0 Security Class for application control purposes.


**7.2.6.8.6** **DSK** **format** **and** **representations**


The S2 Command Class defines a Device Specific Key (DSK) that enables authentication as part of
the S2 Bootstrapping process.

The DSK can be represented with the following pre-defined formats: PIN code, DSK string and QR
code.

DT:00.21.0012.1 The PIN code MUST be 5 decimal digits representing the value of the first 2 bytes of the node’s DSK
and MUST be constructed according to Figure 7.2.


Figure 7.2: PIN code format


DT:00.21.0013.1 The DSK string MUST be 8 groups of 5 decimal digits, each representing 2 bytes of the DSK, separated
with hyphens and MUST be constructed according to Figure 7.3.


Figure 7.3: DSK String format


DT:00.21.0014.1 The first five digits of the DSK string MUST be underlined to help the user identify the PIN code
portion of the DSK string.

DT:00.21.0015.2 The QR code format MUST comply with the “Gen2” format defined in [29]. The QR code MUST
include two TLV blocks: Type 0 (Product Type) and TLV Type 1 (Product ID) as defined by [28].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1170




<!-- PAGE 1172 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Additional formatting requirements for the market certification are given by the Z-Wave Alliance,
refer to [30].


**7.2.6.8.7** **Mandatory** **DSK** **representations**


DT:00.21.0016.1 If a node supports Learn Mode, the DSK representations present on a product MUST comply with
Table 7.2 and the subsections below.


Table 7.2: Mandatory DSK representations for Z-Wave Plus v2
nodes











|Col1|On the Product|On the<br>l<br>leafet|On the<br>box/package|
|---|---|---|---|
|PIN<br>Code|At least one Required.|OP-<br>TIONAL|OPTIONAL|
|DSK<br>String|DSK<br>String|||
|DSK<br>String|Required in at least one place|Required in at least one place|Required in at least one place|
|QR<br>Code|Required if the node supports to be included using<br>SmartStart inclusion|OP-<br>TIONAL|OPTIONAL|


**7.2.6.8.8** **DSK** **on** **the** **product** **or** **UI**







DT:00.21.0017.1 A product MUST have a QR code printed on the its outside or on its UI if it supports to be included
using SmartStart inclusion.


DT:00.21.0018.1 A product MUST carry or display the DSK string or PIN code.

DT:00.21.0019.1 If the product carries the PIN code representation of the DSK, the product leaflet, documentation or
packaging MUST contain the DSK string.


**7.2.6.8.9** **DSK** **on** **documentation** **or** **leaflet**


DT:00.22.0002.1 It is RECOMMENDED that a leaflet inside the product’s box, advertises the QR code and the full
DSK string.


**7.2.6.8.10** **DSK** **on** **the** **product’s** **box/package**


DT:00.22.0003.1 The product packaging SHOULD carry the QR code and DSK string on its outside.


**7.2.6.8.11** **Filtering** **Security** **Class** **for** **controlling** **nodes**


DT:00.23.0004.1 For Command Classes always supported non-securely (always in the NIF), a controlling node MAY
accept a command at any security level shared with a sending S2 node.


DT:00.21.001A.1 For Command Classes supported securely, a controlling node MUST discard the command from a
supporting node if not received at the highest common security level between the controlling node
and the sending S2 node.


DT:00.21.001B.1 A controlling node MUST NOT discard a command if the sending node does not support the S2
Command Class.


A node is considered controlling or supporting based on which command it sends or receives. Each
command node’s role is marked in [25].


DT:00.22.0006.1 Further, a controller node that has performed S2 bootstrapping to a Node A SHOULD discard controlling commands from Node A if not received using the highest common security level for Command
Classes that are always supported non-securely (always in the NIF).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1171




<!-- PAGE 1173 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.6.8.12** **Controlling** **nodes:** **Security** **Class** **learning**


Any Z-Wave Plus v2 node controlling Command Classes (not using association groups) MUST discover
the destination capabilities using every Security Class. If it intends to create associations between 2
other nodes, it MUST also discover which keys have been granted to both nodes.


If the controller is the SIS, it SHOULD skip the discovery as it knows which keys have been granted.
If the controller is not the SIS or does not know which security levels to use with a destination, the
following discovery algorithm is RECOMMENDED:


1. Request the NIF and read its contents, look for S2/Supervision and S0


2. If S2 is supported, for every S2 key starting from the highest:


a. Issue the S2 Commands Supported Get


i. If receiving no answer (or S2 Nonce Reports), conclude that the corresponding Security
Class has not been granted to the node


ii. If receiving an S2 Commands Supported Report with an empty list, conclude that the
corresponding Security Class has been granted and is not the highest


iii. If received an S2 Commands Supported Report with a non-empty list, conclude that
the corresponding Security Class has been granted and is the highest.


3. If S0 is supported, discover if S0 key was granted:


a. Issue a S0 encrypted S0 Security Command Supported Get command


b. If S2 was in the NIF :


i. If not receiving any response, conclude that the S0 Security Class has not been granted
to the node


ii. If receiving an S0 Commands Supported Report with an empty list, conclude that the
S0 Security Class has been granted and is not the highest


iii. If receiving an S0 Commands Supported Report with a non-empty list, conclude that
the S0 Security Class has been granted and is the highest


c. If S2 was not in the NIF:


i. If receiving an S0 Commands Supported Report, conclude that S0 is the highest granted
key


ii. If not receiving any response, conclude that the S0 Security Class has not granted to
the node

The _Role_ _Type_ _Specification_ provides recommended timeouts when waiting for responses to get type
commands.


**7.2.7** **Command** **Class** **Control** **Specific** **Requirements**


Certain rules must be fulfilled depending on which command classes are controlled. The following
subsections detail the requirements of special command classes. Details about individual Command
Class control can be found in Section 6.


DT:00.11.0034.1 If a Device Type mandates that a Command Class MUST be controlled, that Command Class MUST
be fully controlled. Partial control is not acceptable for Command Classes that have mandatory
control requirements. Refer to _Command_ _Class_ _Control_ for full and partial control definitions.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1172




<!-- PAGE 1174 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.7.1** **Anti-Theft** **Command** **Class**


Control of this command class is limited to an entity that has been granted permission by the Z-Wave
Alliance to control this Command Class and has been granted a locking entity ID. The list of granted
locking entity IDs is defined in [22].

Any node controlling this Command Class without authorization will be failed in certification.


DT:00.11.002B.1 A node controlling this Command Class MUST NOT provide access to the locking functionality feature
of the Command Class to a consumer/end-user of the node; i.e. end users MUST NOT be able to
lock nodes themselves.

DT:00.11.002C.1 Control of this command class by a node which is also offered in a non-service market where an end
consumer has access to network control features MUST use a different Product ID and Product Type
ID between the service and consumer versions of the product.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1173




<!-- PAGE 1175 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.8** **SmartStart** **Requirements**


DT:00.11.0026.1 A Z-Wave Plus v2 node MUST either support to be included in a network using SmartStart inclusion
or provide SmartStart inclusion of other nodes. A controller providing SmartStart inclusion of other
nodes MAY also support being included in a network using SmartStart inclusion.


DT:00.11.0027.1 A SmartStart product documentation MUST respect the requirements described in 3.10.4 Documentation related to SmartStart.


DT:00.11.0028.1 A node supporting to be included using SmartStart inclusion MUST have a QR code printed on its
outside or its UI. (refer to Section 7.2.6.8.7). The QR code MUST indicate version 1 (SmartStart
enabled nodes).


DT:00.11.0029.1 A SmartStart node MUST carry and keep the same Learn Mode DSK during its entire lifetime. Refer
to Section 7.2.6.8.2 and Section 7.2.6.8.6.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1174




<!-- PAGE 1176 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.9** **Z-Wave** **Long** **Range** **Support**


**7.2.9.1** **Nodes** **supporting** **to** **be** **included** **with** **Z-Wave** **Long** **Range**


DT:00.11.002E.1 Nodes supporting Z-Wave Long Range MUST have a QR code printed on its outside or its UI (refer
to 3.6.8.5 Mandatory DSK representations). The QR code MUST include a Type 4 (Supported
Protocols) TLV block (refer to [28]) and indicate that Z-Wave Long Range is supported.


DT:00.11.002F.1 A node supporting Z-Wave Long Range MUST only request any Security Class that require Authentication for the S2 Bootstrapping during a Z-Wave Long Range SmartStart inclusion.


**7.2.9.2** **Nodes** **supporting** **to** **include** **using** **Z-Wave** **Long** **Range**


DT:00.11.0030.1 Controller nodes that can include other nodes using Z-Wave Long Range MUST allow to configure
the Bootstrapping Mode TLV of provisioning list entries to “Z-Wave Long Range SmartStart” (value
0x02) for entries that advertise Z-Wave Long Range as a supported protocol


DT:00.11.0031.1 A controller node MUST only grant Security Classes that require Authentication for the S2 Bootstrapping during a Z-Wave Long Range SmartStart inclusion.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1175




<!-- PAGE 1177 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.10** **Required** **Documentation**


The following requirements for end user documentation apply to all Z-Wave Plus v2 compliant products. The documentation may be provided as product manuals, quick start guides, electronic help
files, web pages, etc.


**7.2.10.1** **Terminology**


DT:00.31.0001.1 The product documentation MUST use the terminology indicated in Table 7.3 for Z-Wave related
functionality.


Table 7.3: Z-Wave Z-Wave Plus v2 documentation terminology

|Z -Wave functionality|Documentation ter-<br>minology|Example|
|---|---|---|
|Inclusion|Add|The process of adding a node to the Z-Wave<br>network.|
|Exclusion|Remove|The process of removing a node from the Z-Wave<br>network.|
|Replication|Copy|The process of copying network information<br>from one controller to another.|



**7.2.10.2** **Additional** **documentation** **required** **for** **Z-Wave** **Certification**


DT:00.31.0002.1
In addition to the rules defined above the following technical documentation MUST be made available
to the certification test lab upon submitting the product for certification:


     - Documentation about how to activate any functionality available in the device related to Z-Wave
behavior

     - If any special procedures are REQUIRED to test any item in the certification form, such procedures MUST be clearly described


     - If the product is a Z-Wave controller, documentation on how to send any controlled command
from the controller MUST be included, refer to Section 6.


**7.2.10.3** **Documentation** **for** **Classic** **Inclusion** **and** **Exclusion**


DT:00.31.0003.1 For Z-Wave end nodes Role Types, the documentation MUST describe:


     - How to include and exclude the device in an existing network when using Classic inclusion.


DT:00.31.0004.2 For Z-Wave controller Role Types, the documentation MUST describe:


     - How to include and exclude the device in an existing network using classic inclusion.


     - How to include and exclude other devices.


     - How to put the controller into learn mode to receive network information from another controller.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1176




<!-- PAGE 1178 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.10.4** **Documentation** **related** **to** **SmartStart**


DT:00.31.0005.1 The documentation MUST describe:


     - How to locate the DSK representation(s) on the product.


     - How to access the DSK representation(s) via the UI, if available.


DT:00.31.0006.2 For nodes providing SmartStart functionalities, the documentation MUST include a short description
of what is SmartStart. The following wording is RECOMMENDED:


_SmartStart_ _enabled_ _products_ _can_ _be_ _added_ _into_ _a_ _Z-Wave_ _network_ _by_ _scanning_ _the_ _Z-Wave_
_QR_ _Code_ _present_ _on_ _the_ _product_ _with_ _a_ _controller_ _providing_ _SmartStart_ _inclusion._ _No_
_further_ _action_ _is_ _required_ _and_ _the_ _SmartStart_ _product_ _will_ _be_ _added_ _automatically_ _within_
_10_ _minutes_ _of_ _being_ _switched_ _on_ _in_ _the_ _network_ _vicinity._


DT:00.31.0007.1 For controllers providing the SmartStart functionality, the documentation MUST describe:


     - How to perform a secure inclusion of a SmartStart node (adding the node in the Node Provisioning List and powering up/installing the node)


     - How to access and edit the Node Provisioning List.


DT:00.31.0019.1 For nodes supporting to be included using SmartStart, which do not follow the recommendation to
enter SmartStart Learn Mode automatically after powering on, the documentation MUST describe:


     - How to manually enter SmartStart Learn Mode if already powered up


     - Whether or not the node keeps SmartStart Learn Mode enabled after a failed SmartStart inclu
sion.


DT:00.31.001A.1 For nodes supporting to be included using SmartStart, which do not follow the recommendation to
stay in SmartStart Learn Mode forever until included, the documentation MUST describe:


     - How long the node stays in SmartStart Learn Mode


     - Whether or not the node keeps SmartStart Learn Mode enabled after a failed SmartStart inclu
sion.


**7.2.10.5** **Documentation** **related** **to** **devices** **from** **multiple** **manufacturers**


DT:00.31.0008.1 The product documentation MUST include a section which describes how products from different
manufacturers and product categories can be a part of the same Z-Wave network, and that the
different mains powered nodes can act as repeaters regardless of manufacturers.


The following is the RECOMMENDED wording:

_This_ _product_ _can_ _be_ _operated_ _in_ _any_ _Z-Wave_ _network_ _with_ _other_ _Z-Wave_ _certified_ _devices_
_from other manufacturers._ _All mains operated nodes within the network will act as repeaters_
_regardless_ _of_ _vendor_ _to_ _increase_ _reliability_ _of_ _the_ _network._


**7.2.10.6** **Documentation** **for** **Association** **Command** **Class**


DT:00.31.0009.1 The documentation MUST include a description of the association groups available in the product.


DT:00.31.000A.1 Each group MUST include the following information:

     - Grouping identifier


     - Maximum number of devices that can be added to the group


     - Description of how the association group is used and/or triggered by the product


     - Description of any mapping between groups (e.g. Root Device mirrored End Point group)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1177




<!-- PAGE 1179 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.10.7** **Documentation** **for** **Configuration** **Command** **Class**


DT:00.31.000B.1 If the product implements support of the Configuration Command Class, the documentation MUST
include a description of each configuration parameter available in the product.

DT:00.31.000C.1 Each configuration parameter MUST be listed with the following information:


     - Parameter number

     - Description of parameter and its effect on the product


     - Default value and allowed values


     - Size (number of bytes)

DT:00.32.0001.1 The documentation SHOULD also list other configuration parameter properties such as read-only or
advanced flag, etc.


**7.2.10.8** **Documentation** **for** **Wake** **Up** **Command** **Class**


DT:00.31.000D.1 If the node supports the Wake Up Command Class, the product documentation MUST describe how
to manually Wake Up the node.


**7.2.10.9** **Documentation** **for** **Security** **2** **Command** **Class**


DT:00.31.000E.2 If a node based on an end node Role Type supports its Command Classes only when granted the
Access Control Security key, the documentation MUST indicate that an S2 security enabled controller
is required to operate the product.


DT:00.31.000F.1 The documentation MUST list the supported Command Classes, their version and their required
Security class if any.


For example, a Lock Device Type list and a Binary Switch Device Type list are given in Table 7.4
and Table 7.5.


Table 7.4: Lock DT Supported Command Classes documentation

|Table 7.4: Lock example Command Class|DT Supported Command Classes Version|s documentation Required Security Class|
|---|---|---|
|**Command Class**|**Version**|**Required Security Class**|
|Association|2|S0 or Access Control|
|Association Group Information|3|S0 or Access Control|
|Basic|2|S0 or Access Control|
|Device Reset Locally|1|S0 or Access Control|
|Door Lock|4|S0 or Access Control|
|Firmware Update Meta Data|5|S0 or Access Control|
|Indicator<br>|3|S0 or Access Control|
|Manufacturer Specifc|1|S0 or Access Control|
|Multi Channel Association|3|S0 or Access Control|
|Powerlevel|1|S0 or Access Control|
|Security 0|1|None|
|Security 2|1|None|
|Supervision|1|None|
|Transport Service|2|None|
|Version|3|S0 or Access Control|
|Z-Wave Plus Info|2|None|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1178




<!-- PAGE 1180 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 7.5: Binary Switch DT Supported Command Classes documentation example

|Command Class|Version|Required Security Class|
|---|---|---|
|Association|2|Highest granted Security Class|
|Association Group Information|3|Highest granted Security Class|
|Basic|2|Highest granted Security Class|
|Binary Switch|2|Highest granted Security Class|
|Device Reset Locally|1|Highest granted Security Class|
|Firmware Update Meta Data|5|Highest granted Security Class|
|Indicator<br>|3|Highest granted Security Class|
|Manufacturer Specifc|1|Highest granted Security Class|
|Multi Channel Association|3|Highest granted Security Class|
|Powerlevel|1|Highest granted Security Class|
|Security 2|1|None|
|Supervision|1|None|
|Transport Service|2|None|
|Version|3|Highest granted Security Class|
|Z-Wave Plus Info|2|None|



**7.2.10.10** **Documentation** **for** **Supervision** **Command** **Class**


DT:00.31.0015.1 If a node supports the Supervision Command Class, the product documentation MUST describe the
list of cases and/or conditions where it would issue a _Supervision_ _Report_ _Command_ with a status
indicating WORKING or FAIL, for a valid and supported set of parameters in the encapsulated
command.


For example, it is not necessary to describe that a Supervision encapsulated _Association Set Command_
would return FAIL if trying to establish a new association in a group that is already full.


**7.2.10.11** **Documentation** **for** **Basic** **Command** **Class**


DT:00.31.0014.2 If the product supports Basic Command Class, the product documentation MUST include information
on the usage of the Basic Command Class and the resulting product behavior


**7.2.10.12** **Documentation** **for** **Notification** **Command** **Class**


DT:00.31.0015.1 If the product implements support of the Notification Command Class, the documentation MUST
specify the implemented Notification Type(s) and Event(s).


**7.2.10.13** **Documentation** **for** **dynamic** **capabilities**


DT:00.31.0010.1 If the product can alter its capabilities depending on a configuration parameter or based on a user
interaction, the documentation MUST include a list of all events that can trigger capability change
and describe:


     - How to perform such actions


     - What capabilities are being altered.


DT:00.31.0011.1 The product documentation MUST indicate to the end user that it is necessary to ask a controlling
node to rediscover the product’s capabilities after altering capabilities.


DT:00.31.0012.1 The product documentation MUST indicate that it is necessary to re-include the node in the network
if the controller does not have any capability rediscovery option.


DT:00.31.0013.1 For nodes based on a controlling Device Type (4.3), the documentation MUST describe how an
(advanced) end user can perform a capability rediscovery of a chosen node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1179




<!-- PAGE 1181 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.2.10.14** **Documentation** **for** **Identity** **function**


DT:00.31.0016.1 The product documentation MUST describe how product can be identified using the Indicator Command Class with the Indicator ID 0x50 (identify).


**7.2.10.15** **Documentation** **for** **Z-Wave** **Long** **Range**


DT:00.31.0017.1 Nodes supporting Z-Wave Long Range MUST indicate in their documentation if they can be included
and/or if they can include other nodes using Z-Wave Long Range.


**7.2.10.15.1** **Nodes** **supporting** **to** **include** **using** **Z-Wave** **Long** **Range**


DT:00.31.0018.1 Controller nodes that can include other nodes using Z-Wave Long Range MUST indicate how to change
the bootstrapping mode (Z-Wave SmartStart vs Z-Wave Long Range SmartStart) of provisioning list
entries.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1180




<!-- PAGE 1182 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **7.3 Z-Wave Plus v2 Device Type Definition**


**7.3.1** **Optional** **Command** **Classes**


Device Types MAY support optional Command Classes on top of the minimum mandatory set of
DT:00.11.000F.1 supported Command Classes. However, the following Command Classes MUST NOT be supported
optionally in a Device Type:


     - Barrier Operator


     - Color Switch


     - Window Covering


     - Multilevel Switch


     - Thermostat Mode


     - Thermostat Setpoint


     - Thermostat Setback


     - Sound Switch


     - Simple AV Control


     - Door Lock


     - Binary Switch

DT:00.11.0010.1 It means that if supported, these command classes MUST fit the exact actuator Command Class list
of a Device Type. If several actuator Command Classes not belonging to the Device Type need to be
supported, they MUST be partitioned in End Points which match the actuator Command Class list
of a Device Type.


Multi Channel Root Devices MAY still aggregate some of the above mentioned Command Classes
from their end points for backwards compatibility. The optional Command Class rule applies:


     - For the node (Root Device) if the node does not support Multi Channel Command Class


     - For each and every end point if the node supports the Multi Channel Command Class


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1181




<!-- PAGE 1183 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.2** **Supporting** **Device** **type** **overview**


The Z-Wave Plus v2 certification program defines a new set of Device Type based on which Command
Classes are supported. They are classified into 3 categories:


 - Actuator supporting device types.


 - Data reporting devices types


 - Other devices types.


The list of Supporting Device Types is shown in Table 7.6, Table 7.7 and Table 7.8.



Table 7.6: Z-Wave Plus v2 Supporting Actuator Device Types

overview


























|Device Type|Mandatory|Recommended options|Role<br>Types|
|---|---|---|---|
|Lock|Door Lock, v4<br>Security 0 (S0)|User Code<br>Entry Control|All|
|Motorized<br>bar-<br>rier|Barrier Operator<br>Notifcation, v8<br>Security 0 (S0)||All|
|Color Switch|Color Switch, v3<br>Multilevel Switch v4 or Binary<br>Switch v2|Multi Command|All|
|Window<br>Cover-<br>ing|Window covering<br>Multilevel Switch v4||All|
|Thermostat|Thermostat Mode, v3<br>Thermostat Setpoint|Clock (support) or Time (con-<br>trol)<br>Multilevel Sensor<br>Schedule, v4<br>Thermostat Setback|All|
|Sound Switch|Sound Switch||All|
|AV Control Point|Simple AV Control||All|
|Multilevel Switch|Multilevel Switch, v4||All|
|Binary Switch|Binary Switch, v2||All|



Table 7.7: Z-Wave Plus v2 Supporting Data Reporting Device
Types overview








|Device Type|Mandatory|Recommended options|Role<br>Types|
|---|---|---|---|
|Entry<br>Control<br>Keypad|Entry Control<br>Security 0 (S0)||All|
|Multilevel Sensor<br>|Multilevel Sensor, v11<br>|Multi Command (control)|All|
|Notifcation Sen-<br>sor|Notifcation, v8|Multi Command (control)|All|
|Meter Sensor|Meter, v5|Multi Command (control)|All|
|Central Scene|Central Scene, v3|Basic (control)|All|



Table 7.8: Z-Wave Plus v2 Supporting Other Device Types

overview

|Device Type|Mandatory|Recommended options|Role<br>Types|
|---|---|---|---|
|Repeater|No other Command Class than<br>Section 7.2.2.1||AOEN|
|IR Repeater|IR Repeater Command Class||AOEN|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1182




<!-- PAGE 1184 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.3** **Controlling** **Device** **type** **overview**


The Z-Wave Plus v2 certification program defines a new set of Device Type for controllers based on
which Command Classes are supported and controlled.


The controlling Device Type overview is shown in Table 7.9.



Table 7.9: Z-Wave Plus v2 Controlling Device Types overview












|Device Type|Mandatory (support)|Mandatory (control)|Role<br>Types|
|---|---|---|---|
|Gateway|CRC-16 Encapsulation<br>Multi Command<br>Node Provisioning<br>Security 0 (S0)<br>Time|Association, version 2<br>Association<br>Group<br>Informa-<br>tion, version 3<br>Basic, version 2<br>Central Scene, version 3<br>CRC-16 Encapsulation<br>Firmware Update Meta Data,<br>version 5 Indicator, version 3<br>Meter, version 5<br>Multi Channel, version 4<br>Multi<br>Channel<br>Association,<br>version 3<br>Multilevel Sensor, version 11<br>Notifcation, version 8<br>Security 0 (S0)<br>Security 2 (S2)<br>Version, version 2<br>Wake up, version 2|CSC|
|Generic<br>Con-<br>troller|Multi Command|Basic<br>Indicator, version 3<br>The<br>actuator<br>Command<br>Classes of at least 1 actuator<br>Device Type<br>Version, version 2<br>Wake up, version 2|CSC, SSC,<br>RPC, PC,<br>EN|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1183




<!-- PAGE 1185 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.4** **From** **Z-Wave** **Plus** **to** **Z-Wave** **Plus** **v2** **certification**


Table 7.10 indicates the recommended transitions from a Z-Wave Plus Device Type to a Z-Wave Plus
v2 Device Type.


Table 7.10: Equivalent Z-Wave Plus and Z-Wave Plus v2 Device







|Table 7.10: Equivalent Z-Wave P Types Z-Wave Plus DT(s)|Plus and Z-Wave Plus v2 Device Suggested Z-Wave Plus v2 DT(s)|
|---|---|
|**Z-Wave Plus DT(s)**<br>|**Suggested Z-Wave Plus v2 DT(s)**|
|On/Of Power Switch<br>Power Strip<br>Valve – Open/close<br>Irrigation control|Binary Switch|
|Siren|Binary Switch<br>Sound Switch|
|Door Lock – Keypad<br>Lockbox|Lock|
|Light Dimmer Switch<br>Fan Switch|Multilevel Switch|
|Set Top box<br>TV<br>Sub system<br>Controller|Gateway<br>Generic Controller|
|Remote Control – Multi purpose<br>Remote control – Simple<br>Wall controller|Generic Controller<br>Central Scene|
|Sub Energy Meter<br>Whole Home Meter|Meter Sensor|
|Gateway<br>Central Controller|Gateway|
|Thermostat – HVAC<br>Thermostat – Setback|Thermostat|
|Remote control -AV|Generic Controller|
|Window Covering|Window Covering|


The following Device Types are unchanged and have the same equivalent Device Type in the Z-Wave
Plus v2 certification program:

 - Sensor  - Notification


 - Sensor  - Multilevel


 - AV Control Point


 - Sound Switch


 - Barrier Operator


 - Entry Control keypad


 - Repeater


The following Device Type is discontinued:


 - Display  - Simple


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1184




<!-- PAGE 1186 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5** **Actuator** **supporting** **types**


**7.3.5.1** **Lock** **DT**


The Lock Device Type is intended for nodes implementing a lock mechanism with optional handles.
It can be a door lock, a lockbox as well as a safe.


**7.3.5.1.1** **Generic** **and** **Specific** **Device** **Class**


DT:01.11.0001.1 The Lock Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_ENTRY_CONTROL (0x40)


     - SPECIFIC_TYPE_DOOR_LOCK (0x01)


**7.3.5.1.2** **S2** **Security** **Classes**


DT:01.11.0002.1 The Root Device MUST request Access Control Security Class if it (or any End Point) uses this
Device Type.


**7.3.5.1.3** **Mandatory** **Command** **Classes**


DT:01.11.0003.1 The Lock MUST support the following Command Classes:


     - Door Lock, version 4


     - Basic, version 2


     - Security 0 (S0)


Recommended optional command classes for advanced applications:


     - User Code


     - Entry Control


     - Generic Schedule


     - Authentication


     - Authentication Media Write


**7.3.5.1.4** **Basic** **Command** **Class** **Requirements**


DT:01.11.0004.1 The Basic Command Class MUST be mapped according to Table 7.11.


Table 7.11: Lock Device Type Basic mapping

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Door Lock Operation Set (Door Lock Mode)|
|Basic Report (Current Value = 0x00)|Door Lock Operation Report (Door Lock Mode = 0x00)|
|Basic Report (Current Value = 0xFF)|Door Lock Operation Report (Door Lock Mode != 0x00)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1185




<!-- PAGE 1187 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.2** **Motorized** **Barrier** **DT**


The Motorized Barrier Device Type is intended for barriers, gates or garage doors devices.


**7.3.5.2.1** **Generic** **and** **Specific** **Device** **Class**


DT:02.11.0001.1 The Motorized Barrier Device Type MUST use the following Generic Device Class:


     - GENERIC_TYPE_ENTRY_CONTROL (0x40)

DT:02.11.0002.1 The Motorized Barrier Device Type MUST use one of the following Specific Device Classes based on
its capabilities within the Barrier Operator Command Class:


     - SPECIFIC_TYPE_SECURE_GATE (0x06) if it can both open and close


     - SPECIFIC_TYPE_SECURE_BARRIER_OPEN_ONLY (0x08) if it can open only


     - SPECIFIC_TYPE_SECURE_BARRIER_CLOSE_ONLY (0x09) if it can close only


**7.3.5.2.2** **S2** **Security** **Classes**


DT:02.11.0003.1 The Root Device MUST request Access Control Security Class if it (or any End Point) uses this
Device Type.


**7.3.5.2.3** **Mandatory** **Command** **Classes**


DT:02.11.0004.1 The Motorized Barrier Devices MUST support the following Command Classes:


     - Barrier Operator

     - Notification, version 8


     - Basic, version 2


     - Security 0 (S0)


**7.3.5.2.4** **Basic** **Command** **Class** **Requirements**


DT:02.11.0005.1 The Basic Command Class MUST be mapped according to Table 7.12.


Table 7.12: Motorized Barrier Device Type Basic mapping

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Barrier Operator Set (Target Value)|
|Basic Report (Current Value = 0x00)|Barrier Operator Report (State = 0x00)|
|Basic Report (Current Value = 0xFF)|Barrier Operator Report (State > 0x00)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1186




<!-- PAGE 1188 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.3** **Color** **Switch** **DT**


The Color Switch Device Type is intended for a lighting product having the ability to change its color.


**7.3.5.3.1** **Generic** **and** **Specific** **Device** **Class**


DT:03.11.0001.1 The Color Switch Device Type MUST use the following Generic Device Classes:


     - GENERIC_TYPE_SWITCH_BINARY (0x10) if supporting Binary Switch


     - GENERIC_TYPE_SWITCH_MULTILEVEL (0x11) if supporting Multilevel Switch

DT:03.11.0002.1 The Color Switch Device Type MUST use the following Specific Device Classes:


     - SPECIFIC_TYPE_COLOR_TUNABLE_BINARY (0x02) if supporting Binary Switch


     - SPECIFIC_TYPE_COLOR_TUNABLE_MULTILEVEL (0x02) if supporting Multilevel
Switch


**7.3.5.3.2** **Mandatory** **Command** **Classes**


DT:02.11.0003.1 The Color Switch MUST support the following Command Classes:


     - Color Switch, version 3


     - Multilevel switch, version 4 or Binary Switch, version 2


     - Basic, version 2


**7.3.5.3.3** **Basic** **Command** **Class** **Requirements**


DT:02.11.0005.1 The Basic Command Class MUST be mapped according to Table 7.13 if supporting the Binary Switch
Command Class or Table 7.14 if supporting the Multilevel Switch Command Class.


Table 7.13: Color Switch Device Type Basic mapping for Binary
Switch

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Binary Switch Set (Target Value)|
|Basic Report (Current Value, Target Value,<br>Duration)|Binary Switch Report (Current Value,<br>Target<br>Value, Duration)|



Table 7.14: Color Switch Device Type Basic mapping for Multilevel

|Table 7.14: Color Switch Dev Switch Basic Command|vice Type Basic mapping for Multilevel Mapped Command|
|---|---|
|**Basic Command**|**Mapped Command**|
|Basic Set (Value)|Multilevel Switch Set (Value)|
|Basic Report (Current Value, Target Value,<br>Duration)|Multilevel Switch Report (Current Value, Target<br>Value, Duration)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1187




<!-- PAGE 1189 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.4** **Window** **Covering** **DT**


The Window Covering Device Type is intended for curtains or blinds allowing the end user to control
the amount of light going through windows.


**7.3.5.4.1** **Generic** **and** **Specific** **Device** **Class**


DT:04.11.0001.1 The Window Covering Device Type MUST use the following Generic Device Classes:


     - GENERIC_TYPE_SWITCH_MULTILEVEL (0x11)

DT:04.11.0002.1 The Window Covering Device Type MUST use one of the following Specific Device Classes based on
its capabilities within the Window Covering Command Class:


     - SPECIFIC_TYPE_CLASS_A_MOTOR_CONTROL (0x05) if no position/endpoint aware
ness


     - SPECIFIC_TYPE_CLASS_B_MOTOR_CONTROL (0x06) if endpoint aware


     - SPECIFIC_TYPE_CLASS_C_MOTOR_CONTROL (0x07) if position and endpoint aware


**7.3.5.4.2** **Mandatory** **Command** **Classes**


DT:04.11.0003.1 The Window Covering MUST support the following Command Classes:


     - Window Covering, version 1


     - Multilevel Switch, version 4 (MUST be redundant to Window Covering, i.e. actuating the same
hardware)


     - Basic, version 2


**7.3.5.4.3** **Basic** **Command** **Class** **Requirements**


DT:04.11.0004.1 The Basic Command Class MUST be mapped according to Table 7.15.



Table 7.15: Window Covering Device Type Basic mapping






|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value=0xFF)|Multilevel Switch Set (0xFF) if endpoint aware<br>Start level change(Up/down) if not endpoint aware|
|Basic Set (Value=0x00)|Multilevel Switch Set (0x00) if endpoint aware<br>Stop level change if not endpoint aware|
|Basic<br>Set<br>(Value=0x01..0x63)|Multilevel Switch Set (0x01..0x63) if position aware<br>Start level change(Up/down) if not position aware|
|Basic<br>Report<br>(Current<br>Value,<br>Target<br>Value,<br>Duration)|Multilevel Switch Report (Current Value, Target Value, Duration)<br>Current Value and Target Value MUST be set to 0xFE if not position<br>aware|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1188




<!-- PAGE 1190 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.5** **Thermostat** **DT**


The Thermostat Device Type is intended by thermostats that support set points and modes. It is
typically used for all mainstream thermostats that can support e.g. Heating, Cooling and Fans.


**7.3.5.5.1** **Generic** **and** **Specific** **Device** **Class**


DT:05.11.0001.1 The Thermostat Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_THERMOSTAT (0x08)


     - SPECIFIC_TYPE_THERMOSTAT_GENERAL_V2 (0x06)


**7.3.5.5.2** **Mandatory** **Command** **Classes**


DT:05.11.0002.1 The Thermostat MUST support the following Command Classes:


     - Thermostat Mode, version 3


     - Thermostat Set Point


     - Basic, version 2


Recommended optional command classes:


     - Multilevel Sensor, supporting Sensor Type 0x01 (temperature)


     - Clock


     - Schedule, version 4


     - Thermostat Setback


As an alternative to supporting Clock, the node can also control:


     - Time


**7.3.5.5.3** **Basic** **Command** **Class** **Requirements**


DT:05.11.0003.1 The Basic Command Class MUST be mapped according to Table 7.16.


Table 7.16: Thermostat Device Type Basic mapping






|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value=0xFF)|Thermostat Mode Set (Mode = 0x01, 0x02 or 0x03)|
|Basic Set (Value=0x00)|Thermostat Mode Set (Mode = 0x00, 0x0B, 0x0C or 0x0D)|
|Basic<br>Report<br>(Current<br>Value<br>=<br>0xFF)|Thermostat Mode Report (Mode = 0x01, 0x02 or 0x03)|
|Basic<br>Report<br>(Current<br>Value<br>=<br>0x00)|Thermostat Mode Report (Mode = 0x00, 0x0B, 0x0C or<br>0x0D)|



DT:05.11.0004.1 Other modes than 0x01, 0x02 or 0x03 MAY be mapped to Basic (Value=0xFF). In this case, it MUST
be documented in the user manual.


DT:05.11.0005.1 Other modes than 0x00, 0x0B, 0x0C or 0x0D MAY be mapped to Basic (Value=0x00). In this case,
it MUST be documented in the user manual.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1189




<!-- PAGE 1191 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.6** **Sound** **Switch** **DT**


The Sound Switch Device Type is intended for products with the ability to issue sound notifications
with a pre-programmed sound inventory. It can be used for a doorbell, chime, siren, alarm clock or
any device issuing sounds.


**7.3.5.6.1** **Generic** **and** **Specific** **Device** **Class**


DT:06.11.0001.1 The Sound Switch Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_AV_CONTROL_POINT (0x03)


     - SPECIFIC_TYPE_SOUND_SWITCH (0x01)


**7.3.5.6.2** **Mandatory** **Command** **Classes**


DT:06.11.0002.1 The Sound Switch MUST support the following Command Classes:


     - Sound Switch


     - Basic, version 2


**7.3.5.6.3** **Basic** **Command** **Class** **Requirements**


DT:06.11.0003.1 The Basic Command Class MUST be mapped according to Table 7.17.


Table 7.17: Sound Switch Device Type Basic mapping

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Sound Switch Tone Play Set (Tone Identifer)<br>|
|Basic Report (Current Value = 0x00)|Sound Switch Tone Play Report (Tone Identifer = 0x00)<br>|
|Basic Report (Current Value = 0xFF)|Sound Switch Tone Play Report (Tone Identifer > 0x00)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1190




<!-- PAGE 1192 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.7** **AV** **Control** **Point** **DT**


The AV Control Point Device Type is intended for products with the ability to receive IR codes. It
can be a TV, DVD player or any multimedia device that can now be also controller via Z-Wave.


**7.3.5.7.1** **Generic** **and** **Specific** **Device** **Class**


DT:07.11.0001.1 The AV Control Point Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_AV_CONTROL_POINT (0x03)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.5.7.2** **Mandatory** **Command** **Classes**


DT:07.11.0002.1 The AV Control Point Device Type MUST support the following Command Classes:


     - Simple AV Control


     - Basic, version 2


**7.3.5.7.3** **Basic** **Command** **Class** **Requirements**


DT:07.11.0003.1 The Basic Command Class MUST be mapped according to Table 7.18.








|Basic|Table 7.18: AV Control Point Device Type Basic mapping Mapped Command|
|---|---|
|**Basic**<br>**Command**|**Mapped Command**|
|Basic<br>Set<br>(Value)|Simple AV Set (Command).<br>The associated AV Codes Commands to the values 0x00 and 0xFF chosen be the<br>manufacturer MUST switch the node’s main functionality On and Of.<br>(such as<br>play/pause or volume up/volume down)|
|Basic<br>Report<br>(Current<br>Value)|None<br>The reported value MAY indicate if the node’s main functionality is On or Of. (such<br>as play/paused) else current value SHOULD be set to 0x00.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1191




<!-- PAGE 1193 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.8** **Multilevel** **Switch** **DT**


The Multilevel Switch Device Type is intended for products that can be switched between more than
2 discrete levels or states, such a light dimmer, water valve or a fan.


**7.3.5.8.1** **Generic** **and** **Specific** **Device** **Class**


DT:08.11.0001.1 The Multilevel Switch Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_SWITCH_MULTILEVEL (0x11)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.5.8.2** **Mandatory** **Command** **Classes**


DT:08.11.0002.1 The Multilevel Switch Device Type MUST support the following Command Classes:


     - Multilevel Switch, version 4


     - Basic, version 2


**7.3.5.8.3** **Basic** **Command** **Class** **Requirements**


DT:08.11.0003.1 The Basic Command Class MUST be mapped according to Table 7.19.


Table 7.19: Multilevel Switch Device Type Basic mapping

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Multilevel Switch Set (Value)|
|Basic Report (Current Value, Duration)|Multilevel Switch Report (Value, Duration)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1192




<!-- PAGE 1194 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.5.9** **Binary** **Switch** **DT**


The Binary Switch Device Type is intended for any actuator functionality that can only be switched
between 2 states (On and Off). It can be a valve, a light switch, a plug-in module.


**7.3.5.9.1** **Generic** **and** **Specific** **Device** **Class**


DT:09.11.0001.1 The Binary Switch Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_SWITCH_BINARY (0x10)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.5.9.2** **Mandatory** **Command** **Classes**


DT:09.11.0002.1 The Binary Switch MUST support the following Command Classes:


     - Binary Switch, version 2


     - Basic, version 2


DT:09.12.0001.1 If the node can measure energy, water or gas consumption, it is RECOMMENDED to support:


     - Meter, version 5


**7.3.5.9.3** **Basic** **Command** **Class** **Requirements**


DT:09.11.0003.1 The Basic Command Class MUST be mapped according to Table 7.20.


Table 7.20: Binary Switch Device Type Basic mapping

|Basic Command|Mapped Command|
|---|---|
|Basic Set (Value)|Binary Switch Set (Value)|
|Basic Report (Current Value, Duration)|Binary Switch Report (Value, Duration)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1193




<!-- PAGE 1195 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.6** **Reporting** **supporting** **Device** **Types**


**7.3.6.1** **Entry** **Control** **Keypad** **DT**


The Keypad Device Type is intended for keypads or authentication devices reporting user input to a
controlling application.


**7.3.6.1.1** **Generic** **and** **Specific** **Device** **Class**


DT:11.11.0001.1 The Entry Control Keypad Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_ENTRY_CONTROL (0x40)


     - SPECIFIC_TYPE_SECURE_KEYPAD (0x0B)


**7.3.6.1.2** **S2** **Security** **Classes**


DT:11.11.0002.1 The Root Device MUST request Access Control Security Class if it (or any End Point) uses this
Device Type.


**7.3.6.1.3** **Mandatory** **Command** **Classes**


DT:11.11.0003.1 The Entry Control Keypad MUST support the following Command Classes:


     - Entry Control


     - Security 0 (S0)


Recommended optional command classes:


     - Indicator, version 3 (with other Indicator IDs than Identify)


**7.3.6.1.4** **Basic** **Command** **Class** **Requirements**


DT:11.11.0004.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1194




<!-- PAGE 1196 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.6.2** **Multilevel** **Sensor** **DT**


The Multilevel Sensor Device Type is intended for sensor reporting instantaneous numerical readings

or measurements.


**7.3.6.2.1** **Generic** **and** **Specific** **Device** **Class**


DT:12.11.0001.1 The Multilevel Sensor Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_SENSOR_MULTILEVEL (0x21)


     - SPECIFIC_TYPE_ROUTING_MULTILEVEL_SENSOR (0x01)


**7.3.6.2.2** **Mandatory** **Command** **Classes**


DT:12.11.0002.1 The Multilevel Sensor MUST support the following Command Classes:


     - Sensor Multilevel, version 11


DT:12.12.0001.1 If the node issues more than one command regularly, it is RECOMMENDED to control:


     - Multi Command


**7.3.6.2.3** **Basic** **Command** **Class** **Requirements**


DT:12.11.0003.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1195




<!-- PAGE 1197 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.6.3** **Notification** **Sensor** **DT**


The Notification Sensor Device Type is intended for sensors reporting events or local state changes.


**7.3.6.3.1** **Generic** **and** **Specific** **Device** **Class**


DT:13.11.0001.1 The Notification Sensor Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_SENSOR_NOTIFICATION (0x07)


     - SPECIFIC_TYPE_NOTIFICATION_SENSOR (0x01)


**7.3.6.3.2** **Mandatory** **Command** **Classes**


DT:13.11.0002.1 The Notification Sensor MUST support the following Command Classes:

     - Notification, version 8


DT:13.12.0001.1 If the node issues more than one command regularly, it is RECOMMENDED to control:


     - Multi Command


**7.3.6.3.3** **Basic** **Command** **Class** **Requirements**


DT:13.11.0003.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1196




<!-- PAGE 1198 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.6.4** **Meter** **Sensor** **DT**


The Meter Sensor Device Type is intended for sensors measuring cumulated values. The most typical application is an electricity meter, but it can also be used for sensor measuring gas or water
consumption.


**7.3.6.4.1** **Generic** **and** **Specific** **Device** **Class**


DT:14.11.0001.1 The Meter Sensor Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_METER (0x31)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.6.4.2** **Mandatory** **Command** **Classes**


DT:14.11.0002.1 The Meter Sensor MUST support the following Command Classes:


     - Meter, version 5


DT:14.12.0001.1 If the node issues more than one command regularly, it is RECOMMENDED to control:


     - Multi Command


DT:14.12.0002.1 For advanced metering applications, it is RECOMMENDED to support the following command
classes:


     - Meter Table Monitor, version 2

     - Meter Table Push Configuration


     - Rate Table Monitor


**7.3.6.4.3** **Basic** **Command** **Class** **Requirements**


DT:14.11.0003.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1197




<!-- PAGE 1199 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.6.5** **Central** **Scene** **DT**


The Central Scene Device Type is intended for nodes with buttons or GUI allowing to report user
input/button press to a central application, which in turn will actuate or control other nodes.


This Device Type can be used for nodes such as wall switches or panels with a set of buttons. Such
devices will send Scene Notifications to the Lifeline destination in order to trigger scenes.


**7.3.6.5.1** **Generic** **and** **Specific** **Device** **Class**


DT:15.11.0001.1 The Central Scene Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_WALL_CONTROLLER (0x18)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.6.5.2** **Mandatory** **Command** **Classes**


DT:15.11.0002.1 The Central Scene MUST support the following Command Classes:


     - Central Scene, version 3


**7.3.6.5.3** **Basic** **Command** **Class** **Requirements**


DT:15.11.0003.1 Basic Command Class MUST NOT be supported


**7.3.6.5.4** **Recommended** **options**


DT:15.12.0001.1 The Central Scene Device Type SHOULD implement controlling capabilities using Association
Groups. It is RECOMMENDED to have a group issuing Basic Set Commands.


DT:15.12.0002.1 Multi Channel End Point SHOULD NOT implement this Device Type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1198




<!-- PAGE 1200 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.7** **Other** **Device** **Types**


**7.3.7.1** **Repeater** **DT**


The Repeater Device Type is intended for nodes being part of the network with no application
functionalities. Such nodes help as Z-Wave repeaters and strengthen the network reliability.


**7.3.7.1.1** **Role** **Type**


DT:21.11.0001.1 The Repeater Device Type MUST use the AOEN Role Type.


**7.3.7.1.2** **Generic** **and** **Specific** **Device** **Class**


DT:21.11.0002.1 The Repeater Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_REPEATER_END_NODE (0x0F)


     - SPECIFIC_TYPE_REPEATER_END_NODE (0x01)


**7.3.7.1.3** **Mandatory** **Command** **Classes**


DT:21.11.0003.2 The Repeater Device Type MUST NOT support any other Application Command Class than the
list defined in Section 7.2.2.1 _Root_ _Device_ _level_ . Additional Management Command Classes MAY be
supported.


DT:21.11.0004.1 The Repeater Device Type MUST NOT control any Command Class.


**7.3.7.1.4** **Basic** **Command** **Class** **Requirements**


DT:21.11.0005.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1199




<!-- PAGE 1201 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.7.2** **IR** **Repeater** **DT**


The IR Repeater Device Type is intended for nodes having the ability to read or repeat IR signals.
They do not have any other application functionality. Such repeater nodes also help as Z-Wave
repeaters and strengthen the network reliability.


**7.3.7.2.1** **Role** **Type**


DT:22.11.0001.1 The IR Repeater Device Type MUST use the AOEN Role Type.


**7.3.7.2.2** **Generic** **and** **Specific** **Device** **Class**


DT:22.11.0002.1 The Repeater Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_REPEATER_END_NODE (0x0F)


     - SPECIFIC_TYPE_IR_REPEATER (0x03)


**7.3.7.2.3** **Mandatory** **Command** **Classes**


DT:22.11.0003.1 The IR Repeater MUST support the following Command Classes:


     - IR Repeater, version 1


DT:22.11.0004.1 The IR Repeater Device Type MUST NOT support any additional Command Class (other than the
mandatory list above and the list defined in Section 7.2.2.1 _Root_ _Device_ _level_ .


DT:22.11.0005.1 The IR Repeater Device Type MUST NOT control any Command Class.


**7.3.7.2.4** **Basic** **Command** **Class** **Requirements**


DT:22.11.0006.1 Basic Command Class MUST NOT be supported


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1200




<!-- PAGE 1202 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.8** **Controlling** **Device** **Types**


**7.3.8.1** **Gateway** **DT**


The Gateway Device Type is intended for all gateway controllers that provide access in and potentially
DT:31.13.0002.1 out of the Z-Wave network as well as extensive controlling capabilities over Z-Wave. This DT MAY
provide transparent access for all types of IP Packets between several network technologies.


**7.3.8.1.1** **Role** **Type**


DT:31.11.0001.1 The Gateway Device Type MUST use the CSC Role Type.


**7.3.8.1.2** **Generic** **and** **Specific** **Device** **Class**


DT:31.11.0002.1 The Gateway Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_STATIC_CONTROLLER (0x02)


     - SPECIFIC_TYPE_GATEWAY (0x07)


**7.3.8.1.3** **S2** **Security** **Classes**


DT:31.11.0003.1 If bootstrapped in another network, it MUST request all S2 Security Classes. (S2 Access Control, S2
Authenticated and S2 Unauthenticated)


**7.3.8.1.4** **Mandatory** **Command** **Classes**


DT:31.11.0004.1 The Gateway MUST support the following Command Classes in a Z-Wave network:


     - CRC-16 Encapsulation


     - Inclusion Controller


     - Multi Command


     - Security 0 (S0)


     - Time


DT:31.11.0005.2 The Gateway SHOULD support Node Provisioning Command Class in a Z-Wave network.


DT:31.11.0005.2 The Gateway MUST support the following Command Classes in an IP network:


     - Z/IP, version 4


DT:31.12.0001.1 If the Z/IP Gateway relies on a Z/IP client to provide application functionalities, it SHOULD support
the following Command Classes in an IP network:


     - Z/IP Gateway


     - Z/IP ND


     - Z/IP Portal


     - Mailbox


     - Network Management Proxy, version 2


     - Network Management Inclusion, version 3


     - Network Management Basic, version 2


DT:31.11.0006.3 The Gateway MUST provide full control of the following Command Classes:


     - Association, version 2


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1201




<!-- PAGE 1203 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


     - Association Group Information, version 3


     - Basic, version 2


     - Central Scene, version 3


     - CRC-16 Encapsulation


     - Firmware Update Meta Data, version 5


     - Indicator, version 3


     - Meter, version 5


     - Multi Channel, version 4


     - Multi Channel Association, version 3


     - Multilevel Sensor, version 11

     - Notification, version 8


     - Security 0 (S0)


     - Security 2 (S2)


     - Version, version 2


     - Wake up, version 2


DT:31.13.0001.1 A Gateway Device Type MAY provide a subset of its capabilities (supported and controlled command
classes) if it has the Secondary Controller Role in a network.


DT:31.11.0008.1 A Gateway Device Type MUST provide full control of any Command Class that it controls. It MUST
NOT provide partial control for any Command Class.


**7.3.8.1.5** **Recommended** **options**


DT:31.12.0002.1 A Gateway Device Type SHOULD support reading and interpreting data form legacy sensors supporting the following Command Classes:


     - Alarm Sensor


     - Binary Sensor

     - Alarm/Notification, version 1.


     - Multilevel Sensor


     - Meter


DT:31.12.0003.1 In order to achieve this, it is RECOMMENDED to implement a database of known devices.


DT:31.12.0004.2 A Gateway controller SHOULD control the Command Classes from all actuator Device Types (Table
7.6).


**7.3.8.1.6** **Basic** **Command** **Considerations**


DT:31.11.0007.1 Basic Command Class MUST NOT be supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1202




<!-- PAGE 1204 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**7.3.8.2** **Generic** **Controller** **DT**


The Generic Controller Device Type is intended for all more constrained or simple controllers allowing
users to make basic use of the Z-Wave network and controlling a pre-defined set of actuator nodes as
well as unknown actuator nodes.


**7.3.8.2.1** **Generic** **and** **Specific** **Device** **Class**


DT:32.11.0001.1 The Generic Controller Device Type MUST use the following Device Classes:


     - GENERIC_TYPE_GENERIC_CONTROLLER (0x01)


     - SPECIFIC_TYPE_NOT_USED (0x00)


**7.3.8.2.2** **Mandatory** **Command** **Classes**


DT:32.11.0002.1 The Generic Controller MUST support the following Command Classes:


     - Multi Command


DT:32.11.0003.3 The Generic Controller MUST provide full control of the following Command Classes:


     - Basic


     - Indicator, version 3


     - The mandatory actuator Command Classes of at least one actuator Device Type


     - Version, version 2


     - Wake up, version 2


DT:32.13.0001.1 A Generic Controller Device Type MAY provide full control or partial control of any other Command
Class not listed above.


**7.3.8.2.3** **Recommended** **options**


DT:32.12.0001.2 A Generic Controller SHOULD control Command Classes from as many actuator Device Types as
possible.


**7.3.8.2.4** **Basic** **Command** **Considerations**


DT:32.11.0004.1 Basic Command Class MUST NOT be supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1203




<!-- PAGE 1205 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **8 Role Type Specification** **8.1 Introduction**


**8.1.1** **Purpose**


This document describes the Z-Wave Plus Role Types. The purpose of the Role Type is to provide a
high level definition of how Z-Wave nodes must react from a Z-Wave networking perspective.


This document is not meant to be read in full. It is aimed at being a scalable documentation process for
network specific functionality for various Z-Wave devices. It should be read together with the Device
Type specification [34], which highlights what Role Types should be used for different Device Types.
A device will typically have one Role Type associated with it, but in some cases there can be more
than one. The developer now only needs to look at one Role Type to determine the implementation
of the network specific functionality to pass certification.


It is however necessary to understand how the Central Static Controller (CSC) works as most devices
will heavily depend on it for direct communication.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1204




<!-- PAGE 1206 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **8.2 Z-Wave Compliance Overview**


The following sections present Z-Wave properties applying to all Z-Wave Plus Role Types defined
RT:00.11.0001.1 in this document. Requirements presented in this chapter MUST be respected by all Z-Wave Plus
devices


**8.2.1** **SIS** **Assignment**


**8.2.1.1** **Non-SIS** **capable** **Primary** **Controllers**


A Z-Wave network may have no SIS capable controller. For instance this is the case if the network
consists of a Portable Controller (PC) which is used to include a number of Always On End Nodes
(AOEN). In this case, the PC acts as the Primary Controller.


RT:00.11.0006.2 If no SIS is present in the network, when including a controller supporting SIS functionality, a non-SIS
capable Primary Controller MUST assign the SIS role to the newly included controller.


**8.2.1.2** **SIS** **capable** **controllers**


RT:00.11.0007.2 All controllers that support the SIS functionality MUST accept to become SIS upon request from a
Primary Controller.


RT:00.11.0008.2 A controller that supports SIS functionality MUST assume the SIS role when creating a new network.


**8.2.1.3** **SIS** **return** **route** **assignment**


RT:00.11.0009.1 When the SIS is present, an including node MUST always assign SIS return route when including an
end node.


**8.2.2** **Network** **Inclusion** **and** **Exclusion**


**Learn** **Mode**


RT:00.11.000A.1 A Z-Wave Plus compliant node MUST support both direct-range and Network Wide Inclusion (NWI).


_Inclusion_ _Process_ outlines the inclusion process.


**Add** **Mode**


Add mode is used by a controller for including a new node to a network.


RT:00.11.003E.2 The SIS MUST show the new added nodes in the list of included nodes after an inclusion has been

carried out by an Inclusion Controller.


**8.2.3** **Security** **bootstrapping**


**8.2.3.1** **Security** **0** **Command** **Class**


RT:00.21.0001.1 Controllers MUST be able to perform Security 0 bootstrapping if they support the Security 0 Command Class. Refer to [34].


If a controller has the Inclusion Controller role in a network and includes a node that supports Security

RT:00.21.0002.1
0 Command Class only (i.e. does not support Security 2 Command Class), it MUST perform Security
0 bootstrapping immediately after including the node.


RT:00.21.0003.1


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1205




<!-- PAGE 1207 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the SIS and the Inclusion Controller both support the Inclusion Controller Command Class, the
inclusion controller MUST NOT perform S0 bootstrapping unless instructed by the SIS with an
Inclusion Controller Initiate Command (S0_INCLUSION).


If the SIS and the Inclusion Controller both support the Inclusion Controller Command Class, the SIS
RT:00.21.0005.1 MUST NOT perform S0 bootstrapping. The SIS should instruct the Inclusion Controller to perform
S0 bootstrapping or interview the included node non-securely.



RT:00.21.0004.1



If an error happens during S0 bootstrapping of an S0 capable controller, the included controller MAY
refuse to provide network functions (others than Learn Mode). In this case, the included controller
MUST indicate to the user that it needs to be excluded and re-included in the Z-Wave network.


**8.2.3.1.1** **Upgrading** **non-secure** **networks**



RT:00.23.0001.1 If a controller is included in a non-secure network as an inclusion controller, it MAY start using its
own S0 network key and perform S0 bootstrapping with newly included nodes.


A controller MUST NOT start using its own S0 network key if S0/S2 bootstrapping failed.


**8.2.3.2** **Security** **2** **Command** **Class**


The following sections describe requirements for controllers supporting the Security 2 Command Class


**8.2.3.2.1** **Bootstrapping** **capabilities**


Security 2 mandates certain functionalities depending on the controller’s role in the network.


If a controller has the SIS role:


RT:00.21.0006.1 - It MUST support the SIS side of the Inclusion Controller Command Class


RT:00.21.0007.1 - It MUST perform Security 2 bootstrapping.


RT:00.21.0008.1 - It MUST support inclusion of nodes that implement any combination of Security 2 Security
Classes


RT:00.21.0009.1 - It MUST have input and display method for support of all Security Classes.


RT:00.21.0006.1 - It MAY support inclusion using CSA


If a controller has the Inclusion Controller role:


RT:00.21.000A.1 - It MUST support the Inclusion Controller side of the Inclusion Controller Command Class


RT:00.21.000B.1 - It MUST NOT perform Security 2 bootstrapping


If a controller has the Primary Controller role:


RT:00.21.0003.1 - It MAY perform Security 2 bootstrapping


**8.2.3.2.2** **Granting** **Security** **Classes**


RT:00.21.000C.1 A controller with a user interface for PIN code input (and optionally a QR scanning capability) MUST
comply with following when bootstrapping S2 nodes:


     - It MUST grant membership of all requested Classes if the joining node requests membership of
the S2 Access Control Class (unless specified otherwise by a user).

     - It MAY ask the user for confirmation before granting S2 Authenticated Class key if the node
does not request membership of the S2 Access Control Class.


     - It SHOULD provide a way to inspect and adjust the list of the Security Class memberships that
will be granted to the joining node


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1206




<!-- PAGE 1208 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A constrained controller with no QR scanning capability and no user interface for PIN code input
RT:00.21.000D.1 MUST comply with following when bootstrapping S2 nodes:


     - It MUST grant membership of the S2 Unauthenticated Class if the joining node requests membership of the S2 Unauthenticated Class.


     It MUST abort the S2 bootstrapping entirely (grant no key) if the joining node does not request
membership of the S2 Unauthenticated Class.


**8.2.3.2.3** **Informing** **the** **user** **about** **security**



RT:00.21.000E.1


RT:00.22.0001.1



If a node has been security bootstrapped with the S0 Command Class in a S2 capable network, the
SIS/Primary controller MUST issue a warning message to the user informing that the node has not
been included securely. The SIS/Primary controller SHOULD request a new NIF to the included node
after security bootstrapping to verify if the included node supports S2 before issuing the message to
the user.


This is made to ensure that the end user is aware of which security level a node has been bootstrapped
and therefore identify if a S0 downgrade attack took place during bootstrapping or if a non-S2 inclusion
controller bootstrapped the joining node.



If an S2 node has not been granted the highest requested S2 key during bootstrapping, the SIS/Primary
RT:00.21.000F.1 controller MUST issue a warning message to the user informing that the node has not been included
with the highest security. This is OPTIONAL if the user has actively chosen which keys to grant and
security bootstrapping completed successfully.


In an Inclusion Controller scenario, the SIS’ UI may not be active during S2 bootstrapping. In this
case, the following rules apply:



RT:00.23.0005.1




- If the SIS automatically grants unauthenticated key for a node that request the S2 Unauthenticated Class, it MAY notify the end user the next time it uses the UI.



RT:00.22.0002.1 - If the SIS timed out during S2 bootstrapping, it SHOULD instruct the end user that the node
needs to be excluded and re-included.


**8.2.4** **Device** **Reset** **Locally** **support**


RT:00.11.000B.1 If a device can be reset to factory default locally on the device, the device MUST be able to issue a
Device Reset Locally Command via its Lifeline to notify the Lifeline destination that the device has
been reset to its factory default state. The product documentation MUST include instructions on
how to perform a reset to factory default operation.


RT:00.11.000C.1 If a device cannot be locally (or manually) reset to factory default, the device MUST NOT implement
the Device Reset Locally functionality and MUST NOT list the Device Reset Locally Command Class
identifier in the NIF.


RT:00.11.000D.1 If a device is reset, it MUST perform the reset operation regardless of whether the delivery of the
Device Reset Locally Notification is successful or not. It is RECOMMENDED that devices implement
a mechanism that allows the user to determine when the reset operation is completed.


When a node is reset:


RT:00.11.000E.1 - it MUST forget its current HomeID and consider itself excluded from the network.

RT:00.13.0001.1 - The configuration of _Application_ _Command_ _Classes_ MAY stay unchanged (e.g configuration
parameters, Thermostat Setpoint, Clock, Door lock Timeout configuration, User codes, …)



RT:00.11.000F.1




 - The configuration of other Command Classes (Section 3, Section 4 or Section 5) MUST be reset
to default (i.e. S2 keys are forgotten, Associations and Wake-Up configurations are cleared, etc.)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1207




<!-- PAGE 1209 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.2.5** **Node** **interview** **and** **response** **timeouts**


During a node capability discovery or interview, as well as traffic generated due to user activation, a

RT:00.11.0010.1
controlling nodes MUST timeout waiting for responses (reports) as part of the capability discovery or
controlling scenarios.


Two timers named CommandTime and ReportTime are used for timing out during a node discovery
interview. Illustrations are given for secure and non-secure cases in Figure 8.1 and Figure 8.2


     - CommandTime is measured by the application


RT:00.12.0001.1 - ReportTime timeout SHOULD be set to CommandTime + 1 second.

The communication flow MUST be as shown in Figure 8.1 and Figure 8.2


Figure 8.1: Node Interview ReportTime timeout without security


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1208




<!-- PAGE 1210 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.2: Node Interview ReportTime timeout with security


**8.2.6** **Polling** **Devices**


A controlling device may monitor nodes or issue requests for status information.Communication patterns include, but are not limited to, the transmission of a:


     - No Operation (NOP) Command to verify that a node is operational


     - Get Command requesting status information in a Report Command


     - Set Command followed by a Get Command requesting status information in a Report Command


RT:00.11.0011.1 Communication MUST be considered polling if a controlling device autonomously sends requests to
one or more nodes in a repeating fashion to monitor nodes or to get information from nodes. This
applies to any combination of commands.


Z-Wave is a radio technology with limited bandwidth. Therefore, it is NOT RECOMMENDED to use
RT:00.11.0012.1 polling. If used, polling communication MUST comply with the requirements stated in the following
subsections _Polling with no errors_, _Polling with transmit error_ and _Polling with missing Report Frame_


RT:00.11.0013.1 Communication MUST NOT be considered as polling if:


     - A node issues one or more commands in a burst initiated by a user action. This applies to any
combination of commands; also requests.


     - A node issues one or more commands initiated by the inclusion of another node. This applies
to any combination of commands; also requests.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1209




<!-- PAGE 1211 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.2.6.1** **Polling** **with** **no** **errors**


Two timers named CommandTime and PollTime are used for polling requirements with no error.
Illustrations are given for secure and non-secure cases in Figure 8.3 and Figure 8.4


The following requirements apply to the normal case where a polling request is successful:


RT:00.11.0014.1 - CommandTime MUST be measured by the application


RT:00.11.0015.1 - The application MUST wait PollTime before polling any other node


RT:00.12.0002.1 - PollTime SHOULD be 10 seconds + CommandTime or more


RT:00.11.0016.1 - PollTime MUST NOT be less than 1 second + CommandTime


Figure 8.3: Polling (No errors, without security)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1210




<!-- PAGE 1212 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.4: Polling (No errors, with security)


**8.2.6.2** **Polling** **with** **transmit** **error**


Two timers named CommandTime and PollTime are used for polling requirements with transmission
error. Illustrations are given for secure and non-secure cases in Figure 8.5 and Figure 8.6.


RT:00.11.0017.1 Note that in the case of a missing Ack, the Sending node MUST transmit the Get Command 3 times
before considering the Ack to be missing. CommandTime is measured from the first Get Command
transmission to the timeout.


The following requirements apply to the case where a polling request is not successful.


RT:00.11.0018.1 - If the transmission fails, the application MUST wait PollTime before polling any other node.
PollTime MUST be 10 seconds + CommandTime or more


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1211




<!-- PAGE 1213 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.5: Polling (No Ack, without security)


Figure 8.6: Polling (no ack with Security 0)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1212




<!-- PAGE 1214 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.2.6.3** **Polling** **with** **missing** **Report** **Frame**


Two timers named CommandTime and ReportTime are used for polling requirements when transmission is successful but with missing report. Illustrations are given for secure and non-secure cases in
Figure 8.7 and Figure 8.8.


The following requirements apply to the case where a polling request is successful but no Report frame
is received.


RT:00.11.0019.1 - The application MUST wait ReportTime for the reply from node X before polling any other
node


RT:00.11.001A.1 - ReportTime MUST be CommandTime + 10 seconds or more


Figure 8.7: Polling (no Report frame, without security)


Figure 8.8: Polling (no Report frame, with security)


**8.2.7** **Unsolicited** **communication**


RT:00.13.0002.1 A device MAY autonomously send control commands or status information in response to physical
events or in response to a timer.


Unsolicited communication patterns include, but are not limited to, the transmission of a:


     - Control command turning on light in response to a detected movement


     - Power meter report sending a usage report

Different requirements apply to unsolicited data collection communication and unsolicited control
communication, respectively.


**8.2.7.1** **Unsolicited** **data** **collection** **communication**


Bursts of one or more commands which carry status information transmitted repeatedly without any
RT:00.11.001B.1 user intervention MUST be considered to be unsolicited data collection communication.


Using the transmission of a control command or a NOP command as a heartbeat indication MUST
also be considered unsolicited data collection communication.


RT:00.11.001C.1 To save bandwidth, data collection communication MUST comply with the following requirements.


     - A device MAY issue unsolicited data collection communication in any burst size


     - A device MUST NOT issue new unsolicited data collection communication less than 30 seconds

since the last burst.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1213




<!-- PAGE 1215 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.2.7.2** **Unsolicited** **control** **communication**


Bursts of one or more control commands initiated by a user action, a physical event or a time trigRT:00.11.001D.1 ger MUST be considered control communication. Control communication MUST comply with the
following requirements:


     - A device MAY issue unsolicited control communication in any burst size.


     - A device MAY issue unsolicited control communication at any interval since the last burst


**8.2.8** **Runtime** **communication**


**8.2.8.1** **Routing**


RT:00.11.001E.1 A Z-Wave Plus node MUST use by default the last working route to communicate with a target node.
An illustration is given in Figure 8.9


Figure 8.9: Successful transmission using last working routes


Over time, there is a risk that nodes are moved or stop working. To ensure that nodes adapt to
RT:0011.001F.1 changing network topology and failing repeaters, a Z-Wave Plus node MUST enable dynamic route
resolution. Dynamic route resolution consists of trying the following routes:


     - Last working routes


     - Calculated routes


     - Explorer Frame


Illustrations are given in Figure 8.10 and Figure 8.11.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1214




<!-- PAGE 1216 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.10: Successful transmission using Explorer Frame


RT:00.11.0020.1 A node MUST perform 3 routing attempts based on last working routes and/or calculated routes
before sending an Explorer Frame. As outlined in Figure 8.10, controllers may calculate routes using
the local neighbor map.


RT:00.13.0003.1 Listening Sleeping End Nodes (LSEN) and Reporting Sleeping End Nodes (RSEN) MAY use return
routes injected by a controller. The outlined sequence of transmission attempts is handled entirely by
the routing protocol.



RT:00.13.0004.1


RT:00.12.0003.1



In case the destination is not reachable, all routed transmission attempts will fail and ultimately, the
routing protocol will have to give up delivering the frame. After a failed transmission, the application
MAY try to transmit again in case a new event occurs, e.g. because the user issues a new button

press.


The steps in Figure 8.11 involve at least three routing attempts. When all routing attempts are
unsuccessful, it is very unlikely that any other transmission attempt to the same target will succeed.
The sending node SHOULD give up the frame transmission.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1215




<!-- PAGE 1217 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.11: Unsuccessful transmission


RT:00>13.0005.1 Nodes based on a controller role type MAY skip transmission attempts if they are associated to a
non-existing NodeID.


**8.2.8.2** **Wake-Up** **communication** **timeout** **protection**


A battery powered node supporting Wake-Up communication sends a Wake Up Notification Command
to get attention when it is awake and receives a Wake Up No More Information Command when it
can safely return to sleep.


RT:00.12.0004.1 A battery powered Z-Wave Plus node supporting Wake-Up communication SHOULD implement a
timeout mechanism which makes the node return to sleep if the node does not receive a Wake Up No
More Information Command.


If no Wake Up No More Information Command is received from the Wake Up destination, the node
RT:00.11.0021.2 MUST respond to the Wake Up destination until 10 seconds have elapsed since the last transmission
or reception of an application frame supported by the node, a NOP frame or a Request Node Info
Frame with the Wake Up destination.


An illustration is given in Figure 8.12.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1216




<!-- PAGE 1218 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 8.12: Wake Up Command Class


**8.2.9** **Network** **maintenance**


RT:00.12.0005.1 The network rediscovery (Request neighbor update) feature SHOULD only be used as last resort in
case the runtime communication fails.


**8.2.10** **SmartStart** **requirements**


**8.2.10.1** **Support** **requirements**


**8.2.10.1.1** **SmartStart** **learn** **mode** **activation**


RT:00.11.0023.1 A node supporting SmartStart inclusion MUST enter SmartStart Learn Mode by default when ready
after powering up, regardless of network inclusion status.


RT:00.11.0024.1 A node supporting SmartStart inclusion MUST fall back on SmartStart Learn Mode after deactivating
Learn Mode.


**8.2.10.1.2** **Higher** **Inclusion** **Request** **Interval**


If a very power-constrained battery node is designed to settle at a higher Max Inclusion Request
Interval ( _aNwkSmartStartMaxInclusionRequestInterval_ in [35]) than the default 512 seconds, this value
MUST be advertised in the node’s provisioning information (QR Code, refer to [34] and [28]).


RT:00.11.0025.1


**8.2.10.2** **Control** **requirements**


RT:00.11.002B.1 A controller providing control of the SmartStart functionality is NOT REQUIRED to support the
SmartStart functionality and support being included in a network using SmartStart inclusion.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1217




<!-- PAGE 1219 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.2.10.2.1** **Command** **Class** **support**


RT:00.11.002E.2 A Z/IP Gateway providing the SmartStart functionality MUST support the following Command
Classes on the IP side:


     - Network Management Inclusion Command Class, version 3 or newer


RT:00.12.0009.1 A Z/IP Gateway providing the SmartStart functionality SHOULD support the following Command
Classes on the IP side:


     - Node Provisioning Command Class


**8.2.10.2.2** **User** **interface**


RT:00.11.0032.3 A controller providing control of the SmartStart functionality MUST:


     - Provide a method for the end user to view the Node Provisioning List entries with their network
inclusion status (included/ not included or failed).


     - Provide a method for the end user to manually add and remove entries in the Node Provisioning
List.


     - Provide a method for the end user to edit available settings for each entry in the Node Provisioning List. (e.g., Inclusion setting, Advanced joining). A controller application MAY provide
no available settings.


     - Support S2 inclusion with authentication using the DSK PIN code.


If a user removes a node from the Node Provisioning List and the node is still included in the Z-Wave
RT:00.11.0033.1 network, the controller MUST inform the end user that the node will stay in the network and requires
to be excluded manually or reset to factory default in order to leave the Z-Wave Network.


RT:00.11.0034.1 A controller MUST inform the end user that S2 only (non-SmartStart) nodes present in the Provisioning List require to perform a classic inclusion to add them into the Z-Wave network.


**8.2.10.2.3** **QR** **Code** **scanning** **capability**


RT:00.12.0006.1 A controller providing the SmartStart functionality SHOULD provide a QR Code scanning capability.

If the controller offers a QR Code scanning capability:

RT:00.11.0035.1 - It MUST support the addition of nodes using QR Code format defined in [29] in its Provisioning
List when scanning the QR Code.

RT:00.12.0007.1 - It SHOULD support scanning of S2 only QR codes representing the DSK String prefixed with
“zws2dsk:”. (example: “zws2dsk:34028-23669-20938-46346-33746-07431-56821-14553”) in order
to simplify the S2 bootstrapping process.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1218




<!-- PAGE 1220 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **8.3 Role Type Overview**


Z-Wave Role Types is used as part of the Z-Wave Plus certification program. Role types define how
battery and network functionalities must be implemented.


This is to provide better uniformity and hence ensuring better interoperability between Z-Wave Plus
devices.

Role types are backwards compatible with Z-Wave products certified under earlier certification programs. The Role Types are device specific and hence the Device Type will define which Role Type(s)
a given device can support.


Table 8.1 shows an overview of Role Types which are described in details in Chapter 5.



Table 8.1: Role Type Overview






















|Role Type|Ab<br>-<br>bre-<br>via-<br>tion|Re-<br>peat|Power<br>ersource|Can<br>be<br>SIS|Net<br>-<br>work<br>Setup|Life-<br>line<br>Setup|Report<br>Through<br>Lifeline|Direct<br>con-<br>trol<br>-<br>lable|Heart<br>beat com-<br>munca-<br>tion|
|---|---|---|---|---|---|---|---|---|---|
|**Central**<br>**Static**<br>**Controller**|CSC||Mains|||||||
|**Sub Static**<br>**Controller**|SSC||Mains|||||||
|**Portable**<br>**Controller**|PC||Bat-<br>tery|||||||
|**Reporting**<br>**Portable**<br>**Controller**|RPC||Bat-<br>tery|||||||
|**Portable**<br>**End Node**|PEN||Bat-<br>tery|||||||
|**Always On**<br>**End Node**|AOEN||Mains|||||||
|**Listening**<br>**Sleeping**<br>**End Node**|LSEN||Bat-<br>tery|||||||
|**Reporting**<br>**Sleeping**<br>**End Node**|RSEN||Bat-<br>tery|||||||
|**Network**<br>**Aware End**<br>**Node**|NAEN||Mains|||||||



The following functionalities depend on the actual Role Type:


**Repeater** : Indicates whether the device can act as repeater in the network. This requires an always
listening device, which can accommodate any routing requests immediately.


**Power** **source** : Mains powered devices are accessible immediately and are always listening devices.
Battery powered devices focus on battery lifetime extension as one of the primary objectives.


**Can** **be** **SIS** : The node supports the Static Update Controller (SUC) and SUC node ID Server
(SIS) functions. When SIS functionality is enabled, the controller also takes the Primary Controller
role. All other controllers operate as Inclusion Controllers, i.e. they can request that nodes are
included/excluded. If a SIS is present in the network, it is RECOMMENDED that all other devices
update their network topology once a day and before configuring associations.


**Network** **setup** : The node is capable of managing the network and inclusion/exclusion of nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1219




<!-- PAGE 1221 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Setup** **lifeline** : The node is able to configure lifeline associations.


**Report** **through** **lifeline** : The node MUST be able to report events via a lifeline association to a
central home control application.

**Direct** **controllable** : Mains powered devices and battery devices configured as Frequently Listening
(FL) nodes can be controlled at any time.


**Heart** **beat** **communication** : Operating as a sleeping device, the node is able to connect at given
intervals to a central home control application to allow delivery of messages from other devices. Such
a node supports the Wake Up Command Class.


**8.3.1** **Detecting** **the** **Role** **Type** **of** **a** **device**


The Role Type of a node can be requested via the Z-Wave Plus Info Command Class, which MUST
RT:00.11.0036.1 be listed as the first supported Command Class in the Node Information Frame (NIF) by all Z-Wave
Plus nodes. For details about Z-Wave Plus Info Command Class, refer to Section 3.






|Role Type|Value|Table 8.2: Role Type identifiers Identifier|
|---|---|---|
|**Role Type**|**Value**|**Identifer**|
|Central<br>Static<br>Controller (CSC)|0x00|_ROLE_TYPE_CONTROLLER_CENTRAL_STATIC_|
|Sub Static Con-<br>troller (SSC)|0x01|_ROLE_TYPE_CONTROLLER_SUB_STATIC_|
|Portable<br>Con-<br>troller (PC)|0x02|_ROLE_TYPE_CONTROLLER_PORTABLE_|
|Reporting<br>Portable<br>Con-<br>troller (RPC)|0x03|_ROLE_TYPE_CONTROLLER_PORTABLE_REPORTING_|
|Portable<br>End<br>Node (PEN)|0x04|_ROLE_TYPE_END_NODE_PORTABLE_|
|Always On End<br>Node (AOEN)|0x05|_ROLE_TYPE_END_NODE_ALWAYS_ON_|
|Reporting Sleep-<br>ing<br>End<br>Node<br>(RSEN)|0x06|_ROLE_TYPE_END_NODE_SLEEPING_REPORTING_|
|Listening<br>Sleep-<br>ing<br>End<br>Node<br>(LSEN)|0x07|_ROLE_TYPE_END_NODE_SLEEPING_LISTENING_|
|Network<br>Aware<br>End<br>Node<br>(NAEN)|0x08|_ROLE_TYPE_END_NODE_NETWORK_AWARE_|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1220




<!-- PAGE 1222 -->

RT:00.11.0037.1



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **8.4 Role Type Definitions**


The following sections describe requirements for individual Role Types. Each Role Type has requirements categorized in the following subsections:


1. Protocol Requirements


2. Setup

3. Runtime Configuration


4. Runtime Communication

The Setup subsection describes the specific requirements for a given Role Type during and after a
network inclusion. Figure 8.13 shows the different steps of a node setup / commissioning.


Figure 8.13: Node Setup/Commissioning


**Network** **inclusion**


The network inclusion process is described in _Inclusion_ _Process_ . Additional recommendations are
given for the different Role Types.


**(S0/S2)** **Security** **bootstrapping**


The security (Security 0 or Security 2) bootstrapping takes place immediately after the network
inclusion. Refer to Section 4.


**Discover** **supported** **Command** **Classes**


The controlling node reads the supported command classes before interviewing each of them.


**Command** **Class** **interview**

Each role type specifies some requirements that must be observed during the Command Class interview:

 - **Lifeline** **configuration:** :


When interviewing the Association or Multi Channel Association Command Class, the including
controller sets up the lifeline association if it is the SIS. If a SIS is present in the network, the
destination NodeID of the Lifeline group MUST be the SIS NodeID. Requirements are detailed
for each Role Type in the following sections. Refer to [34] and Section 7 for Lifeline group
definition


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1221




<!-- PAGE 1223 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


     - **Battery** **considerations:**


Some requirements apply for battery powered nodes, supporting the Wake Up Command Class.
Details are given for each Role Type.


**Commissioning** **and** **runtime** **phases**

The commissioning phase is defined as the period after a node’s inclusion during which the Security
bootstrapping, Lifeline configuration, Wake Up configuration and initial device interview is made by
a controller.


RT:00.12.0008.1 It is RECOMMENDED that a controller does not display a newly included node as ready to be
operated during the commissioning phase.


The commissioning phase is considered over when the initial interview is completed or latest 10 minutes
after the network inclusion.


Once the commissioning phase is over, a node is said to be in the runtime phase.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1222




<!-- PAGE 1224 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.1** **Central** **Static** **Controller** **(CSC)**


The Central Static Controller Role Type is intended for always powered devices which are capable of
operating as a central controller. The CSC will be the central device for most network communications
and other devices will rely on it for unsolicited information via the lifeline association to the CSC
(which is also the SIS). This will enable the user to receive key information without having to perform
major network configuration tasks.


The CSC is typically a router, central gateway or some sort of central communication panel.


**8.4.1.1** **CSC** **Protocol** **Requirements**


RT:01.11.0001.1 The CSC MUST respect requirements described in Section 8.2.


RT:01.11.0002.1 The CSC MUST support the Static Update Controller (SUC) and SUC node ID Server (SIS) functions.


RT:01.11.0003.1 The CSC MUST be mains powered and MAY have a battery back-up.

RT:01.11.0004.1 The CSC MUST set the listening flag to 1 in its NIF.


RT:01.11.0005.1 The CSC MUST support and control the S0 and S2 Command Classes.


RT:01.11.0006.2 The CSC MUST support the following network roles:


     - SIS


     - Secondary controller (if Learn Mode is supported)


     - Inclusion controller (if Learn Mode is supported)


**8.4.1.1.1** **If** **first** **node** **in** **the** **network**


RT:01.11.0007.3 If the CSC is the first node in the network, it MUST set itself the SIS role and MUST support the
following network functions:


     - Include new nodes (“Add mode”)


     - Exclude nodes


     - Remove failing nodes


RT:01.13.0001.2 Additionally, it MAY support the following network function:


     - Replace failing nodes


     - Learn Mode


RT:01.11.0008.1 It MUST NOT be possible to activate Learn Mode if the CSC is the SIS and other nodes are included
in the network.


**8.4.1.2** **CSC** **setup**


**8.4.1.2.1** **Inclusion** **process**


RT:01.12.0001.1 It is RECOMMENDED to use soft buttons for activating learn mode and add mode on a CSC Role
Type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1223




<!-- PAGE 1225 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.1.2.2** **Lifeline** **configuration**


When including a node,


RT:01.11.0009.1 - if the CSC is the SIS: it MUST set itself as the Association group ID 1 (Lifeline) destination.


RT:01.13.0003.1 - if the CSC is not the SIS: it MAY set the SIS’ NodeID as the Association group ID 1 (Lifeline)
destination.


RT:01.11.0016.1 The CSC MUST assign a return route for the SIS after setting the lifeline of End Node Role Types.


Details and requirements about establishing the Lifeline are provided in _Association Group Information_
_(AGI)_ _Command_ _Class,_ _version_ _1-3_ and _Multi_ _Channel_ _Association_ _Command_ _Class,_ _version_ _2-5_ .


**8.4.1.2.3** **CSC** **including** **a** **SSC,** **PC,** **RPC** **or** **NAEN**


**Battery** **considerations**


If the CSC is the SIS and the included node is of Role Type RPC:

RT:01.11.000A.1 - The CSC MUST configure the Wake Up Interval Set Command destination NodeID to its
NodeID.


RT:01.11.000B.1 - The CSC MUST send a Wake Up No More Information Command when the CSC has no more
command to transmit.


**8.4.1.2.4** **CSC** **including** **a** **EN,** **LSEN** **or** **RSEN**


**Battery** **considerations**


RT:01.11.000D.1 If the CSC is the SIS and the included node is of Role Type PEN or RSEN, the CSC MUST:

     - configure the Wake Up Interval Set Command destination NodeID to its NodeID.


     - send a Wake Up No More Information Command when the CSC has no more command to

transmit.


If the CSC is the SIS and the included node is of Role Type PEN:



RT:01.11.000E.1




- If the node advertises Wake-Up Capabilities (Wake-Up Command Class, version 2 or newer),
the Wake Up Interval Set Command Seconds field MUST be within the allowed range



RT:01.12.0002.1 If the CSC is not the SIS, it SHOULD NOT send a Wake Up Interval Set Command to the included
node.


RT:01.11.0010.1 If the CSC is not the SIS and sends a Wake Up Interval Set Command, the destination NodeID MUST
be the SIS’ NodeID.


**8.4.1.2.5** **CSC** **including** **an** **AOEN**


**Battery** **considerations**


None.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1224




<!-- PAGE 1226 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.1.2.6** **CSC** **including** **another** **CSC**


RT:01.11.0013.1 If the CSC is included by another CSC, the included CSC MUST take the Inclusion Controller role
and MUST support the following network functions:


     - Include new nodes (“Add mode”)


     - Exclude nodes


     - Learn mode


     - Remove failing node


RT:01.13.0002.1 Additionally, it MAY support the following network function:


     - Replace failing node


**Battery** **considerations**


None.


**8.4.1.2.7** **CSC** **included** **by** **a** **PC,** **RPC,** **SSC**


RT:01.11.0014.1 The CSC MUST accept to take the SIS role when a PC, RPC or SSC assigns it to the included CSC.

**Lifeline** **configuration**


If the CSC was assigned the SIS role, previously added nodes may have no lifeline associations. The
RT:01.12.0003.1 CSC SHOULD create lifeline associations in all existing nodes that are directly reachable.


**Battery** **considerations**


None.


**8.4.1.3** **CSC** **Runtime** **Configuration**


RT:01.11.0015.1 The CSC MUST instruct a reporting node (RPC, RSEN, PEN) to return to sleep after application
data has been delivered to the node. This is done by sending a Wake Up No More Information
Command. An illustration is given in Figure 8.12.


**8.4.1.4** **CSC** **Runtime** **Communication**


No requirements


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1225




<!-- PAGE 1227 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.2** **Sub** **Static** **Controller** **(SSC)**


The Sub Static Controller Role Type is intended for static controllers which are not suitable as central
controllers. It is aimed at applications that require a static controller to manage a subset of nodes. It
is typically offered as a bundled package with e.g. sensors.


**8.4.2.1** **SSC** **Protocol** **Requirements**


RT:02.11.0001.1 The SSC MUST respect requirements described in Section 8.2


RT:02.11.0002.1 The SSC MUST be mains powered and MAY have battery back-up.

RT:02.11.0003.1 The SSC MUST set the listening flag to 1 in its NIF.


RT:02.11.0004.1 The SSC MUST NOT support the SIS functionality.

RT:02.12.0001.1 The SSC SHOULD NOT configure lifeline associations.


RT:02.11.0005.1 The SSC MUST support the following network roles:


     - Primary controller


     - Secondary controller


     - Inclusion controller


**8.4.2.1.1** **If** **first** **node** **in** **the** **network**


RT:02.11.0006.1 If the SSC is the first node in the network, it MUST take the Primary Controller role and MUST
support the following network functions:


     - Include new nodes (“Add mode”)


     - Exclude nodes


     - Learn mode


RT:02.11.0007.1 It MUST NOT be possible to activate Learn Mode if the SSC is the Primary Controller and other
nodes are included in the network.


**8.4.2.2** **SSC** **Setup**


**8.4.2.2.1** **Inclusion** **process**


RT:02.12.0002.1 It is RECOMMENDED to use a physical push button for activating learn mode and a soft button for
activating add mode on a SSC Role Type.


**8.4.2.2.2** **Lifeline** **configuration**


No requirement


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1226




<!-- PAGE 1228 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.2.2.3** **SSC** **including** **a** **CSC**


RT:02.11.0008.1 If the SSC is the Primary Controller and a CSC is added to the network, the SSC MUST assign the
SIS role to the CSC.


RT:02.13.0001.1 If the SSC is the Primary Controller and has previously included some Wake Up nodes, it MAY
re-assign the Wake Up destination NodeID to the CSC/SIS for the previously included Wake Up
nodes at the next Wake Up Notification.


RT:02.11.0009.1 The SSC becomes an inclusion controller and MUST support the following network functions:


     - Include new modes (“Add mode”)


     - Exclude nodes


     - Learn mode


**Battery** **considerations**


None.


**8.4.2.2.4** **SSC** **including** **an** **RPC,** **PEN** **or** **RSEN**



RT:02.12.0003.1


RT:02.11.000A.1



If there is a SIS in the network, the SSC SHOULD NOT send a Wake Up Interval Set Command to
the included node. If there is a SIS in a network and the SSC sends a Wake Up Interval Set Command,
the destination NodeID MUST be the SIS’ NodeID.



RT:02.12.0004.1 If there is no SIS present in the network, the SSC SHOULD send a Wake Up Interval Set Command

RT:02.11.000B.1 with its own NodeID as destination. If issuing a Wake Up Interval Set Command, the SSC MUST
respect the following rules:


     - If the included node is of Role Type RPC, PEN or RSEN:



RT:02.12.0005.1


RT:02.11.000C.1



**–** The SSC SHOULD set the Wake Up Interval Set Command Seconds field to the default
Wake Up time advertised by the included node.


 - If the included node is of Role Type PEN:


**–** If the node advertises Wake-Up Capabilities (Wake-Up Command Class, version 2 or
newer), the Wake Up Interval Set Command Seconds field MUST be within the allowed

range.


**8.4.2.2.5** **SSC** **including** **an** **SSC,** **PC,** **AOEN,** **LSEN,** **or** **NAEN**


**Battery** **considerations**


None.


**8.4.2.3** **SSC** **Runtime** **Configuration**


No requirements.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1227




<!-- PAGE 1229 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.2.4** **SSC** **Runtime** **communication**


No requirements.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1228




<!-- PAGE 1230 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.3** **Portable** **Controller** **(PC)**


The Portable Controller Role Type is intended for portable controllers that can setup and maintain a
Z-Wave network but do not require unsolicited reporting. It is typically used by home control remotes
that control a few lights.


**8.4.3.1** **PC** **Protocol** **Requirements**


RT:03.11.000.1 The PC MUST respect requirements described in Section 8.2


RT:03.11.0002.1 The PC MUST be battery powered and support the Battery Command Class.

RT:03.11.003.1 The PC MUST set the listening flat to 0 in its NIF.

RT:03.12.0001.1 The PC SHOULD NOT configure lifeline associations when adding nodes to the network.


RT:03.11.0004.1 The PC MUST support the following network roles:


     - Primary controller


     - Secondary controller


     - Inclusion controller


**8.4.3.1.1** **If** **first** **node** **in** **the** **network**


RT:03.11.0005.1 If the PC is the first node in the network, it MUST take the Primary Controller role and MUST
support the following network functions:


     - Include new nodes (“Add mode”)


     - Exclude nodes


     - Learn mode


RT:03.11.0006.1 It MUST NOT be possible to activate Learn Mode if the PC is the Primary Controller and other
nodes are included in the network.


**8.4.3.2** **PC** **Setup**


**8.4.3.2.1** **Inclusion** **process**


RT:03.12.0002.1 It is RECOMMENDED to use physical push buttons for activating Learn Mode and Add Mode on a
PC Role Type.


**8.4.3.2.2** **Lifeline** **configuration**


No requirement.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1229




<!-- PAGE 1231 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.3.2.3** **PC** **including** **a** **CSC**


RT:03.11.0007.1 If the PC is the Primary Controller and a CSC is added to the network, the PC MUST assign the
SIS role to the CSC.


RT:03.11.0008.1 The PC becomes an inclusion controller and MUST support the following network functions:


     - Include new nodes (“Add mode”)


     - Exclude nodes


     - Learn mode


**Battery** **considerations**


None.


**8.4.3.2.4** **PC** **including** **an** **RPC,** **PEN,** **or** **RSEN**


**Battery** **considerations**


None.


**8.4.3.2.5** **PC** **including** **an** **SSC,** **PC,** **AOEN,** **LSEN** **or** **NAEN**


**Battery** **considerations**


None.


**8.4.3.3** **PC** **Runtime** **Configuration**


No requirements.


**8.4.3.4** **PC** **Runtime** **communication**


No requirements.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1230




<!-- PAGE 1232 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.4** **Reporting** **Portable** **Controller** **(RPC)**


The Reporting Portable Controller Role Type is intended for portable reporting controllers, which
need to setup a Z-Wave network and also send unsolicited messages.


The RPC Role Type may for instance be used for a battery powered thermostat which can include
and exclude nodes in a small network. In addition, the thermostat may be configured remotely.


**8.4.4.1** **RPC** **protocol** **requirements**


RT:04.11.0001.1 The RPC MUST respect requirements described in Section 8.2.


RT:04.11.0002.1 The RPC MUST be battery powered and support the following Command Classes: - Battery Command Class      - Wake Up Command Class, version 2 or newer

RT:04.11.0003.1 The RPC MUST set the listening flag to 0 in its NIF.

RT:04.12.0001.1 The RPC SHOULD NOT configure lifeline associations when adding nodes to the network.


RT:04.11.0004.1 The RPC MUST support the following network roles:


     - Primary controller


     - Secondary controller


     - Inclusion controller


**8.4.4.1.1** **If** **first** **node** **in** **the** **network**


RT:04.11.0005.1 If the RPC is the first node in the network, it MUST take the Primary Controller role and MUST
support the following network functions:       - Include new nodes (“Add mode”) * Exclude nodes * Learn
mode


RT:04.12.0006.1 It MUST NOT be possible to activate Learn Mode if the RPC is the Primary Controller and other
nodes are included in the network.


**8.4.4.2** **RPC** **Setup**


**8.4.4.2.1** **Inclusion** **process**


RT:04.12.0002.1 It is RECOMMENDED to use physical push buttons for activating learn mode and add mode on an
RPC Role Type.


**8.4.4.2.2** **Lifeline** **configuration**


RT:04.13.0001.1 When including a node, if a SIS is present in the network, the RPC MAY set the SIS’ NodeID as the
Association group ID 1 (Lifeline) destination.


Details and requirements about establishing the Lifeline are provided in the Association and Multi
Channel Association control specifications _Command_ _Class_ _Control_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1231




<!-- PAGE 1233 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.4.2.3** **RPC** **including** **a** **CSC**


RT:04.11.0007.1 If the RPC is the Primary Controller and a CSC is added to the network, the RPC MUST assign the
SIS role to the CSC.


RT:04.11.0008.1 The RPC becomes an inclusion controller and MUST support the following network functions: Include new nodes (“Add mode”)       - Exclude nodes       - Learn mode


**Battery** **considerations** None


**8.4.4.2.4** **RPC** **including** **an** **RPC,** **PEN** **or** **RSEN**


**Battery** **considerations** None


**8.4.4.2.5** **RPC** **including** **an** **SSC,** **PC,** **AOEN,** **LSEN** **or** **NAEN**


**Battery** **considerations** None


**8.4.4.3** **RPC** **runtime** **configuration**


RT:04.11.0009.1 The RPC MUST support the Wake Up Command Class as described in 0.


RT:04.12.0005.1 The RPC SHOULD have a physical push button for waking up the device for expedited communication. This enables interactive delivery of new configuration parameters or firmware updates.


RT:04.11.000A.1 The RPC MUST implement a Minimum Wake Up Interval in the range 0 ..4200 (i.e. between 0 second
and 70 minutes).


RT:04.11.000B.1 If the RPC’s Minimum Wake Up Interval is 0, the RPC MUST implement a Maximum Wake Up
Interval greater than 0.


**8.4.4.4** **RPC** **runtime** **communication**


RT:04.11.000C.1 The RPC MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for more details.


**8.4.4.4.1** **Portable** **End** **Node** **(PEN)**


The Portable End Node Role Type is intended for battery powered devices that aim for the lowest
possible power consumption. The PEN only wakes up in response to a physical event such as a button
press. The PEN allows for optimal cost, as no EEPROM is required.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1232




<!-- PAGE 1234 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.5** **Portable** **End** **Node** **(PEN)**


**8.4.5.1** **PEN** **protocol** **requirements**


RT:05.11.0001.1 The PEN MUST respect requirements described in Section 8.2.


RT:05.11.0002.1 The PEN MUST be battery powered and support the following Command Classes:


     - Battery Command Class


     - Wake Up Command Class, version 2 or newer

RT:05.11.0003.1 The PEN MUST set the listening flag to 0 in its NIF.


The PEN can only be added to a network and has no network role requirement.


**8.4.5.2** **PEN** **setup**


The setups of a PEN by a CSC, SSC, PC or RPC are respectively described in Section 8.4.1.2.4,
Section 8.4.2.2.4, Section 8.4.3.2.4 or Section 8.4.4.2.5. The PEN has no additional requirement when
being included.


**8.4.5.2.1** **Inclusion** **process**


RT:05.12.0001.1 It is RECOMMENDED to use a physical push button for activating learn mode on a PEN Role Type.


**8.4.5.3** **PEN** **Runtime** **configuration**


RT:05.11.0004.1 The PEN MUST support the Wake Up Command Class as described in Section 8.2.8.2.


RT:05.12.0002.1 The PEN SHOULD use a default Wake-Up interval of 0.


RT:05.12.0003.1 The PEN SHOULD have a physical push button for waking up the device for expedited communication. This enables interactive delivery of new configuration parameters or firmware updates.


**8.4.5.4** **PEN** **Runtime** **communication**


RT:05.11.0005.1 The PEN MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for more details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1233




<!-- PAGE 1235 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.6** **Always** **On** **End** **Node** **(AOEN)**


The Always On End Node Role Type is intended for mains powered devices that are always reachable.
One example of such a device is a light switch.


**8.4.6.1** **AOEN** **protocol** **requirements**


RT:06.11.0001.1 The AOEN MUST respect requirements described in Section 8.2.


RT:06.11.0002.1 The AOEN MUST be mains powered and MAY have a battery back-up.

RT:06.11.0003.1 The AOEN MUST set the listening flag to 1 in its NIF. The AOEN can only be added to a network
and has no network role requirement.


**8.4.6.2** **AOEN** **setup**


The setups of an AOEN by a CSC, SSC, PC or RPC are respectively described in Section 8.4.1.2.5,
Section 8.4.2.2.5, Section 8.4.3.2.5 or Section 8.4.4.2.5. The AOEN has no additional requirement
when being included.


**8.4.6.2.1** **Inclusion** **process**


RT:06.12.0001.1 It is RECOMMENDED to use a physical push button for activating learn mode on an AOEN Role
Type.


**8.4.6.3** **AOEN** **runtime** **configuration**


AOEN can always be configured, as it is always listening.


**8.4.6.4** **AOEN** **runtime** **communication**


RT:06.11.0004.1 The AOEN MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for more details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1234




<!-- PAGE 1236 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.7** **Reporting** **Sleeping** **End** **Node** **(RSEN)**


The Reporting Sleeping End Node Role Type is intended for battery-powered devices that only wake
up and communicates when an event has occurred. This allows to reconfigure the device remotely.
Examples include sensors, wall controllers etc.


**8.4.7.1** **RSEN** **protocol** **requirements**


RT:07.11.0001.1 The RSEN MUST respect requirements described in Section 8.2.


RT:07.11.0002.1 The RSEN MUST be battery powered and support the following Command Classes: - Battery Command Class      - Wake Up Command Class, version 2 or newer

RT:07.11.0003.1 The RSEN MUST set the listening flag to 0 in its NIF.


The RSEN can only be added to a network and has no network role requirement.


**8.4.7.2** **RSEN** **setup**


The setups of an RSEN by a CSC, SSC, PC or RPC are respectively described in Section 8.4.1.2.4,
Section 8.4.2.2.4, Section 8.4.3.2.4 or Section 8.4.4.2.4.


The RSEN has no additional requirement when being included.


**8.4.7.2.1** **Inclusion** **process**


RT:07.12.0001.1 It is RECOMMENDED to use a physical push button for activating learn mode on an RSEN Role
Type.


**8.4.7.2.2** **RSEN** **runtime** **configuration**


RT:07.11.0004.1 The RSEN MUST support the Wake Up Command Class as described in Section 8.2.8.2 and in Figure
8.12.


RT:07.12.0002.1 The device SHOULD have a physical push button for waking up the device for expedited communication. This enables interactive delivery of new configuration parameters or firmware updates.


RT:07.11.0005.1 The RSEN MUST implement a Minimum Wake Up Interval in the range 0 .. 4200 (i.e. between 0
second and 70 minutes).


RT:07.11.0006.1 If the RSEN’s Minimum Wake Up Interval is 0, the RSEN MUST implement a Maximum Wake Up
Interval greater than 0.


**8.4.7.2.3** **RSEN** **runtime** **communication**


RT:07.11.0007.1 The RSEN MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1235




<!-- PAGE 1237 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.8** **Listening** **Sleeping** **End** **Node** **(LSEN)**


The Listening Sleeping End Node Role Type is intended for battery-operated devices that can be
reached even though they are sleeping thanks to Beaming (FL nodes). Examples include Door Locks
and Battery operated Thermostats.


**8.4.8.1** **LSEN** **Protocol** **Requirements**


RT:08.11.0001.1 The LSEN MUST respect requirements described in Section 8.2.


RT:08.11.0002.1 The LSEN MUST be battery powered and support the Battery Command Class.

RT:08.11.0003.1 The LSEN MUST set the listening flag to 0 in its NIF.


The LSEN can only be added to a network and has no network role requirement.


**8.4.8.2** **LSEN** **Setup**


The setups of an LSEN by a CSC, SSC, PC or RPC are respectively described in Section 8.4.1.2.4,
Section 8.4.2.2.4, Section 8.4.3.2.4 or Section 8.4.4.2.4. The LSEN has no additional requirement when
being included.


**8.4.8.2.1** **Inclusion** **Process**


RT:08.12.0001.1 It is RECOMMENDED to use a physical push button for activating learn mode on a LSEN Role
Type.


**8.4.8.3** **LSEN** **Runtime** **Configuration**


A LSEN can always be configured, as it is reachable via FLiRS communication.


**8.4.8.4** **LSEN** **Runtime** **Communication**


RT:08.11.0004.1 The LSEN MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for details.


RT:08.11.0005.1 The LSEN MUST stay awake for at least 2 seconds after communicating.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1236




<!-- PAGE 1238 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**8.4.9** **Network** **Aware** **End** **Node** **(NAEN)**


The Network Aware End Node Role Type is intended for end nodes with application controlling
capabilities, which are leveraging controller functionalities to be aware of the network topology and
nodes capabilities.


The SIS (or primary controller) will consider a NAEN as a controller, but the NAEN will not be able
to include new nodes in the network.


**8.4.9.1** **NAEN** **Protocol** **Requirements**


RT:09.11.0001.1 The NAEN MUST respect requirements described in Section 8.2.


RT:09.11.0002.1 The NAEN MUST be mains powered and MAY have a battery back-up.

RT:09.11.0003.1 The NAEN MUST set the listening flag to 1 in its NIF.


RT:09.11.0006.1 The NAEN can only be added to a network and MUST take the inclusion controller or the secondary
controller role when added to a network.


RT:09.11.0004.1 The NAEN MUST NOT provide the following network functions:


     - Include new nodes


     - Exclude nodes


     - Remove failing node


     - Replace failing node


**8.4.9.2** **NAEN** **Setup**


The setups of an NAEN by a CSC, SSC, PC or RPC are respectively described in Section 8.4.1.2.3,
Section 8.4.2.2.5, Section 8.4.3.2.5 or Section 8.4.4.2.5. The NAEN has no additional requirement
when being included.


**8.4.9.2.1** **Inclusion** **process**


RT:09.12.0001.1 It is RECOMMENDED to use a physical push button for activating learn mode on an NAEN Role
Type.


**8.4.9.3** **NAEN** **Runtime** **Configuration**


The NAEN can always be configured, as it is always listening.


**8.4.9.4** **NAEN** **Runtime** **communication**


RT:09.11.0005.1 The NAEN MUST communicate via the lifeline association if any lifeline association exists. Refer to

[34] for more details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1237




<!-- PAGE 1239 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **9 Appendices**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1238




<!-- PAGE 1240 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **9.1 ASCII Codes**


The standard ASCII table defines 128 character codes (from 0 to 127), of which, the first 32 are
control codes (non-printable), and the remaining 96 character codes are printable characters. Figure
9.1 shows the hexadecimal values of the ASCII character codes, e.g. the ASCII code for the capital
letter “A” is equal to 0x41:


Figure 9.1: The Standard ASCII Table


In addition to the 128 standard ASCII codes (the ones listed above ranging from 0 to 127), most
systems have another 128 extra codes which form what is known as extended ASCII (with ranges from
128 to 255). The OEM Extended ASCII character set is included in all PC-compatible computers
as the default character set when the system boots before loading any operating system and under
MS-DOS. It includes some foreign signs, some marked characters and also pieces to draw simple
panels. Figure 9.2 shows the hexadecimal values of the OEM Extended ASCII character codes, e.g.
the ASCII code for the capital letter “Æ” is equal to 0x92:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1239




<!-- PAGE 1241 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 9.2: OEM Extended ASCII Table


Below are listed codes for players, radios etc. as an alternative to the OEM Extended ASCII codes.
Undefined values MUST be ignored.


Figure 9.3: Players Table


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1240




<!-- PAGE 1242 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **9.2 CRC-CCITT Source Code**


The checksum algorithm implements a CRC-CCITT using initialization values equal to 0x1D0F and
0x1021 (normal representation) as the poly.


**9.2.1** **Header** **file**



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1241




<!-- PAGE 1243 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**9.2.2** **Implementation**

```
/**

 * @file
 * Functions for calculation of CRC.
 * @copyright 2018 Silicon Laboratories Inc.
 */

#include <CRC.h>

#define POLY 0x1021 /* crc-ccitt mask */

uint16_t CRC_CheckCrc16(

 uint16_t crc,

 uint8_t *pDataAddr,
 uint16_t bDataLen)
{

 uint8_t WorkData;

 uint8_t bitMask;

 uint8_t NewBit;

 while (bDataLen--)

 {

  WorkData = *pDataAddr;
  pDataAddr++;
  for (bitMask = 0x80; bitMask != 0; bitMask >>= 1)

  {
   /* Align test bit with next bit of the message byte, starting with msb. */
   NewBit = ((WorkData & bitMask) != 0) ^ ((crc & 0x8000) != 0);

   crc <<= 1;

   if (NewBit)

   {

    crc ^= POLY;

   }
  } /* for (bitMask = 0x80; bitMask != 0; bitMask >>= 1) */
 }

 return crc;

}

```

© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1242




<!-- PAGE 1244 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **9.3 Inclusion Process**


This section outlines the recommended inclusion process that all Role Types should follow.


The processes for both node including and being included are covered.


**9.3.1** **Being** **Included**


Figure 9.4: Inclusion Process for the Node being Included


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1243




<!-- PAGE 1245 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**9.3.2** **Including** **a** **Node**


Figure 9.5: Inclusion Process for the Including Node


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1244




<!-- PAGE 1246 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **References**


[1] D. J. Bernstein. A state-of-the-art Diffie-Hellman function. 2022. URL: [http://cr.yp.to/ecdh.](http://cr.yp.to/ecdh.html)
[html.](http://cr.yp.to/ecdh.html)


[2] Barak Boaz and Shai Halevi. A Model and Architecture for Pseudo-Random Generation with
Applications to /dev/random. In _Proceedings_ _of_ _the_ _12th_ _ACM_ _Conference_ _on_ _Computer_ _and_
_Communications Security_, CCS 2005, 203–212. New York, NY, USA, November 2005. Association
for Computing Machinery. [doi:10.1145/1102120.1102148.](https://doi.org/10.1145/1102120.1102148)


[3] Scott O. Bradner. Key words for use in RFCs to Indicate Requirement Levels. RFC 2119, March
1997. URL: [https://www.rfc-editor.org/info/rfc2119,](https://www.rfc-editor.org/info/rfc2119) [doi:10.17487/RFC2119.](https://doi.org/10.17487/RFC2119)


[4] Anders Brandt and Jakob Buron. Transmission of IPv6 Packets over ITU-T G.9959
Networks. RFC 7428, February 2015. URL: [https://www.rfc-editor.org/info/rfc7428,](https://www.rfc-editor.org/info/rfc7428)
[doi:10.17487/RFC7428.](https://doi.org/10.17487/RFC7428)

[5] Alex Conta. Extensions to IPv6 Neighbor Discovery for Inverse Discovery Specification. RFC
3122, June 2001. URL: [https://www.rfc-editor.org/info/rfc3122,](https://www.rfc-editor.org/info/rfc3122) [doi:10.17487/RFC3122.](https://doi.org/10.17487/RFC3122)


[6] Dr. Steve E. Deering and Bob Hinden. IP Version 6 Addressing Architecture. RFC 4291, February
2006. URL: [https://www.rfc-editor.org/info/rfc4291,](https://www.rfc-editor.org/info/rfc4291) [doi:10.17487/RFC4291.](https://doi.org/10.17487/RFC4291)


[7] Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno. _Cryptography_ _Engineering:_ _Design_
_Principles_ _and_ _Practical_ _Applications_ . Wiley Publishing, Inc., Indianapolis, IN, 2010. ISBN
9780470474242.

[8] Bob Hinden and Dr. Steve E. Deering. Internet Protocol, Version 6 (IPv6) Specification. RFC
2460, December 1998. URL: [https://www.rfc-editor.org/info/rfc2460,](https://www.rfc-editor.org/info/rfc2460) [doi:10.17487/RFC2460.](https://doi.org/10.17487/RFC2460)


[9] S. Matyas, C. Meyer, and J. Oseas. Generating strong one-way functions with cryptographic
algorithm. _IBM_ _Technical_ _Disclosure_ _Bulletin_, 27:5658–5695, 1985.


[10] Robert Moskowitz and Rene Hummen. HIP Diet EXchange (DEX). Internet Draft
draft-moskowitz-hip-dex-02, Internet Engineering Task Force (IETF), June 2005. Work in
Progress. URL: [https://datatracker.ietf.org/doc/html/draft-moskowitz-hip-dex-02.](https://datatracker.ietf.org/doc/html/draft-moskowitz-hip-dex-02)


[11] National Institute of Standards and Technology (NIST). Advanced Encryption Standard (AES).
Technical Report Federal Information Procesing Standards Publications (FIPS PUBS) 197, U.S.
Department of Commerce, Washington, D.C., November 2001. [doi:10.6028/NIST.FIPS.197.](https://doi.org/10.6028/NIST.FIPS.197)


[12] National Institute of Standards and Technology (NIST). Recommendation for Block Cipher Modes of Operation: Methods and Techniques. Technical Report Special Publication (NIST SP) 800-38A, U.S. Department of Commerce, Washington, D.C., January 2001.
[doi:10.6028/NIST.SP.800-38A.](https://doi.org/10.6028/NIST.SP.800-38A)


[13] National Institute of Standards and Technology (NIST). Recommendation for Block Cipher
Modes of Operation: Galois/Counter Mode (GCM) and GMAC. Technical Report Special Publication (NIST SP) 800-38C, U.S. Department of Commerce, Washington, D.C., November 2007.
[doi:10.6028/NIST.SP.800-38C.](https://doi.org/10.6028/NIST.SP.800-38C)


[14] National Institute of Standards and Technology (NIST). Recommendation for Random Number Generation Using Deterministic Random Bit Generators. Technical Report Special Publication (NIST SP) 800-90A, U.S. Department of Commerce, Washington, D.C., January 2012.
[doi:10.6028/NIST.SP.800-90A.](https://doi.org/10.6028/NIST.SP.800-90A)


[15] National Institute of Standards and Technology (NIST). Recommendation for Block Cipher
Modes of Operation: The CMAC Mode for Authentication. Technical Report Special Publication (NIST SP) 800-38B, U.S. Department of Commerce, Washington, D.C., October 2016.
[doi:10.6028/NIST.SP.800-38B.](https://doi.org/10.6028/NIST.SP.800-38B)


[16] William A. Simpson, Dr. Thomas Narten, Erik Nordmark, and Hesham Soliman. Neighbor Discovery for IP version 6 (IPv6). RFC 4861, September 2007. URL: [https://www.rfc-editor.org/](https://www.rfc-editor.org/info/rfc4861)
[info/rfc4861,](https://www.rfc-editor.org/info/rfc4861) [doi:10.17487/RFC4861.](https://doi.org/10.17487/RFC4861)


[17] Doug Whiting, Russ Housley, and Niels Ferguson. Counter with CBC-MAC (CCM). RFC 3610,
September 2003. URL: [https://www.rfc-editor.org/info/rfc3610,](https://www.rfc-editor.org/info/rfc3610) [doi:10.17487/RFC3610.](https://doi.org/10.17487/RFC3610)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1245