<!-- PAGE 1034 -->

CC:0023.01.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.9** **Z/IP** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **OBSOLETED**


New implementations MUST use the Z/IP Command Class Version 2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1033

---

<!-- PAGE 1035 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.10** **Z/IP** **Command** **Class,** **version** **2**


The Z/IP Command Class is a special Command Class intended for encapsulation of Z-Wave commands in IP packets.


Z/IP Packets may be exchanged between IP hosts running over physical layers such as Ethernet or
WiFi.


**5.2.10.1** **Security** **considerations**


This Command Class is used to encapsulate Z-Wave Commands in an IP network. A Z/IP Gateway
will forward some of the encapsulated Z-Wave commands into the Z-Wave Network.


The Z-Wave nodes may use encryption to protect the integrity of the Z-Wave network (refer to Security
0 and Security 2 Command Classes). IP nodes should always assume to be in a hostile network and
support an encryption mechanism, such as DTLS.


**If** **an** **IP** **node** **implements** **IP** **LAN** **security** **(DTLS** **or** **equivalent):**


CC:0023.02.00.41.001 - Z/IP Packet received via secure IP channel MUST be accepted and a Z/IP Gateway MUST
forward the optional Z-Wave Command in the Z-Wave network.


      - Z/IP Packet received via non-secure IP channel:


CC:0023.02.00.41.002 - Z/IP Discovery Command Class MUST be accepted. - All other encapsulated Command Classes

CC:0023.02.00.41.003 MUST be discarded.


**If** **an** **IP** **node** **does** **not** **implement** **IP** **LAN** **security** **(DTLS** **or** **equivalent):**


CC:0023.02.00.41.004 - All Z/IP Packet received via non-secure IP channel MUST be accepted.


CC:0023.02.00.43.001 If the Z/IP Command Class interface is used to communicate between applications within the same
machine, the use of DTLS is OPTIONAL.


CC:00.23.02.00.41.005 If the Z/IP Command Class interface is used to communicate between applications across an IP
network, the use of DTLS is REQUIRED.


**5.2.10.2** **Interoperability** **considerations**


CC:0023.02.00.32.001 Any Z-Wave Command Class SHOULD be sent encapsulated in a Z/IP Packet if a transmission takes
place in an IP network.


CC:0023.02.0031.001 Commands part of this Command Class MUST NOT be encapsulated in a Z/IP Packet Command.


**5.2.10.3** **Z/IP** **Packet** **Command**


IP->UDP:4123->Z/IP Packet Command->Optional Z-Wave command


IP->UDP:41230->DTLS->Z/IP Packet Command->Optional Z-Wave command


CC:0023.02.02.11.001 A Z/IP Packet Command MUST be carried in a UDP packet, using destination port 4123 when no
LAN security is used.


CC:0023.02.02.11.002 A Z/IP Packet Command MUST be carried in a UDP packet, using destination port 41230 when
DLTS is used.


CC:0023.02.02.11.003 A node returning an answer to a Z/IP Packet (Ack/NAck Response) MUST swap the UDP source
and destination ports.


The Z/IP Packet may carry a Z-Wave command or it may be used to communicate positive or negative
acknowledgement for the delivery of another Z/IP Packet.


CC:0023.02.02.11.004 The Z/IP Packet MUST NOT be used for transmission between native Z-Wave nodes. The Z/IP
Packet is intended for transport of encapsulated Z-Wave commands inside IP packets in an IP envi
ronment.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1034




<!-- PAGE 1036 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


For that reason, normal Z-Wave MAC layer frame size limitations do not apply to this command,
however Z-Wave MAC Layer frame size and Z-Wave Transport Service Command Class size limitations
apply to the Z-Wave Command field.


Table 5.149: Z/IP Packet Command





















|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|
|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|Command = COMMAND_ZIP_PACKET (0x02)<br>|
|Ack<br>Request|Ack<br>Response|NAck<br>Response|(NAck fags)|(NAck fags)|(NAck fags)|_Reserved_|_Reserved_|
|Ack<br>Request|Ack<br>Response|NAck<br>Response|Waiting|Queue<br>Full|Option<br>Error|Option<br>Error|Option<br>Error|
|Header ext.<br>included|Z-Wave Cmd<br>included|More<br>Information|Secure<br>Origin|_Reserved_|_Reserved_|_Reserved_|_Reserved_|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Res|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|Source End Point|
|Bit address|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|Destination End Point|
|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|Header extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|Header extension N (Optional)|
|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|Z-Wave Command 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|Z-Wave Command M (Optional)|


CC:0023.02.02.11.005 A receiving node MUST inspect the header flags in order to determine the offset to use for accessing
the optional fields. If the packet contains invalid data, e.g. the ACK_RES and NACK_RES bits are
both set to 1 or if the length of the extended header does not add up, a receiving node MUST ignore
the packet.


**Ack** **Request** **(1** **bit)**

CC:0023.02.02.11.006 This flag signals that the receiving node MUST return an Ack or NAck message in response to the
actual Z/IP Packet.

CC:0023.02.02.11.007 This field MUST be encoded according to Table 5.150.


Table 5.150: Z/IP Packet::Ack Request Flag encoding

|Value|Description|
|---|---|
|‘1’|Return Ack or NAck<br>|
|‘0’|No confrmation needed|



CC:0023.02.02.11.008 If this flag is set to 1, the Z/IP Packet MUST contain a Z-Wave Command. A receiving node MUST
discard the packet if this flag is set to 1 but no Z-Wave Command is included.

This field is intended for delivery acknowledgement for Z-Wave Commands encapsulated in Z/IP
packets.


CC:0023.02.02.12.001 Z-Wave link-level acknowledgement SHOULD always be used between Z-Wave nodes when Z-Wave is
used as link layer.


CC:0023.02.02.11.009 A Z/IP Gateway MUST return a ”NAck+Waiting” indication no later than 200ms after receiving an
Ack Request if the Z-Wave Command is still being processed or pending delivery.


CC:0023.02.02.13.001 A sending node that has requested an Ack and has waited for more than 300ms without receiving an
Ack or NAck indication MAY conclude that the Z-Wave Command is lost and retransmit the Z/IP
Packet.


CC:0023.02.02.11.00A In case of successful delivery to a Z-Wave node, a Z/IP Packet with Ack Response indication MUST
be returned by the Z/IP Gateway upon reception of the Z-Wave Ack.


CC:0023.02.02.11.00B In case of successful delivery to a Z/IP node, the Z/IP node itself MUST return a Z/IP Packet with
Ack Response indication.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1035




<!-- PAGE 1037 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Ack** **Response** **(1** **bit)**

CC:0023.02.02.11.00C This flag MUST be used to indicate that the destination has received the Z-Wave Command encapsulated in a preceding Z/IP packet.

CC:0023.02.02.11.00D This field MUST NOT be interpreted as a confirmation that the destination has accepted the application command carried in the Z-Wave Command field.

CC:0023.02.02.11.00E This field MUST be encoded according to Table 5.151.



CC:0023.02.02.11.00F



Table 5.151: Z/IP Packet::Ack Response Flag encoding


|value|Description|
|---|---|
|‘1’|This Z/IP Packet acknowledges a preceding packet that requested an Ack<br>Response|
|‘0’|This Z/IP Packet does not acknowledge a preceding packet that requested<br>an Ack Response.<br>A receiving node MUST inspect the NAck Response feld|



CC:0023.02.02.11.010 If this field is set to 1, the _Seq No_ field value MUST be the same as the Z/IP packet being acknowledged.


**NAck** **Response** **(1** **bit)**


CC:0023.02.02.11.011
This flag MUST be used to indicate that the destination has not (yet) received the Z-Wave Command
encapsulated in a preceding Z/IP Packet.

CC:0023.02.02.11.012 This field MAY be set to 1 by intermediate nodes such as a Z/IP Gateway. This field MUST be
encoded according to Table 5.152.



CC:0023.02.02.11.013



Table 5.152: Z/IP Packet::NAck Response Flag encoding


|value|Description|
|---|---|
|‘1’|This Z/IP Packet negatively acknowledges a preceding packet that re-<br>quested an Ack Response. (i.e. the Z-Wave Command was not delivered<br>to the destination)<br>A receiving node MUST inspect the NAck fags felds.<br>|
|‘0’|This feld and the _NAck fags_ felds may be ignored.|



CC:0023.02.02.11.014 If this field is set to 1, the _Seq_ _No_ field value MUST be the same as the Z/IP packet being negatively
acknowledged.

If this field is set to 1 but none of the _NAck_ _flags_ field is set to 1, the Z-Wave Command was lost but
no specific reason is provided.

**(NAck** **flags)** **Waiting** **(1** **bit)**

CC:0023.02.02.12.002 This flag is a companion flag to the _NAck_ _Response_ flag. It SHOULD be inspected only if the _NAck_
_Response_ flag field is set to 1 and SHOULD be ignored otherwise.

CC:0023.02.02.11.015 This flag MUST be ignored if the _Queue_ _Full_ flag is set to 1.

CC:0023.02.02.11.016 This flag MUST be used to indicate that the destination may have a long response time. i.e. the
Z-Wave Command has not timed out yet and is pending delivery. This field MUST be encoded
according to Table 5.153.


|value|Table 5.153: Z/IP Packet::Waiting Flag encoding Description|
|---|---|
|value|Description|
|‘1’|Waiting: the preceding Z/IP Packet encapsulated Z-Wave Command is<br>not yet delivered to the destination and delivery will be attempted later<br>on|
|‘0’|Not waiting: the preceding Z/IP Packet encapsulated Z-Wave Command<br>will not be delivered later on.|



CC:0023.02.02.13.002


CC:0023.02.02.12.003


CC:0023.02.02.11.017



An ”Expected Delay” Option MAY be returned by a Z/IP Gateway, indicating how long it should take
before the final delivery acknowledgment status is known, refer to Section 5.2.13.2.1. A sending node


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1036




<!-- PAGE 1038 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


SHOULD use this information to provide better user responsiveness. A default value of 90 seconds
MUST be used by the sending node if no ”Expected delay” Option is provided.


A Z/IP ”NAck+Waiting” indication is returned for every packet that is queued up. If a sending node
triggers to queue up three Z-Wave Commands, it will receive a ”NAck+Waiting” indication after each
packet. It may be desirable to queue up three configuration commands if the intention is to perform
a few configuration changes and allow a battery node to return to sleep.


If a sending node wants to transfer larger amounts of data or commands, e.g. probing capabilities
CC:0023.02.02.12.004 or downloading a new firmware image, it is RECOMMENDED to send a single Z/IP Packet using
the More Information field to make the destination node stay awake. When a Z/IP Ack Response
indication is returned to the sending node, it can start transferring packets at a higher rate.


CC:0023.02.02.11.018 A Z/IP Gateway MUST return a ”NAck+Waiting” indication no later than 200ms after receiving an
Ack Request indication if the Z-Wave Command is still pending delivery.


CC:0023.02.02.11.019 If a message has been delayed for more than 60 seconds, an intermediate receiver, such as a Z/IP
Gateway, MUST transmit a new ”NAck+Waiting” indication every 60 seconds to let the sending node
know that it is still operational.


CC:0023.02.02.13.003 A sending node waiting for more than 90 seconds after receiving a ”NAck+Waiting” indication MAY
conclude that the Z-Wave Command is lost and retransmit a new Z/IP Packet.


CC:0023.02.02.11.01A A Z/IP Gateway issuing a ”NAck+Waiting” indication MUST subsequently issue an Ack Response
indication when the Z-Wave Command has been delivered.


CC:0023.02.02.11.01B A Z/IP Gateway MUST return a Z/IP _NAck_ _Response_ indication if the Z-Wave Command delivery
is aborted or not successful.

**(NAck** **flag)** **Queue** **Full** **(1** **bit)**

CC:0023.02.02.12.005 This flag is a companion flag to the NAck Response flag. It SHOULD be inspected only if the NAck
Response flag is set to 1 and SHOULD be ignored otherwise.

CC:0023.02.02.11.01C This flag MUST be used by a Z/IP Gateway for packets targeting battery nodes, in a busy network,
during bulk data transfers or route re-discovery.

CC:0023.02.02.13.004 This flag MAY also be returned for always listening Z-Wave destinations.


CC:0023.02.02.11.01D A sending node MUST wait for at least 10 seconds before re-transmitting a new Z/IP Packet.

CC:0023.02.02.11.01E This flag MUST be returned by a Z/IP Gateway if there is no more room in the queue system used
for delivering Commands into the Z-Wave network. This field MUST be encoded according to Table
5.154.


Table 5.154: Z/IP Packet::Queue Full Flag encoding

|value|Description|
|---|---|
|‘1’|Queue is full: the preceding Z/IP Packet Command is discarded and will<br>not be delivered to the destination|
|‘0’|Queue OK|



**(NAck** **flag)** **Option** **Error** **(1** **bit)**

CC:0023.02.02.12.006 This flag is a companion flag to the _NAck_ _Response_ flag. It should only be inspected if the _NAck_
_Response_ flag is set to 1 and SHOULD be ignored otherwise.

CC:0023.02.02.11.01F This flag MUST be set to 1 if a critical option is not recognized by the receiving node and the entire
Z/IP Packet was discarded.

CC:0023.02.02.11.020 This flag MUST NOT be set to 1 if an elective option is not recognized by the receiving node. Elective
options MUST be silently ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1037




<!-- PAGE 1039 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.155: Z/IP Packet::Option Error Flag encoding

|value|Description|
|---|---|
|‘1’|Option Error: A critical extension was not understood and the entire<br>Z/IP Packet was discarded|
|‘0’|(no error)|



CC:0023.02.02.12.007 A node setting this flag to 1 SHOULD include the offending Option in the ”NAck+OptionError”
indication returned to the originating node.


CC:0023.02.02.11.021 A node receiving a ”NAck+OptionError” indication MUST NOT process the Z/IP Packet Options in
the Header Extension field as it is only included for debugging purposes.


**Header** **extension** **Included** **(1** **bit)**

This flag is used to indicate that a _Header_ _Extension_ field is included in the Z/IP Packet. Refer to
the _Header_ _Extension_ field description below.

CC:0023.02.02.11.022 This flag MUST be encoded according to Table 5.156.


Table 5.156: Z/IP Packet::Header Extension Included Flag encod
|Table 5. ing value|.156: Z/IP Packet::Header Extension Included Flag encod- Description|
|---|---|
|value|Description<br>|
|‘1’|Header Extension feld MUST be included in the Z/IP Packet<br>|
|‘0’|Header Extension feld MUST NOT be included in the Z/IP Packet|



**Reserved**

CC:0023.02.02.11.023 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Z-Wave** **Command** **Included** **(1** **bit)**

This flag is used to indicate that a _Z-Wave_ _Command_ field is included in the Z/IP packet. Refer to
the _Z-Wave_ _Command_ field description below.

CC:0023.02.02.11.024 This flag MUST be encoded according to Table 5.157.


Table 5.157: Z/IP Packet::Z-Wave Command Included Flag encod
|Table 5. ing value|.157: Z/IP Packet::Z-Wave Command Included Flag encod- Description|
|---|---|
|value|Description<br>|
|‘1’|Z-Wave Command feld MUST be included in the Z/IP Packet<br>|
|‘0’|Z-Wave Command feld MUST NOT be included in the Z/IP Packet|



CC:0023.02.02.11.025 If a Z/IP Packet is received with payload length = 0 and the ”Z-Wave command included” bit set to
1, a receiving node MUST treat the Z/IP Packet as if the ”Z-Wave command included” bit was set
to 0.

CC:0023.02.02.11.04A If receiving a Z/IP Command with the Ack Request field set to 1 and no _Z-Wave_ _Command_ _included_,
a Z/IP Gateway MUST issue a NOP frame to the destination and return a Z/IP Packet with Ack
Response if the destination acknowledged the NOP frames.


**More** **Information** **(1** **bit)**

This flag is used to indicate the Z/IP Gateway that it should prevent a sleeping node from returning
to sleep during the next minute.



CC:0023.02.02.11.026


CC:0023.02.02.13.005



This flag MUST indicate that more Z/IP Packets with Z-Wave Commands will be subsequently
transmitted. A sending node knowing that it will be sending more commands to the destination node
MAY set this flag to 1.



CC:0023.02.02.11.027 This flag MUST be encoded according to Table 5.158.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1038




<!-- PAGE 1040 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.158: Z/IP Packet::More Information Flag encoding

|value|Description|
|---|---|
|‘1’|The Z/IP Gateway should keep the sleeping node awake|
|‘0’|The Z/IP Gateway should put the sleeping node to sleep|



**Secure** **Origin** **(1** **bit)**

This field indicates if the Z-Wave Command is to be treated securely.


CC:0023.02.02.11.028 The value 1 MUST indicate that the Z-Wave Command MUST be treated securely (i.e. it was or will
be sent using encryption in the Z-Wave network).


CC:0023.02.02.11.029 The value 0 MUST indicate that the Z-Wave Command MUST NOT be treated securely. (i.e. it was
or will be sent non-securely in the Z-Wave network)


CC:0023.02.02.11.02A A Z/IP Gateway forwarding the contents of an encrypted Z-Wave frame MUST set the Secure Origin
flag to ‘1’.


CC:0023.02.02.11.02B A Z/IP Gateway forwarding the contents of a non-encrypted Z-Wave frame MUST set the Secure
Origin flag to ‘0’.


CC:0023.02.02.11.02C
A Z/IP Gateway MUST inspect the Secure Origin flag when forwarding a Z-Wave Command contained
in a Z/IP Packet from an IP network to a Z-Wave network.


CC:0023.02.02.11.02D
A Z/IP Gateway MUST NOT use secure communication via Z-Wave if this flag is set to ‘0’ and MUST
use secure communication via Z-Wave if this flag is set to ‘1’.


**Seq** **No** **(8** **bits)**

This field is used to identify Z/IP Packet duplicates or retransmissions.

CC:0023.02.02.11.02E This field MUST carry a unique sequence number. Each sequence number MUST be generated from
an 8-bit counter that is incremented by 1 whenever a new sequence number is generated. When a
node powers up, the sequence counter MUST be initialized to a random value.


CC:0023.02.02.13.006 The counter MAY be shared with other Command Classes.


CC:0023.02.02.11.02F Retransmitted Z/IP packets MUST carry the same value as the original Z/IP Packet. A Z/IP Ack or
NAck packet MUST carry the same Seq No value as the Z/IP packet being acknowledged.


CC:0023.02.02.11.030 Multiple Z/IP Packets may be received in case of link-layer retransmissions. Z/IP Packet duplicates
MUST be ignored by a receiving node.


**Source** **End** **Point** **(7** **bits)**

This field is used to indicate the originating end point from which the Z-Wave Command was sent.

CC:0023.02.02.11.031 This field MUST be in the range 0..127.


The Source End Point value 0 represents the Root Device. Refer to the Multi Channel Command
Class for more details.


**Bit** **address** **(1** **bit)**

This field is used to advertise if the _destination_ _End_ _Point_ field is specified as a bit mask.

CC:0023.02.02.11.032 The value 0 MUST indicate that the Destination End Point field is specified as a single End Point.

CC:0023.02.02.11.033 The value 1 MUST indicate that the Destination End Point field is specified as a bit mask. Only
destination end points 1..7 are bit addressable.


CC:0023.02.02.11.034 Bit addressing MUST NOT be used if the encapsulated command is a request (requiring a reply from
the destination).


**Destination** **End** **Point** **(7** **bits)**

This field is used to indicate the destination End Point of the actual Z-Wave Command.


CC:0023.02.02.11.035


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1039




<!-- PAGE 1041 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the _Bit_ _address_ field is set to 0, this field MUST carry a single End Point identifier value in the
range 0..127.


CC:0023.02.02.11.036 The value 0 MUST represent the Root Device. Values in the range 1..127 MUST represent an actual
End Point.

CC:0023.02.02.11.037 If the Bit address field is set to 1, this field MUST use the following encoding:


      - Bit 0 in the Destination End Point indicates if End Point 1 is a destination


      - Bit 1 in the Destination End Point indicates if End Point 2 is a destination


      - …


CC:0023.02.02.11.038 The bit value 0 MUST be used to advertise that the corresponding End Point is not a destination.


The bit value 1 MUST be used to advertise that the corresponding End Point is a destination.


**Header** **Extension** **(variable)**

CC:0023.02.02.11.039 This field is used for advertising additional Z/IP Packet Options that are necessary in certain cases.
A Z/IP node MUST support and parse this field.

CC:0023.02.02.11.03A This field MUST be omitted if the _Header_ _extension_ _Included_ field is set to 0.

CC:0023.02.02.11.03B If the _Header_ _Extension_ _Included_ field is set to 1, this field MUST be formatted as follows:


Table 5.159: Header Extension Field

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Header Extension Length|Header Extension Length|Header Extension Length|Header Extension Length|Header Extension Length|Header Extension Length|Header Extension Length|Header Extension Length|
|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|Z/IP Packet Option 1, 1|
|…|…|…|…|…|…|…|…|
|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|Z/IP Packet Option P, 1|
|…|…|…|…|…|…|…|…|
|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|Z/IP Packet Option 1, N|
|…|…|…|…|…|…|…|…|
|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|Z/IP Packet Option P, N|



**Header** **Extension** **Length** **(1** **byte)**

CC:0023.02.02.11.03C This field MUST indicate the combined length in bytes of the Z/IP Header Extension Length and all
the Z/IP Packet Options included in the Z/IP Header Extension.

CC:0023.02.02.11.03D This field MUST be in the range 1..255. The length of the Header Extension field cannot exceed 255
bytes.


**Z/IP** **Packet** **Option** **(variable)**


CC:0023.02.02.11.03E Each Z/IP Packet Option MUST be treated parsed as a block using the following format:


Table 5.160: Z/IP Packet Option (variable) Field

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical|Option Type|Option Type|Option Type|Option Type|Option Type|Option Type|Option Type|
|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|
|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|Option Data 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|Option Data L (Optional)|



CC:0023.02.02.11.03F A receiving node MUST accept receiving supported options in any order.


**(Z/IP** **Packet** **Option)** **Critical** **(1** **bit)**

This field is used to indicate if the whole Z/IP Packet Command must be ignored if the option is not
recognized by the receiving node.


CC:0023.02.02.11.040


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1040




<!-- PAGE 1042 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The value 0 MUST indicate that the option is elective and a receiving node MUST ignore this option
only and continue processing the frame if the option is not recognized.


CC:0023.02.02.11.041 The value 1 MUST indicate that the option is critical and a receiving node MUST discard the entire
Z/IP Packet Command and return a Z/IP Packet Command with the Option Error flag set to 1 if
the option is not recognized.


CC:0023.02.02.11.042 An option MUST be considered as recognized even if:

      - The Option Length field is set to a greater value than expected

      - Reserved fields in the Option Data field are not set to 0.


CC:0023.02.02.11.043 An option MUST NOT be considered as recognized when:

      - The Option Type field is set to an unknown value.

      - A field value in the Option Data field value which is out of expected range or seems to be using
reserved values.


**(Z/IP** **Packet** **Option)** **Option** **Type** **(7** **bits)**

This field is used to indicate which format to use for parsing the corresponding _Option_ _Data_ field.
The list of defined Option Type is specified in Section 5.2.13.2.


CC:0023.02.02.11.044 A receiving node MUST accept supported Z/IP Packet Options in any order.


**(Z/IP** **Packet** **Option)** **Option** **Length** **(8** **bits)**

CC:0023.02.02.11.045 This field MUST indicate the length of the corresponding Option Data field in bytes.


**(Z/IP** **Packet** **Option)** **Option** **Data** **(L** **bytes)**

CC:0023.02.02.11.046 This field is used to carry the actual Option data. It MUST be parsed and interpreted using the
corresponding _Option_ _Type_ field value.

CC:0023.02.02.11.047 The size of this field in bytes MUST be according the corresponding Option Length field. This field
MUST be omitted if the corresponding Option Length field is set to 0.


**Z-Wave** **Command** **(M** **bytes)**

CC:0023.02.02.11.048 This field carries a complete Z-Wave command. This field MUST be formatted according to the
corresponding command class as defined in Section 4, Section 3, Section 2 and in this specification.


CC:0023.02.02.12.008 A sending Z/IP client SHOULD be aware that this command will be transmitted over a Z-Wave
network and therefore respect the Z-Wave Command length limitations. A Z/IP Client SHOULD
limit the length of this field to 45 bytes for non-S2 destination nodes and 117 bytes for S2 supporting
nodes.

CC:0023.02.02.11.049 This field MUST be omitted if the _Z-Wave_ _Cmd_ _Included_ field is set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1041

---

<!-- PAGE 1043 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.11** **Z/IP** **Command** **Class,** **version** **3**


The Z/IP Packet Command Class, version 3 adds the support of the Encapsulation Format Info
Option to the Z/IP Packet Option types.


**5.2.11.1** **Compatibility** **considerations**


Z/IP Packet Command Class, version 3 is backwards compatible with the Z/IP Packet Command
Class, version 2.


CC:0023.03.00.21.001 A device supporting Z/IP Packet Command Class, version 3 MUST support Z/IP Packet Command
Class, version 2.

CC:0023.03.00.21.002 All fields and commands not described in this version MUST remain unchanged from version 2.


CC:0023.03.00.21.003 A node supporting the Z/IP Packet Command Class, version 3 MUST support the Encapsulation Format Information Option and respect the requirements specified in _Encapsulation_ _Format_ _Information_
_Option_ .


**5.2.11.2** **Z/IP** **Packet** **Command**


CC:0023.03.02.11.001 The frame structure MUST remain unchanged from version 2.


**Secure** **Origin** **(1** **bit)**

This field is superseded by the Encapsulation Format Information Option.


CC:0023.03.02.11.002 A version 3 sending node MUST use the Encapsulation Format Information Option with a version 3
receiving node.

CC:0023.03.02.11.003 This field MUST be ignored by a receiving node if an Encapsulation Formation Information Z/IP
Option is included in the Z/IP Packet.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1042

---

<!-- PAGE 1044 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.12** **Z/IP** **Command** **Class,** **version** **4**


The Z/IP Packet Command Class, version 4 adds the support of a Keep Alive command in order to
prevent the closure of a Z/IP DTLS session and introduces new Z/IP Packet Options.


**5.2.12.1** **Compatibility** **considerations**


Z/IP Packet Command Class, version 4 is backwards compatible with the Z/IP Packet Command
Class, version 3.


CC:0023.04.00.21.001 A device supporting Z/IP Packet Command Class, version 4 MUST support Z/IP Packet Command
Class, version 3.

CC:0023.04.00.21.002 All fields and commands not described in this version MUST remain unchanged from version 3.


CC:0023.04.00.21.003 A node supporting the Z/IP Packet Command Class, version 4 MUST respect the requirements
specified in _Z-Wave_ _Multicast_ _Addressing_ _Option_ .


The Z/IP Keep Alive Command is introduced in this version in order to prevent a DTLS session to time
out between a Z/IP Client and server. The default DTLS timeout configured in Z/IP deployments is
60 seconds, i.e. a peer will close the DTLS connection if no command is sent or received in 60 seconds.


The Installation and Maintenance Report Option is extended with new TLVs and a new option is added
to indicate a receiving client the addressing method that has been used on the Z-Wave network.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1043




<!-- PAGE 1045 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.12.2** **Z/IP** **Keep** **Alive** **Command**


This command is used to as a Keep Alive probe for a DTLS session between two IP nodes.


CC:0023.04.03.21.001 This command SHOULD be issued at a minimum interval of 25 seconds and at a maximum interval

of 55 seconds after the last sent or received command in order to prevent session closure.


Table 5.161: Z/IP Keep Alive Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|Command Class = COMMAND_CLASS_ZIP (0x23)|
|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|Command = COMMAND_ZIP_KEEP_ALIVE (0x03)|
|Ack Request|Ack Response|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



**Reserved**

CC:0023.04.03.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Ack** **Request** **(1** **bit)**

This field is used by a sending node to request an acknowledgement for this command from a receiving
node.


CC:0023.04.03.11.002 The value 1 MUST indicate that an acknowledgement is requested.


The value 0 MUST indicate that an acknowledgement is not requested.

CC:0023.04.03.11.003 If this flag is set to 1, a receiving node MUST return a Z/IP Keep Alive Command with the _Ack_
_Response_ flag set to 1.

CC:0023.04.03.11.004 This field MUST NOT be set to 1 if the Ack Response field is set to 1.


**Ack** **Response** **(1** **bit)**

This field is used by a node to acknowledge that it received a Z/IP Keep Alive Command with the
_Ack_ _Request_ flag set to 1.


CC:0023.04.03.11.005 The value 1 MUST indicate that this command is an acknowledgement for a received Z/IP Keep Alive
Command.


The value 0 MUST indicate that this command is not an acknowledgement

CC:0023.04.03.11.006 This field MUST NOT be set to 1 if the Ack Request field is set to 1.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1044

---

<!-- PAGE 1046 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13** **Z/IP** **Command** **Class,** **version** **5**


**5.2.13.1** **Compatibility** **considerations**


Z/IP Packet Command Class, version 5 is backwards compatible with the Z/IP Packet Command
Class, version 4.


A device supporting Z/IP Packet Command Class, version 5 MUST support Z/IP Packet Command
Class, version 4.

All fields and commands not described in this version MUST remain unchanged from version 4.


**5.2.13.2** **List** **of** **defined** **Z/IP** **Packet** **Options**


The list of defined Z/IP Packet Option Types is listed in Table 52 and each type is defined in the
following subsections.


CC:0023.00.02.11.001 A sending node using a given option MUST support as a minimum the version indicated in Table 52
for the Z/IP Command Class.


Table 5.162: Z/IP Packet Option types

|Option Type|Type value|Class|Version|
|---|---|---|---|
|Expected delay|1|Elective|2|
|Installation and Maintenance Get|2|Elective|2|
|Installation and Maintenance Report|3|Elective|2|
|Encapsulation Format Information|4|Critical|3|
|Z-Wave Multicast Addressing|5|Elective|4|



CC:0023.00.02.11.002 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0023.00.02.11.003 A receiving node MUST accept supported options in any order.


**5.2.13.2.1** **Expected** **Delay** **Option**


This option is used to advertise an expected delay when issuing a Z/IP Packet command with
”NAck+Waiting” indication.


Table 5.163: Expected Delay Option

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical = 0|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|Option Type = ZIP_OPTION_EXPECTED_DELAY = 1|
|Option Length = 3|Option Length = 3|Option Length = 3|Option Length = 3|Option Length = 3|Option Length = 3|Option Length = 3|Option Length = 3|
|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|
|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|Seconds 2|
|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|Seconds 3 (LSB)|



**Critical** **(1** **bit)**

CC:0023.00.02.11.004 The Critical field MUST be set to 0.


**Option** **Type** **(7** **bits)**

CC:0023.00.02.11.005 The Option Type field MUST be set to 0x01 to indicate the Expected Delay Option.


**Option** **Length** **(8** **bits)**

CC:0023.00.02.11.006 The Option Length field MUST indicate the length of the Seconds field.


**Seconds** **(24** **bits)**


CC:0023.00.02.11.007


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1045




<!-- PAGE 1047 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Seconds field MUST indicate the expected time in seconds before issuing a new Z/IP Packet
Command with a new status.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1046




<!-- PAGE 1048 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.2** **Installation** **and** **Maintenance** **Get** **Option**


This option is used to request a receiving node to return a Z/IP Packet Command containing the
Installation and maintenance Report Option.


CC:0023.00.02.11.008 In order to trigger an Installation and Maintenance Report to be returned, a sending node MUST:


      - Add this Option in the Z/IP Packet Command


      - Add a Z-Wave Command in the Z/IP Packet Command (NOP Command Class MAY be used
if the sending node does not have any other Z-Wave Command to transmit)

      - Set the Ack Request flag to 1 in the Z/IP Packet Command


CC:0023.00.02.11.009 A receiving node MUST:


      - Return a Z/IP Packet Command containing the Installation and Maintenance Report Z/IP
Option after the transmission of the contained Z-Wave Command to the destination.


      If returned, the Installation and Maintenance Report Z/IP Option MUST advertise the statistics
associated to the Z-Wave Command transmission.


CC:0023.00.02.13.001 A receiving MAY ignore the request for an Installation and Maintenance Report if it does not support
this Option.


Table 5.164: Installation and Maintenance Get Option

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical = 0|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|Option Type = INSTALLATION_MAINTENANCE_GET = 2|
|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1047




<!-- PAGE 1049 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.3** **Installation** **and** **Maintenance** **Report** **Option**


This option is used to advertise Z-Wave transmission data about the communication between the Z/IP
Gateway and a Z-Wave device in the network.


The Installation and Maintenance Report Option is used for data relating to the transmission of
an actual frame. Statistical data may be accessed via the Network Management Installation and
Maintenance Command Class.


Table 5.165: Installation and Maintenance Report Option

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical =<br>0|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|Option Type = INSTALLATION_MAINTENANCE_REPORT = 3|
|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|Option Length|
|IME - Type 1|IME - Type 1|IME - Type 1|IME - Type 1|IME - Type 1|IME - Type 1|IME - Type 1|IME - Type 1|
|IME - Length 1|IME - Length 1|IME - Length 1|IME - Length 1|IME - Length 1|IME - Length 1|IME - Length 1|IME - Length 1|
|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|IME - Value 1, 1|
|…|…|…|…|…|…|…|…|
|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|IME - Value L, 1|
|…|…|…|…|…|…|…|…|
|IME - Type N|IME - Type N|IME - Type N|IME - Type N|IME - Type N|IME - Type N|IME - Type N|IME - Type N|
|IME - Length N|IME - Length N|IME - Length N|IME - Length N|IME - Length N|IME - Length N|IME - Length N|IME - Length N|
|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|IME - Value 1, N|
|…|…|…|…|…|…|…|…|
|IME - Value L, N|IME - Value L, N|IME - Value L, N|IME - Value L, N|IME - Value L, N|IME - Value L, N|IME - Value L, N|IME - Value L, N|



**Critical** **(1** **bit)**

CC:0023.00.02.11.00A The Critical field MUST be set to 0.


**Option** **Length** **(1** **byte)**

CC:0023.00.02.11.00B This field MUST indicate the combined length (in bytes) of the following IME-TLV fields.


IME       - Type / Length / Value (TLV) (variable)

CC:0023.00.02.11.00C This field is used to carry values advertising Z-Wave transmission statistics. Each TLV block MUST
be encoded according to one of the Types defined in Table 53 and in the following subsections.


CC:0023.00.02.11.00D A sending node using a given TLV MUST support as a minimum the version indicated in Table 53
for the Z/IP Command Class.


CC:0023.00.02.13.002 The Z/IP Gateway MAY send any combination of the IME TLVs when using this Z/IP Packet Option.


Table 5.166: Z/IP Packet::IME-Type/Length/Value encoding

|IME Type<br>-|Name|IME Length<br>-|Version|
|---|---|---|---|
|0x00|Route Changed|1 byte|2|
|0x01|Transmission Time (TT)|2 bytes|2|
|0x02|Last Working Route (LWR)|5 bytes|2|
|0x03|Incoming RSSI|5 bytes|4|
|0x04|ACK channel|1 byte|4|
|0x05|Transmit channel|1 byte|4|
|0x06|Routing scheme|1 byte|4|
|0x07|Routing attempts|1 byte|4|
|0x08|Last failed link|2 bytes|4|
|0x09|Tx Power|2 bytes|5|
|0x0A|Measured Noise Floor|2 bytes|5|
|0x0B|Outgoing RSSI|5 bytes|5|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1048




<!-- PAGE 1050 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.4** **Route** **Changed** **(3** **bytes)**


Table 5.167: Route Changed

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|IME - Type = 0x00|
|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|
|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|IME - Value = Route Changed|



**Route** **Changed** **(8** **bits)**

This field is used to indicate if the last working route was changed for the current transmission.

CC:0023.00.02.11.00E If the last working route was changed, this field MUST be set to 0x01.

If the last working route was not changed, this field MUST be set to 0x00.


**5.2.13.2.5** **Transmission** **Time** **(4** **bytes)**


Table 5.168: Transmission Time

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|IME - Type = 0x01|
|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|
|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|IME - Value = Transmission Time 1 (MSB)|
|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|IME - Value = Transmission Time 2 (LSB)|



**Transmission** **Time** **(16** **bits)**

This field is used to indicate the time it took to send the command until the reception of an Ack.
CC:0023.00.02.11.00F The value MUST be encoded using unsigned representation and MUST be specified using the ms
(milliseconds) unit.


**5.2.13.2.6** **Last** **Working** **Route** **(7** **bytes)**


Table 5.169: Last Working Route

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|IME - Type = 0x02|
|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|
|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|IME - Value = Repeater 1|
|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|IME - Value = Repeater 2|
|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|IME - Value = Repeater 3|
|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|IME - Value = Repeater 4|
|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|IME - Value = Speed|



This TLV is used to advertise the last used Working Route. If multiple Last Working Routes exist,
CC:0023.00.02.11.010 this MUST be the one used to transmit the frame.


**Repeater** **1-4** **(4** **bytes)**

This field contains the NodeID of the repeaters used for the last working route.


CC:0023.00.02.11.011 The value 0 MUST indicate that the actual repeater was not used.


Values in the range 1..232 MUST indicate an actual NodeID used as repeater.


CC:0023.00.02.11.012
The first Repeater byte set to 0 MUST indicate that no more repeaters were used for the transmission.
If the first Repeater byte is set to 0, it means that the Last Working Route (LWR) is a direct
transmission.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1049




<!-- PAGE 1051 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Speed** **(8** **bits)**

CC:0023.00.02.11.013 This field is used to advertise the transmission speed used to reach the destination node. This field
MUST be encoded according to Table 5.170.


Table 5.170: IME Speed Encoding

|Value|Protocol|Speed|
|---|---|---|
|0x01|Z-Wave|9.6 kbit/sec|
|0x02|Z-Wave|40 kbit/sec|
|0x03|Z-Wave|100 kbit/sec|
|0x04|Z-Wave Long Range|100 kbit/sec|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Incoming** **RSSI** **(7** **bytes)**


Table 5.171: Incoming RSSI

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|IME - Type = 0x03|
|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|
|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|IME - Value = RSSI hop 1|
|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|IME - Value = RSSI hop 2|
|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|IME - Value = RSSI hop 3|
|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|IME - Value = RSSI hop 4|
|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|IME - Value = RSSI hop 5|



The IME       - Values advertise the RSSI value measured in the incoming direction (back towards the
source of the message).


**RSSI** **Hop** **(5** **bytes)**


CC:0023.00.02.11.014 The RSSI values MUST be encoded as using signed representation in the dBm unit and according to
Table 5.172.

|Value (signed)|Table 5.172: RSSI Encoding Description|
|---|---|
|Value (signed)|Description|
|0x7F (127)|RSSI_NOT_AVAILABLE This value is returned for unused hops or if<br>no RSSI measurement is available.|
|0x7E (126)|RSSI_MAX_POWER_SATURATED This value is returned if the mea-<br>sured RSSI is above the maximum power.|
|0x7D (125)|RSSI_BELOW_SENSITIVITY This value is returned if the measured<br>RSSI is below the receiver’s sensitivity|
|0x7E…0xE1 (124..-31)|Reserved|
|0xE0 (-32)|-32 dBm|
|0xDF (-33)|-33 dBm|
|…|…|
|0x80 (-128)|-128 dBm|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1050




<!-- PAGE 1052 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.7** **ACK** **channel** **(3** **bytes)**


Table 5.173: ACK Channel

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|IME - Type = 0x04|
|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|
|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|IME - Value = ACK channel|



**ACK** **channel** **(8** **bits)**


This value reports the RF channel on which the ACK for this frame was received.


**5.2.13.2.8** **Transmit** **channel** **(3** **bytes)**


Table 5.174: Transmit Channel

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|IME - Type = 0x05|
|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|
|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|IME - Value = Transmit channel|



**Transmit** **channel** **(8** **bits)**


This value reports the RF channel on which the Z-Wave Command was transmitted.


**5.2.13.2.9** **Routing** **scheme** **(3** **bytes)**


Table 5.175: Routing Scheme

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|IME - Type = 0x06|
|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|
|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|IME - Value = Routing scheme|



**Routing** **scheme** **(8** **bits)**

This value reports the routing scheme that was used to find the successful route for delivering the
Z-Wave Command.


CC:0023.00.02.11.015 The Routing scheme value MUST encoded according to Table 5.176.


Table 5.176: Routing Scheme IME::Routing Scheme encoding

|Value|Description|
|---|---|
|0x00|Idle|
|0x01|Direct transmission (no routing)|
|0x02|Application static route|
|0x03|Last working route|
|0x04|Next to last working route|
|0x05|Return route or controller auto route|
|0x06|Direct resort|
|0x07|Explorer frame|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1051




<!-- PAGE 1053 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.10** **Routing** **attempts** **(3** **bytes)**


Table 5.177: Routing Attempts

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|IME - Type = 0x07|
|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|IME - Length = 1|
|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|IME - Value = Routing attempts|



**Routing** **attempts** **(8** **bits)**


This TLV reports the number of routing attempts that were performed before successfully delivering
the Z-Wave Command.


**5.2.13.2.11** **Failed** **link** **(4** **bytes)**


Table 5.178: Failed Link

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|IME - Type = 0x08|
|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|
|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|IME - Value = Failed Link Neighbor NodeID 1|
|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|IME - Value = Failed Link Neighbor NodeID 2|



**Failed** **Link** **Neighbor** **NodeID** **(16** **bits)**


This TLV is used if the transmission of the Z-Wave Command failed. The value reports the neighbor
NodeIDs of the failing link in the last attempted route.


CC:0023.00.02.12.001 If the last node failed, Failed Link Neighbor NodeID 2 SHOULD be set to 0x00.


**5.2.13.2.12** **Tx** **Power** **(2** **bytes)**


This TLV is used to report the Tx Power (in dBm) used during the transmissions with the remote
node.


Table 5.179: Tx Power

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|IME - Type = 0x09|
|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|
|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|IME - Value = Local Node Tx Power|
|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|IME - Value = Remote Node Tx Power|



**Local** **Node** **Tx** **Power** **(8** **bits)**

This field is used to indicate the Tx Power (in dBm) used for the transmission from the local node.

This field MUST be encoded as using signed representation in the dBm unit.


The value 0x7F (127) MUST indicate that the measurement is not available.


All other values MUST represent the actual Tx Power setting, in dBm.


**Remote** **Node** **Tx** **Power** **(8** **bits)**

This field is used to indicate the Tx Power (in dBm) used by the remote node for the transmission.

This field MUST be encoded as using signed representation in the dBm unit.


The value 0x7F (127) MUST indicate that the measurement is not available.


All other values MUST represent the actual Tx Power setting, in dBm.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1052




<!-- PAGE 1054 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.13** **Measured** **Noise** **Floor** **(2** **bytes)**


This TLV is used to report the Measured Noise Floor (in dBm) used during the transmissions with
the remote node.


Table 5.180: Measured Noise Floor

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|IME - Type = 0x0A|
|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|IME - Length = 2|
|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|IME - Value = Local Node Measured Noise Floor|
|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|IME - Value = Remote Node Measured Noise Floor|



**Local** **Node** **Measured** **Noise** **Floor** **(8** **bits)**

This field is used to indicate the Measured Noise Floor (in dBm) by the local node during the transmission.

This field MUST be encoded as using signed representation and MUST be encoded according to Table
5.181.

|Value (signed)|Table 5.181: Noise Floor Encoding Description|
|---|---|
|Value (signed)|Description|
|0x7F (127)|NOT_AVAILABLE. This value is returned for unused hops or if no RSSI<br>measurement is available.|
|0x7E (126)|MAX_POWER_SATURATED This value is returned if the measured<br>RSSI is above the maximum power.|
|0x7D (125)|BELOW_SENSITIVITY. This value is returned if the measurement is<br>below the receiver’s sensitivity.|
|0x7D (125)..<br>0x80<br>(-128)|This value represents the measurement in dBm|



**Remote** **Node** **Measured** **Noise** **Floor** **(8** **bits)**

This field is used to indicate the Measured Noise Floor (in dBm) by the remote node during the
transmission.

This field MUST be encoded as using signed representation and MUST be encoded according to Table
5.181.


**5.2.13.2.14** **Outgoing** **RSSI** **(7** **bytes)**


Table 5.182: Outgoing RSSI

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|IME - Type = 0x0B|
|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|IME - Length = 5|
|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|IME - Value = Outgoing RSSI hop 1|
|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|IME - Value = Outgoing RSSI hop 2|
|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|IME - Value = Outgoing RSSI hop 3|
|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|IME - Value = Outgoing RSSI hop 4|
|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|IME - Value = Outgoing RSSI hop 5|



The IME - Values advertise the RSSI value measured in the outgoing direction (from our local node
to the remote node).


**Outgoing** **RSSI** **Hop** **(5** **bytes)**


The RSSI values MUST be encoded as using signed representation in the dBm unit and according to
Table 5.172.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1053




<!-- PAGE 1055 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.15** **Encapsulation** **Format** **Information** **Option**


The Encapsulation Format Information Option is used to carry information about the Z-Wave encapsulations that were or must be used to communicate between the Z-Wave node and the sending host
(e.g. a Z/IP Gateway).


The purpose of this Option is to preserve the encapsulation between a Z-Wave node and a host (e.g.
Z/IP Gateway).


CC:0023.00.02.11.016 A Z/IP Gateway MUST use the encapsulation indicated in the Encapsulation Format Information
Option when transmitting Z/IP Commands over in a Z-Wave Network.


CC:0023.00.02.11.017 A Z/IP Gateway receiving a Z-Wave Command that must be forwarded over an IP network MUST
indicate in the Encapsulation Format Information Option what the Z-Wave encapsulation was.


CC:0023.00.02.11.018 If a Z/IP client receives this Option and the Z-Wave Command requires to return a response, the
Z/IP client MUST apply the encapsulation indicated by the Option when sending a reply.


CC:0023.00.02.13.003 A Z/IP client MAY use this Option to dictate the encapsulation format when sending unsolicited

messages.


Table 5.183: Encapsulation Format Information Option

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical = 1|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|Option Type = ENCAPSULATION_FORMAT_INFO = 4|
|Option Length = 2|Option Length = 2|Option Length = 2|Option Length = 2|Option Length = 2|Option Length = 2|Option Length = 2|Option Length = 2|
|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|Security 2 Security Class|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|CRC16|



**Critical** **(1** **bit)**

CC:0023.00.02.11.019 This field indicates that the whole frame MUST be discarded if the extension is not supported.

This field MUST be set to 1 when using the Encapsulation Format Info Option.


**Option** **Type** **(7** **bits)**

CC:0023.00.02.11.01A The Type field MUST be set to 4 for the Encapsulation Format Information Option.


**Option** **Length** **(8** **bits)**

CC:0023.00.02.11.01B The Option Length field MUST indicate the length of the Option Data fields, which is currently
defined as 2 bytes long.


**Security** **2** **Security** **Class** **(1** **byte)**

CC:0023.00.02.11.01C This Security 2 Security Class field indicates which Security 2 Security Class MUST be used for
communication with the target node.


CC:0023.00.02.11.01D A receiving node MUST replace previous information about a node’s secure capabilities with the
information contained in this field and attempt subsequent communication with the target node using
the highest security key contained in this command.

CC:0023.00.02.11.01E This field MUST be encoded as a bit field and according to Table 5.184.

|Bit set to 1|Table 5.184: Security Class Field Encoding Security 2 - Security Class|
|---|---|
|Bit set to 1|Security 2 - Security Class|
|None|NON_SECURE|
|0|S2_UNAUTHENTICATED|
|1|S2_AUTHENTICATED|
|2|S2_ACCESS_CONTROL|
|7|S0|



**CRC16** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1054




<!-- PAGE 1056 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The CRC16 field indicates whether communication with the target node use CRC16 encapsulation or
not.


CC:0023.00.02.11.01F The value 1 MUST indicate that CRC16 encapsulation is used and MUST be used for subsequent
communication with the Z-Wave node.


CC:0023.00.02.11.020 The value 0 MUST indicate that CRC16 encapsulation is not used and MUST NOT be used for
subsequent communication with the Z-Wave node.

CC:0023.00.02.11.021 The CRC16 field MUST NOT be set to 1 if the Security 2 Security Class field is different than
”NON_SECURE”


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1055




<!-- PAGE 1057 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.13.2.16** **Z-Wave** **Multicast** **Addressing** **Option**


This option is used to advertise if Multicast Addressing has been used by the sending node in the
Z-Wave network.


CC:0023.00.02.12.002 A Z/IP Client SHOULD NOT use this option when sending a Z/IP Packet Command.


CC:0023.00.02.11.022 A Z/IP Gateway supporting Z/IP Command version 4 or newer MUST use this option in a Z/IP
Packet Command if forwarding a command that has been received using Multicast addressing from a
Z-Wave node.


The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all considered multicast addressing methods.


Table 5.185: Z-Wave Multicast Addressing Option

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Critical = 0|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|Option Type = ZWAVE_MULTICAST_ADDRESSING = 5|
|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|Option Length = 0|



**Critical** **(1** **bit)**

CC:0023.00.02.11.023 The Critical field MUST be set to 0.


**Option** **Type** **(7** **bits)**

CC:0023.00.02.11.024 The Option Type field MUST be set to 0x05 to indicate the Z-Wave Multicast Addressing Option.


**Option** **Length** **(8** **bits)**

CC:0023.00.02.11.025 The Option Length field MUST indicate the length of the Option Data field.

CC:0023.00.02.11.026 No Option Data is currently defined for this option; this field MUST be set to 0 and the Option Data
field MUST be omitted.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1056