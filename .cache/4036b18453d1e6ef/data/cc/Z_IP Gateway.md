<!-- PAGE 1059 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15** **Z/IP** **Gateway** **Command** **Class,** **version** **1**


The Z/IP gateway Command Class is used for configuration and management of a Z/IP gateway, e.g.
to enable portal communication.


**5.2.15.1** **Interoperability** **considerations**


The Z/IP Gateway Command Class is intended for use together with the Z/IP Portal Command
Class to provide a streamlined workflow for preparing and performing installation of Z/IP Gateways
in consumer premises. Section 5.2.18.1.1 presents the concepts of tunnel creation, maintenance and
bootstrapping of a Z/IP Gateway. A Z/IP Gateway may operate in a standalone environment where
it is only accessed locally or it may create a tunnel to a portal provider to allow remote access.
Commands defined in this Command Class MUST be encapsulated in Z/IP Packets.


**5.2.15.2** **Gateway** **Mode** **Set** **Command**


Any host may send the Gateway Mode Set command during initial configuration of the gateway.
Most likely, a service provider or an OEM will use the command in a central facility when preparing
deployment at customer premises.


Table 5.186: Gateway Mode Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|Command = GATEWAY_MODE_SET|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Mode** **(1** **byte)**

This field sets the communication mode of the Z/IP Gateway

|Value|Table 5.187: Gateway Mode Set::Mode encoding Mode|
|---|---|
|Value|Mode|
|0x01|Stand-alone (default)|
|0x02|Portal|



If Mode is set to ”Stand-alone”, the Z/IP Gateway MUST NOT do any attempts to create secure
tunnels to other peers in the LAN or in the Internet.

The default mode SHOULD be ”Stand-alone”. By default, peer profiles SHOULD NOT be defined.


A Mode value set to ”Portal” MUST be ignored if the actual gateway does not support the Z/IP
Portal Command Class, If Mode is set to ”Portal”, the Z/IP Gateway MUST use the peer profile
defined with the Gateway Peer Set command to create a secure connection to the portal server.

Once the Z/IP Gateway has been configured for portal connection creation, the Z/IP Gateway
SHOULD be locked for unauthorized access by issuing a Gateway Lock Set; refer to Section 5.2.15.8.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1058




<!-- PAGE 1060 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.3** **Gateway** **Mode** **Get** **Command**


The Gateway Mode Get command is used to request the current Z/IP Gateway operational mode.


The Gateway Mode Report Command MUST be returned in response to this command except if the
Z/IP Gateway is locked with the Gateway Lock Set command and the Hide parameter of the Gateway
Lock Set command was enabled.


In that case, the Gateway Mode Get command MUST be silently ignored.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.188: Gateway Mode Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|Command = GATEWAY_MODE_GET|



**5.2.15.4** **Gateway** **Mode** **Report** **Command**


This command is used to advertise the mode.


Table 5.189: Gateway Mode Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|Command = GATEWAY_MODE_REPORT|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Mode** **(1** **byte)**

This field indicates the communication mode of the Z/IP Gateway. Refer to Section 5.2.15.2 and
Table 5.187 for details.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1059




<!-- PAGE 1061 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.5** **Gateway** **Peer** **Set** **Command**


The Peer Set Command is used to define one or more peers to which the Z/IP Gateway connects.
The peer may be a portal server or one or more Z/IP Gateways.


A Peer Set command MUST always carry the peer identity as an IPv6 address and an IP port number.
The command SHOULD also specify the symbolic peer name as a FQDN.

If the Gateway Mode is set to ”Portal”, there MUST NOT be defined more than one Peer profile.

If the Gateway Mode is set to ”Stand-alone”, there MUST NOT be defined any peer profiles.


Table 5.190: Gateway Mode Peer Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|Command = GATEWAY_PEER_SET<br>|
|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|
|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|
|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|
|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|
|Reserved|Reserved|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|
|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|
|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|
|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|



**Peer** **Profile** **(8** **bits)**

This field identifies the actual peer profile.


The value 0 (zero) is reserved for future use.

The first peer profile MUST be number 1.


**IPv6** **Address**

Full IPv6 address with no compression. The address SHOULD be in the ULA IPv6 prefix or in a
globally routable IPv6 prefix. The address MAY be an IPv4-mapped IPv6 address.

The field MUST NOT carry a link-local IPv6 address.

The IPv6 address MAY be specified as ::/128 (all zeros), i.e. the unspecified address. If setting the IPv6
address field to the unspecified IPv6 address, the Peer Name field MUST be set to a DNS-resolvable
FQDN.


**Port** **(16** **bits)**

This field MUST carry the port number that the peer is listening on. The peer SHOULD use port
number 44123 [19].


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Peer** **Name** **Length** **(6** **bits)**


May be any value from 0 to 63. The value indicates the number of Peer Name bytes following this
field. The number of readable characters may be less since some UTF-8 characters are represented by
two or more bytes.


**Peer** **Name** **(N** **bytes)** **(optional)**

This field is only present if the Peer Name Length field has a value greater than zero.

The Peer Name field MUST be formatted as a UTF-8 based FQDN string such as ”example.com”.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1060




<!-- PAGE 1062 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Only if that fails, the Z/IP Gateway SHOULD try connecting to the peer using the Peer Name and
the Port.


A Z/IP Gateway SHOULD try connecting to the peer using the IPv6 address and the Port.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1061




<!-- PAGE 1063 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.6** **Gateway** **Peer** **Get** **Command**


The Gateway Peer Get Command is used to request active peer profiles.


The Gateway Peer Report Command MUST be returned in response to this command except if the
Z/IP Gateway is locked with the Gateway Lock Set command and the Hide parameter of the Gateway
Lock Set command was enabled.


In that case, the Gateway Peer Get command MUST be silently ignored.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.191: Gateway Mode Peer Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|Command = GATEWAY_PEER_GET<br>|
|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|



**Peer** **Profile** **(8** **bits)**

This field identifies the actual peer profile.

A requesting host SHOULD start specifying the Peer Profile value 1 (one). This will cause the Z/IP
Gateway to indicate the number of actual peers in the returned Gateway Peer Report command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1062




<!-- PAGE 1064 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.7** **Gateway** **Peer** **Report** **Command**


The Gateway Peer Report Command is used to report details of a peer profile.


A Gateway Peer Report command MUST always carry the peer address as an IPv6 address and MUST
include the peer resource name if it was previously specified.


Table 5.192: Gateway Mode Peer Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|Command = GATEWAY_PEER_REPORT<br>|
|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|Peer Profle|
|Peer Count|Peer Count|Peer Count|Peer Count|Peer Count|Peer Count|Peer Count|Peer Count|
|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|
|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|Port 1|
|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|Port 2|
|_Reserved_|_Reserved_|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|Peer Name Length|
|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|Peer Name 1 (UTF-8) (Optional)|
|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|… (Optional)|
|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|Peer Name N (UTF-8) (Optional)|



**Peer** **Profile**

This identifier is used to identify the actual peer profile.


The value 0 (zero) is reserved for future use.


**Peer** **Count** **(8** **bits)**

This field indicates the number of peer profiles currently defined.

If the Peer Count field has the value 0, all other fields of the Gateway Peer Report MUST be 0.


**IPv6** **Address**

This field MUST carry a full IPv6 address with no compression.


**Port** **(16** **bits)**

This field MUST carry the port number that the peer is listening on. The peer SHOULD use port
number 44123 [19].


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Peer** **Name** **Length** **(6** **bits)**


May be any value from 0 to 63. The value indicates the number of Peer Name bytes following this
field. The number of readable characters may be less since some UTF-8 characters are represented by
two or more bytes.


**Peer** **Name** **(N** **bytes)** **(optional)**

This field is only present if the Peer Name Length field has a value greater than zero.

The Peer Name field MUST be formatted as a UTF-8 based FQDN string such as ”example.com”.

If the Peer Count value is zero, the Resource Name string MUST be unspecified (zero-length).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1063




<!-- PAGE 1065 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.8** **Gateway** **Lock** **Set** **Command**


The Lock Set command MUST lock down access to configuration parameters in the Z/IP Gateway
relating to secure connections and portal login. Once the Z/IP Gateway has been locked, it MUST
NOT be possible to unlock the device. Two exceptions apply:


 - A factory default reset MUST unlock the Z/IP Gateway and revert settings to default.


 - An unlock command received via an authenticated secure connection to the portal MUST unlock
the Z/IP Gateway.


Table 5.193: Gateway Lock Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|Command = GATEWAY_LOCK_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Show|Lock|



**Lock** **(1** **bit)**

This field controls if Z/IP Gateway configuration parameters may be changed by the customer.


The value 0 MUST indicate that the parameters are unlocked and can be changed by the customer.


The value 1 MUST indicate that the parameters are locked and cannot be changed by the customer.
The Z/IP gateway MUST accept to receive the Lock=1 flag from any connection.

The Z/IP gateway MUST NOT accept to receive the Lock=0 flag from any connection; except for an
authenticated secure connection to the portal.


To prevent users and trojan viruses from creating tunnels to rogue portals, the Z/IP Gateway SHOULD
automatically lock access to secure tunnel configuration parameters 24 hours after a factory default
reset.


**Show** **(1** **byte)**

This field controls if Z/IP Gateway configuration parameters may be read by the customer after the
Z/IP Gateway has been locked.


The value 0 MUST indicate that parameters are not available to the customer.


The value 1 MUST indicate that parameters are available to the customer.


If the Show parameter is ‘0’ the Z/IP Gateway MUST NOT respond to any queries for Z/IP Gateway
parameters.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1064




<!-- PAGE 1066 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.9** **Unsolicited** **Destination** **Set** **Command**


The Unsolicited Destination Set Command is used to configure the destination information that the
Z/IP Gateway must use for incoming unsolicited frames.


Table 5.194: Unsolicited Destination Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|Command = UNSOLICITED_DESTINATION_SET|
|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|
|…|…|…|…|…|…|…|…|
|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|
|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|
|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|



**Unsolicited** **IPv6** **Destination** **(16** **bytes)**


Unsolicited Z-Wave frames received from any Z-Wave node MUST be forwarded to the Unsolicited
IPv6 Destination address.


**Unsolicited** **Destination** **Port** **(2** **bytes)**


Unsolicited Z-Wave frames received from any Z-Wave node MUST be forwarded to the Unsolicited
IPv6 Destination Port. Byte 1 is the Most Significant byte.


The Unsolicited IPv6 Destination Port SHOULD be port 4123.


IPv6 enabled Z-Wave nodes MAY send Z-Wave commands encapsulated in Z/IP Packets to the Unsolicited IPv6 Destination address. The Z/IP Gateway MUST translate the destination port of Z/IP
Packets destined for the Unsolicited IPv6 Destination address from port 4123 to the port number
defined for the Unsolicited Destination Port.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1065




<!-- PAGE 1067 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.10** **Unsolicited** **Destination** **Get** **Command**


The Unsolicited Destination Get Command is used to request the destination information that the
Z/IP Gateway uses for incoming unsolicited frames.


The Unsolicited Destination Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.195: Unsolicited Destination Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|Command = UNSOLICITED_DESTINATION_GET|



**5.2.15.11** **Unsolicited** **Destination** **Report** **Command**


The Unsolicited Destination Report Command is used to report the destination information that the
Z/IP Gateway uses for incoming unsolicited frames.


The command format is outlined below:


Table 5.196: Unsolicited Destination Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|Command = UNSOLICITED_DESTINATION_REPORT|
|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|Unsolicited IPv6 Destination 1|
|…|…|…|…|…|…|…|…|
|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|Unsolicited IPv6 Destination 16|
|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|Unsolicited Destination Port 1|
|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|Unsolicited Destination Port 2|



Unsolicited IPv6 Destination (16 bytes) Refer to Section 5.2.15.9. Unsolicited Destination Port (2
bytes) Refer to Section 5.2.15.9.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1066




<!-- PAGE 1068 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.12** **Application** **Node** **Info** **Set** **Command**


The Application Node Info Set Command is used to set the application specific part of the Node
Information that a Z/IP Gateway returns when queried by a Z-Wave node.


Table 5.197: Application Node Info Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|Command = COMMAND_APPLICATION_NODE_INFO_SET|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended �spanning two bytes for one command class


**Command** **Class** **(N** **bytes)**


See description _Node_ _info_ _cached_ _report_ _command_ and Table 5.27.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1067




<!-- PAGE 1069 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.15.13** **Application** **Node** **Info** **Get** **Command**


The Application Node Info Get Command is used to request the Node Information that a Z/IP
Gateway returns when queried by a Z-Wave node.


The Application Node Info Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.198: Application Node Info Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|



**5.2.15.14** **Application** **Node** **Info** **Report** **Command**


The Application Node Info Report Command is used to report the Node Information that a Z/IP
Gateway returns when queried by a Z-Wave node. Only the application specific part is returned.


Table 5.199: Application Node Info Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|Command Class = COMMAND_CLASS_ZIP_GATEWAY|
|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|Command = COMMAND_APPLICATION_NODE_INFO_GET|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended �spanning two bytes for one command class


**Command** **Class** **(N** **bytes)**


Refer to Section 5.2.15.12.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1068