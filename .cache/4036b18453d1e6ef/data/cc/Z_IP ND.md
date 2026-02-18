<!-- PAGE 1070 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.16** **Z/IP** **ND** **Command** **Class,** **version** **1**


Z/IP ND Command Class builds on the same principles as IPv6 ND RFC 4861, RFC 3122 and is
inspired by the frame formats. Z/IP ND does however not implement the full range of functions
defined for IPv6 ND.


**5.2.16.1** **Interoperability** **considerations**


Z/IP ND commands allow a Z/IP Gateway to translate between an IPv6 address and a Z-Wave NodeID
(Link-Layer address) when requested by an IP host located in a Z-Wave HAN or anywhere else in an
IPv6 environment. The Z/IP ND Commands are not intended for classic Z-Wave applications. Z/IP
ND messages MUST always be carried in UDP datagrams without Z/IP Packet encapsulation.


**5.2.16.2** **Security** **considerations**


The commands defined in this Command Class MUST always be accepted by a receiving node, regardless of whether IP security (such as DTLS) was used for the transmission.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1069




<!-- PAGE 1071 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.16.3** **Z/IP** **Node** **Solicitation** **Command**


The Z/IP Node Solicitation Command is used to resolve an IPv6 address of a Z-Wave node to the
NodeID (Link-Layer address) of that node in its actual Z-Wave HAN / IP subnet.


Several IPv6 addresses MAY be resolved to the same NodeID.


The Zip Node Solicitation MUST be transmitted in unicast to the Z/IP Gateway of the actual Z/IP
HAN. A Z/IP Gateway MUST NOT respond to Zip Node Solicitation commands received via multi
cast.


A Zip Node Advertisement MUST be returned in response to the Zip Node Solicitation.


Table 5.200: Z/IP Node Solicitation Command


**Reserved**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|
|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|Command = ZIP_NODE_SOLICITATION|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|NodeID = 0|NodeID = 0|NodeID = 0|NodeID = 0|NodeID = 0|NodeID = 0|NodeID = 0|NodeID = 0|
|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|


This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**NodeID** **(8** **bits)**

The NodeID field is not used in the Zip Node Solicitation. The field MUST be set to zero by a
transmitting host and ignored by a receiving host.


**IPv6** **Address** **(16** **bytes)**


The IP address of the target Z-Wave node. It MUST NOT be a multicast address.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1070




<!-- PAGE 1072 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.16.4** **Z/IP** **Inverse** **Node** **Solicitation** **Command**


The Z/IP Inverse Node Solicitation Command is used to resolve a NodeID (link-layer address) of a
Z-Wave node to an IPv6 address of that node in its actual Z-Wave HAN / IP subnet.


The Zip Inverse Node Solicitation MUST be transmitted in unicast to the Z/IP Gateway of the actual
Z/IP HAN. A Z/IP Gateway MUST NOT respond to Zip Inverse Node Solicitation commands received
via multicast.


A _Z/IP_ _Node_ _Advertisement_ _Command_ MUST be returned in response to the Zip Inverse Node
Solicitation.


Table 5.201: Z/IP Inverse Node Solicitation Command


**Reserved**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|
|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|
|Reserved|Reserved|Reserved|Reserved|Local|Reserved|Reserved|Reserved|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|


This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Local** **(1** **bit)**

The flag indicates that the requester would like to receive the site-local address (a.k.a. ULA) even if
a global address exists. The flag is typically used by a configuration tool when creating an association
between HAN nodes within the same site. Using ULA addresses for intra-HAN association serves to
decouple long-term associations in the home from frequently changing global prefixes.


**NodeID** **(8** **bits)**


The NodeID (Link-Layer Address) that is to be resolved to an IPv6 address.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1071




<!-- PAGE 1073 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.16.5** **Z/IP** **Node** **Advertisement** **Command**


The Z/IP Node Advertisement Command is sent by a Z/IP Gateway in response to a unicast Zip
Node Solicitation or a unicast Zip Inverse Node Solicitation. The Zip Node Advertisement SHOULD
advertise valid information in both the IPv6 Address and NodeID fields if such information.


A Zip Node Advertisement MUST NOT be transmitted in unsolicited messages.


A Zip Node Advertisement MUST NOT be transmitted in multicast.


Table 5.202: Z/IP Node Advertisement Command


**Reserved**

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|
|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Local|Validity|Validity|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|
|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|
|…|…|…|…|…|…|…|…|
|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|


This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Local** **(1** **bit)**

The flag indicates that the requester asked for the site-local address (a.k.a. ULA).


A ULA address is returned. A global address may exist.


**Validity** **(2** **bits)**


A two-bit codeword that indicates the validity of the returned information.



Table 5.203: Zip Node Advertisement::Validity parameter encoding






|Value|i<br>Validity identifer|Comment|
|---|---|---|
|0x00|INFORMATION_OK|The Node Advertisement contains valid infor-<br>mation in both the IPv6 Address and NodeID<br>felds.|
|0x01|INFORMATION_OBSO-<br>LETE|The information in the IPv6 Address and<br>NodeID felds is obsolete. No node exists in the<br>network with this address information. The in-<br>formation should only be used to inform a user<br>that the actual node is no more present in the<br>network.|
|0x02|INFORMA-<br>TION_NOT_FOUND|The responding Z/IP Gateway could not locate<br>valid information.<br>IPv6 Address and NodeID<br>felds MUST be ignored.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**NodeID** **(8** **bits)**


The NodeID MUST correspond to the IPv6 Address contained in this Zip Node Advertisement mes
sage.


**IPv6** **Address** **(16** **bytes)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1072




<!-- PAGE 1074 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The IPv6 Address MUST correspond to the NodeID contained in this Zip Node Advertisement mes
sage.


An IPv6 host may have more than one IPv6 address.


If the Zip Node Advertisement is a response to a Zip Node Solicitation, the IPv6 Address MUST be
the same as the one carried in the Zip Node Solicitation.


A Z/IP Gateway returning a Zip Node Advertisement in response to a Zip Inverse Node Solicitation
may have several IPv6 addresses to choose from. The reported IPv6 Address MUST be selected
according to the following priority list:

If ”local” flag is set:

1. Unique Local Address (ULA) prefix

If ”local” flag is not set:


1. Global routable address

2. Unique Local Address (ULA) prefix


In other words, if the Z/IP node has a globally routable address then that address MUST be reported.

Else the locally routable address constructed from a ULA prefix and the NodeID MUST be reported.


If a Z/IP Inverse Node Solicitation command is transmitted in an IPv6 packet the returned Z/IP
Node Advertisement MUST carry the IPv6 address of the actual node.


If a Z/IP Inverse Node Solicitation command is transmitted in an IPv4 packet the returned Z/IP
Node Advertisement MUST carry the IPv4 address of the actual node formatted as an IPv4-mapped
IPv6 address RFC 4291.


The IP address carried in the Z/IP Node Advertisement MAY be all zeros. The reason may be that
the Z/IP Gateway is still waiting for a DHCP response after including a new node. A Z/IP client
MAY re-issue another a Z/IP Inverse Node Solicitation command after a delay of 2 seconds. The
delay MUST be doubled before each new attempt. The delay SHOULD be capped at 32 seconds.


**Home** **ID** **(4** **bytes)**


Unique network address of the link layer network. All nodes in a Z-Wave network share the same
Home ID. The Home ID MAY be used for bookkeeping of complete node information in managed
installations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1073

---

<!-- PAGE 1075 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.17** **Z/IP** **ND** **Command** **Class,** **version** **2**


**5.2.17.1** **Compatibility** **Considerations**


The Z/IP ND Command Class, version 2 introduces support for Extended NodeIDs. This version is
backwards compatible with version 1.

All fields not described in this version MUST remain unchanged from version 1. The following
commands are updated:


 - Z/IP Inverse Node Solicitation Command


 - Z/IP Node Advertisement Command


**5.2.17.2** **Interoperability** **considerations**


Refer to Section 5.2.16.1 Interoperability considerations.


**5.2.17.3** **Security** **considerations**


Refer to Section 5.2.16.2 Security considerations.


**5.2.17.4** **Z/IP** **Inverse** **Node** **Solicitation** **Command**


The Z/IP Inverse Node Solicitation Command is used to resolve a NodeID (link-layer address) of a
Z-Wave node to an IPv6 address of that node in its actual Z-Wave HAN / IP subnet.


The Zip Inverse Node Solicitation MUST be transmitted in unicast to the Z/IP Gateway of the actual
Z/IP HAN. A Z/IP Gateway MUST NOT respond to Zip Inverse Node Solicitation commands received
via multicast.


A Zip Node Advertisement MUST be returned in response to the Zip Inverse Node Solicitation.


Table 5.204: Z/IP Inverse Node Solicitation Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|
|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|Command = ZIP_INV_NODE_SOLICITATION|
|Reserved|Reserved|Reserved|Reserved|Local|Reserved|Reserved|Reserved|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 1.


**NodeID** **(8** **bits)**

This field is used to indicate the NodeID (Link-Layer Address) that is to be resolved to an IPv6
address.


The value 0xFF MUST indicate that the NodeID to be resolved MUST be read from the Extended
_NodeID_ field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to specify the NodeID (Link-Layer Address) that is to be resolved to an IPv6 address.

If the _NodeID_ field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the _NodeID_ field is set to 0xFF, this field MUST indicate the NodeID that is to be resolved to an
IPv6 address.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1074




<!-- PAGE 1076 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.17.5** **Z/IP** **Node** **Advertisement** **Command**


The Z/IP Node Advertisement Command is sent by a Z/IP Gateway in response to a unicast Zip
Node Solicitation or a unicast Zip Inverse Node Solicitation. The Zip Node Advertisement SHOULD
advertise valid information in both the IPv6 Address and NodeID fields if such information.


A Zip Node Advertisement MUST NOT be transmitted in unsolicited messages.


A Zip Node Advertisement MUST NOT be transmitted in multicast.


Table 5.205: Z/IP Node Advertisement Command, version 2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|Command Class = COMMAND_CLASS_ZIP_ND|
|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|Command = ZIP_NODE_ADVERTISEMENT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Local|Validity|Validity|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|IPv6 Address 16|
|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|Home ID 1|
|…|…|…|…|…|…|…|…|
|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|Home ID 4|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 1.


**NodeID** **(8** **bits)**


The NodeID MUST correspond to the IPv6 Address contained in this Zip Node Advertisement mes
sage.


The value 0xFF MUST indicate that the NodeID contained in this ZIP Node Advertisement message
MUST be read from the _Extended_ _NodeID_ field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to specify the NodeID that is resolved to the specified IPv6 address.

If the _NodeID_ field is in the range 0x00..0xFE, this field MUST be set to the same value as the _NodeID_
field by a sending node.

If the _NodeID_ field is set to 0xFF, this field MUST indicate the NodeID that is to resolved to the
specified IPv6 address.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1075