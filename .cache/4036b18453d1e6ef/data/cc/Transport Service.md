<!-- PAGE 916 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.10** **Transport** **Service** **Command** **Class,** **version** **1**


**THIS** **COMMAND** **HAS** **BEEN** **OBSOLETED**


New implementations MUST use the Transport Service Command Class version 2.

The Transport Service Command Class Version 2 redefines the frame formats used by the
command class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 915

---

<!-- PAGE 917 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.11** **Transport** **Service** **Command** **Class,** **version** **2**


The Transport Service Command Class supports the transfer of datagrams larger than the Z-Wave
frame.

The Transport Service Command Class, version 2 is defined by [20].

The following sections provide additional requirements and frame flows.


**4.2.11.1** **Compatibility** **considerations**


A node supporting the Transport Service Command Class, version 2:

CC:0055.02.00.21.001 - MUST NOT send Transport Service segments with the Payload field longer than 39 bytes.


CC:0055.02.00.21.002 - MUST accept datagrams up to 117 bytes long (3 segments of 39 bytes each).


CC:0055.02.00.23.001 - MAY accept larger datagrams.


**4.2.11.1.1** **Node** **Information** **Frame** **(NIF)**


A node supporting the Transport Service Command Class, version 2:


CC:0055.02.00.21.003 - MUST always advertise this Command Class in its NIF, regardless of the inclusion status and
security bootstrapping outcome.


CC:0055.02.00.21.004 - MUST NOT advertise this Command Class in its S0/S2 Supported Command Class list or in
the Multi Channel End Point capabilities.


**4.2.11.2** **Example** **Frame** **flows**


CC:0055.02.00.11.001 A supporting node MUST comply with the following frame flows.


**4.2.11.2.1** **As** **things** **should** **always** **work** **-** **the** **default** **case**


      - Node A initiates a 117-byte frame transmission to Node B


**–** Node A sends FirstSegment(datagram size = 117, Session ID = 10, Payload = bytes 1..39)


**–**
Node B receives the FirstSegment with valid Transport Service FCS (16-bit checksum) and
valid MPDU FCS (8 or 16 bits checksum, depending on transmission speed)


∗Node B creates a tracking list for the datagram; bytes 1..39 are marked as received


∗Node B starts segment rx timer

**–** Node A sends SubsequentSegment(datagram size = 117, datagram offset = 39, Session ID
= 10, Payload = bytes 40..78)


**–** Node B receives the SubsequentSegment with valid Transport Service and MPDU FCS


∗Node B updates the tracking list for the datagram; bytes 40..78 are marked as received


∗Node B (re-)starts segment rx timer

**–** Node A sends SubsequentSegment(datagram size = 117, datagram offset = 78, Session ID
= 10, Payload = bytes 79..117)


∗Node A starts a segment_complete tx timer


**–** Node B receives SubsequentSegment with valid Transport Service and MPDU FCS


∗Node B updates the tracking list for the datagram; bytes 79..117 are marked as received,
indicating that this was the last segment


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 916




<!-- PAGE 918 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


∗Node B checks the tracking list for missing segments; none found


 - Node B sends SegmentComplete(Session ID = 10)


 Node A receives SegmentComplete(Session ID = 10) with valid MPDU FCS (8 or 16 bits checksum, depending on transmission speed)


**4.2.11.2.2** **Losing** **first** **segment** **of** **a** **long** **message**


 - Node A initiates a 117-byte frame transmission to Node B:


**–**
Node A sends FirstSegment(datagram size = 117, Session ID = 10, Payload = bytes 1..39).


**–** Node B receives FirstSegment invalid Transport Service or MPDU FCS (the command is
ignored).

**–** Node A sends SubsequentSegment(datagram offset = 39)


**–** Node B receives the SubsequentSegment correctly (valid Transport Service and MPDU
FCS)


**–** Node B sends SegmentWait(Pending segments=0) because no session is open.


**–** Node A waits and restarts the transmission from the FirstSegment.


**4.2.11.2.3** **Losing** **subsequent** **segment**


 - Node A initiates a 117-byte frame transmission to Node B


**–** Node A sends FirstSegment(datagram size = 117, Session ID = 10, Payload = bytes 1..39)


**–** Node B receives the FirstSegment correctly


∗Node B creates a tracking list for the datagram; bytes 1..39 are marked as received


∗Node B starts segment rx timer

**–** Node A sends SubsequentSegment(datagram offset = 39)


**–** Node B receives SubsequentSegment with invalid Transport Service or MPDU FCS. (the
command is ignored)

**–** Node A sends SubsequentSegment(datagram offset = 78)


∗Node A starts segment_complete tx timer


**–** Node B receives SubsequentSegment correctly


∗Node B updates the tracking list for the datagram, indicating that this was the last
segment


∗Node B checks tracking list for the datagram; bytes 40..78 are missing

**–** Node B sends SegmentRequest(datagram offset = 39)

**–** Node A receives SegmentRequest(datagram offset = 39) correctly

**–** Node A send SubsequentSegment(datagram offset = 39)

**–** Node B receives SubsequentSegment(datagram offset = 39) correctly


∗Node B updates the tracking list for the datagram


∗Node B checks the tracking list for missing segments; none found


∗Node B clears segment rx timer


 - Node B sends SegmentComplete(Session ID = 10)


 - Node A receives SegmentComplete(Session ID = 10) correctly


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 917




<!-- PAGE 919 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**4.2.11.2.4** **Losing** **last** **segment**


 - Node A initiates a 117-byte frame transmission to Node B


**–** Node A sends FirstSegment(datagram size = 117, Session ID = 10, Payload = bytes 1..39)


**–** Node B receives FirstSegment


∗Node B creates a tracking list for the datagram; bytes 1..39 are marked as received


∗Node B starts segment rx timer

**–** Node A sends SubsequentSegment(datagram offset = 39)


**–** Node B receives SubsequentSegment correctly


∗Node B updates the tracking list for the datagram; bytes 40..78 are marked as received


∗Node B (re-)starts segment rx timer

**–** Node A sends (the last) SubsequentSegment(datagram offset = 78)


∗Node A starts segment_complete tx timer


**–** Node B receives SubsequentSegment with invalid Transport Service or MPDU FCS. (the
command is ignored)


**–** Node B segment rx timer times out.


∗Node B checks tracking list for the datagram; bytes 79..117 are missing

**–** Node B sends SegmentRequest(datagram offset = 78)


∗Node B starts a segment rx timer to wait for the SubsequentSegment frame


∗If the segment rx timer times out, Node B bails out: discard all received segments and
return to idle (e.g. sender may be down or sleeping)

**–** Node A receives SegmentRequest(datagram offset = 78)

**–** Node A sends SubsequentSegment(datagram offset = 78)

**–** Node B receives SubsequentSegment(datagram offset = 78)


∗Node B updates the tracking list for the datagram; bytes 79..117 are marked as received


∗Node B checks tracking list for missing segments; none found


**–** Node B sends SegmentComplete(Session ID = 10)


**–** Node A receives SegmentComplete(Session ID = 10) correctly


∗Node A stops the segment_complete tx timer


**4.2.11.2.5** **Losing** **SegmentComplete**


 - Node A initiates a 117-byte frame transmission to Node B


**–** Node A sends FirstSegment(datagram size = 117, Session ID = 10, Payload = bytes 1..39)


**–** Node B receives FirstSegment correctly


∗Node B creates tracking list for the datagram; bytes 1..39 are marked as received


∗Node B starts a segment rx timer

**–** Node A sends SubsequentSegment(datagram offset = 39)

**–** Node B receives SubsequentSegment(datagram offset = 39) correctly


∗Node B updates the tracking list for the datagram; bytes 40..78 are marked as received


∗Node B (re-)starts segment rx timer

**–** Node A sends SubsequentSegment(datagram offset = 78)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 918




<!-- PAGE 920 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


∗Node A starts a segment_complete timer

**–** Node B receives SubsequentSegment(datagram offset = 78) correctly.


∗Node B updates the tracking list for the datagram; bytes 79..117 are marked as received,
indicating that this was the last segment


∗Node B checks tracking list for missing segments; none found


**–** Node B sends SegmentComplete(Session ID = 10)


**–** Node A receives SegmentComplete with an invalid MPDU FCS. (the command is ignored)


**–** Node A segment_complete tx timer times out

∗Node A sends SubsequentSegment(datagram offset = 78) one more time


     - Node A starts a segment_complete timer again.


     - If the segment_complete timer times out, Node A bails out: return “Error” callback
to calling application

**–** Node B receives SubsequentSegment(datagram offset = 78) correctly


∗Node B updates the tracking list for the datagram; bytes 79..117 are marked as received,
indicating that this was the last segment


∗Node B checks tracking list for missing segments; none found


**–** Node B sends SegmentComplete(Session ID = 10) once more


**–** Node A receives SegmentComplete(Session ID = 10) correctly


**–** Node A stops the segment_complete timer


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 919




<!-- PAGE 921 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **5 Network-Protocol Command Classes** **5.1 Network-Protocol Command Class Overview**


General Command Class overview and rules are described in _Application_ _Command_ _Classes_ and are
valid for the Command Classes presented in this document.


No additional considerations apply for the Network-Protocol Command Classes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 920




<!-- PAGE 922 -->

CC:0074.01.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **5.2 Network-Protocol Command Class** **Definitions**


**5.2.1** **Inclusion** **Controller** **Command** **Class,** **version** **1**


The Inclusion Controller Command Class is used after a node’s network inclusion between the SIS

and an inclusion controller to inform each other of the remaining setup required for the included node.

Examples of such setup operations could be Z-Wave Plus Lifeline configuration or Security 2 bootstrapping.


If the S2 bootstrapping is handled by a SIS after the Z-Wave network inclusion has been handled by
an inclusion controller, the joining node will detect two different NodeIDs for Network inclusion and
S2 bootstrapping. The NodeID of the including controller is not relevant for the authentication of the
joining node. Therefore, the joining node MUST NOT abort the S2 bootstrapping in response to a
changing NodeID.



CC:0074.01.00.11.002 The SIS, inclusion controller and joining node MUST follow the frame flow illustrated in Figure 1.


Figure 5.1: Inclusion Controller Frame Flow


CC:0074.01.00.11.003 The SIS, inclusion controller and joining node MUST comply with the following steps:


1. Inclusion Controller, C, performs network inclusion of Joining Node, B.



CC:0074.01.00.11.004


CC:0074.01.00.11.005


CC:0074.01.00.11.006


CC:0074.01.00.11.007


CC:0074.01.00.11.008



2. Inclusion Controller, C, MUST send Inclusion Controller Initiate to SIS, A, immediately following the network inclusion.


3. SIS, A, MUST request a Node Info Frame from Joining Node, B.


4. Joining Node, B, MUST respond to SIS, A, with a Node Info Frame


**Option** **1** : If Joining Node B supports S2:


1. SIS, A, MUST start the Security 2 bootstrapping as described in _Security_ _2_ _(S2)_ _Command_
_Class,_ _version_ _1_, including user dialogs.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 921




<!-- PAGE 923 -->

CC:0074.01.00.11.00A


CC:0074.01.00.11.00B


CC:0074.01.00.12.001


CC:0074.01.00.11.009


CC:0074.01.00.12.002



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


2. Joining Node, B, MUST accept being S2 bootstrapped by the SIS


**Option** **2** : If Joining Node, B does not support S2 and supports S0


7. If SIS, A wants S0 bootstrapping performed for Joining Node, B, it will send an Inclusion
Controller Initiate(S0_INCLUSION) to Inclusion Controller, C


8. Inclusion Controller, C MUST perform S0 bootstrapping if it has the S0 network key after
receiving Inclusion Controller Initiate(S0_INCLUSION)


9. Inclusion Controller, C MUST return an Inclusion Controller Complete to SIS, A to indicate if
S0 bootstrapping attempt took place and if it was successful.


Following the Security bootstrapping, regardless whether it failed, successful or was not applicable:


10. SIS, A, SHOULD perform any probing needed of the Joining Node, B.


11. SIS, A, MUST send an Inclusion Controller Complete Command to the Inclusion Controller, C.


12. Inclusion Controller, C, SHOULD perform any probing needed of the Joining Node, B.


**5.2.1.1** **Compatibility** **considerations**


**5.2.1.1.1** **Node** **information** **frame** **(NIF)**



CC:0074.01.00.21.002 A supporting node MUST always advertise the Inclusion Controller Command Class in its NIF,
regardless of the security bootstrapping outcome when having the SIS or Inclusion Controller role.


CC:0074.01.00.23.001 A supporting node MAY keep or remove the Inclusion Controller Command Class in/from its NIF if
it has the primary or secondary controller role.


**5.2.1.1.2** **Legacy** **controllers**


If an Inclusion Controller that does not support the Inclusion Controller Command Class includes a
new node in a network, the SIS will never receive an Inclusion Controller Initiate Command. If no
Initiate Command has been received approximately 10 seconds after a new node has been added to a
network, the SIS SHOULD start interviewing the newly included node (step 10 above).


CC:0074.01.00.22.001

If an Inclusion Controller includes a node and the SIS does not support the Inclusion Controller
CC:0074.01.00.21.003 Command Class, the Inclusion Controller MUST perform S0 bootstrapping immediately after inclusion
if applicable.


**5.2.1.2** **Inclusion** **controller** **initiate** **command**


This command is used to ask a receiving node to perform specific steps in the inclusion/bootstrapping

process.



CC:0074.01.01.13.001


CC:0074.01.01.11.001


CC:0074.01.01.11.005



The initiate command asks the controller to perform a specific step of the inclusion process. The
Inclusion Controller Initiate Command is first sent from an inclusion controller to the SIS, then the
SIS MAY choose to perform the rest of the inclusion by itself or it MAY ask the inclusion controller
to perform one or more of the inclusion steps.


This command MUST be sent through highest common Security Class of the SIS and Inclusion
Controller, if no common Security Class exists, non-secure is allowed. Inclusion Controllers MUST
send this command following a successful network inclusion. It also means that if the SIS receives this
command at a less-secure than the highest common Security class, it MUST ignore this command.
E.g. Non-secure Initiate Commands MUST be ignored by the SIS, unless the SIS has a record of
including the Inclusion Controller non-securely.



CC:0074.01.01.11.002 This command MUST NOT be issued via multicast addressing. A receiving node MUST NOT return
a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the
broadcast NodeID and the Multi Channel multi-End Point destination are all considered multicast

addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 922




<!-- PAGE 924 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.1: Inclusion Controller Initiate Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|
|Command = INITIATE|Command = INITIATE|Command = INITIATE|Command = INITIATE|Command = INITIATE|Command = INITIATE|Command = INITIATE|Command = INITIATE|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|
|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|



**Node** **ID**

CC:0074.01.01.11.003 This field is used to indicate the NodeID of the node being included. The receiving node MUST
perform the steps on the NodeID indicated by this field


**Step** **ID**

CC:0074.01.01.11.004 This field is used to indicate which step is to be performed on the specified. The field MUST comply
with :Table 5.2



Table 5.2: Inclusion Controller Initiate::Step ID encoding










|Value|i<br>Identifer|Description|
|---|---|---|
|0x01|PROXY_IN-<br>CLUSION|This Value MUST be used only when:<br>• The sending node is the inclusion controller<br>• The receiving node is the SIS<br>This Value is used to indicate the SIS that it MUST take<br>over the node inclusion and perform S2 bootstrapping if<br>releveant.<br>The SIS MUST return an Inclusion Controller Complete<br>Command when the step has been completed.<br>The SIS MAY ask the inclusion controller to perform some<br>of the steps by itself before returning an Inclusion Con-<br>troller Complete Command.|
|0x02|S0_INCLUSION|This value MUST be used only when:<br>• The sending node is the SIS<br>• The receiving node is the inclusion controller<br>This value is used to indicate to the inclusion controller<br>that it MUST perform S0 bootstrapping.<br>The inclusion controller MUST reply with an Inclusion<br>Controller Complete Command when the S0 bootstrap-<br>ping has been performed (or attempted).|
|0x03|PROXY_IN-<br>CLUSION_RE-<br>PLACE|This value MUST be used only when:<br>• The sending node is the inclusion controller<br>• The receiving node is the SIS<br>This value is identical to PROXY_INCLUSION but is<br>used in case the newly included node has replaced a failed<br>node.<br>This value is used to indicate the SIS that it MUST take<br>over the node inclusion and perform S2 bootstrapping if<br>relevant.<br>The SIS MUST return an Inclusion Controller Complete<br>Command when the step has been completed.<br>The SIS MAY ask the inclusion controller to perform some<br>of the steps by itself before returning an Inclusion Con-<br>troller Complete Command.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 923




<!-- PAGE 925 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.1.3** **Inclusion** **controller** **complete** **command**


CC:0074.01.02.11.001 This command MUST be sent after a controller has completed the requested inclusion steps.


CC:0074.01.02.11.002 This command MUST be sent using the highest common Security Class of the SIS and Inclusion
Controller. If no common Security Class exists, non-secure transmission is allowed.


CC:0074.01.02.11.003 An inclusion controller MUST perform optional node interview after receiving a Inclusion Controller

CC:0074.01.02.11.004 Complete Command with Step ID, PROXY_INCLUSION. A SIS MUST do its device probe before
sending the COMPLETE command with step ID PROXY_INCLUSION.


Table 5.3: Inclusion Controller Complete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|Command Class = COMMAND_CLASS_INCLUSION_CONTROLLER|
|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|Command = COMPLETE|
|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|Step ID|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Step** **ID**

This field is used to indicate the step that has been completed.


CC:0074.01.02.11.005
A sending node MUST set this field to the same value as the last received Inclusion Controller Initiate
Command.


**Status**

CC:0074.01.02.11.006 This field is used to indicate the status of the advertised Step ID. It MUST comply with Table 5.4


Table 5.4: Inclusion Controller Complete::Status encoding

|Value|i<br>Status CODE identifer|Description|
|---|---|---|
|0x01|STEP_OK|The performed step was completed without error.|
|0x02|STEP_USER_RE-<br>JECTED|The step was rejected by user|
|0x03|STEP_FAILED|The step failed, because of a communication or protocol<br>error.|
|0x04|STEP_NOT_SUP-<br>PORTED|The step failed, because it Is not supported by the sending<br>node.|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 924




<!-- PAGE 926 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.2** **IP** **Configuration** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** THIS COMMAND CLASS HAS BEEN OBSOLETED New implementations MUST
NOT use the IP configuration Command Class. Refer to the Z/IP and Network management
Command Classes.


The IP Configuration Command Class is used to configure network identifiers for IPV4 devices. The
intended use of the command class is illustrated in the figure below.


Figure 5.2: Configuration of network identifiers for IPV4 devices


In the figure the Z-Wave Remote to the left, sends an IP Configuration Command to the Z-Wave
enabled IP device, telling it to acquire its configuration using DHCP. The Z-Wave enabled IP device
will now perform a standard DHCP IP request to the DHCP server over an IP based network.

Another example might be where the Z-Wave Remote statically configures the Z-Wave enabled IP
device with fixed IP, subnet, DNS etc. by sending an IP Configuration Command.


Note that this class is only intended for IPV4 and not IPV6 support.


**5.2.2.1** **IP** **configuration** **set** **command**


The IP Configuration Set Command used to configure IPV4 settings in a device.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 925




<!-- PAGE 927 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.5: IP Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|
|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|Command = IP_CONFIGURATION_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Auto IP|Auto DNS|
|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|
|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|
|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|
|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|
|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|
|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|
|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|
|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|
|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|
|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|
|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|
|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|
|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|
|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|
|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|
|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|
|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|
|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|
|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|
|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Auto** **IP** (1bit)

If Auto IP bit is set, the following fields are ignored: IP Address, Subnet Mask, and Gateway. And
are allocated by DHCP or BOOTP instead.


**Auto** **DNS** (1bit)


The Auto DNS if set indicates to ignore DNS1 and DNS2 and allocate DNS by DHCP instead. Note
that some devices might not support Auto DNS without Auto IP set.


**IP** **Address** (32 bit)

The IP Address indicates the static IP address of the device itself. The first byte is the most significant
byte.


**Subnet** **mask** (32 bits)

The Subnet Mask determines the portion of the IP address that represents the subnet. The first byte
is the most significant byte.


**Gateway** (32 bits)


The Gateway indicates the default gateway that serves as an access point to another network. The
first byte is the most significant byte.


**DNS1** (32 bits)


The DNS1 allows the use of domain name system (DNS) server names instead of using numerical IP
addresses for management packet routing. In case the device will not need DNS, and SHOULD NOT
query it from DHCP then leave field as all zeroes. The first byte is the most significant byte.


**DNS2** (32 bits)


The DNS2 provides a secondary DNS server name. In case only one DNS server is available or the
device will not need DNS then leave field as all zeroes. The first byte is the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 926




<!-- PAGE 928 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.2.2** **IP** **configuration** **get** **command**


The IP Configuration Get Command is used to request the IPV4 settings in a device.

The IP Configuration Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing. A receiving node MUST NOT return
a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the
broadcast NodeID and the Multi Channel multi-End Point destination are all considered multicast

addressing methods.


Table 5.6: IP Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|
|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|Command = IP_CONFIGURATION_GET|



**5.2.2.3** **IP** **configuration** **report** **command**


The IP Configuration Report Command used to return IPV4 settings in a device.


Table 5.7: IP Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|
|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|Command = IP_CONFIGURATION_REPORT|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Auto IP|Auto DNS|
|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|IP Address 1|
|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|IP Address 2|
|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|IP Address 3|
|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|IP Address 4|
|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|Subnet Mask 1|
|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|Subnet Mask 2|
|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|Subnet Mask 3|
|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|Subnet Mask 4|
|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|Gateway 1|
|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|Gateway 2|
|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|Gateway 3|
|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|Gateway 4|
|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|DNS1 1|
|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|DNS1 2|
|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|DNS1 3|
|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|DNS1 4|
|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|DNS2 1|
|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|DNS2 2|
|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|DNS2 3|
|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|DNS2 4|
|LeaseTime 1|LeaseTime 1|LeaseTime 1|LeaseTime 1|LeaseTime 1|LeaseTime 1|LeaseTime 1|LeaseTime 1|
|LeaseTime 2|LeaseTime 2|LeaseTime 2|LeaseTime 2|LeaseTime 2|LeaseTime 2|LeaseTime 2|LeaseTime 2|
|LeaseTime 3|LeaseTime 3|LeaseTime 3|LeaseTime 3|LeaseTime 3|LeaseTime 3|LeaseTime 3|LeaseTime 3|
|LeaseTime 4|LeaseTime 4|LeaseTime 4|LeaseTime 4|LeaseTime 4|LeaseTime 4|LeaseTime 4|LeaseTime 4|



Refer to explanation of parameters in IP Configuration Set Command description.


**Lease** **Time** (32 bits)

The lease time specifies the time the IP address has been granted, if Auto IP is being used (in seconds).
If the device does not know its lease period it MUST return 0 for the lease time fields.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 927




<!-- PAGE 929 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.2.4** **IP** **configuration** **DHCP** **release** **command**


The IP Configuration DHCP Release Command used to release the DHCP lease.


Table 5.8: IP Configuration DHCP Release Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|
|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|Command = IP_CONFIGURATION_RELEASE|



**5.2.2.5** **IP** **configuration** **DHCP** **renew** **command**


The IP Configuration DHCP Renew Command used to force the renewal of the DHCP lease.


Table 5.9: IP Configuration DHCP Renew Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|Command Class = COMMAND_CLASS_IP_CONFIGURATION|
|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|Command = IP_CONFIGURATION_RENEW|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 928




<!-- PAGE 930 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.3** **Mailbox** **Command** **Class,** **version** **1**


The Mailbox Command Class is intended for IP based gateway deployments with distributed mailbox
resources. One example is a constrained gateway device which is offloaded by another IP host with
sufficient memory to host the Mailbox Service. The Mailbox Service may be hosted by a LAN host
or an Internet server.


The Mailbox Command Class allows any mailbox capable device to either make itself into a Mailbox
Service, or utilize another Mailbox Service in the network.


**5.2.3.1** **Mailbox** **framework**


The Mailbox Command Class describes a framework that consists of two specific Mailbox Modes
described below:


1. Mailbox Proxy, which forwards mailbox requests to a Mailbox Service.


2. Mailbox Service, which accepts the forwarded mailbox requests and stores them until the designated recipient announces that it is awake.


A mailbox device MAY support one or both of the two Mailbox Modes. However, a mailbox device
MUST NOT take both Mailbox Modes in a network.

Before configuring Mailbox Proxy forwarding, a configuring node MUST ensure that the forwarding
and receiving devices support their respective required modes. The information can be found using
the Mailbox Configuration Get Command and Mailbox Configuration Report Command.


**5.2.3.1.1** **Mailbox** **proxy**


The Mailbox Proxy device forwards all received frames that are destined for a non-listening node to
the configured Mailbox Service. Before forwarding the frame, it MUST be attempted to send the
frame to the node first as it may be awake following a manual activation or inclusion. If the Mailbox
Proxy can deliver the frame to the non-listening node, the Mailbox Proxy MUST NOT forward the
frame to the Mailbox Service.


The Mailbox Proxy MUST support the Wake Up Command Class.


**5.2.3.1.2** **Mailbox** **service**


The Mailbox Service serves as a conventional mailbox, with the addition that it may receive forwarded
frames from a Mailbox Proxy. A Mailbox Service may have a finite mailbox queue capacity, which is
reported in the Mailbox Configuration Report. The Mailbox Service MUST NOT communicate with
a Z/IP client directly, since it may not be able to route messages to the client.


**5.2.3.1.3** **Frame** **flow**


Figure 5.3 illustrates the communication between a Z/IP Client (1) attempting communication to a
non-listening node (4). The communication is passing through the Mailbox Proxy (2) which initially
will attempt direct communication with (4). If failing to reach (4), the frame will be forwarded to the
Mailbox Service (3) using the Mailbox Queue Command with Push Operation.


Following the Mailbox Queue push, the Mailbox Service will send a Mailbox Queue Command with
Waiting Operation to the proxy, piggybacking the original UDP command on the message. The Proxy
will build a ”NACK Waiting” Z/IP Command targeted for the Z/IP node, based on the piggy backed
message from the Proxy Service. The Proxy Service MUST also append the Expected Delay header
extension to the ”NACK Waiting” Z/IP Command. This step MUST be repeated every 60s seconds
as long as the message is in the mailbox.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 929




<!-- PAGE 931 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Upon wake-up, the non-listening node (4) will transmit a Wake Up Notification to the Mailbox Proxy
(2), which must be configured using the Wake Up Command Class. Whenever the Mailbox Proxy (2)
receives a Wake Up Notification, the notification will be forwarded as a Z/IP Packet to the Mailbox
Service (4). The Mailbox Service inspects the queue to see if there are any frames for (4) and responds
with either an empty Mailbox Queue Command Pop operation with ”Last” bit set to 1 or any frames
that may be in queue, finishing with the last frame having ”Last” bit set to 1.


Mailbox Proxy (2) receives the Mailbox Queue Pop frame on which it performs a Virtual Node Rewrite
to match the original sender of the UDP frame of the Mailbox Queue Pop command. The frame is
sent from the virtual node to (4) followed by a ”Wake Up No More Information” Command. Any
eventual reports will be replied to the virtual node that forwards them to (1). The proxy MUST send
a Mailbox Queue Command with ACK operation to the Proxy Service when it has delivered the frame
and potentially the ”No more information”


Figure 5.3: Mailbox Frame Flow


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 930




<!-- PAGE 932 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.3.2** **Mailbox** **configuration** **get** **command**


The Mailbox Configuration Get Command is used to request the Mailbox configuration from a supporting device.

The Mailbox Configuration Report command MUST be returned in response to a Mailbox Configuration Get command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.10: Mailbox Configuration Get Comand

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|Command = MAILBOX_CONFIGURATION_GET|



**5.2.3.3** **Mailbox** **configuration** **set** **command**


Table 5.11: Mailbox Configuration Set Comand

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|Command = MAILBOX_CONFIGURATION_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Mode|Mode|Mode|
|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|
|…|…|…|…|…|…|…|…|
|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|
|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|
|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|



**Reserved** (5 bits)

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Mode** (3 bits)

The Mode field is used to advertise the Mailbox mode to be configured in the node. This field MUST
be encoded according to Table 5.12.

|Value|Table 5.12: Mailbox Configuration Set::Mode encoding Description|
|---|---|
|**Value**|**Description**|
|0x00|Disable Mailbox Service<br>Disable Mailbox Proxy forwarding|
|0x01|Enable Mailbox Service|
|0x02|Enable Mailbox Proxy forwarding|



**Forwarding** **Destination** **Ipv6** **Address** (16 bytes)

If the Mailbox Proxy Forwarding is enabled in the Mode field, the Forwarding Destination Ipv6
Address field MUST specify the Forwarding Destination Ipv6 Address. The field MUST specify an Ipv6
formatted address of the Mailbox Service to receive forwarded mailbox packages. If the Forwarding
Destination is identified by an Ipv4 address this field MUST be formatted as an Ipv4-mapped Ipv6
address RFC 4291.

If the Mailbox Proxy Forwarding is not enabled in the Mode field, the Forwarding Destination Ipv6
Address MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**UDP** **Port** **Number** (2 bytes)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 931




<!-- PAGE 933 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field indicates the UDP Port number of the Mailbox Service running at the Forwarding Destination.

If the Mailbox Proxy Forwarding is not enabled in the Mode field, this field MUST be set to 0 by a
sending node and MUST be ignored by a receiving node.


**5.2.3.4** **Mailbox** **configuration** **report** **command**


Table 5.13: Mailbox Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|Command = MAILBOX_CONFIGURATION_REPORT|
|Reserved|Reserved|Reserved|Supported Modes|Supported Modes|Mode|Mode|Mode|
|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|Mailbox Capacity – Byte 1|
|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|Mailbox Capacity – Byte 2|
|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|Forwarding Destination Ipv6 Address – Byte 1|
|…|…|…|…|…|…|…|…|
|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|Forwarding Destination Ipv6 Address – Byte 16|
|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|UDP Port Number – Byte 1|
|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|UDP Port Number – Byte 2|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Supported** **Modes** (2 bits)

The Supported Modes bit field is used to advertise the functionalities supported by the node. This
field MUST be encoded according to Table 5.14


Table 5.14: Mailbox Configuration Report::Supported Modes encoding

|Value|Description|
|---|---|
|0x01|Mailbox Service supported|
|0x02|Mailbox Proxy supported|



**Mode** (3 bits)


Refer to Section 5.2.3.3.


**Mailbox** **Capacity** (2 bytes)

This field advertises the number of frames (at a maximum of 1280 bytes per frame) that may be stored
in the mailbox while waiting for a Wake Up Notification.


A value of 0 MUST indicate that the mailbox will only support mailbox forwarding to another Mailbox
Service.

A value of 0xFFFF MUST indicate that the mailbox in effect have no storage limitation.


**Forwarding** **Destination** **Ipv6** **Address** (16 bytes)


Refer to Section 5.2.3.3.


**UDP** **Port** **Number** (2 bytes)


Refer to Section 5.2.3.3.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 932




<!-- PAGE 934 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.3.5** **Mailbox** **queue** **command**


The Mailbox Queue Command is a container for various operations between a mailbox proxy and a
Mailbox Service.


Table 5.15: Mailbox Queue Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|Command = MAILBOX_QUEUE|
|Reserved|Reserved|Reserved|Reserved|Last|Operation|Operation|Operation|
|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|
|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|Mailbox Entry – Byte 1|
|…|…|…|…|…|…|…|…|
|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|Mailbox Entry – Byte N|



**Reserved** (6 Bit)

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Last** (1 bit)

The Last field is used to indicate if the current mailbox frame is the last in the queue for the specific
device. The Last bit only applies when the ”Pop” Operation is used.


The value 1 MUST indicate that the frame is the last on the queue.


The value 0 MUST indicate that more frames will follow.


**Operation** (3 bits)

The encoding of the Operation field MUST be according to Table 5.16.

|Value|Table 5.16: Mailbox Queue::Operation Description|
|---|---|
|**Value**|**Description**|
|0x00|Push.<br>Queue a message from the proxy to the Mailbox Service|
|0x01|Pop.<br>Dequeue a message from the Mailbox Service to the Mailbox Proxy for delivery<br>on the PAN|
|0x02|Waiting.<br>Service->Proxy: send waiting messages to the client.|
|0x03|Ping.<br>Service->Proxy: send UDP ping messages to the client.|
|0x04|ACK.<br>Proxy->Service: Frame has been delivered.<br>Service->Proxy: Frame has been queued.|
|0x05|NACK.<br>Proxy->Service: Frame was not queued.<br>Wait for ACK before attempting<br>queuing.<br>Service->Proxy: Node is not responding. Keep in queue.|
|0x06|Queue Full.<br>Proxy->Service: The capacity of the Mailbox Service has been reached. Wait<br>until queue has been emptied.|



All other values are reserved and MUST NOT be used by a sending node.


Reserved values MUST be ignored by a receiving node.


**Queue** **Handle** (8 bits)

The Queue Handle field is used to identify the queue this message belongs to. A service uses this
handle with the source IP of the MAILBOX_QUEUE message to identify the queue to which a


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 933




<!-- PAGE 935 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


message belongs to.


**Mailbox** **Entry** (N Bytes)

The Mailbox Entry field contains the entire received UDP Package. Including, ZIP headers and
Z-Wave Payload.


To avoid duplicate entries, the Mailbox Service MUST maintain a list of CRC16 checksums for each
mailbox entry. All mailbox entries MUST be unique, if a matching CRC16 exists for an incoming
package, the incoming package MUST be discarded.


When WAITING timer elapses the mailbox MUST send a WAITING message to all clients that has
posted entries to the mailbox.


**5.2.3.6** **Mailbox** **wake** **up** **notification** **command**


This command allows a mailbox proxy resource to notify a Mailbox Service resource that a wake up
device is currently awake.


A Mailbox Proxy resource MAY send this command to a Mailbox Service resource.


A Mailbox Service resource MUST NOT send this command to a mailbox proxy resource.


Table 5.17: Mailbox Wake Up Notification Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|Command = MAILBOX_WAKEUP_NOTIFICATION|
|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|



**Queue** **Handle** (8 bits)

This field is used to specify the actual queue handle to send notification to.


**5.2.3.7** **Mailbox** **failing** **node** **command**


This command allows a mailbox proxy resource to notify a Mailbox Service resource that a wake up
device is no longer available.


A Mailbox Proxy resource MAY send this command to a Mailbox Service resource.


A Mailbox Service resource MUST NOT send this command to a mailbox proxy resource.


Table 5.18: Mailbox Failing Node Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|Command Class = COMMAND_CLASS_MAILBOX|
|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|Command = MAILBOX_NODE_FAILING|
|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|Queue Handle|



**Queue** **Handle** (8 bits)

This field is used to specify the actual queue.


A receiving Mailbox Service resource MUST discard all state information and enqueued messages for
the actual queue.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 934




<!-- PAGE 936 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.3.8** **Frame** **flow** **diagrams** **Examples**


Figure 5.4: Mailbox proxy queue full frame flow


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 935




<!-- PAGE 937 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.5: Normal frame flow


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 936




<!-- PAGE 938 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.6: Z/IP Client goes offline and stops replying to UDP ping


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 937




<!-- PAGE 939 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.7: Sleeping node misses 2 Wake Up intervals and proxy tells service to flush queue


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 938




<!-- PAGE 940 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.8: Mailbox Service is offline


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 939




<!-- PAGE 941 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.4** **Mailbox** **Command** **Class,** **version** **2**


The Mailbox Command Class, version 2 introduces a better handling of Wake Up periods for Wake
Up nodes.


Z/IP Clients are partly responsible for issuing controlling commands to supporting nodes and conduct
the minimum required interview for each Command Class of a supporting node. A Z/IP Gateway
supporting the Mailbox Command Class, version 2 indicates to the Z/IP Client that the Wake Up
Command Class minimum interview will be fully conducted by the Z/IP Gateway and the Z/IP Client
MUST NOT send any Wake Up Command Class commands, when the mailbox service is enabled.


With the Mailbox service enabled:


 - If either the Z/IP Client or Gateway supports Mailbox Command Class, version 1, the Z/IP
Client MUST issue a Wake Up No More Information Command when it has completed its
interview of a sleeping node.


 - If both the Z/IP Client or Gateway support Mailbox Command Class, version 2 or newer,
the Z/IP Client MUST NOT issue a Wake Up No More Information Command when it has
completed its interview of a sleeping node.


**5.2.4.1** **Examples** **and** **frame** **flows**


**5.2.4.1.1** **Node** **interview** **process**


The node interview process is shown in Figure 5.9 and Figure 5.10. The requirement applies as soon
as a client has received a Node Add Status (ADD_NODE_STATUS_DONE) command, regardless
of who initiated the node inclusion.


Figure 5.9: Node interview with Mailbox v1


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 940




<!-- PAGE 942 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.10: Node interview with Mailbox v1


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 941




<!-- PAGE 943 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5** **Network** **Management** **Command** **Class,** **version** **1**


**5.2.5.1** **Compatibility** **considerations**


The commands defined in the following sections may span more than the available payload length
CC:0000.00.00.21.001 in Z-Wave frames. If the command payload does not fit in a single frame, commands MUST be
fragmented using the Transport Service Command Class.


CC:0000.00.00.21.002 When using IP transport, the IP UDP data segment length limit of 1280 bytes MUST be respected.



CC:0000.00.00.22.001



There is a risk that a controlling node would try to issue Network Management commands to a
controller which does not support functionality due to its Network role (i.e. Secondary controller). A
controller SHOULD adjust its NIF (or S0/S2 Commands Supported Report Command) based on its
network role after inclusion.



CC:0000.00.00.21.004 When a node has the SIS, Primary controller or Inclusion controller role, it MUST support:


      - Network Management Inclusion Command Class


      - Network Management Basic Command Class


      - Transport Service Command Class


CC:0000.00.00.21.005 When a node has the secondary controller role, it MUST support:


      - Network Management Basic Command Class


The Z-Wave Network Management commands are organized as follows



Table 5.19: Z-Wave Network Management Commands







|Command Class|Purpose|
|---|---|
|Network Management<br>Proxy|The command class is used to report the list of nodes present in<br>a Z-Wave Network and report the secure/non-secure capabilities of<br>each of those nodes<br>Version 2 of this command class extends the node capability report-<br>ing to Multi Channel End Points.|
|Network Management<br>Basic Node|The command class is used to remotely control network management<br>operations related to including supporting nodes into a Z-Wave net-<br>work.<br>The available functionalities are :<br>• Enable Learn mode<br>• Request a node to broadcast its Node Information Frame<br>• Request a node to request a network topology update to the<br>SUC<br>• Reset a controller to the factory default state<br>Version 2 of this command class extends the learn mode activation<br>commands In order to support S2 and adds the following function-<br>ality:<br>• Request a node to report its S2 DSK.|


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 942




<!-- PAGE 944 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.20: Z-Wave Network Management Commands 2










|Command Class|Purpose|
|---|---|
|Network Management<br>Inclusion|This command class is used to remotely control network management<br>operations related to including other nodes into a Z-Wave network.<br>The available functionalities are :<br>• Enable Add mode<br>• Remove a node from the network<br>• Remove a Failed NodeID from the network<br>• Replace a Failed NodeID in the network<br>• Request the node to ask a specifc node to perform a Neighbor<br>update.<br>• Instruct the supporting node to assign a return route to an-<br>other end node node<br>• Instruct the supporting node to remove return routes in an-<br>other end node node<br>Version 2 of this command class extends the Add/Remove/Replace<br>commands to support S2 and adds the following functionality:<br>• A supporting node can be instructed which S2 keys to grant<br>to a joining node.<br>• A supporting node can be provided a DSK input for S2 au-<br>thentication.|
|Network Management<br>Primary|This command class is used to remotely trigger a controller change<br>operation.|
|Network Management<br>Installation and<br>maintenance|This command class is used for maintenance and optimization pur-<br>poses. The available functionalities are :<br>• Manipulate priority routes (working routes)<br>• Request network statistics recorded by the node.|



**5.2.5.1.1** **Sequence** **number** **management**


The following text applies to all sequence numbers used by Network Management Command Classes.


CC:0000.00.00.21.006 Each sequence number MUST be generated from an 8-bit counter that is incremented by 1 whenever a
new sequence number is generated. When a node powers up, the sequence counter MUST be initialized
to a random value.


CC:0000.00.00.23.001 All command classes referring to this section MAY use the same global counter.


CC:0000.00.00.21.007 When responding to a request command, a responding node MUST echo the sequence number used
by the requesting node.


CC:0000.00.00.21.008 When receiving response to a request command, the requesting node MUST verify that the response
carries the same sequence number as the request command.


**5.2.5.2** **Scope** **of** **network** **management**


Network management commands may be used in a number of scenarios. Three scopes have been
identified:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 943




<!-- PAGE 945 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.11: Scope of network management


**5.2.5.2.1** **Intranode**


When used in an intranode configuration, the network management command classes are primarily
used for implementation convenience. As an example, a software module of the Z/IP Gateway application may be used to provide a standard IP-based interface for other Linux applications inside
a set-top box. In this way an application programmer does not have to bother about serial port
communication, Telnet command parsing, etc.


**5.2.5.2.2** **Intranet** **(LAN)**


Managed building automation systems may implement one central network manager controlling a
number of geographically distributed Z/IP Gateways via the network management command classes.
Each Z/IP Gateway may be instructed to perform local inclusion or exclusion of nodes; thus creating
a large infrastructure segmented into subnets.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 944




<!-- PAGE 946 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.2.3** **Internet** **(WAN)**


The help desk of a service provider may provide support from a remote call center via the Internet.
This enables the deployment of border routers, remote controls and plug-in modules in consumer
environments without relying on the technical interest and/or capabilities of the user.


**5.2.5.3** **Security** **considerations**


CC:0000.00.00.42.001 Network management is a powerful toolbox. From an application level, it SHOULD be ensured that
the user does not unintentionally reset the controller or remove nodes.


CC:0000.00.00.41.001 At the same time it MUST be ensured that it is not possible for unauthorized persons to inject
malicious commands into the network, e.g. resetting the primary controller to default factory settings.


CC:0000.00.00.41.002 All Network Management Command Class MUST be sent securely when used on a Z-Wave network,
using at least Z-Wave Security 0 Command Class, version 1. When used on the LAN side other means
of security should be used.


If the network management commands are carried in IP packets over Z-Wave, a minimum level of
security is automatically applied since S0 network security is mandatory for all Z/IP traffic.


CC:0000.00.00.42.002 When Z-Wave network management commands are carried over IP LAN and WAN media (intranet
& internet) the IP traffic SHOULD be using secure communication. A Z/IP Gateway MAY allow
a LAN-based IP host to send un encrypted Network Management commands to a controller via the
Z/IP Gateway. Support for un encrypted Network Management commands SHOULD be disabled by
default and after a factory reset.


**5.2.5.3.1** **Designing** **for** **single-threading** **and** **limited** **transmit** **buffer**


In order to support constrained CPU platforms, the Z-Wave API has been designed for single-threaded
CC:0000.00.00.41.003 operation. A node MUST ignore Network Management command if already processing or executing
another Network Management command.


CC:0000.00.00.42.003 A node SHOULD NOT ignore the command if it is identical to the command currently being processed/executed (e.g. Add Node Command with mode: Stop when Add Mode is active)


CC:0000.00.00.41.004 A node MUST return status messages to the node that actually initiated the operation.


CC:0000.00.00.41.005 An controlling node MUST time out waiting for a status message. The time out SHOULD depend on

CC:0000.00.00.42.004 the actual command. If not receiving a status message within the defined time out for a command,
the node SHOULD re-send the Network Management command using the same sequence number to
allow the target node to detect duplicates.

CC:0000.00.00.43.001 A receiving node MAY return a ”busy” indication. Doing so could however lead to transmit buffer
overflows. Care should be taken to avoid this during implementation.


The Z-Wave Ack does not necessarily indicate that the command is being executed, but that it has
CC:0000.00.00.41.006 been received by the protocol. The sending application MUST wait for the Network Management
command callback, or time out.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 945




<!-- PAGE 947 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.4** **Network** **management** **proxy** **command** **class,** **version** **1**


The Network Management Proxy Command Class provides functions to access basic network information such as the list of nodes currently present in the Z-Wave network.


**5.2.5.4.1** **Node** **list** **get** **command**


This command is used to request the network node list from local storage in a node.


CC:0052.01.01.11.001 The Node List Report Command MUST be returned in response to this command.


CC:0052.01.01.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressCC:0052.01.01.11.003 ing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.21: Node List Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|Command = NODE_LIST_GET (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**5.2.5.4.2** **Node** **list** **report** **command**


This command carries node data requested with the Node List Get Command.



CC:0052.01.02.11.001


CC:0052.01.02.12.001



In addition, when a node has been added to or removed from the network or when the Z/IP Gateway
has acquired the SIS role, the Z/IP Gateway MUST send an unsolicited Node List Report with the
new network information to the unsolicited destination.



CC:0052.01.02.11.002 If the unsolicited destination itself has initiated the node addition or removal, this command SHOULD
NOT be sent.


CC:0052.01.02.11.004 The Z/IP Gateway MAY send an unsolicited Node List Report when it is ready after power reset.
If no unsolicited destination has been set, the gateway MUST NOT send a Node List Report upon
network changes.


Table 5.22: Node List Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|
|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|
|…|…|…|…|…|…|…|…|
|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|



**Seq** **No** **1byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **8** **bits)**

CC:0052.01.02.11.003 This field indicates the status of Node List data carried in the command. The field MUST take one
of the following values:


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 946




<!-- PAGE 948 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


      - 0x00: The Node List Data contains the latest updated node list.


      - 0x01: The Node List Data may be outdated.


**Node** **List** **Controller** **ID** **(1** **byte)**


The Node List Controller ID is a NodeID pointing at a controller, which keeps latest updated node
list. The value 0x00 indicates that Node List Controller ID is unknown.


CC:0052.01.02.12.002 The Node List Controller SHOULD provide up-to-date information, but the actual freshness of data
depends on the network construction. If a portable controller is primary there may be no access to
the most recent network data. In that case the user may have to manually wake up the portable
controller and initiate a controller replication to an always listening secondary controller.


No explicit Z-Wave route is provided for reaching the Node List Controller. The requesting node may
use methods such as explorer discovery or Controller Network Update if the node does not already
hold a working route to the indicated Node List Controller.


The Node List Controller ID may not support Network Management Proxy Command Class.


**Node** **List** **Data** **(29** **bytes)**

This field carries a complete bitmap presenting all included nodes as a set bit (‘1’) while unused
NodeIDs are presented as a (‘0’). The first bit in the bitmap represents NodeID 1; the last bit
represents NodeID 232.


A receiving node can use the Node Info Cached Get Command to get information on individual node
properties.


**5.2.5.4.3** **Node** **info** **cached** **get** **command**


This command is used to request node capabilities that have been cached by another node. The
command works as a proxy function provided by the node list controller. The purpose is to preserve
the bandwidth of the Z-Wave network and to provide access to properties of sleeping nodes.


CC:0052.01.03.11.001 The Node Info Cached Report Command MUST be returned in response to this command.


CC:0052.01.03.13.001 A Z/IP client MAY issue the Node Info Cached Get command as an IPv4 broadcast or an IPv6 ‘all

CC:0052.01.03.11.002 routers’ multicast packet. A Z/IP Gateway MUST accept such a packet and return a Node Info
Cached Report in response.


CC:0052.01.03.11.003 A Node Info Cached Report returned by a Z/IP Gateway in response to an IP multicast packet
MUST be delayed by a random delay in the range 0..450msec as more than one Z/IP Gateway may
be responding.


CC:0052.01.03.11.004 The Z/IP Gateway MUST respond to an IP multicast by returning a unicast IP packet.


CC:0052.01.03.13.002 A Z/IP Client MAY time out waiting for Node Info Cached Report commands after 500msec.


Table 5.23: Node Info Cached Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Max Age|Max Age|Max Age|Max Age|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0052.01.03.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 947




<!-- PAGE 949 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Max** **Age** **(4** **bits)**


The maximum age of the Node Info frame, given in 2^n minutes. If the cache entry does not exist
CC:0052.01.03.12.001 or if it is older that the value given in this field, the Z/IP Gateway SHOULD attempt to get a fresh
Node Info Frame before responding to this command.

A value of 15 means infinite, i.e. No Cache Refresh. A value of 0 means force update. The values
1..15 allow for cache timeouts in the range 2min, 4min, …, 11days – and infinite.


**NodeID** **(1** **byte)**

CC:0052.01.03.11.006 This field MUST indicate the NodeID for which the receiving node is to return cached data.


The value 0x00 MUST be interpreted as the ID of the queried network management node.


**5.2.5.4.4** **Node** **info** **cached** **report** **command**


This command is used for returning cached node information.


Table 5.24: Node Info Cached Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status<br>|Status<br>|Status<br>|Status<br>|Age<br>|Age<br>|Age<br>|Age<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended –> spanning two bytes for one command class


**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(4** **bits)**

This field is used to indicate the Node Info Cached information status. This field MUST comply with
CC:0052.01.04.11.001 Table 5.25.


Table 5.25: Node Info Cached Report::Status parameter encoding

|Value|i<br>Status identifer|Description|
|---|---|---|
|0x00|STATUS_OK|The requested NodeID could be found and up-to-date in-<br>formation is returned.|
|0x01|STATUS_NOT_RE-<br>SPONDING|The requested NodeID could be found but fresh informa-<br>tion could not be retrieved.|
|0x02|STATUS_UNKNOWN|The NodeID is unknown.|



**Age** **(4** **bits)**

This field indicates the age of the Node Info frame, i.e. the time elapsed since the data has been
CC:0052.01.04.11.002 received by the actual node. This field MUST be expressed in ”2^n minutes”. This field’s value
MUST be rounded down, i.e.12 minutes MUST be reported as 2^3 = 8 minutes and not as 2^4 = 16

min.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 948




<!-- PAGE 950 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**List** **(1** **bit)**


The Optional Functionality bit indicates if true ( == ‘1’) the node supports more command classes
in addition to the ones covered by the device classes listed in this message. The additional command
classes follow the device class fields.


**Reserved**

CC:0052.01.04.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

**Z-Wave** **Protocol** **Specific** **Part**


CC:0052.01.04.11.004
This field is the protocol specific part of the NIF. It MUST be set as received in the Node Information
Frame.


**Basic** **Device** **Class** **(1** **byte)**

This field indicates the Basic Device Class of the actual node.


**Generic** **Device** **Class** **(1** **byte)**

This field indicates the Generic Device Class of the actual node. The Generic Device Classes for
Z-Wave Plus are listed in [34] and Section 7.

**Specific** **Device** **Class** **(1** **byte)**

This field indicates the Specific Device Class of the actual node. The Specific Device Classes for
Z-Wave Plus are listed in [34] and Section 7.


**Command** **Class** **(N** **bytes)**

This field indicates the command classes implemented by the actual node.


CC:0052.01.04.11.005 The Security Scheme 0 Mark MUST be used to delimit Command Classes available non-securely and
securely.


CC:0052.01.04.11.006 The Support/Control Mark MUST be used before and after the Security Scheme 0 Mark if it was
present in the node’s NIF.

CC:0052.01.04.11.007 A Command Class field structure example is shown in Table 5.26. The field MUST comply with Table
5.27.


Table 5.26: Command Class field structure example

|Description|i<br>Command Class feld content|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|…|7|6|5|4|3|2|1|0|
|Non-secure Supported Command Classes|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|Non-secure Supported Command Classes|…|…|…|…|…|…|…|…|
|Non-secure Supported Command Classes|Command Class M *)|Command Class M *)|Command Class M *)|Command Class M *)|Command Class M *)|Command Class M *)|Command Class M *)|Command Class M *)|
|Support/Control Mark|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|
|Non-secure Controlled Command Classes|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|Non-secure Controlled Command Classes|…|…|…|…|…|…|…|…|
|Non-secure Controlled Command Classes|Command Class K *)|Command Class K *)|Command Class K *)|Command Class K *)|Command Class K *)|Command Class K *)|Command Class K *)|Command Class K *)|
|Security Scheme 0 Mark|0xF1|0xF1|0xF1|0xF1|0xF1|0xF1|0xF1|0xF1|
|Security Scheme 0 Mark|0x00|0x00|0x00|0x00|0x00|0x00|0x00|0x00|
|S0 Secure Supported Command Classes|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|S0 Secure Supported Command Classes|…|…|…|…|…|…|…|…|
|S0 Secure Supported Command Classes|Command Class L *)|Command Class L *)|Command Class L *)|Command Class L *)|Command Class L *)|Command Class L *)|Command Class L *)|Command Class L *)|
|Support/Control Mark|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|0xEF|
|S0 Secure Controlled Command Classes|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|S0 Secure Controlled Command Classes|…|…|…|…|…|…|…|…|
|S0 Secure Controlled Command Classes|Command Class P *)|Command Class P *)|Command Class P *)|Command Class P *)|Command Class P *)|Command Class P *)|Command Class P *)|Command Class P *)|



*) Command classes may be extended –> spanning two bytes for one command class


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 949




<!-- PAGE 951 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Command Class|Table 5.27: Special Command Class identifiers Description|
|---|---|
|**Command Class**<br>**ID**|**Description**<br>|
|0x20..0xEE|Command Class identifer<br>|
|0xF101..0xFFFF|Extended Command Classes identifer|
|0xEF|Command Class Support/Control Mark<br>Anything between this mark and the next mark is Controlled and not supported|
|0xF100|Security Scheme 0 Command Class Mark.<br>Command Classes following this Mark are supported or controlled with Secu-<br>rity Scheme 0|



**5.2.5.5** **Network** **management** **proxy** **command** **class,** **version** **2**


**5.2.5.5.1** **Compatibility** **considerations**


The Network Management Proxy Command Class, version 2 is backwards compatible with Network
CC:0052.02.00.21.001 Management Proxy Command Class, version 1. A node supporting Network Management Proxy
Command Class, version 2 MUST also support Network Management Proxy Command Class, version
1.


All commands not mentioned in this version remain unchanged from version 1.


The following command has been extended to support S2 bootstrapping information:


      - Node Info Cached Report


The following commands have been added to support Multi Channel End Point probing:


      - Network Management Multi Channel End Point Get Command


      - Network Management Multi Channel End Point Report Command


      - Network Management Multi Channel Capability Get Command


      - Network Management Multi Channel Capability Report Command


      - Network Management Multi Channel Aggregated Members Get Command


      - Network Management Multi Channel Aggregated Members Report Command


**5.2.5.5.2** **Node** **info** **cached** **report** **command**


This command is used for returning cached node information.


Table 5.28: Node Info Cached Report Command v2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|Command = NODE_INFO_CACHED_REPORT (0x04)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status<br>|Status<br>|Status<br>|Status<br>|Age<br>|Age<br>|Age<br>|Age<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 950




<!-- PAGE 952 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


*) Command classes may be extended –> spanning two bytes for one command class


Fields not described in this version remain unchanged from version 1.


**Granted** **Keys** **(8** **bits)**

This field is used to indicate which network keys were granted during bootstrapping. This field MUST
CC:0052.02.04.11.001 be treated as a bitmask and comply with Table 5.85


**Command** **Class** **(N** **bytes)**


Refer to Section 5.2.5.4.4 and Table 5.27.


CC:0052.02.04.11.002 The Security Command Class Mark (0xF100) MUST indicate command classes supported using the
highest listed Security Key in the Granted Key field value.


**5.2.5.5.3** **Network** **management** **multi** **channel** **end** **point** **get** **command**


This command is used to query the number of Multi Channel End Points and other relevant Multi
Channel attributes.


CC:0052.02.05.11.001 The Network Management Multi Channel End Point Report Command MUST be returned in response
to this command unless it is to be ignored.


Table 5.29: Network Management Multi Channel End Point Get
Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0052.02.05.11.002 This field MUST indicate the NodeID for which the receiving node is to return cached data. If the
specified NodeID does not exist, this command MUST be ignored.


**5.2.5.5.4** **Network** **management** **multi** **channel** **end** **point** **report** **command**


This command is used to advertise the number of Multi Channel End Points implemented by a node.


Table 5.30: Network Management Multi Channel End Point Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Res|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|
|Res|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 951




<!-- PAGE 953 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**NodeID** **(1** **byte)**

CC:0052.02.06.11.001 This field MUST indicate the NodeID for which the receiving node is to return cached data.


**Reserved** **/** **Res**

CC:0052.02.06.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Individual** **End** **Points** **(7** **bits)**

CC:0052.02.06.11.003 This field MUST advertise the number of individual End Points implemented by this node.


CC:0052.02.06.11.004 The value MUST be in the range 0..127. The sum of the values advertised by the Individual End
Points and Aggregated End Points fields MUST be in the range 0..127.


**Aggregated** **End** **Points** **(7** **bits)**

CC:0052.02.06.11.005 This field MUST advertise the number of Aggregated End Points implemented by this node.


CC:0052.02.06.11.006 The value MUST be in the range 0..127. The sum of the values advertised by the Individual End
Points and Aggregated End Points fields MUST be in the range 0..127.

CC:0052.02.06.11.007 If no Aggregated End Points are implemented, this field MUST advertise the value 0 (zero).


**5.2.5.5.5** **Network** **management** **multi** **channel** **capability** **get** **command**


This command is used to query the capabilities of one individual End Point or Aggregated End Point.


CC:0052.02.07.11.001 The Network Management Multi Channel Capability Report Command MUST be returned in response
to this command unless it is to be ignored.


Table 5.31: Network Management Multi Channel Capability Get
Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Res|End Point|End Point|End Point|End Point|End Point|End Point|End Point|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0052.02.07.11.002 This field MUST indicate the NodeID for which the receiving node is to return cached data.


**Res**

CC:0052.02.07.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**End** **Point** **(7** **bits)**

CC:0052.02.07.13.001 This field MAY specify a valid End Point as advertised by the Multi Channel End Point Report. If
the specified End Point does not exist, this command MUST be ignored.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 952




<!-- PAGE 954 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.5.6** **Network** **management** **multi** **channel** **capability** **report** **command**


This command is used to advertise the generic and specific device class and the supported command
classes of one End Point.


Table 5.32: Network Management Multi Channel Capability Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|
|Res|End Point|End Point|End Point|End Point|End Point|End Point|End Point|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended –> spanning two bytes for one command class


**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0052.02.08.11.001 This field MUST indicate the NodeID for which the receiving node is to return cached data.


**Res** **(1** **bit)**

CC:0052.02.08.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Command** **Class** **Length** **(1** **byte)**

CC:0052.02.08.11.003 This field MUST advertise the length in bytes of the Command Class field.


**End** **Point** **(7** **bits)**

CC:0052.02.08.11.004 This field MUST advertise a valid End Point as advertised by the Multi Channel End Point Report.


**Generic** **Device** **class** **(8** **bits)**

This field indicates the Generic Device Class of the advertised End Point.

**Specific** **Device** **class** **(8** **bits)**

This field indicates the Specific Device Class of the advertised End Point.


**Command** **Class** **(N** **bytes)**

CC:0052.02.08.11.005 This field MUST advertise Command Classes supported or controlled by the End Point in question.


Refer to Section 5.2.5.4.4 and Table 5.27.


CC:0052.02.08.11.006 The Security Command Class Mark (0xF100) MUST indicate command classes supported using the
highest listed Security Key in the Granted Key field value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 953




<!-- PAGE 955 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.5.7** **Network** **management** **multi** **channel** **aggregated** **members** **get** **command**


This command is used to query the members of an Aggregated End Point.


CC:0052.02.09.11.001 The Network Management Multi Channel Aggregated Members Report Command MUST be returned
in response to this command unless it is to be ignored.


Table 5.33: Network Management Multi Channel Aggregated
Members Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0052.02.09.11.002 This field MUST indicate the NodeID for which the receiving node is to return cached data. This
command MUST be ignored if the NodeID field is not valid.


**Res**

CC:0052.02.09.11.003 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Aggregated** **End** **Point** **(7** **bits)**

CC:0052.02.09.11.004 This field MUST specify an Aggregated End Point. This command MUST be ignored if the End Point
does not exist or is not an Aggregated End Point.


**5.2.5.5.8** **Network** **management** **multi** **channel** **aggregated** **members** **report** **command**


This command is used to advertise the members of an Aggregated End Point.


Table 5.34: Network Management Multi Channel Aggregated
Members Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|
|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|
|Res|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|
|…|…|…|…|…|…|…|…|
|Res|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0052.02.0A.11.001 This field MUST indicate the NodeID for which the receiving node is to return cached data.


**Res**

CC:0052.02.0A.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 954




<!-- PAGE 956 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Aggregated** **End** **Point** **(7** **bits)**

CC:0052.02.0A.11.003 This field MUST advertise an Aggregated End Point.


CC:0052.02.0A.11.004
If the command is returned in response to a Multi Channel Aggregated Members Get, this field MUST
advertise the same value as was received in the Multi Channel Aggregated Members Get command.


**Number** **of** **Members** **(8** **bits)**

CC:0052.02.0A.11.005 This field MUST advertise the number of members of the aggregated End Points


**Member** **Endpoint** **(N** ***** **7** **bits)**


This list is used to advertise the End Point members of the Aggregated End Point advertised in the
CC:0052.02.0A.11.006 Aggregated End Point field. The length of the list MUST be determined from the Number of Members
field. This field MUST be omitted if the Number of Members field is set to 0.


CC:0052.02.0A.11.007 Each object in the list is a 7-bit End Point ID. The addressing bit (Res) MUST be set to 0 by a
sending node and MUST be ignored by a receiving node.


**5.2.5.6** **Network** **management** **proxy** **command** **class,** **version** **3**


**5.2.5.6.1** **Compatibility** **considerations**


The Network Management Proxy Command Class, version 3 is backwards compatible with Network
Management Proxy Command Class, version 2.

CC:0052.03.00.21.001 All commands and fields not mentioned in this version MUST remain unchanged from version 1.


The Command Class is extended with these 2 commands:


      - Failed Node List Get Command


      - Failed Node List Report Command


The strategy for considering that nodes are failing (or non-responsive/unlikely to respond to frames
again) is implementation specific and may differ from one supporting node to another. A controlling
node SHOULD allow the Replace Failed Node and Remove Failed node network management functions
for nodes reported as failing.


**5.2.5.6.2** **Failed** **node** **list** **get** **command**


This command is used to request the network node list that is marked as failing (or non-responsive).


CC:0052.03.0B.11.001 The Failed Node List Report Command MUST be returned in response to this command.


CC:0052.03.0B.11.002 This command MUST NOT be issued via multicast addressing. A receiving node MUST NOT return

CC:0052.03.0B.11.003 a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the
broadcast NodeID and the Multi Channel multi-End Point destination are all considered multicast

addressing methods.


Table 5.35: Failed Node List Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|
|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|Command = FAILED_NODE_LIST_GET (0x0B)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 955




<!-- PAGE 957 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.6.3** **Failed** **node** **list** **report** **command**


This command is used to advertise the current list of failing nodes in the network.


Table 5.36: Failed Node List Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|
|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|
|…|…|…|…|…|…|…|…|
|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Failed** **Node** **List** **Data** **(29** **bytes)**

This field carries a complete bitmask representation of nodes ranging from NodeID 1 to NodeID 232.


CC:0052.03.0C.11.001 Bit 0 in byte 1 MUST represent NodeID 1


Bit 1 in byte 1 MUST represent NodeID 2


…


Bit 7 in byte 29 MUST represent NodeID 232


CC:0052.03.0C.11.002 The value 0 MUST indicate that the NodeID is either not part of the network or part of the network
and fully functional.


The value 1 MUST indicate that the NodeID is part of the network and is failing (or not responding
to frames)


**5.2.5.7** **Network** **management** **proxy** **command** **class,** **version** **4**


**5.2.5.7.1** **Compatibility** **Considerations**


The Network Management Proxy Command Class, version 4 is backwards compatible with Network
Management Proxy Command Class, version 3.

All commands and fields not mentioned in this version MUST remain unchanged from version 3.


This version of the Network Management Proxy Command Class introduces support for the Z-Wave
Long Range protocol. The following commands are updated:


      - Node List Report Command


      - Node Info Cached Get Command


      - Network Management Multi Channel End Point Get Command


      - Network Management Multi Channel End Point Report Command


      - Network Management Multi Channel Capability Get Command


      - Network Management Multi Channel Capability Report


      - Network Management Multi Channel Aggregated Members Get Command


      - Network Management Multi Channel Aggregated Members Report Command


      - Failed Node List Report Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 956




<!-- PAGE 958 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.7.2** **Node** **list** **report** **command**


This command is used to advertise the list of nodes in the Z-Wave / Z-Wave Long Range network.


A Z/IP Gateway MAY send an unsolicited Node List Report when it is ready after power reset. If no
unsolicited destination has been set, the gateway MUST NOT send a Node List Report upon network
changes.


Table 5.37: Node List Report Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|Command = NODE_LIST_REPORT (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|Node List Controller ID|
|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|Node List Data 1|
|…|…|…|…|…|…|…|…|
|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|Node List Data 29|
|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|Extended Node List Length (MSB)|
|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|Extended Node List Length (LSB)|
|Extended Node List 1|Extended Node List 1|Extended Node List 1|Extended Node List 1|Extended Node List 1|Extended Node List 1|Extended Node List 1|Extended Node List 1|
|…|…|…|…|…|…|…|…|
|Extended Node List N|Extended Node List N|Extended Node List N|Extended Node List N|Extended Node List N|Extended Node List N|Extended Node List N|Extended Node List N|



All fields not described below MUST remain unchanged from version 3.


**Extended** **Node** **List** **Length** **(2** **bytes)**

This field is used to advertise the length in byte of the Extended Node List. A sending node SHOULD
set this field to the smallest value allowing to advertise all NodeIDs present in the current network.


**Extended** **Node** **List** **(N** **bytes)**

This field is used to advertise the list of nodes included in the network with a NodeID greater than
255.

The length of this field (in bytes) MUST be according to the Extended Node List Length field.

This field MUST be treated as a bitmask and encoded as follow.


 - Bit 0 in byte 1 MUST represent NodeID 256 (0x100)


 - Bit 1 in byte 1 MUST represent NodeID 257 (0x101)


 - etc.


The value 0 MUST indicate that no node has the corresponding NodeID assigned in the network.
The value 1 MUST indicate there is a node with the corresponding NodeID assigned present in the
network.


**5.2.5.7.3** **Node** **info** **cached** **get** **command**


This command is used to request the capabilities of a node present in the network.


The Node Info Cached Report Command MUST be returned in response to this command.


A Z/IP client MAY issue the Node Info Cached Get command as an IPv4 broadcast or an IPv6 ‘all
routers’ multicast packet. A Z/IP Gateway MUST accept such a packet and return a Node Info
Cached Report in response.


A Node Info Cached Report returned by a Z/IP Gateway in response to an IP multicast packet
MUST be delayed by a random delay in the range 0..450msec as more than one Z/IP Gateway may
be responding.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 957




<!-- PAGE 959 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Z/IP Gateway MUST respond to an IP multicast by returning a unicast IP packet.


A Z/IP Client MAY time out waiting for Node Info Cached Report commands after 500msec.


Table 5.38: Node Info Cached Get Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|Command = NODE_INFO_CACHED_GET (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Max Age|Max Age|Max Age|Max Age|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the receiving node is to return cached data. The
value 0x00 MUST be interpreted as the ID of the queried network management node.

The value 0xFF MUST indicate that the queried NodeID is indicated in the Extended NodeID field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the NodeID for which the Node Information is requested

This field MUST be set to the same value as the NodeID field by a sending node and ignored by a
receiving node if the NodeID field value is in the range 0x00..0xFE

This field MUST be used in place of the NodeID if the NodeID field is set to 0xFF.


**5.2.5.7.4** **Network** **management** **multi** **channel** **end** **point** **get** **command**


This command is used to query the number of Multi Channel End Points and other relevant Multi
Channel attributes.


The Network Management Multi Channel End Point Report Command MUST be returned in response
to this command unless it is to be ignored.


Table 5.39: Network Management Multi Channel End Point Get
Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|Command = NM_MULTI_CHANNEL_END_POINT_GET (0x05)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the number of endpoints is requested. If the specified
NodeID does not exist, this command MUST be ignored.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the requested NodeID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 958




<!-- PAGE 960 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which the number of
endpoints MUST be returned.

If the specified NodeID does not exist, this command MUST be ignored.


**5.2.5.7.5** **Network** **management** **multi** **channel** **end** **point** **report** **command**


This command is used to advertise the number of Multi Channel End Points implemented by a node.


Table 5.40: Network Management Multi Channel End Point Report Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|Command = NM_MULTI_CHANNEL_END_POINT_REPORT (0x06)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Res|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|Individual End Points|
|Res|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|Aggregated End Points|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the number of endpoints is advertised.

If the specified NodeID does not exist, this command MUST be ignored.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the advertised NodeID.

If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which the number of
endpoints is advertised.


**5.2.5.7.6** **Network** **management** **multi** **channel** **capability** **get** **command**


This command is used to query the capabilities of one individual End Point or Aggregated End Point.


The Network Management Multi Channel Capability Report Command MUST be returned in response
to this command unless it is to be ignored.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 959




<!-- PAGE 961 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.41: Network Management Multi Channel Capability Get
Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|Command = NM_MULTI_CHANNEL_CAPABILITY_GET (0x07)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Res|End Point|End Point|End Point|End Point|End Point|End Point|End Point|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the capabilities are requested.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the requested NodeID.

If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which the number of
endpoints is advertised.

If the specified NodeID does not exist, this command MUST be ignored.


**5.2.5.7.7** **Network** **management** **multi** **channel** **capability** **report** **command**


This command is used to advertise the generic and specific device class and the supported command
classes of one End Point.


Table 5.42: Network Management Multi Channel Capability Report Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|Command = NM_MULTI_CHANNEL_CAPABILITY_REPORT (0x08)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|Command Class Length|
|Res|End Point|End Point|End Point|End Point|End Point|End Point|End Point|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which an endpoint’s capabilities are advertised.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 960




<!-- PAGE 962 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the advertised NodeID for which an endpoint’s capabilities are advertised.

If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which an endpoint’s
capabilities are advertised.


**5.2.5.7.8** **Network** **management** **multi** **channel** **aggregated** **members** **get** **command**


This command is used to query the members of an Aggregated End Point.


CC:0052.04.09.11.001 The Network Management Multi Channel Aggregated Members Report Command MUST be returned
in response to this command unless it is to be ignored.


Table 5.43: Network Management Multi Channel Aggregated
Members Get Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_GET (0x09)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the aggregated endpoints are requested.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the requested NodeID.

If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which the number of
endpoints is advertised.

If the specified NodeID does not exist, this command MUST be ignored.


**5.2.5.7.9** **Network** **management** **multi** **channel** **aggregated** **members** **report** **command**


This command is used to advertise the members of an Aggregated End Point.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 961




<!-- PAGE 963 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.44: Network Management Multi Channel Aggregated
Members Report Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY|
|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|Command = NM_MULTI_CHANNEL_AGGREGATED_MEMBERS_REPORT (0x0A)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Res|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|Aggregated End Point|
|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|Number of Members|
|Res|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|Member Endpoint 1|
|…|…|…|…|…|…|…|…|
|Res|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|Member Endpoint N|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field MUST indicate the NodeID for which the aggregated endpoint members are advertised.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the Extended NodeID
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to indicate the advertised NodeID for which the aggregated endpoint members are
advertised.

If the NodeID field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the NodeID field is set to 0xFF, this field MUST indicate the NodeID for which the aggregated
endpoint members are advertised.


**5.2.5.7.10** **Failed** **node** **list** **report** **command**


This command is used to advertise the current list of failing nodes in the network.


Table 5.45: Failed Node List Report Command v4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PROXY (0x52)|
|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|Command = FAILED_NODE_LIST_REPORT (0x0C)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|Failed Node List Data 1|
|…|…|…|…|…|…|…|…|
|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|Failed Node List Data 29|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|
|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|Extended Failed Node List 1|
|…|…|…|…|…|…|…|…|
|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|Extended Failed Node List N|



All fields not described below MUST remain unchanged from version 3.


**Extended** **Failed** **Node** **List** **Length** **(2** **bytes)**

This field is used to advertise the length in byte of the Extended Node List.

A sending node SHOULD set this field to the smallest value allowing to advertise all failed NodeIDs
present in the current network.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 962




<!-- PAGE 964 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Extended** **Failed** **Node** **List** **(N** **bytes)**

This field is used to advertise the list of failing nodes with a NodeID greater than 255.

The length of this field (in bytes) MUST be according to the Extended Failed Node List Length field.

This field MUST be treated as a bitmask and encoded as follow:


      - Bit 0 in byte 1 MUST represent NodeID 256 (0x100)


      - Bit 1 in byte 1 MUST represent NodeID 257 (0x101)


      - etc.


The value 0 MUST indicate that the NodeID is either not part of the network or part of the network
and fully functional.


The value 1 MUST indicate that the NodeID is part of the network and is failing (or not responding
to frames)


**5.2.5.8** **Network** **Management** **Basic** **Node** **Command** **Class,** **version** **1**


**5.2.5.8.1** **Default** **set** **command**


This command is used to set the Controller back to the factory default state.


CC:004D.01.06.11.001 The Default Set Complete Command MUST be returned in response to this command. A receiving
node MUST return the DEFAULT_SET_BUSY status if it is already busy executing another network
management command.


CC:004D.01.06.11.002 This command MUST NOT be issued via multicast addressing.


CC:004D.01.06.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


CC:004D.01.06.12.001 This function SHOULD be used with care as it could render a network unusable if the primary
controller in an existing network is set back to default. If a node is set to default while it is still a
member of a network, the node will become a failing NodeID in that network.


Table 5.46: Default Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|Command = DEFAULT_SET (0x06)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**5.2.5.8.2** **Default** **set** **complete** **command**


This command is used to indicate if the Default Set operation was executed successfully or not.


Table 5.47: Default Set Complete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|Command = DEFAULT_SET_COMPLETE (0x07)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Seq** **No** **(8** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 963




<!-- PAGE 965 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Refer to _Sequence_ _number_ _management_ .


**Status** **(8** **bits)**

CC:004D.01.07.11.001 This field indicates the status of the default set operation. This field MUST comply with Table 5.48.


Table 5.48: Default Set Complete::Status encoding






|Value|i<br>Identifer|Description|
|---|---|---|
|0x06|DE-<br>FAULT_SET_DONE|The Default Set operation has been completed successfully.|
|0x07|DE-<br>FAULT_SET_BUSY|The Default Set operation has not been executed because the<br>node is busy.|



**5.2.5.8.3** **Learn** **mode** **set** **command**


This command is used to allow a node to be added to (or removed from) the network. When a node
is added to the network, the node is assigned a valid Home ID and NodeID.


This command allows a controlling application to request the transmission of Node Information Frames
(NIFs) in regular intervals until included, removed or until learn mode is disabled again.


CC:004D.01.01.12.001 Learn mode SHOULD be enabled only when necessary, and it SHOULD always be disabled again
as quickly as possible. However, to ensure a successful synchronization of the inclusion process the
device SHOULD be able to stay in learn mode at least 5 seconds.


CC:004D.01.01.11.006 The Learn Mode Set Status Command MUST be returned in response to this command unless it is
to be ignored.


CC:004D.01.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:004D.01.01.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.49: Learn Mode Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|Command = LEARN_MODE_SET (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:004D.01.01.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Mode** **(8** **bits)**

CC:004D.01.01.11.005 The Mode field controls operation. This field MUST comply with Table 5.50.


CC:004D.01.01.13.001


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 964




<!-- PAGE 966 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 5.50: Learn Mode Set::Mode parameter encoding






|Value|i<br>Identifer|Description|
|---|---|---|
|0x00|ZW_SET_LEARN_MODE_DIS-<br>ABLE|Stop the learn mode of the node.<br>The command MAY be ignored if Learn Mode<br>was not activated.<br>The command MAY be ignored if network in-<br>clusion or security bootstrapping is ongoing.|
|0x01|ZW_SET_LEARN_MODE_CLAS-<br>SIC|Start the learn mode on the controller and ac-<br>cept only being included in direct range|
|0x02|ZW_SET_LEARN_MODE_NWI|Start the learn mode on the controller and ac-<br>cept routed inclusion.|



Examples of Learn Mode activation and deactivation are given in Figure 5.12


**5.2.5.8.4** **Learn** **mode** **in** **a** **controller**


If the receiving node is a controller, it receives and stores the node list and routing table for the
network during inclusion. This information transmitted as part of the controller replication. This
function will most likely change the capabilities of the controller.


**5.2.5.8.5** **Learn** **mode** **set** **status** **command**


This command is used to indicate the progress of the Learn Mode Set command.


Table 5.51: Learn Mode Set Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(8** **bits)**

CC:004D.01.02.11.001 This field indicates the outcome of the learn mode and MUST comply with Table 5.52.


Table 5.52: Learn Mode Status::Status parameter encoding

|Value|i<br>Identifer|Description|
|---|---|---|
|0x06|LEARN_MODE_DONE|The learn process is complete and the controller<br>is now included into (or excluded from) the net-<br>work.<br>If the node supports S0 or S2, it indicates that<br>the network inclusion and security bootstrap-<br>ping were completed successfully (This include<br>the case where the node wasgranted no S2 key).|
|0x07|LEARN_MODE_FAILED|The learn process failed in some general way|
|0x09|LEARN_MODE_SECU-<br>RITY_FAILED|The learn process is complete and the node was<br>included in a network but security bootstrap-<br>ping failed. The node is **not** operating securely.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 965




<!-- PAGE 967 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Reserved**

CC:004D.01.02.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**New** **NodeID** **(1** **byte)**


The NodeID assigned to the new node by another primary controller or inclusion controller.

If the node was removed from the network or if the Status field is different than
LEARN_MODE_DONE, this field MUST be set to 0x00.


**5.2.5.8.6** **Node** **information** **send** **command**


This command is used to trigger a receiving node to issue a Node Information Frame (NIF).


CC:004D.01.05.11.001 A node receiving this command MUST send a Node Information Frame to the indicated NodeID with
the indicated transmission options. No status message is returned for this command.



CC:004D.01.05.13.001


CC:004D.01.05.12.001


CC:004D.01.05.13.002



A management application MAY use this message to make a node identify itself towards a Z-Wave
remote control during association operations. This command SHOULD NOT be used while learn
mode is activated. Instead, periodic Node Information Frame transmissions MAY be enabled along
with learn mode; refer to Section 5.2.5.8.1.


Table 5.53: Node Information Send Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|Command = NODE_INFORMATION_SEND (0x05)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|
|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Destination** **NodeID** **(1** **byte)**



CC:004D.01.05.13.003 This field indicates the NodeID of the node that will receive the Node Information frame. The NodeID
MAY be set to the broadcast NodeID to reach all nodes within direct range.


CC:004D.01.05.12.002 Acknowledgement SHOULD NOT be requested when broadcasting.


**tx** **Options** **(1** **byte)**

This field allows a management application to specify if the Node Information frame is to be sent with
CC:004D.01.05.11.002 special properties. This field MUST be treated as a bitmask and MUST comply with Table 5.54.



Table 5.54: Node Information Send::Tx Options encoding












|Value|l i<br>Option fag identifer|Description|
|---|---|---|
|0x00|NULL|Transmit at normal power level without any transmit op-<br>tions.|
|0x01|TRANSMIT_OP-<br>TION_ACK|Request acknowledgment from destination node.<br>Allow<br>routing.|
|0x02|TRANSMIT_OP-<br>TION_LOW_POWER|Transmit at low output power level (1/3 of normal RF<br>range)|
|0x10|TRANSMIT_OP-<br>TION_NO_ROUTE|Send only in direct range|
|0x20|TRANSMIT_OP-<br>TION_EXPLORE|Resolve new routes via explorer discovery if existing routes<br>fail|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 966




<!-- PAGE 968 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:004D.01.05.12.003 It is RECOMMENDED for a sending node to use the TRANSMIT_OPTION_NO_ROUTE tx Option and the broadcast NodeID in this command.


**5.2.5.8.7** **Network** **update** **request** **command**


This command is used to request network topology updates from the SUC/SIS node.


CC:004D.01.03.11.001 A node MUST NOT use this command if no SUC is present in the network.


The SUC can only handle one network update at a time, so care should be taken not to have multiple
controllers in the network ask for updates at the same time.


This command will generate a lot of network activity that will use bandwidth and stress the SUC.
CC:004D.01.03.12.001 Therefore, network updates SHOULD be requested as seldom as possible.


CC:004D.01.03.11.002 The Network Update Request Status Command MUST be returned in response to this command.


CC:004D.01.03.11.003 This command MUST NOT be issued via multicast addressing.


CC:004D.01.03.11.004 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.55: Network Update Request Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**5.2.5.8.8** **Network** **update** **request** **status** **command**


This command is used to indicate if the Network Update Request command execution has completed
successfully or not.


Table 5.56: Network Update Request Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|Command = NETWORK_UPDATE_REQUEST (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**


CC:004D.01.04.11.001
This field is used to indicate the status of the Network Update process. This field MUST comply with
Table 5.57.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 967




<!-- PAGE 969 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.57: Network Update Request Status::Status parameter en


|Value|Table 5.57: Network Up coding Status identifier|pdate Request Status::Status parameter en- Description|
|---|---|---|
|**Value**|**Status identifer**|**Description**|
|0x00|ZW_SUC_UP-<br>DATE_DONE|The update process succeeded|
|0x01|ZW_SUC_UP-<br>DATE_ABORT|The update process aborted because of an error|
|0x02|ZW_SUC_UP-<br>DATE_WAIT|The SUC node is busy|
|0x03|ZW_SUC_UP-<br>DATE_DISABLED|The SUC functionality is disabled|
|0x04|ZW_SUC_UP-<br>DATE_OVERFLOW|The controller requested an update after more than 64<br>changes have occurred in the network. The controller has<br>to make a replication.|


**5.2.5.8.9** **Use** **cases** **and** **frame** **flows**





**5.2.5.8.10** **Z/IP** **client** **requesting** **a** **node** **to** **interrupt** **Learn** **Mode**


The frame flow for interrupting Learn Mode is shown in Figure 5.12.


Figure 5.12: Z/IP Client interrupting learn mode


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 968




<!-- PAGE 970 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.9** **Network** **management** **basic** **node** **command** **class,** **version** **2**


**5.2.5.9.1** **Compatibility** **considerations**


The Network Management Basic Command Class, version 2 is backwards compatible with Network
CC:004D.02.00.21.001 Management Basic Command Class, version 1. A node supporting Network Management Basic Command Class, version 2 MUST also support Network Management Basic Command Class, version 1.


All commands not mentioned in this version remain unchanged from version 1.


The following commands are introduced to allow a GUI to display the DSK of a S2 node and advertise

interview status:


      - DSK Get Command


      - DSK Report Command


The following commands have been extended to return information about the S2 bootstrapping outcome and the node interview process after activating Learn Mode:


      - Learn Mode Set Command


      - Learn Mode Set Status Command


**5.2.5.9.2** **Learn** **mode** **set** **command**


This command is used to allow a node to be added to (or removed from) the network. When a node
is added to the network, the node is assigned a valid Home ID and NodeID.


This command allows a controlling application to request the transmission of Node Information Frames
(NIFs) in regular intervals until included, removed or until learn mode is disabled again.


CC:004D.02.01.12.001 Learn mode SHOULD be enabled only when necessary, and it SHOULD always be disabled again
as quickly as possible. However, to ensure a successful synchronization of the inclusion process the
device SHOULD be able to stay in learn mode at least 5 seconds.


CC:004D.02.01.11.001 The Learn Mode Set Status Command MUST be returned in response to this command.


CC:004D.02.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:004D.02.01.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.58: Learn Mode Set Command v2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|Command = LEARN_MODE_SET|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Return interview<br>status|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



Fields not described in this version remain unchanged from version 1.


**Return** **Interview** **Status** **(1** **bit)**

This field is used to request that the receiving node returns an additional Learn Mode Set Status
Command when the node interview is completed.


CC:004D.02.01.11.004 The value 0 MUST indicate that the receiving node MUST return a Learn Mode Set Status Command
when the learn mode is over.


The value 1 MUST indicate that the receiving node MUST return a Learn Mode Set Status Command
when learn mode is over and an additional Learn Mode Set Status Command with status set to

LEARN_MODE_INTERVIEW_COMPLETED when the inclusion node interview is over.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 969




<!-- PAGE 971 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


An illustration is given in Figure 5.13.


**5.2.5.9.3** **Learn** **mode** **set** **status** **command**


This command is used to indicate the progress of the Learn Mode Set command.


Table 5.59: Learn Mode Set Status Command v2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|Command = LEARN_MODE_SET_STATUS (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New Node ID|New Node ID|New Node ID|New Node ID|New Node ID|New Node ID|New Node ID|New Node ID|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|



Fields not described in this version remain unchanged from version 1.


**Status** **(8** **bits)**

CC:004D.02.02.11.001 This field indicates the outcome of the learn mode and MUST comply with Table 5.60.


Table 5.60: Learn Mode Status version 2::Status parameter encod






|Value|Table 5.60: Learn Mode ing Identifier|e Status version 2::Status parameter encod- Description|Ver-|
|---|---|---|---|
|**Value**|**Identifer**|**Description**|**Ver-**<br>**sion**|
|0x06|LEARN_MODE_DONE|The learn process is complete and the controller<br>is now included into (or excluded from) the net-<br>work. If the node supports S0 or S2, it indicates<br>that the network inclusion and security boot-<br>strapping were completed successfully (This in-<br>clude the case where the node was granted no<br>S2 key).|1|
|0x07|LEARN_MODE_FAILED|The learn process failed in some general way|1|
|0x09|LEARN_MODE_SECU-<br>RITY_FAILED|The learn process is complete and the node was<br>included in a network but security bootstrap-<br>ping failed. The node is **not** operating securely.|1|
|0x0A|LEARN_MODE_INTER-<br>VIEW_COMPLETED|This<br>status<br>is<br>used<br>to<br>report<br>that<br>the<br>post-inclusion interview is completed after net-<br>work inclusion|2|


**Granted** **Keys** **(8** **bits)**







This field is used to indicate which network keys were granted during bootstrapping.

CC:004D.02.02.11.002 This field MUST be treated as a bitmask and comply with Table 5.85.


**KEX** **Fail** **Type** **(8** **bits)**

This field is used to indicate which error occurred in case S2 bootstrapping was not successful.

CC:004D.02.02.11.003 This field MUST comply with Table 5.86.


**DSK** **(16** **bytes)**

This field is used to indicate the DSK of the including controller that performed S2 bootstrapping to
the node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 970




<!-- PAGE 972 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This information can be used for post inclusion verification.


**5.2.5.9.4** **DSK** **get** **command**


This command is used to request the S2 DSK of a node.


CC:004D.02.08.11.001 The DSK Report Command MUST be returned in response to this command.


CC:004D.02.08.11.002 This command MUST NOT be issued via multicast addressing.


CC:004D.02.08.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.61: DSK Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|Command = DSK_GET (0x08)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Add<br>Mode|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Add** **mode** **(1** **bit)**

This field is used to request the Add Mode or Learn Mode DSK.


S2 Controllers may have 2 key pairs, one static key pair used for Learn mode (being included in a
network) and one dynamic key pair changing at each bootstrapping used for Add mode (including
other nodes in the network).


CC:004D.02.08.11.004 The value 0 MUST indicate that the node MUST return its Learn Mode DSK


The value 1 MUST indicate that the node MUST return its Add Mode DSK:


CC:004D.02.08.11.005 A node not supporting an Add Mode dynamic key pair MUST return its Learn Mode DSK.


**5.2.5.9.5** **DSK** **Report** **Command**


This command is used by a node to advertise its DSK.


Table 5.62: DSK Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_BASIC|
|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|Command = DSK_REPORT (0x09)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Add<br>Mode|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Add** **mode** **(1** **bit)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 971




<!-- PAGE 973 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate if the Add Mode or Learn Mode DSK is advertised in this command.


CC:004D.02.09.11.001 The value 0 MUST indicate that the node advertises its Learn Mode DSK


The value 1 MUST indicate that the node advertises its Add Mode DSK.


**DSK** **(16** **bytes)**

This field is used to transmit the S2 DSK. For details, refer to Section 4.


**5.2.5.9.6** **Use** **cases** **and** **frame** **flows**


**5.2.5.9.7** **Z/IP** **Client** **requesting** **a** **node** **to** **report** **node** **interview** **status**


The frame flow for returning status messages at the end of Learn mode and the end of the post-inclusion
device interview is shown in Figure 5.13.


Figure 5.13: Node advertising the end of the interview process


**5.2.5.10** **Network** **management** **inclusion** **command** **class,** **version** **1**


The Network Management Inclusion Command Class provides functionality only available in a primary
controller, inclusion controller or SIS. Since this is a dynamic property, there is a risk that a remote
host tries to use commands in a controller which has become secondary in the meantime.


**5.2.5.10.1** **Node** **add** **command**


This command is used to activate or de-activate add mode on a controller.



CC:0034.01.01.13.001



The process of adding a node is started by the network management application sending a Node
Add command to a controller. The network management application receives a status message later
on indicating if the inclusion attempt was successful or not. If NWI inclusion was used, the calling
application MAY re-issue this command if more nodes are to be included.



CC:0034.01.01.12.001 The Add Mode SHOULD be disabled after a certain time to avoid adding another node unexpectedly.
It is RECOMMENDED to have a timer that disables the Node Add state after a given time without
any activity.


CC:0034.01.01.11.001 Add Mode MUST be de-activated after any inclusion attempt, even if interrupted.


CC:0034.01.01.11.008


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 972




<!-- PAGE 974 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Node Add Status Command MUST be returned in response to this command unless it is to be
ignored.


CC:0034.01.01.11.003 This command MUST NOT be issued via multicast addressing.


CC:0034.01.01.11.004 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.63: Node Add Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|
|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0034.01.01.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.

This field is use to indicate to the receiving node if the Add Mode must be activated or de-activated.

CC:0034.01.01.11.006 This field MUST comply with Table 5.64.


Table 5.64: Node Add::Mode parameter encoding

|Value|i<br>Identifer|Description|
|---|---|---|
|0x01|ADD_NODE_ANY|Add any type of node to the network.|
|0x05|ADD_NODE_STOP|Stop Add Mode.<br>The command MAY be ignored if Add Mode was not ac-<br>tivated.<br>The command MAY be ignored if network inclusion or<br>security bootstrapping is ongoing.|



Examples of Add Mode activation and deactivation are given in Figure 5.14.


**tx** **Options** **(1** **byte)**


CC:0034.01.01.11.007
The tx Options field allows a controlling node to specify if transmissions MUST use special properties.
This field MUST be treated as a bitmask and MUST comply with Table 5.65.



Table 5.65: Node Add::Tx Options encoding






|Value|l i<br>Option fag identifer|Description|
|---|---|---|
|0x00|ADD_NODE_ANY|Transmit at normal power level without any transmit op-<br>tions.|
|0x02|TRANSMIT_OP-<br>TION_LOW_POWER|Transmit at low output power level (1/3 of normal RF<br>range)|
|0x20|TRANSMIT_OP-<br>TION_EXPLORE|Allow network-wide inclusion|



CC:0034.01.01.12.002 If the Mode is set to NODE_ADD_ANY, it is RECOMMENDED to set this field to TRANSMIT_OPTION_EXPLORE.

CC:0034.01.01.13.002 Installer scenarios with a requirement for more confidential transfer of network security keys MAY
set the flag TRANSMIT_OPTION_LOW_POWER. This requires that the new node is included in
direct range of the including controller.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 973




<!-- PAGE 975 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.10.2** **Node** **add** **status** **command**


This command is used to report the result of the Node Add Command or report that a new node was
included.


Table 5.66: Node Add Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|
|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended –> spanning two bytes for one command class


**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**

CC:0034.01.02.11.001 This field indicates the outcome of the add mode and MUST comply with Table 5.67.



Table 5.67: Node Add Status::Status parameter encoding








|Value|i<br>Status identifer|Description|
|---|---|---|
|0x06|ADD_NODE_STA-<br>TUS_DONE|The new node has been included in the network.<br>If the new node and controller support S0 or S2, it indi-<br>cates that the network inclusion and security bootstrap-<br>ping were completed successfully (This include the case<br>where the node was granted no S2 key).|
|0x07|ADD_NODE_STA-<br>TUS_FAILED|Transmit at low output power level (1/3 of normal RF<br>range)|
|0x09|ADD_NODE_STA-<br>TUS_SECU-<br>RITY_FAILED|Allow network-wide inclusion|



**Reserved**

CC:0034.01.02.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**New** **NodeID** **(1** **byte)**

CC:0034.01.02.11.005 This field MUST indicate the assigned NodeID to the newly added node. This field is valid if Status
is different than NODE_ADD_STATUS_FAILED.

This field MUST be set to 0x00 if no NodeID was assigned to the included node.


**Node** **Info** **Length** **(1** **byte)**


CC:0034.01.02.11.004


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 974




<!-- PAGE 976 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to indicate the length in bytes of the encapsulated Node Information fields. This field
MUST be included in the length calculation. The value MUST indicate the length of the following
fields:

      - Node Info Length (this field)

      - List / Z-Wave Protocol Specific Part

      - Opt Func / Z-Wave Protocol Specific Part


      - Basic Device Class


      - Generic Device Class

      - Specific Device Class


      - Command Class


**List.** **(1** **bit)**


Refer to _Node_ _info_ _cached_ _report_ _command_


**Opt.** **Func.** **(1** **bit)**


Refer to _Node_ _info_ _cached_ _report_ _command_

**Z-Wave** **Protocol** **Specific** **Part**


Refer to _Node_ _info_ _cached_ _report_ _command_


**Basic** **Device** **Class** **(1** **byte)**


Refer to _Node_ _info_ _cached_ _report_ _command_


**Generic** **Device** **Class** **(1** **byte)**


Refer to _Node_ _info_ _cached_ _report_ _command_

**Specific** **Device** **Class** **(1** **byte)**


Refer to _Node_ _info_ _cached_ _report_ _command_


**Command** **Class** **(N** **bytes)**


Refer to _Node_ _info_ _cached_ _report_ _command_


**5.2.5.10.3** **Node** **remove** **command**


This command is used to activate or de-activate node remove mode. The remove operation only works
in direct range between the controller and the node that is to be removed.


CC:0034.01.03.12.001 The Node Remove mode SHOULD be disabled after a certain time to avoid removing another node
unexpectedly. It is RECOMMENDED to have a timer that disables the Node Remove mode after a
given time without any activity.


CC:0034.01.03.11.001 Node Remove mode MUST be de-activated after any removal attempt, even if interrupted.


CC:0034.01.03.11.007 The Node Remove Status Command MUST be returned in response to this command unless it is
ignored.


CC:0034.01.03.11.003 This command MUST NOT be issued via multicast addressing.


CC:0034.01.03.11.004 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 975




<!-- PAGE 977 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.68: Node Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|Command = NODE_REMOVE (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0034.01.03.11.005 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Mode** **(1** **byte)**

CC:0034.01.03.11.006 This field is use to indicate to the receiving node if the node removal process must be activated or
de-activated. This field MUST comply with Table 5.69.



CC:0034.01.03.13.001



Table 5.69: Node Remove::Mode parameter encoding

|Value|i<br>Mode identifer|Description|
|---|---|---|
|0x01|REMOVE_NODE_ANY|Remove any type of node from the network|
|0x05|REMOVE_NODE_STOP|Stop the node removal process.<br>The command MAY be ignored if the remove process was<br>not activated.<br>The command MAY be ignored if network exclusion is<br>ongoing.|



The process of removing a node is started by sending this command with Mode set to REMOVE_NODE_ANY. The removal process is complete when a Node Remove Status command with
status set to NODE_REMOVE_STATUS_DONE is returned.


**5.2.5.10.4** **Node** **remove** **status** **command**


This command is used to advertise the status of a node removal attempt.


Table 5.70: Node Remove Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|Command = NODE_REMOVE_STATUS|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**



CC:0034.01.04.11.001 This field is used to advertise status of a node removal attempt. This field MUST comply with Table
5.71.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 976




<!-- PAGE 978 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 5.71: Status parameter of Node Remove Status encoding






|Value|i<br>Status identifer|Description|
|---|---|---|
|0x06|REMOVE_NODE_STA-<br>TUS_DONE|The node has now been removed and the controller is ready<br>to continue normal operation again.<br>Removed NodeID is returned.|
|0x07|REMOVE_NODE_STA-<br>TUS_FAILED|The remove process failed (no node was removed)|



**NodeID** **(1** **byte)**

This field is used to advertise the NodeID that was attempted to be removed from the network.

CC:0034.01.04.12.001 This field SHOULD be set to 0x00 if no attempt has been made.


**5.2.5.10.5** **Failed** **node** **remove** **command**


This command is used to remove a non-responding node.


A non-responding node is put onto the failed NodeID list by a controller when detected. In case the
CC:0034.01.07.11.001 node responds again at a later stage, it is removed from the failed NodeID list. A node MUST be on
the failed NodeID list and as an extra precaution also fail to respond before it is removed. Responding
nodes MUST NOT be removed.


CC:0034.01.07.11.002 The Failed Node Remove Status Command MUST be returned in response to this command when
the removal attempt has been made.


CC:0034.01.07.11.003 This command MUST NOT be issued via multicast addressing.


CC:0034.01.07.11.004 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.72: Failed Node Remove Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|Command = FAILED_NODE_REMOVE|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0034.01.07.11.005 This field is used to specify the NodeID of the failing node which MUST be removed.


**5.2.5.10.6** **Node** **neighbor** **update** **request** **command**


This command is used to instruct a node with NodeID to perform a Node Neighbor Update operation
in order to update the topology on the controller.


CC:0034.01.0B.11.001 The Node Neighbor Update Status Command MUST be returned in response to this command when
the neighbor search is completed.


CC:0034.01.0B.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.01.0B.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 977




<!-- PAGE 979 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.73: Node Neighbor Update Request Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|Command = NODE_NEIGHBOR_UPDATE_REQUEST|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0034.01.0B.11.004 This field is used to specify the NodeID of the failing node which MUST perform the Node Neighbor
Update operation.


**5.2.5.10.7** **Node** **neighbor** **update** **status** **command**


This command is used to report the status of a Node Neighbor Update operation.


Table 5.74: Node Neighbor Update Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|Command = NODE_NEIGHBOR_UPDATE_STATUS|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**

CC:0034.01.0C.11.001 This field is used to advertise status of the neighbor update operation. This field MUST comply with
Table 5.75.


Table 5.75: Node Neighbor Update Status::Status encoding






|Value|i<br>Status identifer|Description|
|---|---|---|
|0x22|NEIGHBOR_UP-<br>DATE_STATUS_DONE|New neighbor list received|
|0x23|NEIGHBOR_UP-<br>DATE_STATUS_FAIL|Getting new neighbor list failed|



CC:0034.01.0D.11.001



**5.2.5.10.8** **Return** **route** **assign** **command**


This command is used to make a controller assign static return routes (up to 4) to an end node node.
This allows the end nodes to communicate directly with other nodes.

Up to 5 different destinations can be allocated return routes. Attempts to assign new return routes
when all 5 destinations already are allocated will be ignored.


Allocated return routes can only be cleared using the Return Route Delete Command.

The controller calculates the shortest routes from the end node (Source NodeID field) to the destination
node (Destination NodeID field) and transmits the return routes to the end node (Source NodeID
field).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 978




<!-- PAGE 980 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Return Route Assign Complete Command MUST be returned in response to this command when
the route assignment is completed.


CC:0034.01.0D.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.01.0D.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.76: Return Route Assign Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|Command = RETURN_ROUTE_ASSIGN|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Source NodeID|Source NodeID|Source NodeID|Source NodeID|Source NodeID|Source NodeID|Source NodeID|Source NodeID|
|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|Destination NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Source** **NodeID** **(1** **byte)**

This field is used to specify the NodeID of the node which will be assigned the return route.


**Destination** **NodeID** **(1** **byte)**

This field is used to specify the destination NodeID for which the Source NodeID will have a route
assigned.


**5.2.5.10.9** **Return** **route** **assign** **complete** **command**


This command is used to indicate the status of a return route assignment attempt.


Table 5.77: Return Route Assign Complete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|Command = RETURN_ROUTE_ASSIGN_COMPLETE|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**


CC:0034.01.0E.11.001
This field is used to advertise status of the return route assignment attempt. This field MUST comply
with Table 5.78.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 979




<!-- PAGE 981 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.78: Return Route Assign Complete::Status encoding












|Value|i<br>Option identifer|Description|
|---|---|---|
|0x00|TRANSMIT_COM-<br>PLETE_OK|Successfully transmitted|
|0x01|TRANSMIT_COM-<br>PLETE_NO_ACK|No acknowledgement is received before timeout from the<br>destination node. Acknowledgement is discarded in case<br>it is received after the time out.|
|0x02|TRANSMIT_COM-<br>PLETE_FAIL|Not possible to transmit data because the Z-Wave network<br>is busy (jammed).|
|0x03|N/A|Reserved|
|0x04|TRANSMIT_COM-<br>PLETE_NOROUTE|No route found to assign to the destination. No frame was<br>transmitted.|
|0x05|TRANSMIT_COM-<br>PLETE_VERIFIED|This status code is identical to 0x00. The route was suc-<br>cessfully transmitted.|



**5.2.5.10.10** **Return** **route** **delete** **command**


This command is used to make a controller delete all static return routes from an end node. Allocated

return routes can only be removed using this command. All return routes are cleared when using this
command.


CC:0034.01.0F.12.001 After issuing this command, an application SHOULD issue Return Route Assign Commands to create
return routes for all relevant associations.


CC:0034.01.0F.11.001 The Return Route Delete Complete Command MUST be returned in response to this command.


CC:0034.01.0F.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.01.0F.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.79: Return Route Delete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|Command = RETURN_ROUTE_DELETE (0x0F)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**NodeID** **(1** **byte)**

CC:0034.01.0F.11.004 This field is used to specify the NodeID of which the return routes MUST be deleted.


**5.2.5.10.11** **Return** **route** **delete** **complete** **command**


This command is used to indicate the status of a return route deletion attempt.


Table 5.80: Return Route Delete Complete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|Command = RETURN_ROUTE_DELETE_COMPLETE (0x10)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 980




<!-- PAGE 982 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Status** **(1** **byte)**

CC:0034.01.10.11.001 This field is used to advertise status of the return route deletion attempt. This field MUST comply
with Table 5.81.


Table 5.81: Return Route Delete Complete::Status encoding








|Value|i<br>Option identifer|Description|
|---|---|---|
|0x00|TRANSMIT_COM-<br>PLETE_OK|Successfully transmitted|
|0x01|TRANSMIT_COM-<br>PLETE_NO_ACK|No acknowledgement is received before timeout from the<br>destination node. Acknowledgement is discarded in case<br>it is received after the time out.|
|0x02|TRANSMIT_COM-<br>PLETE_FAIL|Not possible to transmit data because the Z-Wave network<br>is busy (jammed).|



**5.2.5.10.12** **Use** **cases** **and** **frame** **flows**


**5.2.5.10.13** **Z/IP** **Client** **requesting** **a** **node** **to** **interrupt** **Add** **Mode**


The frame flow for interrupting Add Mode is shown in Figure 5.14.


Figure 5.14: Z/IP Client requesting a node to interrupt Add Mode


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 981




<!-- PAGE 983 -->

CC:0034.02.00.21.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.11** **Network** **management** **inclusion** **command** **class,** **version** **2**


**5.2.5.11.1** **Compatibility** **considerations**


The Network Management Inclusion Command Class, version 2 is backwards compatible with Network
Management Inclusion Command Class, version 1. A node supporting Network Management Inclusion
Command Class, version 2 MUST also support Network Management Inclusion Command Class,
version 1.


All commands not mentioned in this version remain unchanged from version 1.


The following commands are introduced to support the multiple security keys and DSK functionalities
of the Security 2 Command Class:


 - Node Add Keys Report Command


 - Node Add Keys Set Command


 - Node Add DSK Report Command


 - Node Add DSK Set Command


The following command has been extended to support the new S2/inclusion controller bootstrapping

process:


 - Node Add Command


 - Node Add Status Command


 - Failed Node Replace Command


 - Failed Node Replace Status Command

Use-cases and frames flows for the new functionalities of this Command Class are shown in _Use_ _cases_
_and_ _frame_ _flows_ .


**5.2.5.11.2** **Node** **add** **command**


This command is used to add nodes to the Z-Wave network.



CC:0034.02.01.11.005 The Node Add Status Command MUST be returned in response to this command unless it is to be
ignored.


CC:0034.02.01.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.02.01.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.82: Node Add Command V2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|Command = NODE_ADD (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|
|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|



Fields not described in this version remain unchanged from version 1.


**Mode** **(1** **byte)**

This field is use to indicate to the receiving node which mode to use for the inclusion of a new node.
CC:0034.02.01.11.004 This field MUST comply with Table 5.83.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 982




<!-- PAGE 984 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.83: Encoding of Node Add :: Mode parameter






|Value|i<br>Identifer|Description|Ver-<br>sion|
|---|---|---|---|
|0x01|NODE_ADD_ANY|Add any type of node to the network and allow<br>Security 0 bootstrapping|1|
|0x05|NODE_ADD_STOP|Stop Add Mode.<br>The command MAY be ignored if Add Mode<br>was not activated.<br>The command MAY be ignored if network in-<br>clusion or security bootstrapping is ongoing|1|
|0x07|NODE_ADD_ANY_S2|Not possible to transmit data because the<br>Z-Wave network is busy (jammed).|2|



Examples of Add Mode activation and deactivation are also given in _Z/IP_ _Client_ _requesting_ _a_ _node_ _to_
_interrupt_ _Add_ _Mode_ .


**5.2.5.11.3** **Node** **add** **status** **command**


This command is used to report the result of a node inclusion.


Table 5.84: Node Add Status Command V2

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|
|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|



*) Command classes may be extended –> spanning two bytes for one command class


Fields not described in this version remain unchanged from version 1.


**Command** **Class** **(N** **bytes)**


Refer to _Node_ _info_ _cached_ _report_ _command_ and Table 5.27.


CC:0034.02.02.11.001 The Security Command Class Mark (0xF100) MUST indicate command classes supported using the
highest listed Security Key in the Granted Key field value.


**Granted** **Keys** **(8** **bits)**

This field is used to indicate which network keys were granted during bootstrapping.

CC:0034.02.02.11.002 This field MUST be treated as a bitmask and comply with Table 5.85


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 983




<!-- PAGE 985 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.85: Node Add Status::Granted keys encoding


**KEX** **Fail** **Type** **(8** **bits)**

|Bit|Description|
|---|---|
|0|Indicates the Unauthenti-<br>cated Security Class Key|
|1|Indicates the Authenticated<br>Security Class Key|
|2|Indicates the Access Con-<br>trol Security Class Key|
|7|Indicates<br>the<br>Security<br>0<br>Network Key|


This field is used to indicate which error occurred in case S2 bootstrapping was not successful.

This field MUST comply with Table 5.86.

CC:0034.02.02.11.003


Table 5.86: Node Add Status::Kex Fail Type encoding








|Value|i<br>KEX Fail Type Identifer|Description|
|---|---|---|
|0x00|•|Bootstrapping was successful|
|0x01|KEX_FAIL_KEX_KEY|Key failure indicating that no match exists between re-<br>quested/granted keys in the network.|
|0x02|KEX_FAIL_KEX_SCHEM|EScheme failure indicating that no scheme is supported by<br>controller or joining node specifed an invalid scheme.|
|0x03|KEX_FAIL_KEX_CURVE|S Curve failure indicating that no curve is supported by con-<br>troller or joining node specifed an invalid curve.|
|0x05|KEX_FAIL_DECRYPT|Node failed to decrypt received frame.|
|0x06|KEX_FAIL_CANCEL|User has cancelled the S2 bootstrapping.|
|0x07|KEX_FAIL_AUTH|The Echo KEX Set/Report frame did not match the earlier<br>exchanged frame.|
|0x08|KEX_FAIL_KEY_GET|The joining node has requested a key, which was not<br>granted by the including node at an earlier stage.|
|0x09|KEX_FAIL_KEY_VER-<br>IFY|Including node failed to decrypt and hence verify the re-<br>ceived frame encrypted with exchanged key.|
|0x0A|KEX_FAIL_KEY_RE-<br>PORT|The including node has transmitted a frame containing a<br>diferent key than what is currently being exchanged.|



**5.2.5.11.4** **Node** **add** **keys** **report** **command**


This command is used to inform which S2 keys have been requested during S2 bootstrapping.


CC:0034.02.11.11.001 The Node Add Keys Set Command MUST be returned in response to this command.


CC:0034.02.11.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.02.11.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.87: Node Add Keys Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|Command = NODE_ADD_KEYS_REPORT (0x11)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Request<br>CSA|
|Requested Keys|Requested Keys|Requested Keys|Requested Keys|Requested Keys|Requested Keys|Requested Keys|Requested Keys|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 984




<!-- PAGE 986 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Request** **CSA** **(1** **bit)**

This field is used to indicate if the joining node is requesting CSA (Client-Side Authentication, refer
to Section 4).


CC:0034.02.11.11.004 The value 1 MUST indicate that the node requests CSA.


The value 0 MUST indicate that the node does not request CSA.


**Requested** **Keys** **(1** **bytes)**

This field is used to advertise the requested keys by the joining node.

CC:0034.02.11.11.005 This field MUST be treated as a bitmask and comply with Table 5.85

CC:0034.02.12.11.004 This field MUST be set to 0x00 if the Accept field is set to 0.


**Accept** **(1** **bit)**

This field is used to indicate if the S2 bootstrapping process is accepted by the user and must continue.


CC:0034.02.12.11.005 The value 0 MUST indicate that the S2 bootstrapping is not accepted and MUST be interrupted.
The value 1 MUST indicate that the S2 bootstrapping is accepted and MUST continue.


**5.2.5.11.5** **Node** **add** **DSK** **report** **command**


This command is used to report the DSK of the node being S2 bootstrapped and indicates whether
an input is needed for node authentication.


CC:0034.02.13.11.001 The Node Add DSK Set Command MUST be returned in response to this command.


CC:0034.02.13.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.02.13.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.88: Node Add DSK Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|Command = NODE_ADD_DSK_REPORT|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Input DSK Length|Input DSK Length|Input DSK Length|Input DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|DSK 16|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**Input** **DSK** **Length** **(4** **bits)**


CC:0034.02.13.11.004
This field is used to indicate how many DSK bytes MUST be input as a minimum to authenticate the
node being included.


CC:0034.02.13.11.005 The value 0 MUST indicate that no user input is necessary (e.g. Unauthenticated Security Class or
CSA has been granted).


**DSK** **(16** **bytes)**

This field is used to transmit the DSK of the node being S2 bootstrapped. Refer to Section 4.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 985




<!-- PAGE 987 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.11.6** **Node** **add** **DSK** **set** **command**


This command is used to indicate the S2 bootstrapping controller if the DSK is accepted and report
the user input when needed.


Table 5.89: Node Add DSK Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|Command = NODE_ADD_DSK_SET|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Accept|Reserved|Reserved|Reserved|Input DSK Length|Input DSK Length|Input DSK Length|Input DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Input** **DSK** **Length** **(4** **bits)**

This field indicates the length in bytes of the DSK input by the user.


CC:0034.02.14.11.001
This field MUST be set to the same or a higher value than the ”Input DSK Length” field value received
in the Node Add DSK Report Command that caused this command to be returned.


CC:0034.02.14.11.002 The value 0 MUST indicate that no user input has been done (e.g. Unauthenticated Security Class,
CSA has been granted or user refused to input DSK).


**Input** **DSK** **(N** **bytes)**

CC:0034.02.14.11.003 This field indicates the DSK input by the user. A receiving node (Z/IP gateway) MUST overwrite
the part of the DSK with the Input DSK contained in this frame

CC:0034.02.14.11.004 The length of this field in bytes MUST be according to the Input DSK Length field value. If the Input
DSK Length is set to 0, this field MUST be omitted.


**Accept** **(1** **bit)**

This field is used to indicate if the DSK Report is accepted by the user and if S2 bootstrapping must
continue.


CC:0034.02.14.11.005 The value 0 MUST indicate that the DSK Report is not accepted and S2 bootstrapping MUST be
interrupted.


The value 1 MUST indicate that the DSK Report is accepted and S2 bootstrapping MUST continue.


**5.2.5.11.7** **Failed** **node** **replace** **command**


This command is used to replace a non-responding node with a new one in having the same NodeID.


CC:0034.02.09.11.005 The Failed Node Replace Status Command MUST be returned in response to this command unless
it is to be ignored.


CC:0034.02.09.11.002 This command MUST NOT be issued via multicast addressing.


CC:0034.02.09.11.003 A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 986




<!-- PAGE 988 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.90: Failed Node Replace Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|Command = FAILED_NODE_REPLACE|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|
|…|…|…|…|…|…|…|…|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|



Fields not described in this version remain unchanged from version 1.


**Mode** **(1** **byte)**

This field indicates the type of operation for the failed replace process.

CC:0034.02.09.11.004 This field MUST comply with Table 5.91



CC:0034.02.09.13.001



Table 5.91: Failed Node Replace::Mode encoding



|Value|i<br>Identifer|Description|Ver-<br>sion|
|---|---|---|---|
|0x01|START_FAILED_NODE_<br>PLACE|RE-<br>Initiate a failed node replace process.|1|
|0x05|STOP_FAILED_NODE_R<br>PLACE|E-<br>Cancel a failed node replace process.<br>The command MAY be ignored if no replaced<br>failed process is active.<br>The command MAY be ignored if network in-<br>clusion is ongoing|1|
|0x07|START_FAILED_NODE_<br>PLACE_S2|RE-<br>Initiate a failed node replace process and allow<br>S2 bootstrapping for the new node|2|


**5.2.5.11.8** **Failed** **node** **replace** **status** **command**


This command is used to indicate the progress of the Replace Failed Node Command.





Table 5.92: Failed Node Replace Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|Command = FAILED_NODE_REPLACE_STATUS|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|Node ID|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|



Fields not described in this version remain unchanged from version 1.


**Granted** **Keys** **(8** **bits)**

This field is used to indicate which network keys were granted during bootstrapping.

CC:0034.02.0A.11.001 This field MUST be treated as a bitmask and comply with Table 5.85


**KEX** **Fail** **Type** **(8** **bits** **)**


Refer to _Node_ _add_ _status_ _command_ and Table 5.86


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 987




<!-- PAGE 989 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.11.9** **Use** **cases** **and** **frame** **flows**


**5.2.5.11.10** **Z/IP** **Client** **with** **SIS** **or** **Primary** **controller** **including** **an** **S2** **node**


The frame flow for an S2 capable node inclusion using the Network Management Inclusion Command
Class is shown in Figure 5.15.


Figure 5.15: Node inclusion with a SIS/Primary controller


**5.2.5.11.11** **Z/IP** **Client** **with** **an** **S2** **inclusion** **controller** **including** **an** **S2** **node**


When performing S2 bootstrapping, the unsolicited destination of the Z/IP Gateway will receive a
unsolicited Node Add S2 Keys Report from the Z/IP Gateway. The Z/IP Client at this point has two
options:


CC:0034.02.00.11.001 1. Automatically grant requested S2 Classes without presenting a user dialog in the S2 Keys Report
step. In this case, the Z/IP Client MUST present a user dialog in next step before sending the
DSK Set



CC:0034.02.00.11.002


CC:0034.02.00.13.001



2. Using advanced joining where the user MUST confirm the specific keys being requested in a
dialog, before continuing to next step. In this case, the Z/IP MAY present a user dialog in next
step before sending the DSK Set, if required by the S2 Classes being granted.


This is done without the SIS having entered Add Node mode. From this point on the S2 inclusion
frame flow is same as when including through the SIS.

The frame flow for the node inclusion when an S2 capable inclusion controller has been used for
including a new S2 capable node is shown in Figure 5.16.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 988




<!-- PAGE 990 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.16: Node inclusion with an S2 inclusion controller


**5.2.5.11.12** **Z/IP** **client** **with** **an** **S2** **inclusion** **controller** **including** **an** **S0** **node**


The unsolicited destination of the Z/IP Gateway will receive an unsolicited Node Add Status Report
CC:0034.02.00.13.002 from the Z/IP Gateway. The unsolicited destination Z/IP Client MAY show a dialog informing that
a node was included by an inclusion controller.

The frame flow for an S0 capable node inclusion using an S2 capable inclusion controller including is
shown in Figure 5.17.


Figure 5.17: S0 node inclusion with an S2 inclusion controller


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 989




<!-- PAGE 991 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.12** **Network** **management** **inclusion** **command** **class,** **version** **3**


**5.2.5.12.1** **Compatibility** **considerations**


The Network Management Inclusion Command Class, version 3 is backwards compatible with the
Network Management Inclusion Command Class, version 2.


CC:0034.03.00.21.001 A node supporting the Network Management Inclusion Command Class, version 2 MUST also support
the Network Management Inclusion Command Class, version 2.

CC:0034.03.00.21.002 All commands and fields not mentioned in this version MUST remain unchanged from version 2.


The following command has been extended to support the report of a Smart Start node:


      - Node Add Status Command


The following commands are introduced in order to support the Smart Start functionality:


      - Included Node Information Frame Report Command


      - Smart Start Join Started Command

CC:0034.03.00.21.003 Frame flows for the new functionalities of this Command Class are shown in “ref” _network_proto-_
_col_command_classes-command_class_definitions-network_management_command_classes-network_management__
A Z/IP Gateway MUST comply with _Network_ _management_ _inclusion_ _command_ _class,_ _version_ _3_ .


CC:0034.03.00.21.004 A supporting node MUST issue the Node Add Status Command, Included Node Information Frame
Report Command and the Smart Start Join Started Command to the first and the second unsolicited
destinations.


**5.2.5.12.2** **Command** **class** **dependencies**


CC:0034.03.00.21.005 A node supporting the Network Management Inclusion Command Class, version 3 MUST also support
the Node Provisioning Command Class, version 1.


**5.2.5.12.3** **Node** **add** **status** **command**


This command is used to report the result of the Node Add Command or report that a new node was
included.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 990




<!-- PAGE 992 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.93: Node Add Status Command V3

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|Command = NODE_ADD_STATUS (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|
|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK L|DSK L|DSK L|DSK L|DSK L|DSK L|DSK L|DSK L|



CC:0034.03.02.11.001 Fields not described below MUST remain unchanged from version 2.


**Status** **(8** **bits)**

CC:0034.03.02.11.002 This field indicates the outcome of the add mode and MUST comply with Table 5.94.



Table 5.94: Node Add Status::Status parameter encoding V3





|Value|i<br>Status identifer|Description|Ver-<br>sion|
|---|---|---|---|
|0x06|ADD_NODE_STA-<br>TUS_DONE|The new node has been included in the network.<br>If the new node and controller support S0 or S2,<br>it indicates that the network inclusion and secu-<br>rity bootstrapping were completed successfully.<br>(This includes the case where the node was<br>granted no S2 key)|1|
|0x07|ADD_NODE_STA-<br>TUS_FAILED|The process failed, no new node was added in<br>the network.<br>Version 3: This status is also used if the node<br>failed a smart start inclusion and has been re-<br>moved. In this case, it may attempt the inclu-<br>sion again.|1|
|0x09|ADD_NODE_STA-<br>TUS_SECU-<br>RITY_FAILED|Node has been included but the security boot-<br>strapping failed|1|


**DSK** **Length** **(5** **bits)**







CC:0034.03.02.11.003 This field MUST indicate the length of the DSK field in bytes.

CC:0034.03.02.11.004 This field MUST be set to 0 if the added node does not support the S2 Command Class.

CC:0034.03.02.11.005 This field MUST be set to 16 if the added node supports the S2 Command Class.


**DSK** **(L** **bytes)**


CC:0034.03.02.11.006


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 991




<!-- PAGE 993 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST advertise the DSK of the node that has been added to the network.

CC:0034.03.02.11.007 The length of this field (in bytes) MUST be according to the DSK Length field value. This field
MUST be omitted if the DSK Length field is set to 0.


**5.2.5.12.4** **Included** **node** **information** **frame** **report** **command**


CC:0034.03.19.11.006
This command MUST be sent to the (first and second) unsolicited destinations when an Included NIF
(INIF) is received and the following conditions are fulfilled:


      - The advertised NHID matches an entry in the provisioning list

      - The advertised HomeID is different than the current network HomeID.


CC:0034.03.19.11.007 A node issuing this command MUST subsequently issue a Node Provisioning Report Command for
the matched entry in the provisioning list.


With the two commands, a Z/IP client can use the relevant information to guide the user on how to
perform a reset operation on the device.


Table 5.95: Included Node Information Frame Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|Command = INCLUDED_NIF_REPORT (0x19)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0034.03.19.11.002 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**DSK** **Length** **(5** **bits)**

CC:0034.03.19.11.008 This field MUST indicate the length of the DSK field in bytes.

CC:0034.03.19.11.009 This field MUST be set to 16.


**DSK** **(N** **bytes)**

CC:0034.03.19.11.00A This field MUST advertise the DSK of the provisioning list entry that has been matched from the
NHID in the received INIF.

CC:0034.03.19.11.00B The length of this field (in bytes) MUST be according to the DSK Length field value.


**5.2.5.12.5** **Smart** **start** **join** **started** **command**


CC:0034.03.15.11.001 This command MUST be sent to the (first and second) unsolicited destinations when a Smart Start
inclusion starts.


CC:0034.03.15.11.002 The Add Node Status Command MUST be issued after the Smart Start inclusion and S2 bootstrapping
attempts took place.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 992




<!-- PAGE 994 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.96: Smart Start Join Started Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|Command = SMART_START_JOIN_STARTED_REPORT (0x15)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0034.03.15.11.003 This field MUST indicate the length of the DSK field in bytes.

CC:0034.03.15.11.004 This field MUST be set to 16.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the Provisioning List entry which starts the Smart Start
inclusion process.

CC:0034.03.15.11.005 The length of this field (in bytes) MUST be according to the DSK Length field value.


**5.2.5.12.6** **Usage** **and** **frame** **flows**


**5.2.5.12.7** **Z/IP** **Gateway** **adding** **a** **smart** **start** **node** **that** **is** **on** **the** **provisioning** **list**


The frame flow for a Smart Start inclusion of a node previously added on the provisioning list is shown
in Figure 5.18.


Figure 5.18: Smart Start inclusion


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 993




<!-- PAGE 995 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.12.8** **Z/IP Gateway adding a smart start node that is subsequently added on the provisioning**
**list**


The frame flow for a Smart Start inclusion of a node subsequently added on the provisioning list is
shown in Figure 5.19.


Figure 5.19: Smart Start inclusion (2)


**5.2.5.12.9** **Z/IP Gateway receiving an INIF from a node (the provisioning list) included in another**
**network**


The frame flow for a Smart Start inclusion of a node included in another network is shown in Figure
5.20.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 994




<!-- PAGE 996 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.20: Smart Start inclusion (3)


**5.2.5.12.10** **Z/IP** **Gateway** **including** **an** **S2** **only** **node** **that** **is** **on** **the** **provisioning** **list**


The frame flow for an S2 only node (non-Smart Start) inclusion is shown in Figure 5.21. The Z/IP
Client can decide to automatically grant the requested S2 keys or ask the user for confirmation.


Figure 5.21: S2 Only Node inclusion with user interaction


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 995




<!-- PAGE 997 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.13** **Network** **management** **inclusion** **command** **class,** **version** **4**


**5.2.5.13.1** **Compatibility** **considerations**


The Network Management Inclusion Command Class, version 4 is backwards compatible with the
Network Management Inclusion Command Class, version 3.


A node supporting the Network Management Inclusion Command Class, version 4 MUST also support
the Network Management Inclusion Command Class, version 3.

All commands and fields not mentioned in this version MUST remain unchanged from version 3.


This version of the Network Management Inclusion Command Class introduces support for the Z-Wave
Long Range protocol. The following commands are updated:


 - Node Remove Status Command


 - Failed Node Remove Command


 - Failed Node Remove Status Command


The following command is added:


 - Extended Node Add Status Command


**5.2.5.13.2** **Command** **class** **dependencies**


A node supporting the Network Management Inclusion Command Class, version 4 MUST also support
the Node Provisioning Command Class, version 1.


A node supporting the Network Management Inclusion Command Class, version 4 MUST also support
the Node Provisioning Bootstrapping Mode TLV (type=0x36) with value set to 0x02 (Z-Wave Long
Range SmartStart Bootstrapping)


Node remove status command


This command is used to advertise the status of a node removal attempt.


Table 5.97: Node Remove Status Command V4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|Command = NODE_REMOVE_STATUS (0x04)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



Fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field is used to advertise the NodeID that was attempted to be removed from the network.

This field SHOULD be set to 0x00 if no attempt has been made.

This field MUST be set to 0xFF if the removed NodeID is greater than 255.


**Extended** **NodeID** **(2** **bytes)**

This field is used to advertise the NodeID that was attempted to be removed from the network.

This field MUST be set to the actual NodeID that was attempted to be removed from the network.

This field SHOULD be set to 0x00 if no attempt has been made.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 996




<!-- PAGE 998 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.13.3** **Failed** **node** **remove** **command**


This command is used to remove a non-responding node.


A non-responding node is put onto the failed NodeID list by a controller when detected. In case the
node responds again at a later stage, it is removed from the failed NodeID list. A node MUST be on
the failed NodeID list and as an extra precaution also fail to respond before it is removed. Responding
nodes MUST NOT be removed.


The Failed Node Remove Status Command MUST be returned in response to this command when
the removal attempt has been made.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods.


Table 5.98: Failed Node Remove Command V4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|Command = FAILED_NODE_REMOVE (0x07)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**

This field is used to specify the NodeID of the failing node which MUST be removed.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the _Extended_ _NodeID_
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to specify the NodeID of the failing node which MUST be removed.

If the _NodeID_ field is in the range 0x00..0xFE, this field MUST be set to the same value as the NodeID
field by a sending node.

If the _NodeID_ field is set to 0xFF, this field MUST indicate the NodeID of the failing node which
MUST be removed.


**5.2.5.13.4** **Failed** **node** **remove** **status** **command**


This command is used to report the results of a failed node removal attempt.


Table 5.99: Failed Node Remove Status Command V4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|Command = FAILED_NODE_REMOVE_STATUS (0x08)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



All fields not described below MUST remain unchanged from version 3.


**NodeID** **(1** **byte)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 997




<!-- PAGE 999 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to specify the NodeID of the failing node which was attempted to be removed.

If this field is set to 0xFF, it MUST indicate that the NodeID is indicated in the _Extended_ _NodeID_
field.


**Extended** **NodeID** **(2** **bytes)**

This field is used to specify the NodeID of the failing node which was attempted to be removed.

If the _NodeID_ field is in the range 0x00..0xFE, this field MUST be set to the same value as the _NodeID_
field by a sending node.

If the _NodeID_ field is set to 0xFF, this field MUST indicate the NodeID of the failing node which was
attempted to be removed.


**5.2.5.13.5** **Extended** **node** **add** **status** **command**


This command is used to report the result of a node inclusion.


Table 5.100: Extended Node Add Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_INCLUSION|
|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|Command = EXTENDED_NODE_ADD_STATUS (0x16)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|Assigned NodeID (MSB)|
|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|Assigned NodeID (LSB)|
|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|
|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|Granted Keys|
|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|KEX Fail Type|



Fields not described below MUST be identical to the _Node_ _add_ _status_ _command_


**Assigned** **NodeID** **(2** **bytes)**

This field MUST indicate the assigned NodeID to the newly added node. This field’s value is valid
only if the Status field is set to ADD_NODE_STATUS_DONE.

This field MUST be set to 0x00 if no new NodeID was assigned to an included node.


**Status** **(1** **byte)**

This field is used to indicate the outcome of the SmartStart inclusion and MUST be encoded according
to Table 5.103.








|Value|Table 5.101: Extended ing Status identifier|Node Add Status::Status parameter encod- Description|
|---|---|---|
|**Value**|**Status identifer**|**Description**|
|0x06|ADD_NODE_STA-<br>TUS_DONE|The inclusion was successful and the node is ready to op-<br>erate|
|0x07|ADD_NODE_STA-<br>TUS_FAILED|The inclusion had an error, the joining node should have<br>reset and no new node is part of the network.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 998




<!-- PAGE 1000 -->

CC:0054.01.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.13.6** **Usage** **and** **frame** **flows**


**5.2.5.13.7** **Z/IP** **Gateway** **including** **a** **SmartStart** **with** **extended** **nodeID**


An example of a frame flow for a Z/IP Gateway including a node using an Extended NodeID is show
in Figure 5.22.


If an entry is set to be bootstrapped using Z-Wave Long Range SmartStart, a Z/IP Gateway MUST
issue the Extended Node Add Status Command when the inclusion is complete.


Node Add Status Command MUST be used only for Z-Wave S2 or Z-Wave SmartStart inclusions


Figure 5.22: Extended NodeID SmartStart inclusion


**5.2.5.14** **Network** **management** **primary** **command** **class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **BEEN** **OBSOLETED** New implementations
MUST NOT support this Command Class.


The Network Management Primary Command Class provides functions to pass on the primary role
to another controller.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 999




<!-- PAGE 1001 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.14.1** **Controller** **change** **command**


This command is used to add a controller node to the network and assign the primary controller role
to the included controller.


This command has the same functionality as Node Add with the exception that the new controller
will become the primary controller and the controller adding the node will become secondary.


CC:0054.01.01.11.001 The Controller Change Status Command MUST be returned in response to this command.


CC:0054.01.01.11.002 This command MUST NOT be issued via multicast addressing.


A receiving node MUST ignore this command if it is received via multicast addressing. The Z-Wave
Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point destination are all
considered multicast addressing methods


Table 5.102: Controller Change Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|
|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|Command = CONTROLLER_CHANGE|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|
|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|tx Options|



**Seq** **No** **(1** **byte)**


Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0054.01.01.11.004 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Mode** **(1** **byte)**

This field is use to indicate to the receiving node if the controller change mode must be activated or
CC:0054.01.01.11.005 de-activated. This field MUST comply with Table 5.103.



Table 5.103: Controller Change::Mode encoding






|Value|i<br>Mode identifer|Description|
|---|---|---|
|0x02|CON-<br>TROLLER_CHANGE_STA|RT<br>Start the process of creating a new primary controller for<br>the network|
|0x05|CON-<br>TROLLER_CHANGE_STO|P<br>Stop the controller change and report a failure|



**tx** **Options** **(1** **byte)**

CC:0054.01.01.11.006 The tx Options field allows a controlling node to specify if transmissions MUST use special properties..
This field MUST be treated as a bitmask and MUST comply with Table 5.104



Table 5.104: Controller Change::Tx Options encoding






|Value|i<br>Mode identifer|Description|
|---|---|---|
|0x00|NULL|Transmit at normal power level without any transmit op-<br>tions.|
|0x02|TRANSMIT_OP-<br>TION_LOW_POWER|Transmit at low output power level (1/3 of normal RF<br>range)|
|0x20|TRANSMIT_OP-<br>TION_EXPLORE|Resolve new routes via explorer discovery if existing routes<br>fail|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1000




<!-- PAGE 1002 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.14.2** **Controller** **change** **status** **command**


This command is used to advertise the outcome of the Controller Change attempt.


Table 5.105: Controller Change Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|Command Class = COMMAND_CLASS_NETWORK_MANAGEMENT_PRIMARY|
|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|Command = CONTROLLER_CHANGE_STATUS|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Status|Status|Status|Status|Status|Status|Status|Status|
|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|
|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|New NodeID|
|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|Node Info Length<br>|
|List.|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|Z-Wave Protocol Specifc Part<br>|
|Opt.<br>Func.|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|Z-Wave Protocol Specifc Part|
|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|Basic Device Class|
|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|Generic Device Class<br>|
|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|Specifc Device Class|
|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|Command Class 1 *)|
|…|…|…|…|…|…|…|…|
|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|Command Class N *)|



*) Command classes may be extended –> spanning two bytes for one command class

For fields’ description, refer to _Node_ _add_ _status_ _command_ .


**5.2.5.15** **Network** **management** **installation** **and** **maintenance** **command** **class,** **version** **1**


The Network Management Installation and Maintenance Command Class is used to access statistical
data. Data relating to the transmission of an actual frame may be obtained via the Z/IP Packet
Installation and Maintenance Header Extension.


      - **–** **All** **Transmissions** **/** **Route** **Information:**


**–** **Packet** **Error** **Count** **(PEC)** – Also sometimes referred to as PER. The number of
unsuccessful transmissions experienced by the device.

**–** **Transmission** **Counter** **(TC)** – Number of frames sent by the specified device.

**–** **Neighbors** **(NB)** – Information on known neighbors for a specified device.


**–** **Network** **Management** **-** **Priority** **Route** **Set**


**–** **Network** **Management** **-** **Priority** **Route** **Get**


**–** **Network** **Management** **-** **Priority** **Route** **Report**


**5.2.5.15.1** **Priority** **route** **set**


This command is used to set the network route to use when sending commands to the specified
NodeID.


CC:0067.01.01.12.001 The use of this command is NOT RECOMMENDED.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1001




<!-- PAGE 1003 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.106: Priority Route Set

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|COMMAND = PRIORITY_ROUTE_SET|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|Repeater 1 [First repeater]|
|Repeater 2|Repeater 2|Repeater 2|Repeater 2|Repeater 2|Repeater 2|Repeater 2|Repeater 2|
|Repeater 3|Repeater 3|Repeater 3|Repeater 3|Repeater 3|Repeater 3|Repeater 3|Repeater 3|
|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|Repeater 4 [Last repeater]|
|Speed|Speed|Speed|Speed|Speed|Speed|Speed|Speed|



**NodeID** **(1** **byte)**

CC:0067.01.01.11.001 This field is used to specify the destination NodeID for which a last working route MUST be set.


**Repeater** **(4** **bytes)**

This field is used to specify repeaters for the route. Each byte represents a NodeID and the first field
(Repeater 1) is the first repeater of the route.


CC:0067.01.01.11.002 The value 0x00 MUST indicate that the byte does not represent a repeater. If the route is shorter
than four repeaters, unused repeaters fields MUST be set to 0x00. If Repeater 1 is set to 0x00, it
means that the Last Working Route is direct (nodes are within direct reach).


**Speed** **(1** **byte)**

CC:0067.01.01.11.003 This field is used to indicate which speed MUST be used for the route. This field MUST comply with
Table 5.107.


Table 5.107: IME Speed Encoding


**5.2.5.15.2** **Priority** **route** **get**

|Value|Speed|
|---|---|
|0x01|9.6 kbit/sec|
|0x02|40 kbit/sec|
|0x03|100 kbit/sec|



This command is used to query the current network route from a node for a given destination.


CC:0067.01.02.11.001 The Priority Route Report MUST be returned in response to this command.


CC:0067.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0067.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.108: Priority Route Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|COMMAND = PRIORITY_ROUTE_GET|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**NodeID** **(1** **byte)**

This field is used to specify the NodeID destination for which the current network route is requested.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1002




<!-- PAGE 1004 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.15.3** **Priority** **route** **report**


This command is used to advertise the current network route in use for an actual destination NodeID.


Table 5.109: Priority Route Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|COMMAND = PRIORITY_ROUTE_REPORT|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Type|Type|Type|Type|Type|Type|Type|Type|
|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|Repeater 1 - 1 [First repeater]|
|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|Repeater 2 – 1|
|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|Repeater 3 – 1|
|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|Repeater 4 - 1 [Last repeater]|
|Speed -1|Speed -1|Speed -1|Speed -1|Speed -1|Speed -1|Speed -1|Speed -1|



**Type** **(1** **byte)**

CC:0067.01.03.11.001 This field is used to indicate the route type. It MUST comply with Table 5.110. A node MUST return
the route with the highest priority value if several routes are available at the node.



CC:0067.01.03.11.002



Table 5.110: Route Type Encoding



|Value|i<br>Identifer|Description|Prior-<br>ity|
|---|---|---|---|
|0x00|–|There is no route defned for the target NodeID.<br>In this case, the Repeater and Speed felds<br>MUST be set to 0x00 and ignored by a receiving<br>node.|4 (low-<br>est)|
|0x01|ZW_PRIOR-<br>ITY_ROUTE_ZW_LWR|The returned route is a last working route. The<br>Last Working route is the last successful route<br>used between the sender and receiver.|2|
|0x02|ZW_PRIOR-<br>ITY_ROUTE_ZW_NLWR|The returned route is a next to last working<br>route.<br>It is a route which was Last Working Route and<br>has been replaced by a new route.|3|
|0x10|ZW_PRIOR-<br>ITY_ROUTE_APP_PR|The returned has been determined by the appli-<br>cation|1<br>(high-<br>est)|


**Repeater** **(4** **bytes)**


Refer to _Priority_ _route_ _set_ .


**Speed** **(1** **byte)**


Refer to _Priority_ _route_ _set_ .







© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1003




<!-- PAGE 1005 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.15.4** **Statistics** **get**


This command is used to query Installation and Maintenance statistics from a node.


CC:0067.01.04.11.001 The Statistics Report MUST be returned in response to this command.


CC:0067.01.04.11.002 This command MUST NOT be issued via multicast addressing.


CC:0067.01.04.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.111: Statistics Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|COMMAND = STATISTICS_GET|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|



**NodeID** **(1** **byte)**

This field is used to specify the NodeID for which statistics are requested.


**5.2.5.15.5** **Statistics** **report**


This command is used to report Installation and Maintenance statistics recorded by a node.


Table 5.112: Statistics Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|COMMAND = STATISTICS_REPORT|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|
|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|
|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|
|…|…|…|…|…|…|…|…|
|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|
|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|
|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|



**NodeID** **(1** **byte)**

CC:0067.01.04.11.004 This field MUST carry the same value as received in the Statistics Get Command.


**Statistics** **(N** **bytes)**

CC:0067.01.04.11.005 The statistics field MUST be formatted as cascaded Type-Length-Value (TLV) structures. The Z/IP

CC:0067.01.04.13.001 Gateway MAY send any combination of TLV structures. Valid types are shown in Table 5.113.


Table 5.113: Statistics Get::Type encoding

|Name|Statistics Type<br>-|Statistics Length (Bytes)<br>-|
|---|---|---|
|Route Changes (RC)|0|1|
|Transmission Count (TC)|1|1|
|Neighbors (NB)|2|n|
|Packet Error Count (PEC)|3|1|
|Sum of transmission times (TS)|4|4|
|Sum of transmission times squared (TS2)|5|4|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1004




<!-- PAGE 1006 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CC:0067.01.04.11.006 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**5.2.5.15.6** **Route** **changes** **(RC)**


Table 5.114: Route Changes

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|Statistics - Type = 0x00|
|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|
|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|Statistics – Value = Route Changes|



**Route** **Changes** **(1** **byte)**

The RC field is used to advertise the number of routing attempts needed to reach a destination. The
number is a combination of Last Working Route (LWR) changes and Jitter measurements during
transmission attempts between the Z/IP Gateway and the Z-Wave device.


RC is incremented automatically by the Z/IP Gateway when either of the below conditions are true:


      - **–** Last Working Route changed from the transmission of one command to the next


      - **–** _𝑇_ _𝑛_      - _𝑇_ _𝑛−_ 1      - 150ms where _𝑇_ _𝑛_ and _𝑇_ _𝑛−_ 1 = _the_ _time_ _needed_ _to_ _complete_ _a_ _transmission_ _of_ _a_
_command_


**–** IF 2 channel and FLIRS node, RC: _𝑇_ _𝑛_ = _𝑇_ _𝑛_ mod 1100


**–** IF 3 channel and FLIRS node, RC cannot increment based on time calculation


**5.2.5.15.7** **Transmission** **Count** **(TC)**


Table 5.115: Transmission Count

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|Statistics - Type = 0x01|
|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|
|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|Statistics – Value = Transmission Count|



**Transmission** **Count** **(1** **byte)**

Total number of transmissions sent by all Z/IP Clients through the Z/IP GW to the specified Z-Wave
destination node.


**5.2.5.15.8** **Neighbors** **(NB)**


Table 5.116: Neighbors

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|Statistics - Type = 0x02|
|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|Statistics – Length = N * 2|
|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|Statistics – Value = NodeID 1|
|Statistics – Value = Repeater 1|Reserved|Reserved|Statistics – Value = Speed 1|Statistics – Value = Speed 1|Statistics – Value = Speed 1|Statistics – Value = Speed 1|Statistics – Value = Speed 1|
|…|…|…|…|…|…|…|…|
|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|Statistics – Value = NodeID N|
|Statistics – Value = Repeater N|Reserved|Reserved|Statistics – Value = Speed N|Statistics – Value = Speed N|Statistics – Value = Speed N|Statistics – Value = Speed N|Statistics – Value = Speed N|



**NodeID** **(N** ***** **1** **byte)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1005




<!-- PAGE 1007 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The NodeID of the actual neighbor.


**Speed** **(N** ***** **4** **bits)**


Table 5.117: Statistics Report::Speed Encoding

|Value|Speed|
|---|---|
|0x01|9.6 kbit/sec|
|0x02|40 kbit/sec|
|0x04|100 kbit/sec|



CC:0067.01.04.11.007 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**Repeater** **(N** ***** **1** **bit)**


If this bit is set then the node is a repeater.


**5.2.5.15.9** **Packet** **error** **count** **(PEC)**


Table 5.118: Packet Error Count

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|Statistics - Type = 0x03|
|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|Statistics – Length = 1|
|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|Statistics – Value = Packet Error Count|



**Packet** **Error** **Count** **(1** **byte)**


CC:0067.01.04.11.008 Also sometimes referred to as PER. PEC is measured by the Gateway. The PEC value MUST be
incremented each time the Gateway detects a failing transmission for each specific Z-Wave destination
node.


Sum of transmission times (TS)


Table 5.119: Sum of Transmission Times

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|Statistics - Type = 0x04|
|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|
|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|Statistics – Value = Sum of transmission times 1 (MSB)|
|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|Statistics – Value = Sum of transmission times 2|
|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|Statistics – Value = Sum of transmission times 3|
|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|Statistics – Value = Sum of transmission times 4 (LSB)|



**Sum** **of** **transmission** **times** **(4** **bytes)**


The sum of all transmission times. This may be used to calculate the average transmission time. The
time is given as a 32-bit unsigned integer MSB in milliseconds.



_⟨𝑇_ _⟩_ = [1]

_𝑁_



_𝑁_
∑︁ _𝑇_ _𝑖_


_𝑖_



Where N is the number of transmissions.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1006




<!-- PAGE 1008 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.15.10** **Sum** **of** **transmission** **times** **squared** **(TS2)**


Table 5.120: Sum of Transmission Times Squared

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|Statistics - Type = 0x05|
|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|Statistics – Length = 4|
|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|Statistics – Value = Sum of transmission times squared 1 (MSB)|
|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|Statistics – Value = Sum of transmission times squared 2|
|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|Statistics – Value = Sum of transmission times squared 3|
|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|Statistics – Value = Sum of transmission times squared 4 (LSB)|



**Sum** **of** **transmission** **times** **squared** **(4** **bytes)**


The sum of the square of all transmission times. This may be used to calculate the variance of the
transmission time. The time is given as a 32 bit unsigned integer MSB in milliseconds^2.


The Variance may be calculated as follows:



_𝑇_ [2] [⟩︀] = [1]
⟨︀

_𝑁_



_𝑁_
∑︁ _𝑇_ _𝑖_ [2]


_𝑖_



(König-Huygens theorem)


Where N is the number of transmissions.


A high variance is a sign of a bad link.


**5.2.5.15.11** **Statistics** **clear**


This command is used to clear all statistic registers maintained by the node.


Table 5.121: Statistics Clear

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|COMMAND = STATISTICS_CLEAR|



A receiving node MUST set all counters to 0.


**5.2.5.15.12** **Use** **cases**


**5.2.5.15.13** **Intranode** **network** **management:** **TV** **OSD** **system** **controlling** **lamps**


Intranode network management is the process close to Z-Wave API programming. No messages ever
leave the device. Messages only flow between different software modules.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1007




<!-- PAGE 1009 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.23: TV OSD System controlling lamps


Using UDP/IP for carrying the messages allows for a simple integration interface between applications
designed by different partners.


**5.2.5.15.14** **Intranet** **network** **management:** **remote** **controlling** **a** **primary** **controller**


Intranet network management extends the use of command messages to separate physical devices.
Messages flow between software modules but the modules reside in separate physical entities having
individual IP addresses – or at least separate NodeIDs.


Figure 5.24: Managing a primary static controller from a remote control


Network management via messages allows for sophisticated interfaces to the primary controller of


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1008




<!-- PAGE 1010 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


a network. Controllers with SUC/SIS capability may also leverage from the Network Management
command classes.


**5.2.5.15.15** **Internet** **network** **management** **#1:** **call-center** **support** **for** **TV** **OSD** **user**


Internet network management uses the same command messages. Messages flow between software
modules but the modules reside in separate physical entities in a non-trusted environment such as the
Internet. Remote access technologies should be used to protect the communication.


In this use case a TV user may call the service provider for support in adding a new lamp to the
network.


Figure 5.25: TV OSD System


Internet network management #2: remote management of Z/IP network


In this use case a user may use an IP based home control management system running in the LAN
for setting up the Z/IP network. The user may use normal UDP transport in the LAN environment.
Due to the critical nature of the network management command classes the user however should use
remote access protection technologies over LAN as well as over Internet. The benefit of designing a
home control system using remote access protection by default is that it may be moved from a location
in the LAN to any place in the Internet and work completely unaffected.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1009




<!-- PAGE 1011 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 5.26: Z/IP Router in consumer premises


**5.2.5.15.16** **Traffic** **flow:** **gathering** **node** **information**


The following sequence diagram introduces a new concept of gathering Node Information.


The node list provides an overview of the nodes in the network; as good as the Z/IP gateway can
provide this information. Using that node list, the requesting host may request information on individual nodes from the Z/IP Gateway. The ”Node Info Cached Get” command reports all supported
and controlled classes.


Figure 5.27: Gathering node information


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1010




<!-- PAGE 1012 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.16** **Network** **management** **installation** **and** **maintenance** **command** **class,** **version** **2**


**5.2.5.16.1** **Compatibility** **considerations**


The Network Management Installation and Maintenance Command Class, version 2 is backwards
compatible with the Network Management Installation and Maintenance Command Class, version 1.

CC:0067.02.01.21.002 All commands and fields not mentioned in this version MUST remain unchanged from version 1.


The following commands have been added to allow a supporting node to report the RSSI it measured
in each channel of the network:


      - RSSI Get Command


      - RSSI Report Command


**5.2.5.16.2** **RSSI** **get** **command**


This command is used to query the measured RSSI on the Z-Wave network from a node.


CC:0067.02.07.11.001 The RSSI Report Command MUST be returned in response to this command.


CC:0067.02.07.11.002 This command MUST NOT be issued via multicast addressing.


CC:0067.02.07.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.122: RSSI Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|Command = RSSI_GET (0x07)|



**5.2.5.16.3** **RSSI** **report** **command**


This command is used to advertise the measured RSSI on the Z-Wave network for each used channel.


Table 5.123: RSSI Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|
|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|
|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|
|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|



**Channel** **1** **RSSI** **(8** **bits)**

CC:0067.02.08.11.001 This field MUST carry the measured RSSI value on channel 1.

CC:0067.02.08.11.002 This field MUST be encoded as using signed representation in the dBm unit and according to Table
5.124.


**Channel** **2** **RSSI** **(8** **bits)**

CC:0067.02.08.11.003 This field MUST carry the measured RSSI value on channel 2.

CC:0067.02.08.11.004 This field MUST be encoded as using signed representation in the dBm unit and according to Table
5.124.


**Channel** **3** **RSSI** **(8** **bits)**


CC:0067.02.08.11.005


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1011




<!-- PAGE 1013 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field MUST carry the measured RSSI value on channel 3, if applicable.

CC:0067.02.08.11.006 This field MUST be encoded as using signed representation in the dBm unit and according to Table
5.124.

|Value(signed)|Table 5.124: RSSI Encoding Description|
|---|---|
|**Value(signed)**|**Description**|
|127 (0x7F)|RSSI_NOT_AVAILABLE.<br>This value is returned for unused channels or if no RSSI measurement is avail-<br>able.|
|126 (0x7E)|RSSI_MAX_POWER_SATURATED<br>This value is returned if the measured RSSI is above the maximum power.|
|125 (0x7D)|RSSI_BELOW_SENSITIVITY.<br>This value is returned if the measured RSSI is below the receiver’s sensitivity.|
|-32..-128<br>(0xE0..0x80)|These values represent the actual RSSI measurement value from respectively<br>-32 dBm to -128 dBm|



CC:0067.02.08.11.007 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**5.2.5.17** **Network** **management** **installation** **and** **maintenance** **command** **class,** **version** **3**


**5.2.5.17.1** **Compatibility** **considerations**


The Network Management Installation and Maintenance Command Class, version 3 is backwards
compatible with the Network Management Installation and Maintenance Command Class, version 2.

All commands and fields, that are not mentioned in this version MUST remain unchanged from version
2.


The following command has been added to notify the Z/IP Client application the occurrence of S2
Nonce Resynchronization event, (including extended NodeID support) :


      - S2 Resynchronization Event Command


The following commands are introduced to support extended NodeIDs:


      - Extended Statistics Get


      - Extended Statistics Report


**5.2.5.17.2** **S2** **resynchronization** **event** **command**


This command is used to notify the Z/IP Client application the occurrence of S2 Nonce Resynchronization event. This will allow the client application to recover faster from a synchronization error
that may cause message delay and loss.


The Z/IP Gateway MUST send this command to the Unsolicited destinations when the Gateway
received Nonce Report with SOS flag equal to 1 while Verify Delivery to the sending node is inactive.


The Z/IP Gateway MUST NOT send this command in the following cases:

      - The Z/IP Gateway received the Nonce Report with SOS flag equals to 1 and Verify Delivery to
sending node is active.

      - The Z/IP Gateway received the Nonce Report with SOS flag equals to 1 and the ZIP NAK is
sent to the Z/IP Client application.


      The Z/IP Gateway received the Nonce Report with SOS flag equals to 1 when the sending node
cannot decrypt the frame sent from the Gateway.


      - The Z/IP Gateway received Nonce Get (i.e., node coming out of power reset.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1012




<!-- PAGE 1014 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 5.125: S2 Resynchronization Event Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|COMMAND = S2_RESYNCHRONIZATION_EVENT (0x09)|
|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|NodeID|
|Reason|Reason|Reason|Reason|Reason|Reason|Reason|Reason|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



**NodeID** **(8** **bits)**

The NodeID field contains the NodeID of the peer node triggering a nonce resynchronization.

This field MUST be set to 0xFF if the NodeID triggering a nonce resynchronization is greater than
255.


**Reason** **(8** **bits)**

The reason field contains the detailed reason for the Resynchronization event. This field MUST
encoded as described in Table 5.126. This field MUST use signed encoding.

|Value|Table 5.126: S2 Resynchronization Event Reason Encoding Description|
|---|---|
|**Value**|**Description**|
|0|SOS_EVENT_REASON_UNANSWERED<br>A Nonce Report with SOS equals to 1 was received at an unexpected time<br>and no response was sent.<br>Application may use this information to abort<br>Supervision Report timeout if the remote NodeID matches.<br>The Nonce Report was unanswered because the retransmission was performed<br>while the S2 layer was idle or transmitting to another NodeID.<br>In this case, a frame to NodeID was most likely lost. If the ZIP Client had<br>only one frame outstanding with NodeID, it can safely be assumed that the<br>frame was lost.<br>Note: Supervision Encapsulation should be used to acknowledge outstanding<br>frames.|
|-127..-1|_Reserved_|
|1..127|_Reserved_|



**Extended** **NodeID** **(2** **bytes)**

This field is used to advertise the NodeID of the peer node triggering a nonce resynchronization.

This field MUST be set to the actual NodeID that was triggered a Nonce resynchronization.


**5.2.5.17.3** **Extended** **statistics** **get**


This command is used to query Installation and Maintenance statistics from a node.


The Extended Statistics Report MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.127: Extended Statistics Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|COMMAND = EXTENDED_STATISTICS_GET (0x0B)|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1013




<!-- PAGE 1015 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Extended** **NodeID** **(2** **bytes)**

This field is used to specify the NodeID for which statistics are requested. A receiving node MUST
return a report for the NodeID indicated in this field.


**5.2.5.17.4** **Extended** **statistics** **report**


Table 5.128: Extended Statistics Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|COMMAND_CLASS = COMMAND_CLASS_NETWORK_MANAGEMENT_INSTALLA-<br>TION_MAINTENANCE (0x67)|
|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|COMMAND = EXTENDED_STATISTICS_REPORT (0x0C)|
|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|Extended NodeID (MSB)|
|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|Extended NodeID (LSB)|
|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|Statistics – Type 1|
|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|Statistics – Length 1|
|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|Statistics – Value 1|
|…|…|…|…|…|…|…|…|
|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|Statistics – Type N|
|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|Statistics – Length N|
|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|Statistics – Value N|



**NodeID** **(2** **bytes)**

This field is used to advertise the NodeID for which statistics are advertised. No TLV MUST be
appended for non-existing NodeIDs or if no statistics have been saved for the advertised NodeID.


**Statistics** **(N** **bytes)**

The statistics field MUST be formatted as cascaded Type-Length-Value (TLV) structures. The Z/IP
Gateway MAY send any combination of TLV structures. Valid types are shown in Table 5.113 and
described in section _Statistics_ _report_ .


**5.2.5.18** **Network** **management** **installation** **and** **maintenance** **command** **class,** **version** **4**


**5.2.5.18.1** **Compatibility** **considerations**


The Network Management Installation and Maintenance Command Class, version 4 is backwards
compatible with the Network Management Installation and Maintenance Command Class, version 3.

All commands and fields not mentioned in this version MUST remain unchanged from version 3.

The following commands have been added to allow a supporting node to configure the channel to use
for Z-Wave Long Range:

 - Z-Wave Long Range Channel Configuration Set

 - Z-Wave Long Range Channel Configuration Get

 - Z-Wave Long Range Channel Configuration Report


The following commands have been extended to allow a supporting node to report the RSSI it measured
in the Z-Wave Long Range channel of the network:


 - RSSI Report Command


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1014




<!-- PAGE 1016 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.18.2** **RSSI** **report** **command**


This command is used to advertise the measured RSSI on the Z-Wave network for each used channel.


Table 5.129: RSSI Report Command V4

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE|
|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|Command = RSSI_REPORT (0x08)|
|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|Channel 1 RSSI|
|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|Channel 2 RSSI|
|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|Channel 3 RSSI|
|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|Z-Wave Long Range Primary Channel RSSI|
|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|Z-Wave Long Range Secondary Channel RSSI|



Fields not described below MUST remain unchanged from version 3.


**Z-Wave** **Long** **Range** **Primary** **Channel** **RSSI** **(8** **bits)**

This field MUST carry the measured RSSI value on the Z-Wave Long Range Primary Channel.

This field MUST be encoded as using signed representation in the dBm unit and according to Table
5.124.


**Z-Wave** **Long** **Range** **Secondary** **Channel** **RSSI** **(8** **bits)**

This field MUST carry the measured RSSI value on the Z-Wave Long Range Secondary Channel.

This field MUST be encoded as using signed representation in the dBm unit and according to Table
5.124.


**5.2.5.18.3** **Z-Wave** **long** **range** **channel** **configuration** **set**


This command is used to configure which channel to use for the Z-Wave Long Range protocol.


Table 5.130: Z-Wave Long Range Channel Configuration Set

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|
|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_SET (0x0A)|
|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|



**Z-Wave** **Long** **Range** **Channel** **(8** **bits)**

This field is used to specify which channel to use for Z-Wave Long Range.


The value 0x01 MUST indicate to use the Primary Z-Wave Long Range Channel.


The value 0x02 MUST indicate to use the Secondary Z-Wave Long Range Channel.


All other values are reserved.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1015




<!-- PAGE 1017 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.5.18.4** **Z-Wave** **long** **range** **channel** **configuration** **get**


This command is used to request the currently configured Z-Wave Long Range Channel.

The Z-Wave Long Range Channel Configuration Report MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.131: Z-Wave Long Range Channel Configuration Get

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|
|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_GET (0x0D)|



**5.2.5.18.5** **Z-Wave** **long** **range** **channel** **configuration** **report**


This command is used to advertise the configured Z-Wave Long Range Channel.


Table 5.132: Z-Wave Long Range Channel Configuration Report

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|COMMAND_CLASS = NETWORK_MANAGEMENT_INSTALLATION_MAINTENANCE<br>(0x67)|
|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|COMMAND = ZWAVE_LR_CHANNEL_CONFIGURATION_REPORT (0x0E)|
|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|Z-Wave Long Range Channel|



**Z-Wave** **Long** **Range** **Channel** **(8** **bits)**

This field is used to advertise the channel to use for Z-Wave Long Range.


The value 0x01 MUST indicate to use the Primary Z-Wave Long Range Channel.


The value 0x02 MUST indicate to use the Secondary Z-Wave Long Range Channel.


All other values are reserved.


A supporting node SHOULD use the Primary Z-Wave Long Range Channel by default.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1016




<!-- PAGE 1018 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.6** **No** **Operation** **Command** **Class,** **version** **1**


The No Operation Command Class is used to check if a node is reachable by sending a Command
less frame to the specified destination. Feature used by the Z-Wave protocol in many situations e.g.
checking that an excluded node is non-responding. This Command can also be used on application
level e.g. checking if a SUC/SIS is reachable from a new node in the network. This command class
contains no command identifier and data.


**Notice** : It is not necessary to announce the No Operation Command Class in the NIF.


Table 5.133: No Operation Command Class, version 1

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|Command Class = COMMAND_CLASS_NO_OPERATION|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1017




<!-- PAGE 1019 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7** **Node** **Provisioning** **Command** **Class,** **version** **1**


The Node Provisioning Command Class is used to manage a list of unique nodes (Node Provisioning
List) in a Smart Start enabled controller or gateway.


**5.2.7.1** **Terminology**


Smart start allows a controller to include new nodes in a network (or keep them out) without user
interaction.


A Smart Start enabled controller or gateway maintains a **Node** **Provisioning** List or **Provisioning**
**List** (PL). The Provisioning List is a list of unique nodes and their additional associated meta data
necessary for performing their network inclusion and security bootstrapping.


A **Provisioning** **List** **entry** represents a node and its associated data. Provisioning List entries may
also be used for ignoring nodes.


A Z/IP Client or controller can read and edit the Provisioning List entries of a Z/IP Gateway or
controller using this Command Class.


**5.2.7.2** **Compatibility** **considerations**


CC:0078.01.00.22.001 This Command Class MAY be carried in Z/IP Packets or in Z-Wave frames. However, this Command
Class SHOULD only be used in Z/IP Packets.


CC:0078.01.00.21.001 A node supporting this Command Class MUST support at least 232 entries in its Node Provisioning
List.


**5.2.7.3** **Security** **considerations**


This Command Class allows a controlling node to include new nodes in the Z-Wave network and grant
them all the security keys.


CC:0078.01.00.41.001 A node supporting this Command Class MUST NOT support it in a Z-Wave network if its highest
Security Class is lower than S2 Access Control.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1018




<!-- PAGE 1020 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.4** **Node** **Provisioning** **Set** **Command**


This command is used to create or update an entry in the node provisioning list of a supporting node.


Table 5.134: Node Provisioning Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|Command = COMMAND_NODE_PROVISIONING_SET (0x01)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Reserved**

CC:0078.01.01.11.001 This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**DSK** **Length** **(5** **bits)**

CC:0078.01.01.11.002 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.01.11.003 This field MUST be set to 16.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being added or updated.


CC:0078.01.01.11.004 A receiving node MUST add a new entry in the provisioning list if it does not have any entry with
the advertised DSK value.


CC:0078.01.01.11.00D A receiving node MUST ignore a command attempting to create a new entry if the Provisioning List
is full.


CC:0078.01.01.11.005 A receiving node MUST update the corresponding entry in the provisioning list if it already has an
entry with the advertised DSK value.

CC:0078.01.01.11.006 The length of this field (in bytes) MUST be according to the DSK Length field value.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the node.

CC:0078.01.01.13.001 This field MAY contain zero, one or several extensions.


CC:0078.01.01.11.007 Each extension MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].


CC:0078.01.01.11.009 If the Bootstrapping mode Type (0x36) is omitted from this command, the Bootstrapping mode value
1 (Smart Start Mode) MUST be assumed by the receiving node when creating a new entry.


CC:0078.01.01.11.00B If the SmartStart Inclusion Setting Type (0x34) is omitted from this command, the Inclusion setting
value 0 (Pending) MUST be assumed by the receiving node when creating a new entry that has a
SmartStart Bootstrapping mode.


CC:0078.01.01.11.00A The Network Status Type (0x37) MUST NOT be carried in this command. The Network Status Type
(0x37) MUST be ignored if received in this command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1019




<!-- PAGE 1021 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.5** **Node** **Provisioning** **Delete** **Command**


This command is used to delete one or all entries in the node provisioning list of a supporting node. Already included nodes will stay in the Z-Wave network even if no more corresponding node provisioning
list entry is kept by the controller.


Table 5.135: Node Provisioning Delete Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|Command = COMMAND_NODE_PROVISIONING_DELETE (0x02)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.02.11.001 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.02.11.002 This field MUST be set to 0 or 16.


CC:0078.01.02.11.003 The value 0 MUST indicate that the receiving node MUST delete all entries in its Node Provisioning
List.


CC:0078.01.02.11.004 The value 16 MUST indicate that the receiving node MUST delete the entry in its Node Provisioning
List that match the advertised value in the DSK field.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being deleted.


CC:0078.01.02.11.005 A receiving node MUST delete the corresponding entry from the Node Provisioning List if it has an
entry with the advertised DSK value.


CC:0078.01.02.11.006 A receiving node MUST ignore this command if it has no entry with the advertised DSK value.

CC:0078.01.02.11.007 The length of this field (in bytes) MUST be according to the DSK Length field value.

This field MUST be omitted if the DSK Length field is set to 0.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1020




<!-- PAGE 1022 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.6** **Node** **Provisioning** **Get** **Command**


This command is used to request the metadata information associated to an entry in the node Provisioning List of the receiving node.


CC:0078.01.05.11.001 The Node Provisioning Report Command MUST be returned in response to this command.


CC:0078.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0078.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.136: Node Provisioning Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|Command = COMMAND_NODE_PROVISIONING_GET (0x05)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|DSK 1|
|…|…|…|…|…|…|…|…|
|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|DSK N|



**Seq** **No.** **(8** **bits)**


Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.05.11.004 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.05.11.005 This field MUST be set to 16.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the entry being requested.


CC:0078.01.05.11.006 A receiving node MUST return the corresponding DSK entry if it has an entry matching the requested
DSK in its Provisioning List.


CC:0078.01.05.11.007 A receiving node MUST return a report containing no DSK (DSK Length set to 0) if the requested
DSK value is not in its Provisioning List.

CC:0078.01.05.11.008 The length of this field (in bytes) MUST be according to the DSK Length field value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1021




<!-- PAGE 1023 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.7** **Node** **Provisioning** **Report** **Command**


This command is used to advertise the contents of an entry in the node Provisioning List of the
sending node.


Table 5.137: Node Provisioning Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|Command = COMMAND_NODE_PROVISIONING_REPORT (0x06)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Reserved|Reserved|Reserved|DSK Length|DSK Length|DSK Length|DSK Length|DSK Length|
|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|
|…|…|…|…|…|…|…|…|
|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**DSK** **Length** **(5** **bits)**

CC:0078.01.06.11.001 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.06.11.002 This field MUST be set to 0 or 16


CC:0078.01.06.11.003 The value 0 MUST indicate that the requested DSK is not present in the Provisioning List.


**DSK** **(N** **bytes)**

CC:0078.01.06.11.004 This field is used to advertise the DSK for the Provisioning List entry being advertised.

CC:0078.01.06.11.005 The length of this field (in bytes) MUST be according to the DSK Length field value. This field
MUST be omitted if the DSK Length field is set to 0.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the Provisioning List entry.

CC:0078.01.06.13.001 This field MAY contain several extensions.


CC:0078.01.06.11.006 Each extension Type, Length and Value MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].

CC:0078.01.06.13.002 A supporting node MAY set the critical flag to 0 even when advertising critical extensions.

CC:0078.01.06.11.007 If the DSK Length field is set to 0, this field MUST be omitted.

If the DSK Length field is not set to 0:


CC:0078.01.06.11.008 - A sending node MUST advertise the SmartStart Inclusion Setting extension (type 0x34)


CC:0078.01.06.11.009 - A sending node MUST advertise the Bootstrapping mode extension (type 0x36)


CC:0078.01.06.11.00B - A sending node MUST advertise the Network Status extension (type 0x37)


CC:0078.01.06.11.00A - A sending node MUST advertise all other extension data kept in the Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1022




<!-- PAGE 1024 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.8** **Node** **Provisioning** **List** **Iteration** **Get** **Command**


This command is used to read the entire the provisioning list of a supporting node.


CC:0078.01.03.11.001 The Node Provisioning List Iteration Report Command MUST be returned in response to this command unless it is to be ignored.


CC:0078.01.03.11.002 This command MUST NOT be issued via multicast addressing.


CC:0078.01.03.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.

CC:0078.01.03.11.004 A sending node MUST follow the frame flow in Section 5.2.7.11.1.


Table 5.138: Node Provisioning List Iteration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_GET (0x03)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|Remaining Counter|



**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Remaining** **Counter** **(8** **bits)**

This field is used to iterate over the Provisioning List. The field indicates the remaining amount of
CC:0078.01.03.11.005 entries in the Provisioning List. This field MUST be in the range 0x01..0xFF.

CC:0078.01.03.11.006 This field MUST be set to 0xFF to start a new iteration. A supporting node MUST return the first
entry and the actual amount of remaining entries in the returned report, i.e. If the Provisioning list
has 3 elements the first response Remaining Count field MUST be set to 2.

CC:0078.01.03.11.007 A sending node MUST subsequently set this field to the returned value ”Remaining Count” value
received in the returned Report if the ”Remaining Count” value is higher than 0x00. A supporting
node MUST ignore this field if it is not set to the expected next iteration value.

CC:0078.01.03.11.008 This command MUST be ignored by a supporting node if this field is set to a value lower than 0xFF
and no iteration has been started.


Refer to Section 5.2.7.11.1.


**5.2.7.9** **Node** **Provisioning** **List** **Iteration** **Report** **Command**


This command is used to advertise the contents of an entry in the Provisioning List of the sending
node.


Table 5.139: Node Provisioning List Iteration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|Command Class = COMMAND_CLASS_NODE_PROVISIONING|
|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|Command = COMMAND_NODE_PROVISIONING_LIST_ITERATION_REPORT (0x04)|
|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|Seq No|
|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|Remaining Count|
|Reserved|Reserved|Reserved|DSK Length N|DSK Length N|DSK Length N|DSK Length N|DSK Length N|
|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|DSK 1 (Optional)|
|…|…|…|…|…|…|…|…|
|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|DSK N (Optional)|
|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|Meta Data Extension 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|Meta Data Extension M (Optional)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1023




<!-- PAGE 1025 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**Seq** **No** **(8** **bits)** Refer to _Sequence_ _number_ _management_ .


**Remaining** **Count** **(8** **bits)**

The field MUST indicate the remaining amount of entries in the Provisioning List iteration. This field
CC:0078.01.04.11.001 MUST be in the range 0x00..0xFE.


**DSK** **Length** **(5** **bits)**

CC:0078.01.04.11.002 This field MUST indicate the length of the DSK field in bytes.

CC:0078.01.04.11.003 This field MUST be set to 0 or 16.


CC:0078.01.04.11.004 The value 0 MUST indicate that the Provisioning List of the sending node is empty or the Provisioning
List Entry has been deleted after the start of the iteration.


CC:0078.01.04.11.005 The value 16 MUST indicate that the sending node advertises the DSK of a Provisioning List entry.


**DSK** **(N** **bytes)**

This field is used to advertise the DSK for the Provisioning List entry being advertised.

CC:0078.01.04.11.006 The length of this field (in bytes) MUST be according to the DSK Length field value. This field
MUST be omitted if the DSK Length field is set to 0.


**Meta** **Data** **Extension** **(M** **bytes)**

This field is used to carry additional metadata associated to the Provisioning List entry.

CC:0078.01.04.13.001 This field MAY contain several extensions.


CC:0078.01.04.11.007 Each extension Type, Length and Value MUST comply with _Meta_ _Data_ _Extension_ _Format_ and [28].

CC:0078.01.04.13.002 A supporting node MAY set the critical flag to 0 even when advertising critical extensions.

CC:0078.01.04.11.008 If the DSK Length field is set to 0, this field MUST be omitted.

If the DSK Length field is not set to 0:


CC:0078.01.04.11.009 - A sending node MUST advertise the SmartStart Inclusion Setting extension (type 0x34)


CC:0078.01.04.11.00A - A sending node MUST advertise the Bootstrapping mode extension (type 0x36)


CC:0078.01.04.11.00C - A sending node MUST advertise the Network Status extension (type 0x37)


CC:0078.01.04.11.00B - A sending node MUST advertise all other extension data kept in the Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1024




<!-- PAGE 1026 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.10** **Meta** **Data** **Extension** **Format**


CC:0078.01.00.11.001 Each Meta Data extension MUST be parsed according to the following format:


Table 5.140: Meta Data Extension Format

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|Meta Data Type|critical|
|Length|Length|Length|Length|Length|Length|Length|Length|
|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|Value 1 (Optional)|
|…|…|…|…|…|…|…|…|
|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|Value L (Optional)|



**Meta** **Data** **Type** **(7** **bits)**

This field is used to advertise the type of the data contained in the corresponding extension.

CC:0078.01.00.11.002 For the list of defined valid extensions, refer to [28]. Values not defined in [28] are reserved and MUST
NOT be used by a sending node.


**Critical** **(1** **bit)**

This field is used to advertise the criticality of the extension.


CC:0078.01.00.11.003
A supporting node MUST discard and ignore the entire command if this flag is set to ‘1’ and the Meta
Data Type field advertises a value that the node does not support.


CC:0078.01.00.12.001 A controlling node which controls only (i.e. does not support this Command Class) SHOULD keep
the Provisioning List entry in its record even if this flag is set to ‘1’ and the node does not know what
the extension means.

If this flag is set to ‘0’ and the Meta Data Type field advertises a value that the receiving node does
CC:0078.01.00.11.004 not support, the actual extension MUST be ignored and left out the provisioning list entry.


CC:0078.01.00.11.005 In this case, a receiving node MUST continue processing of the encapsulation command after the
discarded extension.


**Length** **(8** **bits)**

CC:0078.01.00.11.006 This field MUST indicate the length of the corresponding Value field in bytes.


**Value** **(L** **bytes)**

CC:0078.01.00.11.007 This field MUST indicate the value of the Meta Data type being advertised in the extension.

The length of this field (in bytes) MUST be according to the corresponding Length field value .This
CC:0078.01.00.11.008 field MUST be omitted if the corresponding Length field is set to 0.

CC:0078.01.00.11.009 The encoding of this field MUST be interpreted with the Meta Data Type field as defined in [28].


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1025




<!-- PAGE 1027 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.7.11** **Usage** **and** **Frame** **Flows**


**5.2.7.11.1** **Z/IP** **Client** **requesting** **the** **entire** **Node** **Provisioning** **list.**


The frame flow for Z/IP client requesting the entire Provisioning List of a supporting node is shown
in Figure 5.28.


Figure 5.28: Reading the entire Node Provisioning List


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1026




<!-- PAGE 1028 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8** **Powerlevel** **Command** **Class,** **version** **1**


The Powerlevel Command Class defines RF transmit power controlling Commands useful when installing or testing a network. The Commands makes it possible for supporting controllers to set/get
the RF transmit power level of a node and test specific links between nodes with a specific RF transmit
power level.


**NOTE:** **This** **Command** **Class** **is** **only** **used** **in** **an** **installation** **or** **test** **situation.**


**5.2.8.1** **Powerlevel** **Set** **Command**


This command is used to set the power level indicator value, which should be used by the node when
transmitting RF, and the timeout for this power level indicator value before returning the power level
defined by the application.


Table 5.141: Powerlevel Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|Command = POWERLEVEL_SET (0x01)|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Power** **level** **(8** **bits)**

CC:0073.01.01.11.001 This field indicates the power level value that the receiving node MUST set. However, a supporting
node MAY decide not to change its actual Tx configuration. In any case, the value received in this
Command MUST be returned in a _Powerlevel_ _Report_ _Command_ in response to a Powerlevel Get
Command as if the power setting was accepted for the indicated duration.

CC:0073.01.01.11.002 This field MUST be encoded according to Table 5.142.

|Value|Table 5.142: Powerlevel Set::Power level encoding Description|
|---|---|
|Value|Description|
|0x00|NormalPower|
|0x01|minus1dBm|
|0x02|minus2dBm|
|0x03|minus3dBm|
|0x04|minus4dBm|
|0x05|minus5dBm|
|0x06|minus6dBm|
|0x07|minus7dBm|
|0x08|minus8dBm|
|0x09|minus9dBm|



CC:0073.01.01.11.003 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


Timeout value is ignored if Power level is set to normalPower.


**Timeout** **(8** **bits)**


The time in seconds the node should keep the Power level before resetting to normalPower level. It
is fundamental, that the timeout IS implemented and followed by the application, for keeping the
network consistent. Valid values are 1-255 resulting in timeouts from 1 second to 255 seconds.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1027




<!-- PAGE 1029 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.2** **Powerlevel** **Get** **Command**


This command is used to request the current power level value.


CC:0073.01.02.11.001 The Powerlevel Report Command MUST be returned in response to this command.


CC:0073.01.02.11.002 This command MUST NOT be issued via multicast addressing.


CC:0073.01.02.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.143: Powerlevel Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|Command = POWERLEVEL_GET (0x02)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1028




<!-- PAGE 1030 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.3** **Powerlevel** **Report** **Command**


This command is used to advertise the current power level.


Table 5.144: Powerlevel Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|Command = POWERLEVEL_REPORT (0x03)|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|Timeout|



**Power** **level** **(8** **bits)**

This value is the current power level indicator value in effect on the node.

CC:0073.01.03.11.001 This field MUST be encoded according to Table 5.142.


If the returned value is normalPower, the timeout value is ignored.


**Timeout** **(8** **bits)**


The time in seconds the node has back at Power level before resetting to normal Power level.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1029




<!-- PAGE 1031 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.4** **Powerlevel** **Test** **Node** **Set** **Command**


This command is used to instruct the destination node to transmit a number of test frames to the
specified NodeID with the RF power level specified. After the test frame transmissions the RF power
level is reset to normal and the result (number of acknowledged test frames) is saved for subsequent
read-back. The result of the test may be requested with a Powerlevel Test Node Get Command.


CC:0073.01.04.12.001 A receiving node SHOULD return an unsolicited Powerlevel Test Node Report Command when it
completed the Powerlevel test initiated by this command.


Table 5.145: Powerlevel Test Node Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|Command = POWERLEVEL_TEST_NODE_SET (0x04)|
|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|
|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|Power Level|
|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|Test Frame Count (MSB)|
|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|Test Frame Count (LSB)|



**Test** **NodeID** **(8** **bits)**


The test NodeID that should receive the test frames.


A power level test will not work with a test NodeID which is either a sleeping or FLiRS node. A
CC:0073.01.04.12.002 controller SHOULD NOT initiate a powerlevel test towards sleeping or FLiRS nodes.


**Power** **level** **(8** **bits)**


The power level indicator value to use in the test frame transmission.

CC:0073.01.04.11.001 This field MUST be encoded according to Table 5.142.


**Test** **frame** **count** **(16** **bits)**

The Test frame count field contains the number of test frames to transmit to the Test NodeID. The
first byte is the most significant byte. Valid Test frame count range is 1..65535.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1030




<!-- PAGE 1032 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.5** **Powerlevel** **Test** **Node** **Get** **Command**


This command is used to request the result of the latest Powerlevel Test.


CC:0073.01.05.11.001 The Powerlevel Test Node Report Command MUST be returned in response to this command.


CC:0073.01.05.11.002 This command MUST NOT be issued via multicast addressing.


CC:0073.01.05.11.003 A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 5.146: Powerlevel Test Node Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|Command = POWERLEVEL_TEST_NODE_GET (0x05)|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1031




<!-- PAGE 1033 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.8.6** **Powerlevel** **Test** **Node** **Report** **Command**


This command is used to report the latest result of a test frame transmission started by the Powerlevel
Test Node Set Command.


Table 5.147: Powerlevel Test Node Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|Command Class = COMMAND_CLASS_POWERLEVEL (0x73)|
|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|Command = POWERLEVEL_TEST_NODE_REPORT (0x06)|
|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|Test NodeID|
|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|Status of operation|
|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|Test frame acknowledged count (MSB)|
|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|Test frame acknowledged count (LSB)|



**Test** **NodeID** **(8** **bits)**

This field advertises the NodeID of the node, which is or has been under test.

CC:0073.01.06.11.001 If a test has been performed, this field MUST reflect the NodeID used in the last test initiated with
the Powerlevel Test Node Set Command.

CC:0073.01.06.11.002 If no test has been performed, this field MUST be set to 0. In this case, the Status of operation and

CC:0073.01.06.13.001 Test frame acknowledged count fields MAY be ignored.


CC:0073.01.06.13.002 It is OPTIONAL to save the last Powerlevel test result in the NVM. If a node saves the last Powerlevel

CC:0073.01.06.13.003 test result in the volatile memory, it MAY set this field to 0 after going to sleep or losing power.


**Status** **of** **operation** **(8** **bits)**

This field indicates the result of the last test initiated with the Powerlevel Test Node Set Command.
CC:0073.01.06.11.003 It MUST be encoded according to Table 5.148.


Table 5.148: Powerlevel Test Node Report::Status of Operation
Encoding

|Value|Description|
|---|---|
|0x00|Test Failed<br>No frame was returned during the test|
|0x01|Test Success<br>At least 1 frame was returned during the test|
|0x02|Test in Progress<br>The test is still ongoing|



CC:0073.01.06.11.004 All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


CC:0073.01.06.13.004 A controller MAY return ”Test Failed” for a non-existing NodeID without carrying the test. However,

CC:0073.01.06.11.005 it MUST return ”Test in Progress” if carrying the test even if it knows that the test will fail.


**Test** **frame** **acknowledged** **count** **(16** **bits)**

This field indicates the number of test frames transmitted, which the Test NodeID has acknowledged.
The first byte is the most significant byte.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1032




<!-- PAGE 1034 -->

CC:0023.01.00.11.001



Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.9** **Z/IP** **Command** **Class,** **version** **1** **[OBSOLETED]**


**Warning:** **THIS** **COMMAND** **CLASS** **VERSION** **HAS** **BEEN** **OBSOLETED**


New implementations MUST use the Z/IP Command Class Version 2.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1033




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




<!-- PAGE 1058 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.14** **Z/IP** **6LoWPAN** **Command** **Class,** **version** **1**


The Z/IP 6LoWPAN Command Class supports the transmission of IPv6 Packets over Z-Wave networks.

The Z/IP 6LoWPAN Command Class, version 1 is defined by RFC 7428.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1057




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




<!-- PAGE 1077 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.18** **Z/IP** **Portal** **Command** **Class,** **version** **1**


The Z/IP Portal Command Class is used for configuration and management communication between
a Z/IP portal server and a Z/IP gateway through a secure connection.


The Z/IP Portal command class is intended for use together with the Z/IP Gateway command class
to provide a streamlined workflow for preparing and performing installation of Z/IP Gateways in
consumer premises.


**5.2.18.1** **Interoperability** **considerations**


This Command Class MUST NOT be used outside trusted environments, unless via a secure connection. This Command Class SHOULD be further limited for use only via a secure connection to an
authenticated portal server.

Commands defined in this Command Class MUST be encapsulated in Z/IP Packets.


**5.2.18.1.1** **On** **the** **use** **of** **Z/IP** **Gateway** **and** **Z/IP** **Portal** **command** **classes**


This section presents the concepts of tunnel creation, maintenance and bootstrapping of a Z/IP
Gateway.


A secure connection is established by the Z/IP gateway connecting to a peer. The Z/IP Gateway::Gateway Peer Set command is used to define a peer.


A secure connection to a portal is a special case of the general secure connection. When connecting to
a portal, the Z/IP Gateway is operated in portal mode; having most network configuration parameters
pushed from the portal. In Portal mode, the Z/IP Gateway only accepts the creation of one peer.


The gateway Mode Set command controls whether the Z/IP gateway operates as a normal IP router;
learning IP network information from the network or if the configuration is pushed from a portal.


A Z/IP Gateway has two modes of operation, each mode determines how the Z/IP Gateway can
be configured and how it should react to a number of command classes. The mode of operation is
determined by the customer depending on the type of product they wish to develop.


1. Service Provider (SP) (Only Portal Mode available)


a. Through Secure Tunnel connection (Locked & Unlocked): MUST accept Portal & Gateway
Command Classes, Firmware Command Class


b. Factory default: Device remains locked, and attempts communication to portal, reverts to
default firmware configuration.


c. Any other attempt to use above command classes MUST be ignored


2. Consumer Electronics (CE) (Portal and Stand-Alone Mode available)


a. Portal Mode:


i. Through Secure Tunnel connection (Locked & Unlocked): MUST accept Portal &
Gateway Command Classes, Firmware Command Class


ii. Local Access (Unlocked only): MUST accept Portal & Gateway Command Classes,
Firmware Command Class


iii. Any other attempt to use above command classes MUST be ignored


iv. Factory default: Device is unlocked, and may connect to portal if there is a default
configuration containing portal configuration


b. Stand-Alone Mode


i. Local access (Unlocked only): MUST accept Portal & Gateway Command Classes,
Firmware Command Class


ii. Any other attempt to use above command classes MUST be ignored


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1076




<!-- PAGE 1078 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


iii. Factory default: Device is unlocked, and may connect to portal if there is a default
configuration containing portal configuration

3. Gateway Lock MUST prevent any configuration parameter in Portal and Gateway from being
modified locally. Configuration through portal is always allowed.


4. Only the secure tunnel is considered a trusted environment when locked. When unlocked the
LAN is also considered “trusted”.


5. In all cases, a Factory Default does not perform Z-Wave Default set, meaning the Z-Wave
network is left intact. If required, Network Management Default Set MAY be called manually
following a Factory Default.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1077




<!-- PAGE 1079 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.18.2** **Gateway** **Configuration** **Set** **Command**


The command is used by a portal server to push settings to a Z/IP Gateway via a secure connection.

The Z/IP gateway MUST return a Gateway Configuration Status message in response to a Gateway
Configuration Set message.


Table 5.206: Gateway Configuration Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|
|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|
|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|
|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|
|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|
|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|
|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|
|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|



**LAN** **IPv6** **Address** **(16** **bytes)**


The LAN IPv6 address MUST be assigned to the LAN interface of the Z/IP Gateway in the consumer
premises network. The LAN IPv6 address MUST be used in combination with the LAN IPv6 prefix
length.

If the LAN IPv6 address is all zeros, the gateway MUST auto-configure a /64 IPv6 ULA prefix for
use by IPv6 enabled hosts in the consumer premises network.

The LAN IPv6 prefix MUST be advertised in IPv6 RAs on the LAN.

**LAN** **IPv6** **Prefix** **Length** **(1** **byte)**

The LAN IPv6 prefix length MUST be used by the LAN interface of the Z/IP Gateway in the consumer
premises network.

**Portal** **IPv6** **Prefix** **(16** **bytes)**

The Z/IP Gateway MUST route all IP traffic for the Portal IPv6 Prefix into the secure connection
connecting the Z/IP Gateway to the Portal network.

The Portal IPv6 Prefix MUST be used in combination with the Portal IPv6 prefix length.

**Portal** **IPv6** **Prefix** **Length** **(1** **byte)**

The Portal IPv6 prefix length MUST be used to scope the routing entry created for the Portal IPv6
Prefix by the Z/IP Gateway.


**Default** **Gateway** **IPv6** **Address** **(16** **bytes)**


The Z/IP Gateway MUST send IP packets to the default gateway if the Z/IP Gateway has no routing
information for the actual prefix; i.e the prefix is neither the LAN nor the PAN.

The Z/IP Gateway MAY be an address in the Portal IPv6 Prefix.

**PAN** **IPv6** **Prefix** **(16** **bytes)**


The PAN IPv6 address MUST be assigned to the PAN interface of the Z/IP Gateway. The PAN IPv6
address MUST be scoped by a /64 IPv6 prefix.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1078




<!-- PAGE 1080 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


If the PAN IPv6 address is all zeros, the gateway MUST auto-configure a /64 IPv6 ULA prefix for
use by Z-Wave nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1079




<!-- PAGE 1081 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.18.3** **Gateway** **Configuration** **Status**


The message is submitted by a Z/IP Gateway to confirm the reception and processing of a Gateway
Configuration Get to a portal.

The Z/IP gateway MUST return a Gateway Configuration Status message in response to a Gateway
Configuration Set message.


Table 5.207: Gateway Configuration Status Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|
|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|Command = GATEWAY_CONFIGURATION_SET|
|Status|Status|Status|Status|Status|Status|Status|Status|



**Status** **(1** **byte)**


Table 5.208: Gateway Configuration Status::Status Encoding

|Value|Status indication|
|---|---|
|0x01|Invalid Confguration Block|
|0xFF|OK|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1080




<!-- PAGE 1082 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.18.4** **Gateway** **Configuration** **Get** **Command**


The message is used by a portal to read back configuration settings from a Z/IP Gateway via a secure
connection.


Table 5.209: Gateway Configuration Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|
|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|Command = GATEWAY_CONFIGURATION_GET|



**5.2.18.5** **Gateway** **Configuration** **Report** **Command:**


The message is used by a Z/IP Gateway to return actual settings to a portal via a secure connection.


Table 5.210: Gateway Configuration Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|
|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|Command = GATEWAY_CONFIGURATION_REPORT|
|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|LAN IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|LAN IPv6 Address 16<br>|
|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|LAN IPv6 Prefx Length<br>|
|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|Portal IPv6 Prefx 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|Portal IPv6 Prefx 16<br>|
|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|Portal IPv6 Prefx Length|
|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|Default Gateway IPv6 Address 1|
|…|…|…|…|…|…|…|…|
|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|Default Gateway IPv6 Address 16<br>|
|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|PAN IPv6 Prefx 1|
|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|…<br>|
|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|PAN IPv6 Prefx 16|



**LAN** **IPv6** **Address** **(16** **bytes)**


Actual IPv6 address assigned to the LAN interface of the Z/IP Gateway in consumer premises.

An all zeros address may have been configured by the portal using a Gateway Configuration Set
command. The portal MUST accept receiving an auto-configured /64 IPv6 ULA address even if an
all-zeros address was specified previously.

**LAN** **IPv6** **Prefix** **Length** **(1** **byte)**

Actual LAN IPv6 prefix length used by the LAN interface of the Z/IP Gateway in consumer premises.

**Portal** **IPv6** **Prefix** **(16** **bytes)**

Actual IPv6 Prefix used by the Z/IP Gateway to reach the portal end of the secure tunnel.

**Portal** **IPv6** **Prefix** **Length** **(1** **byte)**

Actual IPv6 Prefix Length used by the Z/IP Gateway to reach the portal end of the secure tunnel.


**Default** **Gateway** **IPv6** **Address** **(16** **bytes)**

Actual IPv6 default gateway address used by the Z/IP Gateway to reach off-link subnet prefixes.

**PAN** **IPv6** **Prefix** **(16** **bytes)**

Actual IPv6 Prefix used by the Z/IP Gateway to construct IPv6 addresses for Z-Wave nodes.

It may be the ULA prefix if ::/128 was specified in the set.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1081




<!-- PAGE 1083 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**5.2.18.6** **Gateway** **Unregister** **Command**


The message is used by a portal to force the client to close the existing tunnel.


Table 5.211: Gateway Unregister Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|Command Class = COMMAND_CLASS_ZIP_PORTAL|
|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|Command = GATEWAY_UNREGISTER|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1082




<!-- PAGE 1084 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6 Command Class Control**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1083




<!-- PAGE 1085 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.1 Command Class Control Overview**


**6.1.1** **Controlled** **and** **Supported** **Command** **Classes**


A node can _support_ and/or _control_ a given Command Class.


If a Command Class is _supported_ :


The node implements all the Command Class functionalities and can be set and read back by other
CL:0000.00.11.0D.1 nodes. When a Command Class is supported, the node is REQUIRED to implement the whole
Command Class and observe the requirements specified in Section 2, Section 3, Section 4, and Section
5.


If a Command Class is _controlled_ :


The node implements the ability to interview, read and/or set other nodes supporting the Command
CL:0000.00.13.01.1 Class. Nodes controlling Command Classes MAY use a subset of the Commands within a Command
Class (for example only Set commands).


**6.1.1.1** **Control** **via** **association** **groups**


A Basic Set Command sent to Association Group destinations is a form of (static or partial) Command
Class control via association groups.


CL:0000.00.11.02.1 Even if using a Command Class for controlling other nodes via association groups, the usage MUST
comply with the Command Class description (Section 2, Section 3, Section 4, and Section 5) and the
controlling node use properly formed commands.


**6.1.1.2** **“Full”** **control**


When a Command Class is marked as _fully_ controlled during certification, the controlling node is said
CL:0000.00.11.03.1 to implement “full” control of the actual Command Class and it MUST observe the requirements for
the Command Class defined in this document.



CL:0000.00.11.04.1


CL:0000.00.13.03.1


CL:0000.00.11.10.1



_Device_ _Type_ _v2_ _Specification_ mandates some nodes to control a given set of Command Classes. It
means that the controlling node MUST respect the requirements described in this document for the
actual Command Classes.


**6.1.1.3** **Partial** **Control**


When a Command Class is marked as partially controlled during certification, the controlling node is
said to implement _partial_ control of the actual Command Class and it MAY observe only a subset of
the requirements for the Command Class defined in this document. The specific features which are
partially controlled MUST be noted during certification.



CL:0000.00.13.04.1 If a Command Class is partially controlled, the controlling node MAY skip steps or perform them in
a different order for the mandatory node interview detailed in this document. The controlling node
MAY retrieve capabilities from a database based on a node’s manufacturer specific information.


Even if the mandatory node interview is not followed, and not all capabilities are queried, the conCL:0000.00.11.11.1 trolling node MUST NOT send commands or values that the supporting node does not support.


CL:0000.00.13.05.1 If a Command Class is partially controlled, the controlling node MAY implement a subset of the min
CL:0000.00.12.01.1 imum end user functionalities and user interface. A controlling node SHOULD provide functionalities
for the lowest non-deprecated, non-obsoleted Command Class version.


CL:0000.00.11.12.1 All Z-Wave commands sent for a partially controlled Command Class MUST be valid Z-Wave commands


CL:0000.00.11.13.1


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1084




<!-- PAGE 1086 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


All Z-Wave commands sent for a partially controlled Command Class MUST be sent at the highest
Security Class granted during security bootstrapping.


CL:0000.00.11.14.1 Partial Control MAY be used for Application Command Classes only (Refer to Section 6.2). Management and Transport-Encapsulation Command Class MUST be fully controlled. (Refer to Section 6.3
and Section 6.4).


**6.1.2** **Command** **Classes** **Support** **Discovery** **Requirements**


CL:0000.00.11.05.1 A controlling node MUST read the capabilities and secure capabilities of a node/End Point once
before trying to control a given Command Class.


CL:0000.00.11.06.2 A controlling node MUST read the Command Class version number of a supporting node using the
Version Command Class prior to controlling the Command Class. There can be 2 exceptions to this
rule:


     - If the controlling node controls only version 1 of a given Command Class, it may skip requesting
the supporting node version for the actual Command Class.


     - A controlling node may issue version 1 commands in the supporting node interview before
knowing the supporting node Command Class’ version. (e.g., when interviewing the Version
Command Class itself)


CL:0000.00.11.07.1 A node controlling a given command class MUST allow an end user to control the command class in
all listening supporting nodes present in the network operating with a security class that is granted
to the controlling node.


CL:0000.00.11.08.1 A node controlling a Command Class MUST allow an end user to control a sleeping supporting node
if it is the Wake Up destination.


**6.1.3** **Command** **Classes** **Control** **Requirements**


This specification defines how to provide full control of Command Classes by specifying:


     - A required Command Class interview or capability discovery


     - A minimum required set of actions that an end user can perform or trigger and their associated
Z-Wave commands


     - A minimum required set of information relating to the supporting node that the end user can

see or access.


     - An optional set of additional requirements to controlling nodes


**6.1.3.1** **Mandatory** **supporting** **node** **interview**


CL:0000.00.21.01.3 The mandatory node interview specifies the frame flow that MUST be observed on the Z-Wave radio
for full control. Set commands MAY be skipped they would have no effect on the supporting node.


CL:0000.00.21.02.1 This interview MUST be performed prior to issuing any control command to the supporting node.


Preferably, it should be done during the commissioning phase of the supporting node or shortly after
the inclusion of the controlling node.



CL:0000.00.23.01.1


CL:0000.00.21.03.1



A fully controlling node MAY issue additional commands that are not specified in the frame flows and
MAY issue some commands in a different order. The mandatory frame flow indicates the minimum
set of commands that MUST be transmitted to a destination.



CL:0000.00.21.04.1 A fully controlling node MUST NOT skip or abort the interview of a Command Class if another
independent Command Class could not be correctly interviewed.


CL:0000.00.23.02.1


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1085




<!-- PAGE 1087 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


A “partially” controlling node MAY skip steps in the specified frame flow if the queried data would not
be used by the controller, or the data is retrieved from a separate source (i.e. database of Manufacturer
Specific information and capabilities)


CL:0000.00.22.01.1 The following order for reading Command Class capabilities is RECOMMENDED after discovering
the Security Class and encapsulation capabilities of a node:


     - Version Command Class


     - Z-Wave Plus Info Command Class


     - Wake Up Command Class


     - Association OR Multi Channel Association Command Class


     - Association Group Information (AGI) Command Class


     - Actuator Command Classes


     - Data reporting Command Classes


     - Multi Channel Command Class (and repeat the above order for each End Point, if any)


Some interviews or controlling scenarios may trigger no response in return to get type commands. In
CL:0000.00.22.02.1 this case, it is RECOMMENDED to use timeouts according to _Role_ _Type_ _Specification_ .


**6.1.3.2** **Minimum** **end** **user** **functionalities**


The minimum end user functionalities section specifies what minimum set of actions an end user can
perform on a supporting node when using the controlling node.


CL:0000.00.31.01.1 Each section describing a required functionality indicates the command(s) that MUST be transmitted

CL:0000.00.33.01.1 on the Z-Wave radio for full control. Fields not present, not described or marked as “free” in the
mandatory command(s) MAY be used freely by the controlling node either automatically or based on
user input.

CL:0000.00.31.02.1 Fields indicated as “user defined” MUST be filled based on end user input. In this case, the end user
MUST be able to select any value. (e.g. if the field is 2 bytes long, values from 0 to 65535 MUST be
available)

CL:0000.00.31.03.1 Fields indicated as “User defined among supported” MUST be filled based on user input and the
supported values by the supporting node. The controlling node MUST allow the end user to set
values supported by a supporting node even if it does not know what a given value represents.

CL:0000.00.31.04.1 Fields indicated as “User defined among x..y and z” MUST be filled based on user input and MUST
be able to select between the indicated values.

CL:0000.00.31.06.1 Fields indicated as “User defined or x” MUST be filled either based on user input or automatically
by the controller using the indicated value.


CL:0000.00.31.05.1 The product documentation MUST point out how to perform each action associated to the minimum
end user functionalities required by a Command Class.


If a Command Class is partially controlled and some minimum end user functionality are not met,
CL:0000.00.31.07.1 the product documentation MUST describe how the partially controlled command class differs from
the behavior of a fully controlled command class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1086




<!-- PAGE 1088 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.1.3.3** **Command** **Class** **control** **version**


Like a supporting node implements a version of its supported Command Classes, a controlling node
CL:0000.00.11.09.1 MUST also implement a given version of a Command Class it controls. A node controlling version 3
of a Command Class will be able to control the functionalities of version 1, 2 and 3 supporting nodes.

CL:0000.00.11.0A.2 When issuing commands, a controlling node MUST NOT use the fields described in the mandatory
commands sections if they belong to a newer version than the version it claims to control.


CL:0000.00.12.02.1 If a controlling node A controls a node B supporting a lower version, node A SHOULD still use the
format (command payload) corresponding to the version node A controls, regardless of the version
supported by node B.


CL:0000.00.11.0F.1 A controlling node A sending commands to a node B supporting a lower version MUST NOT use
commands introduced in versions that are newer than Node B’s version.


A node controlling a Command Class is not mandated to interview, provide minimum end user
functionality or show node properties belonging to a newer version of the actual Command Class.


When a version is indicated in the mandatory interview or mandatory commands for end user funcCL:0000.00.11.0B.1 tionalities, it MUST represent the minimum common version number between the supporting and
controlling node. For example, with a version 4 controlling node and version 2 supporting node, the
interview, minimum end user functionalities and properties MUST follow version 1 and 2 indications.


**6.1.4** **Command** **Classes** **not** **Present** **in** **this** **Document**


CL:0000.00.13.02.1 A node MAY advertise that it controls a Command Class not (yet) defined in this document during

CL:0000.00.11.0C.1 certification. In this case, the controlling node MUST comply with the following guidelines:


     - It MUST use all Get type commands to read the nodes capabilities during the node interview


     - It SHOULD provide the end user actions using all Set type Commands available in the Command
Class

     - It SHOULD show or let the end user access all relevant state/property/configuration relating
to the Command Class using the Report type Commands available in the Command Class.

A controller following this guideline is likely to be compliant when a new control specification is
released for an actual Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1087




<!-- PAGE 1089 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.2 Application Command Class Control Definitions**


**6.2.1** **Anti-theft** **Unlock** **Command** **Class,** **version** **1**


**6.2.1.1** **Mandatory** **node** **interview**


CL:007E.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.4.


Figure 6.1: Anti-Theft Unlock Command Class interview


**6.2.1.2** **Minimum** **end** **user** **functionalities**


**6.2.1.2.1** **Unlock** **the** **node**


CL:007E.01.31.01.1 If the supporting node is in the locked state and runs in restricted mode, the end user MUST be

CL:007E.01.31.01.1 able send an unlock command. When the end user performs this action, the issued command MUST
comply with Table 6.1.



CL:007E.01.32.01.1



|Field|Table 6.1: Anti-Theft Unlock::Unlock the node Value|
|---|---|
|Field|Value|
|Command|COMMAND_ANTITHEFT_UNLOCK_SET<br>|
|Magic Code length|Controlling node defned in 0x01..0xA, based on user input.<br>|
|Magic Code|User defned<br>The Magic Code SHOULD be shown as a hexadecimal value to the end<br>users.|


**6.2.1.3** **Node** **properties**



CL:007E.01.41.01.1 If the supporting node is in the locked state and runs in restricted mode, the controlling node MUST
have a UI allowing the end user to see that the supporting node is restricted and that the supporting
node requires unlocking to use the full functionality.


CL:007E.01.43.01.1 A controlling node MAY display the information provided in [25] for the reported Z-Wave Alliance
locking entity ID.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1088




<!-- PAGE 1090 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.2** **Barrier** **Operator** **Command** **Class,** **version** **1**


**6.2.2.1** **Mandatory** **node** **interview**


CL:0066.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.2.


Figure 6.2: Barrier Operator Command Class interview


**6.2.2.2** **Minimum** **end** **user** **functionalities**


CL:0066.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.2.2.1** **Initiate** **opening** **(or** **stop** **closing)**


CL:0066.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.2.

|Table Field|6.2: Barrier Operator::Initiate opening (or stop closing) Value|
|---|---|
|Field|Value|
|Command|BARRIER_OPERATOR_SET|
|Target Value|0xFF|



**6.2.2.2.2** **Initiate** **closing**


CL:0066.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.3.


Table 6.3: Barrier Operator::Initiate closing

|Field|Value|
|---|---|
|Command|BARRIER_OPERATOR_SET|
|Target Value|0x00|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1089




<!-- PAGE 1091 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.2.3** **Node** **properties**


CL:0066.01.42.01.1 The controlling node SHOULD have a UI allowing the end user to see/access the following properties:


     - Last known Barrier State (Open, Closed, stopped at a % position or unknown)


     - Last known Subsystems’ state (ON/OFF), if any


**6.2.2.4** **Additional** **control** **requirements**


CL:0066.01.52.01.2 A node controlling this command class SHOULD also control the Notification Command Class. A
node controlling this command class SHOULD activate all supported subsystems by default.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1090




<!-- PAGE 1092 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.3** **Basic** **Command** **Class,** **version** **1-2**


**6.2.3.1** **Mandatory** **node** **interview**


CL:0020.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.3.


Figure 6.3: Basic Command Class interview


CL:0020.01.21.02.2 A controlling node MUST conclude that the Basic Command Class is not supported by a node (or
endpoint) if no Basic Report is returned.


**6.2.3.2** **Minimum** **end** **user** **functionalities**


CL:0020.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.3.2.1** **Set** **the** **node** **On/Off** **state**


CL:0020.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.4

|Field|Table 6.4: Basic::Set the node state Value|
|---|---|
|Field|Value|
|Command|BASIC_SET<br>|
|Value|User defned among 0x00 and 0xFF.<br>More values MAY be available to the end user.|



**6.2.3.3** **Node** **properties**


CL:0020.01.43.01.1 A controlling node MAY have a UI allowing the end user to see the following properties:

     - Last known state (On or Off)

CL:0020.01.42.01.1 A controlling node SHOULD NOT assume that the last state is as defined in the last Set Command
and SHOULD issue a subsequent Basic Get Command even if receiving a Supervision SUCCESS
status after issuing a Basic Set Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1091




<!-- PAGE 1093 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.3.4** **Additional** **control** **requirements**


CL:0020.01.51.01.3 A controlling node MUST NOT use the Basic Command Class for controlling nor showing status (receiving report) of a node (or endpoint) if the controlling node controls at least one actuator command
class supported by a node (or endpoint). The actuator command classes are defined in _Application_
_Command_ _Classes_ .


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1092




<!-- PAGE 1094 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.4** **Binary** **Switch** **Command** **Class,** **version** **1-2**


**6.2.4.1** **Mandatory** **node** **interview**


CL:0025.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.4.


Figure 6.4: Binary Switch Command Class Interview


**6.2.4.2** **Minimum** **end** **user** **functionalities**


CL:0025.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.4.2.1** **Set** **the** **node** **On/Off** **state**


CL:0025.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.5.

|Field|Table 6.5: Binary Switch::Set the node state Value|
|---|---|
|**Field**|**Value**|
|Command|SWITCH_BINARY_SET<br>|
|Value|User defned among 0x00 and 0xFF.<br>|
|Duration (v2)|User defned or 0xFF|



**6.2.4.3** **Node** **properties**


CL:0025.01.51.01.1 A node controlling this Command Class SHOULD have a UI allowing the end user to see the following
properties:

     - Last known state (On or Off)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1093




<!-- PAGE 1095 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.5** **Central** **Scene** **Command** **Class,** **version** **1-3**


**6.2.5.1** **Mandatory** **node** **interview**


CL:005B.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.5.


Figure 6.5: Central Scene Command Class interview


CL:005B.01.23.01.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


**6.2.5.2** **Minimum** **end** **user** **functionalities**


There is no minimum end user functionalities associated with the control of this Command Class.

CL:005B.01.32.01.1 A controlling node SHOULD allow the user to define which other nodes to actuate when receiving a
Central Scene Notification from a given node with a given key attribute and SceneID.


**6.2.5.3** **Node** **properties**


CL:005B.01.41.01.1 The controlling node MUST have a UI allowing the end user to see how many Scenes ID (or buttons)
and key attributes are supported by a node.

CL:005B.01.41.02.1 The controlling node MUST make received Central Scene Notifications available to the end user.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1094




<!-- PAGE 1096 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.5.4** **Additional** **control** **requirements**


CL:005B.01.51.01.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:005B.01.51.02.1 A controlling node MUST associate itself to a group issuing Central Scene Notification Commands in
order to provide end user functionalities.


CL:005B.01.51.03.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Central Scene Notification Commands.


CL:005B.01.53.01.1 It is OPTIONAL for a controlling node to provide end user functionalities and node properties if it
cannot associate itself to an association group sending Central Scene Notification Commands. (e.g.
all Association Groups sending the relevant command are full)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1095




<!-- PAGE 1097 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.6** **Color** **Switch** **Command** **Class,** **version** **1-3**


**6.2.6.1** **Mandatory** **node** **interview**


CL:0033.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.


Figure 6.6: Color Switch Command Class interview


**6.2.6.2** **Minimum** **end** **user** **functionalities**


CL:0033.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.6.2.1** **Set** **the** **color**


CL:0033.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.6.

|Field|Table 6.6: Color Switch::Set the color Value|
|---|---|
|Field|Value|
|Command|SWITCH_COLOR_SET|
|Color component count|Determined by the controlling node based on user input<br>|
|Color Component ID x|User defned among supported<br>|
|Value x|User defned<br>|
|Duration (v2)|User defned or 0xFF|



CL:0033.01.31.03.1 For this functionality, the color selected by the end user MUST be set using a single command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1096




<!-- PAGE 1098 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.6.2.2** **Fade/enhance** **a** **color** **component**


CL:0033.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.7.


Table 6.7: Color Switch::Fade/enhance a color component

|Field|Value|
|---|---|
|Command|SWITCH_COLOR_START_LEVEL_CHANGE<br>|
|Up/down|User defned<br>|
|Color component ID|User defned among supported<br>|
|Duration (v3)|User defned or 0xFF|



**6.2.6.2.3** **Stop** **fading/enhancing** **a** **color** **component**


CL:0033.01.31.05.1 When the end user performs this action, the issued command MUST comply with Table 6.8.


Table 6.8: Color Switch::Stop fading/enhancing a color component

|Field|Value|
|---|---|
|Command|SWITCH_COLOR_STOP_LEVEL_CHANGE<br>|
|Color component ID|User defned among supported|



**6.2.6.3** **Node** **properties**


CL:0033.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:

     - Last known configured color or color components values


**6.2.6.4** **Additional** **control** **requirements**


CL:0033.01.51.01.1 A node controlling this Command Class MUST also control:


     - Binary Switch Command Class, version 2


     - Multilevel Switch, version 4


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1097




<!-- PAGE 1099 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.7** **Configuration** **Command** **Class,** **version** **1-4**


**6.2.7.1** **Mandatory** **node** **interview**


CL:0070.03.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.7.


Figure 6.7: Configuration Command Class interview


**6.2.7.2** **Minimum** **end** **user** **functionalities**


CL:0070.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.7.2.1** **Set** **a** **configuration** **parameter** **Value**


CL:0070.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.9 for
parameters numbers smaller than 256 and Table 6.10 for parameter numbers greater or equal to 256.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1098




<!-- PAGE 1100 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 6.9: Configuration::Set a (normal) configuration parameter

|Table 6.9: Co value Field|onfiguration::Set a (normal) configuration parameter Value|
|---|---|
|Field|Value|
|Command|CONFIGURATION_SET<br>|
|Parameter number|For version 2 or older: User defned<br>For version 3 or newer: User defned among supported parameter<br>numbers.<br>|
|Size|For version 2 or older: User defned among 1, 2 and 4.<br>For version 3 or newer: Automatically determined from confguration<br>parameter number properties<br>|
|Default|User defned or 0x00<br>For version 3 or older: this feld SHOULD NOT be set to 1.<br>|
|Command|For version 2 or older: User defned.<br>For version 3 or newer: User defned among supported values|



Table 6.10: Configuration::Set an extended range configuration parameter value

|Field|Value|
|---|---|
|Command (v2)<br>|CONFIGURATION_BULK_SET<br>|
|Parameter ofset (v2)|For version 2: User defned among any value (256..65535).<br>For version 3 or newer: User defned among supported parameter<br>numbers.<br>|
|Number of Parameters(v2)|User defned or 0x01.<br>|
|Size (v2)|For version 2: User defned among 1, 2 and 4.<br>For version 3 or newer: Automatically determined from confguration<br>parameter number properties<br>|
|Default (v2)|User defned or 0x00<br>For version 3 or older: this feld SHOULD NOT be set to 1.|
|Handshake (v2)<br>|0x00<br>|
|Confguration Value (v2)|For version 2: User defned.<br>For version 3 or newer: User defned among supported values|



**6.2.7.2.2** **Reset** **all** **configuration** **parameter** **values** **to** **default**


CL:0070.04.31.01.1 When the end user performs this action, the issued command MUST comply with Table 6.11.


Table 6.11: Configuration::Reset all configuration parameter values

|Table 6.11: C to default Field|Configuration::Reset all configuration parameter values Value|
|---|---|
|Field|Value|
|Command (v4)|CONFIGURATION_DEFAULT_RESET|



**6.2.7.3** **Node** **properties**


CL:0070.03.41.01.1 If nodes are version 3, the controlling node MUST have a UI allowing the end user to see supported
parameter numbers, their current value, their allowed value range and their default value.

Values MUST be presented according to the Format advertised in the Configuration Properties Report
Command.


CL:0070.01.41.01.1 If nodes are version 1 or 2, the controlling node MUST have a UI showing the known parameters that
have been set by the end user and their current value.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1099




<!-- PAGE 1101 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.7.4** **Additional** **control** **requirements**


CL:0070.04.51.01.1 If nodes are version 4, a node controlling this command class MUST NOT issue a Bulk Set Command
supporting nodes advertising “No Bulk support” in the Configuration Properties Report Commands.


CL:0070.04.51.02.1 If nodes are version 4, a node controlling this command class MUST NOT allow an end user to
issue a Configuration Set or a Bulk Set Command for parameters advertised as “read-only” in the
Configuration Properties Report Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1100




<!-- PAGE 1102 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.8** **Door** **Lock** **Command** **Class,** **version** **1-4**


**6.2.8.1** **Mandatory** **node** **interview**


CL:0062.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.8.


Figure 6.8: Door Lock Command Class interview


**6.2.8.2** **Minimum** **end** **user** **functionalities**


CL:0062.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.8.2.1** **Configure** **the** **door** **lock**


CL:0062.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.12.


Table 6.12: Door Lock::Configure the door lock

|Field|Value|
|---|---|
|Command|DOOR_LOCK_CONFIGURATION_SET<br>|
|Operation type|For version 4 or newer: User defned among supported operation<br>types.<br>For version 3 or older: User defned among 0x01..0x02|
|Outside Door Handles Mode|Free (0xF recommended)|
|Inside Door Handles Mode|Free (0xF recommended)<br>|
|Lock Timeout Minutes|User defned (0x00..0xFD) if Operation Type is set to 0x02, else<br>0xFE<br>|
|Lock Timeout seconds|User defned (0x00..0x3B) if Operation Type is set to 0x02, else<br>0xFE<br>|
|Auto-relock time (v4)|User defned if supported, else 0<br>|
|Hold and release time (v4)|User defned if supported, else 0<br>|
|BTB (v4)|User defned if supported, else 0<br>|
|TA (v4)|User defned if supported, else 0|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1101




<!-- PAGE 1103 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.8.2.2** **Set** **the** **door** **mode**


CL:0062.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.13.

|Field|Table 6.13: Door Lock::Set the door mode Value|
|---|---|
|Field|Value|
|Command|DOOR_LOCK_CONFIGURATION_SET<br>|
|Door Lock Mode|For version 4 or newer: User defned among supported modes.<br>For version 3 or older: User defned among 0x00 and 0xFF.<br>Timed Operation modes MUST NOT be selectable by the end user if the<br>door lock is not confgured in Timed Operation|



**6.2.8.3** **Node** **properties**


CL:0062.01.41.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known Door Lock mode (Secure, Unsecured, etc.)

     - Current door lock configuration


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1102




<!-- PAGE 1104 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.9** **Entry** **Control** **Command** **Class,** **version** **1**


**6.2.9.1** **Mandatory** **node** **interview**


CL:006F.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.9.


Figure 6.9: Entry Control Command Class interview


CL:006F.01.23.01.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


**6.2.9.2** **Minimum** **end** **user** **functionalities**


CL:006F.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.9.2.1** **Configure** **the** **keypad**


CL:006F.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.14.


Table 6.14: Entry Control Keypad::Configure the keypad

|Field|Value|
|---|---|
|Command|ENTRY_CONTROL_CONFIGURATION_SET<br>|
|Key Cache Size|User defned among supported values<br>|
|Key Cache Timeout|User defned among supported values|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1103




<!-- PAGE 1105 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.9.3** **Node** **properties**


CL:006F.01.41.01.1 A controlling node MUST have a UI allowing the end user to see the received Entry Control Notifications (Event type and data)


**6.2.9.4** **Additional** **control** **requirements**


CL:006F.01.51.01.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:006F.01.51.02.1 A controlling node MUST associate itself to a group issuing Entry Control Notification Commands
before performing a supporting node interview and providing end user functionalities.


CL:006F.01.51.03.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Entry Control Notification Commands.


CL:006F.01.52.01.1 A controlling node SHOULD NOT provide end user functionalities if it cannot associate itself to
an association group sending Entry Control Notification Commands. (e.g. all Association Groups
sending the relevant command are full)

CL:006F.01.52.02.1 A controlling node SHOULD have a UI allowing the end user to define what actions to take based on
received Entry Control Notifications.


CL:006F.01.52.03.1 A controlling node SHOULD also control Door Lock Command Class and Barrier Operator Command
Class. It SHOULD also allow the user to set the door mode or initiate opening/closing of a given
node based on received Entry Control Notifications.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1104




<!-- PAGE 1106 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10** **IR** **Repeater** **Command** **Class,** **version** **1**


**6.2.10.1** **Mandatory** **node** **interview**


CL:00A0.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.10.


Figure 6.10: IR Repeater Command Class interview


**6.2.10.2** **Minimum** **end** **user** **functionalities**


CL:00A0.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.10.2.1** **Repeat** **an** **IR** **code**


CL:00A0.01.31.02.1 This action MUST be available to the end user if the supporting node supports repeating IR Codes.


CL:00A0.01.31.03.1 When the end user performs this action, the issued commands MUST comply with Table 6.15.

|Field|Table 6.15: IR Repeater::Repeat an IR Code Value|
|---|---|
|Field|Value|
|Command|IR_REPEATER_REPEAT<br>|
|Sequence number|Controlling node defned. It MUST be incremented at each new repeat<br>action<br>|
|Sub carrier|Controlling node defned within the capabilities of the supporting node<br>|
|Duty Cycle|Controlling node defned within the capabilities of the supporting node<br>|
|Pulse time unit|Controlling node defned within the range advertised by the supporting<br>node in the IR Repeater Capabilities Report Command<br>|
|Report Number|Controlling node defned.|
|Last|1 for the last command, 0 else.<br>|
|Data|Controlling node defned.<br>The end user MUST be able to select an IR Code that will be transferred.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1105




<!-- PAGE 1107 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10.2.2** **Learn** **an** **IR** **code**


CL:00A0.01.31.04.1 This action MUST be available to the end user if the supporting node supports Learning IR Codes.


CL:00A0.01.31.04.1 When the end user performs this action, the issued command MUST comply with Table 6.16.

|Field|Table 6.16: IR Repeater::Learn an IR Code Value|
|---|---|
|Field|Value|
|Command<br>|IR_REPEATER_IR_CODE_LEARNING_START<br>|
|IR Code identifer|User defned among available IR Codes slots<br>|
|Timeout|Controlling node or User defned.<br>|
|Pulse time unit|Controlling node defned within the range advertised by the supporting<br>node in the IR Repeater Capabilities Report Command|



The Controlling node MUST inform the user about the status of the IR Code learning when the IR
Code Learning Status Command is received.


The controlling node MAY allow the end user to interrupt the learning process, if it does, the issued
command MUST comply with Table 6.17.


Table 6.17: IR Repeater::Stop learning an IR code

|Field|Value|
|---|---|
|Command|IR_REPEATER_IR_CODE_LEARNING_STOP|



**6.2.10.2.3** **Erase** **a** **learnt** **IR** **code**


CL:00A0.01.31.05.1 This action MUST be available to the end user if the supporting node supports Learning IR Codes.


CL:00A0.01.31.06.1 When the end user performs this action, the issued command MUST comply with Table 6.18.


Table 6.18: IR Repeater::Erase an IR Code from memory

|Field|Value|
|---|---|
|Command<br>|IR_REPEATER_LEARNT_IR_CODE_REMOVE<br>|
|IR Code identifer|User defned among available IR Codes slots that have a defned IR Code|



**6.2.10.2.4** **Repeat** **a** **learnt** **IR** **code**


CL:00A0.01.31.07.1 This action MUST be available to the end user if the supporting node supports Repeating IR Codes.


CL:00A0.01.31.08.1 When the end user performs this action, the issued command MUST comply with Table 6.19.

|Field|Table 6.19: IR Repeater::Repeat a learnt IR code Value|
|---|---|
|Field|Value|
|Command<br>|IR_REPEATER_REPEAT_LEARNT_CODE<br>|
|IR Code identifer|User defned among available Learnt IR Codes slots|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1106




<!-- PAGE 1108 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.10.3** **Node** **properties**


If the supporting node supports IR Code learning:

CL:00A0.01.41.01.1 - A controlling node MUST have a UI allowing the end user to see the which IR Code Identifiers
contain a valid learnt code.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1107




<!-- PAGE 1109 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.11** **Meter** **Command** **Class,** **version** **1-5**


**6.2.11.1** **Mandatory** **node** **interview**


CL:0032.01.21.01.2 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.11.


Figure 6.11: Meter Command Class interview


**6.2.11.2** **Minimum** **end** **user** **functionalities**


CL:0032.02.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.11.2.1** **Reset** **cumulated** **data**


CL:0032.02.31.02.1 This action MUST be available to the end user if both nodes implement version 2 or newer and the
supporting node indicates that meter reset is supported.


CL:0032.02.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.20.

|Field|Table 6.20: Meter::Reset cumulated data Value|
|---|---|
|Field|Value|
|Command (v2)|METER_RESET|



**6.2.11.3** **Node** **properties**


CL:0032.01.41.01.2 A controlling node MUST have a UI allowing the end user to see the last readings for each supported
scale and all cumulated values. For version 1 supporting nodes, the scale reported in the Meter Report
MUST be accessible to the end user.


CL:0032.01.41.02.1 A controlling node MUST always show the value even if the Type and/or Scale are unknown.


CL:0032.01.42.01.1 A controlling node SHOULD implement the capability to update its list of Meter Type and Scales,
so that new Meter Types and scales added in more recent versions are not presented as unknown.


CL:0032.01.41.03.1 If a controlling node receives an unknown Meter Type or Scale, it MUST allow the end user to identify
the Meter reading and MAY allow the user to assign a free-text description to that Meter reading


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1108




<!-- PAGE 1110 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.11.4** **Additional** **control** **requirements**


CL:0032.01.51.01.1 Unless unsolicited Meter Report Commands are received, a controlling node MUST:


     - Probe the current meter readings for each supported scale (and rate type if v4 nodes) at least
every 6 hours for listening nodes.


     - Probe the current meter readings for each supported scale (and rate type if v4 nodes) when the
supporting node issues a Wake Up Notification Command for sleeping nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1109




<!-- PAGE 1111 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.12** **Multilevel** **Sensor** **Command** **Class,** **version** **1-11**


**6.2.12.1** **Mandatory** **node** **interview**


CL:0031.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.12.


Figure 6.12: Multilevel Sensor Command Class interview


**6.2.12.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.2.12.3** **Node** **properties**


CL:0031.01.41.01.1 A controlling node MUST allow the end user to see the received readings for every Sensor types


CL:0031.01.41.02.1 A controlling node MUST always show the sensor reading values even if the Sensor Type and/or Scale
are unknown.


CL:0031.01.42.01.1 A controlling node SHOULD implement the capability to update its list of Sensor Type and Scales,
so that new Sensor Types and Scales added in [27] are not presented as unknown.


CL:0031.01.41.03.2 If a controlling node receives an unknown Sensor Type or Scale, it MUST allow the end user to identify
the Sensor reading and MAY allow the end user to assign a free-text description to the sensor reading.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1110




<!-- PAGE 1112 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.12.4** **Additional** **control** **requirements**


CL:0031.01.51.01.1 Unless unsolicited Multilevel Sensor Report Commands are received, a controlling node MUST:


     - Probe the current reading for each supported sensor type at least every 6 hours for listening
nodes.


     - Probe the current reading for each supported sensor type when the supporting node issues a
Wake Up Notification Command for sleeping nodes.


CL:0031.01.52.01.1 A node controlling this command class SHOULD also control:


     - Association Command Class, version 2


     - Association Group Information, version 3


CL:0031.01.52.02.1 A controlling node SHOULD associate itself to an association group issuing Multilevel Report Commands after performing a supporting node interview and providing end user functionalities.


CL:0031.01.51.02.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Multilevel Report Commands.

CL:0031.01.52.03.1 Controller SHOULD have a UI allowing the end user to define rules or commands based on received
readings.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1111




<!-- PAGE 1113 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.13** **Multilevel** **Switch** **Command** **Class,** **version** **1-4**


**6.2.13.1** **Mandatory** **node** **interview**


CL:0026.01.21.01.2 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.13. It is OPTIONAL to issue the _Multilevel_ _Switch_ _Supported_ _Get_ _Command_ if a controlling
node does not use this information for its UI.


Figure 6.13: Multilevel Switch Command Class interview


**6.2.13.2** **Mimimum** **End** **User** **Functionalities**


CL:0026.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.13.2.1** **Set** **the** **Level**


CL:0026.01.31.02.2 When the end user performs this action, the issued command MUST comply with Table 6.21.

|Field|Table 6.21: Multilevel Switch::Set the level Value|
|---|---|
|Field|Value|
|Command|SWITCH_MULTILEVEL_SET<br>|
|Value|User defned among 0x00..0x63. Using 0xFF is optional.<br>|
|Duration (v2)|User defned or 0xFF|



**6.2.13.3** **Node** **Properties**


CL:0026.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known state (xx%)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1112




<!-- PAGE 1114 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14** **Notification** **Command** **Class,** **version** **1-8**


**6.2.14.1** **Mandatory** **Node** **Interview**


CL:0071.02.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.14.


Figure 6.14: Notification Command Class interview


CL:0071.02.23.01.1 The step denoted as “1. Read Notification Type Status” in Figure 6.14 MAY be replaced by Notification Set commands for each Notification Type, with the Status field set to 0x00 or 0xFF.


CL:0071.02.23.02.1 A node controlling this command class MAY skip the AGI Interview (refer to Section 6.3.2) if the
supporting node is a Z-Wave Plus node and the controlling node has estalished a Lifeline Association.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1113




<!-- PAGE 1115 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.2** **Minimum** **End** **User** **Functionalities**


No minimum end user functionality is required for this Command Class.


**6.2.14.3** **Node** **Properties**


CL:0071.01.41.01.1 A controlling node MUST have a UI allowing the end user to see the received Notification Reports
(Notification type and event/state).


**6.2.14.4** **Additional** **Control** **Requirements**


CL:0071.01.51.01.1 A controlling node MUST probe state/event notifications from pull nodes


     - at least every 6 hours for listenting nodes.

     - when the supporting node issues a Wake up Notification Command for sleeping nodes.


CL:0071.01.51.02.1 A node controlling this command class MUST also control:


     - Association Command Class, version 2


     - Association Group Information, version 3

CL:0071.01.51.03.1 For Push supporting nodes, a controlling node MUST associate itself to a group issuing Notification
Report Commands before performing a supporting node interview and providing end user functionalities.


CL:0071.01.53.01.1 For Push supporting nodes, it is OPTIONAL for a controlling node to provide end user functionalities
and node properties if it cannot associate itself to an association group sending Notification Report
Commands. (e.g. all Association Groups sending the relevant command are full)


CL:0071.01.51.04.1 A controlling node MUST NOT remove associations in order to associate itself to an association group
issuing Notification Report Commands.

CL:0071.01.52.01.1 Controller SHOULD have a UI allowing the end user to define rules or commands based on received
notifications events/states.

CL:0071.01.52.02.1 A controlling node SHOULD implement the capability to update its Notifications list, so that new
Notifications added in [36] are not presented as unknown.

CL:0071.01.51.05.2 If a controlling node receives an unknown Notification, it MUST allow the end user to identify this
notification and MAY allow the end user to assign a free-text description to that Notification.


**6.2.14.4.1** **Detailed** **Controller** **Guidelines**


This section presents guidelines for controlling legacy sensors nodes supporting the Notification Command Class, version 3-8.


Alarm Command Class version 2 supporting nodes operate in Push mode only. The guidelines presented in Section 6.2.14.4.7 Controlling Pull Mode Sensors can also be used for controlling Alarm CC
version 2 supporting nodes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1114




<!-- PAGE 1116 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.4.2** **Sensor** **database**


The following sections present discovery methods for sensor properties, such as Push/Pull mode or
the use of state idle notifications. Some sensor properties (e.g. configuration parameters, Association
group properties, state variables dependencies) cannot always be discovered.

CL:0071.01.52.03.1 If a controlling node has a database of known certified Notification sensors, it SHOULD be consulted
first before attempting to interview the Notification Command Class of a supporting node. If the
supporting node is present in the database, a controlling node SHOULD read the sensor properties
from the database and skip any discovery.


**6.2.14.4.3** **Push/Pull** **mode** **discovery**


A supporting node does not advertise whether it operates in Push or Pull mode. Therefore a controlling
CL:0071.01.51.06.1 node MUST discover what mode a supporting node implements.


CL:0071.01.52.04.1 The RECOMMENDED discovery steps for a controlling node are the following:


If the supporting node does not support the Association Command Class, it may be concluded that
the supporting node implements Pull Mode and discovery may be aborted.


If the supporting node supports the AGI Command Class, probe the AGI table in the following way
or read the already probed AGI table:


1. Discover how many Association groups the supporting node (and its eventual End Points) implements by issuing an Association Supported Groupings Get Command.


2. For each association group, issue an Association Group Command List Get for the grouping identifier. Inspect the returned Association Group Command List Report and look for the following
pair: {Command Class x = COMMAND_CLASS_NOTIFICATION, Command x = NOTIFICATION_REPORT}. If a match is found, conclude that the supporting node implements Push
Mode and stop the discovery process.


If no match is found at the end of the AGI test, conclude that the supporting node implements Pull
Mode. The AGI test is illustrated in Figure 6.15.


Figure 6.15: Push/Pull Node Discovery, AGI table probing


If the supporting node does not support the AGI Command Class, proceed with the following Notification Command Class test:

1. Discover the list of supported Notification Types by issuing a Notification Supported Get Command.

2. For each supported Notification Type, query the supported Events/States via the Event Supported Get Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1115




<!-- PAGE 1117 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


3. Set the status of one of the Supported Notification Types at the target node using a Notification
Set Command with the following values:

a. Notification Type = (a supported type discovered in step 1)

b. Notification Status = 0xFF

4. Issue a Notification Get Command with the following values:

a. Notification Type = (Same as step 3.a).

b. Notification Event = (a supported Event/State discovered in step 2).

5. The supporting node returns a Notification Report Command.

a. If the Notification Status is 0xFF, the target node implements Push Mode

b. If the Notification Status is 0xFE or 0x00, the target node implements Pull Mode


c. If the target node did not return a report within 10 seconds, it implements Pull Mode

The Notification Command Class test is illustrated in Figure 6.16.


Figure 6.16: Push/Pull Node Discovery, Notification Command Class test


**6.2.14.4.4** **Unknown** **Notifications**


CL:0071.01.52.05.1 This Command Class defines some Notifications as event or states. It is RECOMMENDED to treat
an unknown Notification as its own state variable.


**6.2.14.4.5** **State** **idle**


A controlling node receiving a “State idle” Notification for an event or state of which the “State idle”
CL:0071.01.52.06.1 Notification does not apply (e.g. the “heartbeat” event) SHOULD ignore the Notification. Refer to

[36] for state variables to which the “State idle” notification applies.



CL:0071.01.52.07.2


CL:0071.01.53.02.1



It is not mandatory for nodes supporting Notification Command Class, version 7 or older to send a
“State idle” Notification for returning a state variable to idle. Thus, there is a risk that a “State idle”
is never sent. A controlling node SHOULD NOT use timeouts to consider a state variable to be idle
for example 5 minutes after the last received Notification for v8 or newer supporting nodes. It MAY
allow the end user to mark states variables as idle.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1116




<!-- PAGE 1118 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.14.4.6** **Parameter** **encapsulation**


CL:0071.01.53.03.1 A node implementing version 5 or older MAY use the following parameter encapsulation format: (User
ID, User Code Report Command) instead of (User Code Report Command).


CL:0071.01.52.08.1 A controlling node SHOULD accept the end user Code Report Event Parameter with a User ID byte
prefixed at the beginning of the Notification Event Parameter for backwards compatibility. A controlling node can detect the beginning of the end user Code Report by finding the following consecutive
bytes: {byte x= COMMAND_CLASS_USER_CODE, byte x+1 = USER_CODE_REPORT}.


**6.2.14.4.7** **Controlling** **Pull** **Mode** **Sensors**


The following sections present guidelines for controlling Pull sensors nodes.


**6.2.14.4.8** **Notification** **Get** **Command**


This command is used to retrieve the next Notification from the receiving node’s queue. Below are
recommendations for what values controlling nodes should set in the fields of this command.

**Notification** **Type** **(8** **bits)**

CL:0071.01.52.09.1 A controlling node SHOULD set the Notification Type field to 0xFF.

Earlier specification text suggested that Pull nodes must not ignore this command if the Notification
Type is set to a supported type; rather than 0xFF. Therefore, Pull sensors may respond to a Notification Get for a supported Notification type by retrieving the next notification in the queue matching
the specified Notification Type.

**Notification** **Event** **/State** **(8** **bits)**

CL:0071.01.52.0A.1 A controlling node SHOULD set this field to 0x00.

A receiving node will have an unpredictable behavior if this field is set to a supported Event.


**6.2.14.4.9** **Detecting** **and** **clearing** **persistent** **notifications**


It is optional for Pull nodes to specify a sequence number in notifications.

CL:0071.01.52.0B.1 A controlling node receiving twice the same Notification with identical sequence number SHOULD
consider the Notification as persistent. An example is given in Figure 6.17.


Figure 6.17: Detecting and Clearing Persistent Notifications, identical sequence numbers


Due to unclear specification text, sensors may issue persistent Notifications without a sequence number
CL:0071.01.52.0C.1 field or with a new sequence number every time. Therefore, a controlling node SHOULD consider


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1117




<!-- PAGE 1119 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


a notification to be persistent if it receives the same Notification (type and event/state) 5 times or
more. An example is given in Figure 6.18.


Figure 6.18: Detecting and clearing persistent notifications with incremental sequence numbers


**6.2.14.4.10** **Status** **and** **queue** **empty**


CL:0071.01.52.0D.1
A controlling node SHOULD stop issuing Notification Get Commands when receiving a Queue empty
notification (0xFE). Illustration is given in Figure 6.19.


CL:0071.01.53.04.1
All fields following the Status field MAY be omitted in the Notification Report if it advertises a Status
of 0xFE (queue empty).


Figure 6.19: Pull node event retrieval until receiving queue empty


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1118




<!-- PAGE 1120 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.15** **Simple** **AV** **Control** **Command** **Class,** **version** **1-4**


**6.2.15.1** **Mandatory** **Node** **interview**


CL:0094.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.20.


Figure 6.20: Simple AV Control Command Class interview


**6.2.15.2** **Minimum** **end** **user** **functionalities**


CL:0094.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.15.2.1** **Send** **a** **supported** **AV** **code**


CL:0094.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.22.


Table 6.22: Simple AV Control::Send a supported AV code

|Field|Value|
|---|---|
|Command|SIMPLE_AV_CONTROL_SET<br>|
|Sequence number|Controlling node defned. This feld MUST be incremented every time<br>the end user perform this action<br>|
|Key attributes|User defned<br>|
|Command x|User defned among supported AV codes|



CL:0094.01.31.03.1 The end user MUST be able to select among all supported AV codes even if the controlling node does
not know what the code actually represents.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1119




<!-- PAGE 1121 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.15.3** **Node** **properties**


CL:0094.01.41.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - List of supported AV Codes


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1120




<!-- PAGE 1122 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.16** **Sound** **Switch** **Command** **Class,** **version** **1**


**6.2.16.1** **Mandatory** **node** **interview**


CL:0079.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.21.


Figure 6.21: Sound Switch Command Class interview


**6.2.16.2** **Minimum** **end** **user** **functionalities**


CL:0079.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.16.2.1** **Configure** **the** **sound** **switch**


CL:0079.01.31.02.1 The end user MUST be able to configure the volume and default tone at the supporting node. When
the end user performs this action, the issued command MUST comply with Table 6.23.


Table 6.23: Sound Switch::Configure the sound switch

|Field|Value|
|---|---|
|Command|SOUND_SWITCH_CONFIGURATION_SET<br>|
|Volume<br>|User defned among 0x00..0x64 or 0xFF<br>|
|Default Tone identifer|User defned among supported or 0x00|



**6.2.16.2.2** **Play/stop** **a** **selected** **or** **default** **tone**


CL:0079.01.31.03.1 The end user MUST be able to play the default tone, play a selected tone or stop playing a tone.
When the end user performs this action, the issued command MUST comply with Table 6.24.

|Table Field|6.24: Sound Switch::Play/stop a selected or default tone Value|
|---|---|
|Field|Value|
|Command<br>|SOUND_SWITCH_TONE_PLAY_SET<br>|
|Tone identifer|User defned among supported tones, 0x00 and 0xFF.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1121




<!-- PAGE 1123 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.16.3** **Node** **properties**


CL:0079.01.42.01.1 Controller SHOULD allow the end user to see/access the following properties:

     - (Last known) configured volume

     - (Last known) configured default tone


     - List of supported tones and their duration


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1122




<!-- PAGE 1124 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.17** **Thermostat** **Mode** **Command** **Class,** **version** **1-3**


**6.2.17.1** **Mandatory** **interview**


CL:0040.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.22.


Figure 6.22: Thermostat Mode Command Class interview


**6.2.17.2** **Minimum** **end** **user** **functionalities**


CL:0040.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.17.2.1** **Change** **mode**


CL:0040.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.25.

|Field|Table 6.25: Thermostat Mode::Change mode Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_MODE_SET<br>|
|Mode|User defned among supported modes|



CL:0040.01.31.03.1 The end user MUST be able to select between all supported modes by the supporting node, even if
the controlling node does not know what a given mode represents.


**6.2.17.3** **Node** **properties**


CL:0040.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:


     - Last known mode


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1123




<!-- PAGE 1125 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.18** **Thermostat** **Setback** **Command** **Class,** **version** **1**


**6.2.18.1** **Mandatory** **interview**


CL:0047.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.23.


Figure 6.23: Thermostat Setback Command Class interview


**6.2.18.2** **Minimum** **end** **user** **functionalities**


CL:0047.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.18.2.1** **Configure** **setback**


CL:0047.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.26.


Table 6.26: Thermostat Setback::Change setback for a supported

|Table 6. type Field|.26: Thermostat Setback::Change setback for a supported Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_SETBACK_SET<br>|
|Setback Type|User defned among 0x00..0x02<br>|
|Setpoint State|User defned among 0x00..0x7A and 0x80..0xFF|



**6.2.18.3** **Node** **properties**


CL:0047.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known setback type and state.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1124




<!-- PAGE 1126 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.19** **Thermostat** **Setpoint** **Command** **Class,** **version** **1-3**


**6.2.19.1** **Mandatory** **interview**


CL:0043.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.24.


Figure 6.24: Thermostat Setpoint Command Class interview


It has been found that early implementations of this Command Class applied two non-interoperable
interpretations of the bit mask advertising the support for specific Setpoint Types in the Thermostat
Setpoint Supported Report Command.

Refer to the Thermostat Setpoint Command Class definition (Section 2.2.114, Section 2.2.115) for the
possible bitmask interpretations.


CL:0043.01.22.01.1 A controlling node SHOULD determine the supported Setpoint Types of a version 1 and version 2
supporting node by sending one Thermostat Setpoint Get Command at a time while incrementing
the requested Setpoint Type.


CL:0043.01.21.03.1 If the same Setpoint Type is advertised in the returned Thermostat Setpoint Report Command, the
controlling node MUST conclude that the actual Setpoint Type is supported.


If the Setpoint Type 0x00 (type N/A) is advertised in the returned Thermostat Setpoint Report
CL:0043.01.21.04.1 Command, the controlling node MUST conclude that the actual Setpoint Type is not supported.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1125




<!-- PAGE 1127 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.19.2** **Minimum** **end** **user** **functionalities**


CL:0043.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.19.2.1** **Change** **setpoint** **for** **a** **supported** **type**


CL:0043.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.27.


Table 6.27: Thermostat Setpoint::Change setpoint for a supported

|Table 6. type Field|.27: Thermostat Setpoint::Change setpoint for a supported Value|
|---|---|
|Field|Value|
|Command|THERMOSTAT_SETPOINT_SET<br>|
|Setpoint Type|User defned among supported<br>|
|Setpoint Value|If nodes are version 3 or newer: User defned among supported values<br>If nodes are version 1 or 2: User defned.<br>|
|Precision|User defned<br>|
|Scale|Controller defned<br>|
|Size|User defned|



CL:0043.01.31.03.1 If controlling a version 1 or 2 supporting node, the controlling node MUST allow the user to define
the Setpoint Value freely. The controlling node MUST read back the value with a Thermostat Mode
Get(Setpoint type) or use Supervision Get encapsulation and indicate to the end user if the operation
was successful.


CL:0043.01.31.04.1 The end user MUST be able to set the setpoint for any setpoint type, even if the controlling node
does not know what a given type represents.

CL:0043.01.31.05.1 The Scale field value MUST be identical to the value received in the Thermostat Setpoint Report for
the actual Setpoint Type during the node interview.

CL:0043.01.42.01.1 The controlling node SHOULD let the user define the Setpoint Value in their preferred scale but
MUST convert the value into the supporting node’s scale for issuing the Z-Wave Command.


**6.2.19.3** **Node** **properties**


CL:0043.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:


     - Last known setpoint value for each supported setpoint type.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1126




<!-- PAGE 1128 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.20** **User** **Code** **Command** **Class,** **version** **1-2**


**6.2.20.1** **Mandatory** **interview**


CL:0063.01.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.25.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1127




<!-- PAGE 1129 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 6.25: User Code Command Class interview


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1128




<!-- PAGE 1130 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


CL:0063.01.21.02.3 For a node controlling version 2 or newer:

     - It is OPTIONAL to send an _Extended_ _User_ _Code_ _Get_ _Command_ for every User Identifier to a
node supporting version 2 or newer if:


**–** The controlling node requested the checksum and it is set to 0, or


**–** The controlling node issues an _Extended_ _User_ _Code_ _Set_ _Command_ (User ID = 0, User ID
Status = 0) to delete all user codes, or

**–** The supporting node reports that no more User Identifiers are set in the _Extended_ _User_
_Code_ _Report_ _Command_ with the _Next_ _User_ _Identifier_ field.

     - It is OPTIONAL to send a _User_ _Code_ _Get_ _Command_ for every User Identifier to a node supporting version 1 if the controlling node issues a _User_ _Code_ _Set_ _Command_ (User ID = 0, User
ID Status = 0) to delete all user codes.


CL:0063.01.21.03.1 For a node controlling version 1:

     - It is OPTIONAL to send a _User_ _Code_ _Get_ _Command_ for every User Identifier to any supporting
node if the controlling node issues a _User_ _Code_ _Set_ _Command_ (User ID = 0, User ID Status =
0) to delete the user codes below User ID 256.


CL:0063.01.22.01.1 A controlling node SHOULD NOT automatically delete any user code unless it is the initial interview
right after having included the supporting node in the network.


**6.2.20.2** **Minimum** **end** **user** **functionalities**


CL:0063.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.20.2.1** **Set/modify** **a** **User** **Code**


CL:0063.01.31.02.1 When the end user performs this action, the issued command MUST comply with Table 6.28 if nodes
are v1 or Table 6.29 if nodes are v2 or newer.


Table 6.28: User Code::Set a User Code

|Field|Value|
|---|---|
|Command<br>|USER_CODE_SET (0x01)<br>|
|User Identifers|User defned or controlling node defned among supported User<br>Identifers.<br>|
|User ID Status|Used defned among 0x01 and 0x02<br>0x02 must be used to set a reserved/forbidden user code.<br>|
|User Code|User defned among 0x30..0x39 with a length in the range 4..10<br>bytes.|



A forbidden or reserved User Code is a User Code that cannot be used at the supporting node and
cannot be allocated to a new user, for example if User Code can also be updated locally via a user
interface.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1129




<!-- PAGE 1131 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

|Table Field|6.29: User Code::Set a User Code (v2) Value|
|---|---|
|Field|Value|
|Command|EXTENDED_USER_CODE_SET (0x0B)<br>|
|Number of User Codes (v2)<br>|Controlling node defned<br>|
|User Identifer 1..M (v2)|User defned or controlling node defned among supported User<br>Identifers.<br>|
|User ID status (v2)|Used defned among supported User ID statuses.<br>|
|User Code Length (v2)|Controlling node defned based on the length of the User Code<br>feld.<br>|
|User Code (v2)|User defned among supported ASCII characters with a length in<br>the range 4..10 bytes.|



**6.2.20.2.2** **Erase** **a** **User** **Code**


CL:0063.01.31.03.1 When the end user performs this action, the issued command MUST comply with Table 6.30 if nodes
are v1 and Table 6.31 if nodes are v2 or newer.

|Field|Table 6.30: User Code::Erase a User Code Value|
|---|---|
|Field|Value|
|Command<br>|USER_CODE_SET<br>|
|User Identifers|User defned or controlling node defned among supported User Identifers.|
|User ID Status|Used 0x00|
|User Code|0x00000000|



CL:0063.01.31.04.1 A controlling node MAY allow the end user to erase all user codes at once. In this case, the User
Identifier field MUST be set to 0x00.











|Field|Table 6.31: User Code::Erase a User Code Value|
|---|---|
|Field|Value|
|Command|EXTENDED_USER_CODE_SET (0x0B)<br>|
|Number of User Codes<br>(v2)<br>|Controlling node defned<br>|
|User<br>Identifer<br>1..M<br>(v2)|User defned or controlling node defned among supported User Identifers.|
|User ID status (v2)|0x00|
|User Code Length(v2)|0x00|
|User Code (v2)|Omitted|


**6.2.20.2.3** **Set** **the** **keypad** **mode** **(v2)**


CL:0063.01.31.05.1 This action MUST be available to the end user if nodes are v2 or newer and the supporting node
supports more than one keypad mode. When the end user performs this action, the issued command
MUST comply with Table 6.32.

|Field|Table 6.32: User Code::Set the Keypad Mode Value|
|---|---|
|Field|Value|
|Command (v2)|USER_CODE_KEYPAD_MODE_SET (0x08)<br>|
|Keypad Mode (v2)|User defned among supported keypad modes.|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1130




<!-- PAGE 1132 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.20.2.4** **Set** **the** **Admin** **Code** **(v2)**


CL:0063.01.31.06.1 This action MUST be available to the end user if nodes are v2 or newer and the supporting node
supports the Admin Code functionality. When the end user performs this action, the issued command
MUST comply with Table 6.33.

|Field|Table 6.33: User Code::Set the Admin Code Value|
|---|---|
|Field|Value|
|Command (v2)|ADMIN_CODE_SET (0x0E)<br>|
|Admin Code Length<br>(v2)|Controlling node defned based on the length of the User Code feld.<br>It MUST be possible to de-activate the Admin Code if the supporting<br>node supports Admin Code Deactivation.<br>|
|Admin Code (v2)|User defned among supported ASCII characters with a length in the<br>range 4..10 bytes.|



**6.2.20.3** **Node** **properties**


CL:0063.01.41.01.1 Controller MUST have a UI allowing the end user to see the following properties:


     - Number of supported User Codes


     - The list of last known set User Codes


     - The current keypad mode, if the supporting node supports more than one (v2)


     - The current set Admin Code, if the supporting node supports a Admin Code (v2)


**6.2.20.4** **Additional** **control** **requirements**


It has been found that some version 1 nodes wrongfully report obfuscated User Codes in the User
Code Report (e.g. ‘******’).


CL:0063.01.52.01.1 A controlling node SHOULD understand that a code has been set correctly but cannot be read back
with such nodes.


CL:0063.01.52.02.1 If nodes are version 2 or newer, a controlling node SHOULD verify the User Code checksum (if
supported) periodically (e.g. once a day) to ensure that User Code databases are synchronized.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1131




<!-- PAGE 1133 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21** **User** **Credential** **Command** **Class,** **version** **1**


**6.2.21.1** **Mandatory** **interview**


CL:0083.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.26.


Figure 6.26: User Credential Command Class interview


CL:0083.01.22.02.1 If the All Users Checksum Support field is set in the _User Capabilities Report Command_, the controlling
node SHOULD send an _All_ _Users_ _Checksum_ _Get_ _Command_ to check if there are existing Users or
Credentials present on the supporting node.


CL:0083.01.22.03.1 If the supporting node does not support the _All_ _Users_ _Checksum_ _Get_ _Command_, or if it does and the
All Users Checksum field of the _All_ _Users_ _Checksum_ _Report_ _Command_ is non-zero, the controlling
node SHOULD perform an interview of the existing Users and Credentials according to Figure 6.27.


Figure 6.27: User Credential Command Class optional interview


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1132




<!-- PAGE 1134 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2** **Minimum** **end** **user** **functionalities**


CL:0083.01.31.04.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.21.2.1** **Add/Modify** **a** **User**


CL:0083.01.31.05.1 When the end user performs this action, the issued command MUST comply with Table 6.34.


Table 6.34: User Credential::Add/Modify a User


|Field|Value|
|---|---|
|Command|USER_SET (0x05)<br>|
|Operation Type<br>|Controlling node defned as Add (0x00) or Modify (0x01).<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|User Type|User defned or controlling node defned among the Supported<br>User Types as specifed in the _User Capabilities Report Com-_<br>_mand_.<br>|
|User Active State|User defned or controlling node defned.<br>|
|Credential Rule|User defned or controlling node defned among the Supported<br>Credential Rules as specifed in the_ User Capabilities Report Com-_<br>_mand_.<br>|
|Expiring Timeout Minutes|User defned or controlling node defned. This MUST be non-zero<br>if the User Type is Expiring User (0x07) and MUST be zero if<br>the User Type is not Expiring User (0x07).<br>|
|User Name Encoding|Controlling node defned.<br>|
|User Name Length|Controlling node defned based on the length of the User Name.<br>|
|User Name|User defned or controlling node defned among supported User<br>Name Encoding characters and User Name Length.|



CL:0083.01.33.06.1


CL:0083.01.32.07.1


CL:0083.01.31.08.1



A controlling node MAY offer the User Types under different names. If they are renamed they
SHOULD be accompanied by a description, and the name mapping MUST be noted in the product
documentation.



CL:0083.01.31.09.1 If a controlling node does not offer all User Types, it MUST make note of which User Types are not
controlled in the product documentation.


CL:0083.01.31.10.1
If a controlling node does not offer all Credential Rules, it MUST make note of which Credential Rules
are not controlled in the product documentation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1133




<!-- PAGE 1135 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2.2** **Delete** **a** **User**


CL:0083.01.31.11.1 When the end user performs this action, the issued command MUST comply with Table 6.35.


Table 6.35: User Credential::Delete a User

|Field|Value|
|---|---|
|Command|USER_SET (0x05)<br>|
|Operation Type<br>|Controlling node defned as Delete (0x02).<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|User Type|Omitted or controlling node defned as the default value.<br>|
|User Active State|Omitted or controlling node defned as the default value.<br>|
|Credential Rule|Omitted or controlling node defned as the default value.<br>|
|Expiring Timeout Minutes|Omitted or controlling node defned as the default value.<br>|
|User Name Encoding|Omitted or controlling node defned as the default value.<br>|
|User Name Length|Omitted or controlling node defned as the default value.<br>|
|User Name|Omitted or controlling node defned as the default value.|



CL:0083.01.33.12.1 A controlling node MAY allow the end user to erase all Users and their associated Credentials and

CL:0083.01.31.13.1 schedules at once. In this case, the User Unique Identifier field MUST be set to 0x0000.


**6.2.21.2.3** **Add/Modify** **a** **Credential**


CL:0083.01.31.14.1 When the end user performs this action, the issued command MUST comply with Table 6.36.


Table 6.36: User Credential::Add/Modify a Credential

|Field|Value|
|---|---|
|Command<br>|CREDENTIAL_SET (0x0A)<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|Credential Type|User defned or controlling node defned among supported Cre-<br>dential Types specifed in the_ Credential Capabilities Report Com-_<br>_mand_.<br>|
|Credential Slot|User defned or controlling node defned in the range of one to the<br>Number of Supported Credential Slots for the given Credential<br>Type in the _Credential Capabilities Report Command_.<br>|
|Operation Type|Controlling node defned as Add (0x00) or Modify (0x01).<br>|
|Credential Length|Controlling node defned based on the length of the Credential<br>Data.<br>MUST not be less than the Min Length of Credential<br>Data for the specifc Credential Type specifed in the _Credential_<br>_Capabilities Report Command_ and MUST not be more than the<br>Max Length of Credential Data for the specifc Credential Type<br>specifed in the _Credential Capabilities Report Command_.<br>|
|Credential Data|User defned.|



CL:0083.01.33.15.1 A controlling node MAY infer the Credential Type from the Credential Data provided by the end

user.

CL:0083.01.31.16.1 If a controlling node does not offer all Credential Types, it MUST make note of which Credential
Types are not controlled in the product documentation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1134




<!-- PAGE 1136 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.21.2.4** **Delete** **a** **Credential**


CL:0083.01.31.17.1 When the end user performs this action, the issued command MUST comply with Table 6.37.


Table 6.37: User Credential::Delete a Credential

|Field|Value|
|---|---|
|Command<br>|CREDENTIAL_SET (0x0A)<br>|
|User Unique Identifer|User defned or controlling node defned among supported User<br>Identifers in the range of what was specifed as supported in the<br>_User Capabilities Report Command_.<br>|
|Credential Type|User defned or controlling node defned among supported Cre-<br>dential Types specifed in the_ Credential Capabilities Report Com-_<br>_mand_.<br>|
|Credential Slot|User defned or controlling node defned in the range of one to the<br>Number of Supported Credential Slots for the given Credential<br>Type in the _Credential Capabilities Report Command_.<br>|
|Operation Type|Controlling node defned as Delete (0x02).<br>|
|Credential Length|Zero or controlling node defned.<br>|
|Credential Data|Omitted or User defned.|



CL:0083.01.33.18.1 A controlling node MAY allow the end user to erase all Credentials of a Credential Type for a User

CL:0083.01.31.19.1 Unique Identifier at once. In this case, the User Unique Identifier and Credential Type MUST be
non-zero and the Credential Slot MUST be 0x0000.


CL:0083.01.33.20.1 A controlling node MAY allow the end user to erase all Credentials of all Credential Types for a

CL:0083.01.31.21.1 User Unique Identifier at once. In this case, the User Unique Identifier MUST be non-zero and the
Credential Type MUST be 0x00.


CL:0083.01.33.22.1 A controlling node MAY allow the end user to erase all Credentials for all Users at once. In this case,

CL:0083.01.31.23.1 the User Unique Identifier MUST be 0x0000.


CL:0083.01.33.24.1 A controlling node MAY allow the end user to erase all Credentials for a Credential Type at once. In

CL:0083.01.31.25.1 this case, the User Unique Identifier and Credential Slot MUST be 0x0000 and the Credential Type
MUST be non-zero.


**6.2.21.3** **Node** **properties**


CL:0083.01.41.26.1 A controlling node MUST have a UI allowing the end user to see the following properties:


     - The list of Users and their basic properties:


**–** The User Name


**–** The User Active State


**–** The Credentials assigned to a User and their basic properties:


∗The Credential Type


CL:0083.01.42.27.1 A controlling node SHOULD have a UI allowing the end user to see the following properties:

     - The number of supported User Unique Identifiers


     - The supported Credential Rules (Single, Dual, Triple)


     - The supported Credential Types


     - The list of Users and their additional properties:

**–** The User Unique Identifier


**–** The User Type


**–** The Credential Rule


**–** The Expiring Timeout Minutes, if the User Type is Expiring User (0x07)


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1135




<!-- PAGE 1137 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**–** The Credentials assigned to a User and their additional properties:


∗The Credential Slot


∗The Credential Data


CL:0083.01.41.28.1
A node controlling this command class MUST also control the Notification Command Class, version 8
or newer and have a UI allowing the end user to see Notification Reports with the following Notification
Types.

     - **Notification** **Type** **“Access** **Control”** **(0x06)**


**–** “Credential lock/close operation” (0x23)


**–** “Credential unlock/open operation” (0x24)


**–** “All users deleted” (0x25)


**–** “Multiple credentials deleted” (0x26)


**–** “User added” (0x27)

**–** “User modified” (0x28)


**–** “User deleted” (0x29)


**–** “User unchanged” (0x2A)


**–** “Credential added” (0x2B)

**–** “Credential modified” (0x2C)


**–** “Credential deleted” (0x2D)


**–** “Credential unchanged” (0x2E)


**–** “Valid credential access denied due to User Active State being set to Occupied Disabled” (0x2F)


**–** “Valid credential access denied due to the User’s schedule being inactive” (0x30)


**–** “User access denied due to not enough credentials entered for the User’s Credential
Rule” (0x31)


**–** “Invalid credential used to access the node” (0x32)


**–** “Non-Access credential entered via local interface” (0x33)

     - **Notification** **Type** **“Emergency** **Alarm”** **(0x0A)**


**–** “Panic Alert” (0x04)


**6.2.21.4** **Additional** **control** **requirements**


CL:0083.01.51.29.1 If a node controlling this command class supports setting schedules for Unique User Identifiers, then
they MUST also control the _Schedule_ _Entry_ _Lock_ _Command_ _Class,_ _version_ _4_ _[NEVER_ _CERTIFIED]_,
or higher.


CL:0083.01.52.30.1 If the supporting node supports the _All_ _Users_ _Checksum_ _Report_ _Command_, the controlling node
SHOULD verify the All Users Checksum periodically (e.g. once a day) to ensure that the Users and
Credentials are synchronized between the supporting and controlling nodes.


CL:0083.01.52.31.1 A node controlling this command class SHOULD be resilient to receiving a _User_ _Set_ _Error_ _Report_
_Command_ or a _Credential_ _Set_ _Error_ _Report_ _Command_ when sending a _User_ _Set_ _Command_ or a
_Credential_ _Set_ _Command_, respectively, and try to resend the command with corrected fields.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1136




<!-- PAGE 1138 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.22** **Window** **Covering** **Command** **Class,** **version** **1**


**6.2.22.1** **Mandatory** **interview**


CL:006A.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.28.


Figure 6.28: Window Covering Command Class interview


**6.2.22.2** **Minimum** **end** **user** **functionalities**


CL:006A.01.31.02.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


**6.2.22.2.1** **Go** **to** **position**


CL:006A.01.31.02.1 This action MUST be available to the end user for parameters ID with known positions (odd parameters IDs). When the end user performs this action, the issued command MUST comply with Table
6.38.

|Field|Table 6.38: Window Covering::Go to a Position Value|
|---|---|
|Field|Value|
|Command|WINDOW_COVERING_SET<br>|
|Parameter count|User defned ( 0x01)<br>|
|Parameter ID x|User defned among supported (odd values)<br>|
|Value x|User defned among 0x00..0x63<br>|
|Duration|User defned or 0xFF|



© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1137




<!-- PAGE 1139 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.2.22.2.2** **Start** **level** **change** **up** **or** **down**


CL:006A.01.31.03.1 This action MUST be available to the end user for all supported parameters ID. When the end user
performs this action, the issued command MUST comply with Table 6.39.


Table 6.39: Window Covering::Start Level Change Up or Down

|Field|Value|
|---|---|
|Command|WINDOW_COVERING_START_LEVEL_CHANGE<br>|
|Up/Down|User defned among 0x00 and 0x01<br>|
|Parameter ID|User defned among supported parameters ID<br>|
|Duration|User defned or 0xFF|



**6.2.22.2.3** **Stop** **level** **change**


CL:006A.01.31.04.1 This action MUST be available to the end user for all supported parameters ID. When the end user
performs this action, the issued command MUST comply with Table 6.40.

|Field|Table 6.40: Window Covering::Stop Level Change Value|
|---|---|
|Field|Value|
|Command|WINDOW_COVERING_STOP_LEVEL_CHANGE<br>|
|Parameter ID|User defned among supported parameters ID|



**6.2.22.3** **Node** **properties**


CL:006A.01.42.01.1 Controller SHOULD have a UI allowing the end user to see the following properties:


     - Last known position/value for all parameters IDs with known position


**6.2.22.4** **Additional** **control** **requirements**


CL:006A.01.51.01.2 A controlling node MUST NOT interview and provide controlling functionalities for the Multilevel
Switch Command Class for a node (or endpoint) supporting this Command Class, as it is a fully
redundant and less precise application functionality.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1138




<!-- PAGE 1140 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.3 Management Command Class Control Definitions**


**6.3.1** **Association** **Command** **Class,** **version** **1-4**


**6.3.1.1** **Mandatory** **Node** **interview**


CL:0085.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.29.


Figure 6.29: Association Command Class interview


**6.3.1.2** **Minimum** **End** **User** **functionalities**


No minimum end user functionality is required for this Command Class.


A controlling node implementing a UI that allows an end user to establish association between nodes
CL:0085.01.31.01.1 MUST NOT restrict the end user from establishing associations that are allowed. Refer to Section
6.3.1.4 for allowed associations.


**6.3.1.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.1.4** **Additional** **Control** **requirements**


If the supporting node also supports Multi Channel Association and the controlling node controls
CL:0085.01.51.01.1 Multi Channel Association, the controlling node MUST interview and control the Multi Channel
Association Command Class instead of this Command Class.


CL:0085.01.51.02.1 A controlling node MUST use the Association Group Information (AGI) Command Class to probe the
commands that a given association group will be sending before creating associations towards other
nodes.


If an association group in a Node A sends one or more controlling commands:


CL:0085.01.51.03.3


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1139




<!-- PAGE 1141 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


     - A controlling node MUST NOT associate Node A to a Node B destination that does not support
the Command Class that the Node A will be controlling.


CL:0085.01.53.01.3 - A controlling node MAY create an association to a destination supporting an actuator Command
Class if the actual association group sends Basic Control Command Class.


For Association version 1 and version 2:


CL:0085.01.51.04.3 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A and
Node B’s highest Security Class are not identical.


For Association version 3 or newer:


CL:0085.03.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A was
not granted Node B’s highest Security Class.


If an association group in Node A sends only supporting commands:


CL:0085.01.53.02.3 - A controlling node MAY create an association to any Node B destination if the actual association
group sends commands reflecting the support of a Command Class by the sending Node/End
Point. Refer to [25] for supporting/controlling commands.


CL:0085.01.51.06.1 - A controlling node MUST NOT associate Node A to a Node B destination if Node B was not
granted Node A’s highest Security Class.


**6.3.1.4.1** **Removing** **associations**


CL:0085.01.51.05.1 A controlling node MUST NOT remove already associated nodes to a destination Group to associate
themselves, unless:


     - The destination NodeID/Endpoint has left the network (i.e. SIS has received a Device Reset
Locally Notification)


     - The destination of a group has changed capabilities and does not support the command received
via the association group (also if a Multi Channel End Point is removed).

     - An end user has actively confirmed to remove associations


     - The lifeline group is full and the controlling node has the SIS Role.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1140




<!-- PAGE 1142 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.2** **Association** **Group** **Information** **(AGI)** **Command** **Class,** **version** **1-3**


**6.3.2.1** **Mandatory** **node** **interview**


CL:0059.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.30.


Figure 6.30: Association Group Information (AGI) Command Class interview


CL:0059.01.23.01.1 A controlling node MAY issue a single Association Group Info Get Command by using the List Mode
flag.


**6.3.2.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.2.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1141




<!-- PAGE 1143 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.3** **Battery** **Command** **Class,** **version** **1**


**6.3.3.1** **Mandatory** **node** **interview**


CL:0080:01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.31


Figure 6.31: Battery Command Class interview


**6.3.3.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.3.3** **Node** **properties**


CL:0080.01.41.01.1 A controlling node MUST allow the end user to see the last known battery level.


**6.3.3.4** **Additional** **control** **requirements**


CL:0080.01.52.01.1 Unless unsolicited Battery Report Commands are received, a controlling node SHOULD Probe the
current battery level at least every month


CL:0080.01.51.02.1 A controlling node MUST indicate to the end user that the battery needs to be replaced or reloaded
when the supporting node issues a Battery Report with the _Battery_ _Level_ field set to 0xFF.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1142




<!-- PAGE 1144 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.4** **Device** **Reset** **Locally** **Command** **Class,** **version** **1**


**6.3.4.1** **Mandatory** **node** **interview**


No mandatory node interview is required for this Command Class.


**6.3.4.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.4.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.4.4** **Additional** **control** **requirements**


CL:005A.01.52.01.1 A controlling node receiving the Device Reset Locally Notification Command SHOULD consider
the sending node to be a failing node and accordingly perform relevant maintenance operations like
removing failing nodes, removing associations to failing nodes, etc.

CL:005A.01.51.01.1 A controlling node receiving the Device Reset Locally Notification Command MUST indicate to the
end user that the node has been reset and left the Z-Wave network.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1143




<!-- PAGE 1145 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.5** **Firmware** **Update** **Meta** **Data** **Command** **Class,** **version** **1-6**


**6.3.5.1** **Mandatory** **node** **interview**


CL:007A.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.32.


Figure 6.32: Firmware Update Meta Data Command Class interview


**6.3.5.2** **Minimum** **end** **user** **functionalities**


**6.3.5.2.1** **Firmware** **update**


CL:007A.01.32.01.1 A controlling node SHOULD provide a method for updating the firmware of a supporting node.
The end user SHOULD be able to select a firmware file or ask the controller to look for updates
automatically.


CL:007A.01.31.01.1 If this functionality is available, the issued commands MUST comply with Figure 6.33 when the end
user performs this action.


CL:007A.01.33.01.1 A controlling node MAY use additional commands such as Firmware Update Activation Set Command
for the firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1144




<!-- PAGE 1146 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Figure 6.33: Firmware Update Meta Data::Firmware Update


CL:007A.01.32.02.1
If a controlling node allows the end user to interrupt an ongoing firmware update transfer, it SHOULD
issue a FIRMWARE_UPDATE_MD_REPORT Command with the Last field set to 1 prematurely.


**6.3.5.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


CL:007A.01.42.01.1 A controlling node SHOULD have a UI allowing the end user to see the Firmware version of a
supporting node.


**6.3.5.4** **Additional** **control** **requirements**


If the supporting node supports Battery Command Class and the controlling node controls Battery
CL:007A.01.52.01.1 Command Class, the controlling node SHOULD issue a Battery Get and read the battery level before
initiating a Firmware Update.


CL:007A.01.52.02.1 A controlling node SHOULD NOT initiate a Firmware Update if the supporting node Battery level
is less than 50%.

CL:007A.01.51.01.1 A controlling node MUST perform a full interview of a node after performing a firmware update.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1145




<!-- PAGE 1147 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.6** **Indicator** **Command** **Class,** **version** **1-3**


**6.3.6.1** **Mandatory** **node** **interview**


CL:0087.01.21.01.1 A node controlling this Command Class MUST perform a supporting node interview according to
Figure 6.34.


Figure 6.34: Indicator Command Class interview


**6.3.6.2** **Minimum** **end** **user** **functionalities**


CL:0087.01.31.01.1 A node controlling this command class MUST allow the end user to perform the actions described
below.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1146




<!-- PAGE 1148 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.6.2.1** **Identify**


CL:0087.01.31.02.1 If the supporting and controlling nodes are version 3 or newer, the end user MUST be able to instruct
the node to identify itself. When the end user performs this action, the issued command MUST
comply with Table 6.41.

|Field|Table 6.41: Indicator::Identity Value|
|---|---|
|Field|Value|
|Command|INDICATOR_SET|
|Indicator 0 Value|0x00|
|Indicator object count|0x03|
|Indicator ID 1|0x50|
|Property ID 1|0x03|
|Value 1|0x08|
|Indicator ID 2|0x50|
|Property ID 2|0x04|
|Value 2|0x03|
|Indicator ID 3|0x50|
|Property ID 3|0x05|
|Value 3|0x06|



The supporting node will be switched on 600ms and switched off 200ms three times.


CL:0087.01.33.01.1 A controlling node MAY hide this functionality away from the end user if the supporting node also
supports the Wake Up Command Class.


**6.3.6.3** **Node** **properties**


CL:0087.01.42.01.1 The controlling node SHOULD have a UI allowing the end user to see/access the following properties:


     - Last known Indicators’ state/value (ON/OFF or x%), if any


**6.3.6.4** **Additional** **control** **requirements**


CL:0087.01.51.01.1 A node controlling this command class MUST NOT reuse the identify command for any other purpose
than a node identification application.


CL:0087.01.52.01.3 A node controlling this Command Class SHOULD NOT make a supporting node blink 3 times for
any indication (except when using the Identify Indicator for the Identify purpose).


CL:0087.01.52.02.1 A node controlling this Command Class SHOULD allow the end user to actuate additional indicating

resources.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1147




<!-- PAGE 1149 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.7** **Multi** **Channel** **Association** **Command** **Class,** **version** **2-5**


**6.3.7.1** **Mandatory** **node** **interview**


CL:008E.01.21.01.1 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.35.


Figure 6.35: Multi Channel Association Command Class interview


CL:008E.01.21.02.2 The lifeline association MUST be an End Point Association (controller NodeID after the
MULTI_CHANNEL_ASSOCIATION_SET_MARKER) if:


     - Both nodes implement Multi Channel Association, version 3 or newer.


     - The supporting node also supports the Multi Channel Command Class.


CL:008E.01.22.01.1 The lifeline association SHOULD be a NodeID association in any other case.


**6.3.7.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


CL:008E.01.31.01.1 A controlling node implementing a UI which allows an end user to establish association between nodes
MUST NOT restrict the end user from establishing associations that are allowed. Refer to Section
6.3.7.4 for allowed associations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1148




<!-- PAGE 1150 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.7.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.3.7.4** **Additional** **control** **requirements**


If the supporting node also supports Association and the controlling node controls Association, the
CL:008E.01.51.01.1 controlling node MUST NOT interview and control the Association Command Class.


CL:008E.01.51.02.1 A controlling node MUST use the Association Group Information (AGI) Command Class to probe the
commands that a given association group will be sending before creating associations towards other
nodes.


If an association group in a Node A sends one or more controlling commands:


CL:008E.01.51.03.3 - A controlling node MUST NOT associate Node A to a Node B destination that does not support
the Command Class that the Node A will be controlling.


CL:008E.01.53.01.3 - A controlling node MAY create an association to a destination supporting an actuator Command
Class if the actual association group sends Basic Control Command Class.


For Multi Channel Association version 2 and version 3:


CL:008E.02.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A and
Node B’s highest Security Class are not identical.


For Multi Channel Association version 4 or newer:


CL:008E.04.51.01.1 **–** A controlling node MUST NOT associate Node A to a Node B destination if Node A was
not granted Node B’s highest Security Class.


If an association group sends only supporting commands:


CL:008E.01.53.02.2 - A controlling node MAY create an association to any destination if the actual association group
sends commands reflecting the support of a Command Class by the sending Node/End Point.
Refer to [25] for supporting/controlling commands.


CL:008E.01.51.06.1 - A controlling node MUST NOT associate Node A to a Node B destination if Node B was not
granted Node A’s highest Security Class.


**6.3.7.4.1** **Removing** **associations**


CL:008E.01.51.05.1 A controlling node MUST NOT remove already associated nodes to a destination Group to associate
themselves, unless:


     - The destination NodeID/Endpoint has left the network (i.e. SIS has received a Device Reset
Locally Notification)


     - The destination has changed capabilities and does not support the command received via the
association group (also if a Multi Channel End Point is removed).

     - An end user has actively confirmed to remove associations


     - The lifeline group is full and the controlling node has the SIS Role.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1149




<!-- PAGE 1151 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.8** **Version** **Command** **Class,** **version** **1-3**


**6.3.8.1** **Mandatory** **node** **interview**


CL:0086.01.21.01.2 A node controlling this command class MUST perform a supporting node interview according to
Figure 6.36.


Figure 6.36: Version Command Class interview


CL:0086.01.21.02.1 The interview part starting from the Version Capabilities Get Command is optional. The Controlling node MUST interview the Version Capability Get Command before issuing the Version Z-Wave
Software Get Command if the Controlling node has the intent of using the Z-Wave software version.


**6.3.8.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.8.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1150




<!-- PAGE 1152 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.8.4** **Additional** **control** **requirements**


CL:0086.01.51.01.1 A controlling node interviewing a Multi Channel End Point MUST request the End Point’s Command
Class version from the Root Device if the End Point does not advertise support for the Version
Command Class.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1151




<!-- PAGE 1153 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.9** **Wake-Up** **Command** **Class,** **version** **1-2**


**6.3.9.1** **Mandatory** **node** **interview**


CL:0084.01.23.01.1 If the controlling node has the inclusion controller or secondary controller role in a network, it MAY

CL:0084.01.21.01.2 skip the node interview. In any case, it MUST NOT issue a Wake-Up Interval Set to a supporting
node.


CL:0084.01.21.02.1 If the controlling node has the SIS or primary controller role in a network, it MUST perform a
supporting node interview according to Figure 6.37.


Figure 6.37: Wake Up Command Class interview


CL:0084.01.21.03.1 A controlling node MUST set a supported Wake Up Interval time value when commissioning a version
2 supporting node.


CL:0084.01.21.04.1 A controlling node MUST set its own NodeID as the Wake-Up destination.


**6.3.9.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.3.9.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


CL:0084.01.42.01.1 A controlling node queuing commands for a Wake-Up node SHOULD indicate to the end user that
the commands will be transmitted when the destination wakes up again.


CL:0084.01.43.01.1 A controlling node MAY show to the end user the expected time until the next Wake-Up.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1152




<!-- PAGE 1154 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.3.9.4** **Additional** **control** **requirements**


CL:0084.01.52.01.1 A controlling node SHOULD verify that the Wake Up Interval Set Command executed successfully
by either using Supervision encapsulation or reading back the Wake Up Interval settings.


CL:0084.01.52.02.1 If the Wake Up Interval Set Command was ignored by a version 1 supporting node, the controlling
node SHOULD try again using the currently defined interval at the supporting node and its NodeID.


CL:0084.01.52.03.1 A controlling node SHOULD read the Wake Up Interval of a supporting node when the delays between
Wake Up periods are larger than what was last set at the supporting node.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1153




<!-- PAGE 1155 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024

## **6.4 Transport Encapsulation Command Class Control Defini-** **tions**


**6.4.1** **CRC-16** **Encapsulation** **Command** **Class** **Control** **Definitions,** **version** **1**


**6.4.1.1** **Mandatory** **node** **interview**


No node interview is required for this Command Class


**6.4.1.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.1.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.1.4** **Additional** **Control** **Requirements**


CL:0056.01.52.01.1 A controlling node SHOULD use CRC-16 encapsulation to communicate with a supporting node when
no security encapsulation is used and the communication speed is lower than 100 kbits/s.


CL:0056.01.51.01.1 A controlling node MUST support the CRC-16 Command Class and correctly handle received commands encapsulated with CRC-16.


CL:0056.01.51.02.1 A controlling node MUST use CRC-16 encapsulation to return a response to a command if the request
was received using CRC-16 encapsulation (aka “answer-as-asked”).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1154




<!-- PAGE 1156 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.2** **Multi** **Channel** **Command** **Class,** **version** **3-4**


**6.4.2.1** **Mandatory** **node** **interview**


CL:0060.01.21.01.3 A node controlling this Command Class MUST perform a supporting node interview as follows:


Figure 6.38: Multi Channel Command Class interview


CL:0060.01.23.01.1 A controlling node MAY skip the interview of aggregated End Points and MAY skip issuing a Multi
Channel Capability Get for any of the aggregated endpoints.


CL:0060.01.23.02.1 A controlling node MAY skip sending a _Multi_ _Channel_ _End_ _Point_ _Find_ _Report_ _Command_ if there are
no dynamic endpoints. ( _Dynamic_ field set to 0 in the _Multi_ _Channel_ _End_ _Point_ _Report_ _Command_ ).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1155




<!-- PAGE 1157 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.2.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.2.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.2.4** **Additional** **Control** **Requirements**


CL:0060.01.51.01.2 A node controlling this Command Class MUST provide control of all its controlled command classes
on every individual End Point.


**6.4.2.4.1** **Root** **Device** **and** **End** **Point** **Command** **Classes**


When End Point functionality is advertised in the Root Device NIF, service discovery mechanisms
like mDNS and installer-style GUIs risk presenting a Root Device functionality which is actually a
mirror representation of an End Point functionality.


Therefore, application command classes of the Root Device capabilities that are also advertised by at

CL:0060.01.52.01.1
least one End Point SHOULD be filtered out by controlling nodes before presenting the functionalities
via service discovery mechanisms like mDNS or to users in a GUI.


**6.4.2.4.2** **S0** **only** **Multi** **Channel** **nodes**


The following considerations apply for nodes supporting S0 and Multi Channel Command Class but
do not support S2 Command Class.


Legacy S0 only nodes may implement some secure and some non-secure End Points. Such a node
supporting S0 must advertise S0 in the Multi Channel Capability Report Command for a given End
point if the End Point can be addressed with S0 encapsulation.


CL:0060.01.52.02.1 A controlling node SHOULD use S0 encapsulation with all End Points if the Root Device was bootstrapped with the S0 Command Class.


CL:0060.01.53.01.1 A controlling node MAY interview and control Command Classes present in the Multi Channel Capability Report of an End Point non-securely if the End Point does not respond to S0 encapsulated
traffic.


**6.4.2.4.3** **Association** **and** **Multi** **Channel** **Association** **mapping**


The following considerations apply for nodes supporting Association and/or Multi Channel Association
and Multi Channel Command Class.


The Association groups functionality may be fully or partially mirrored between the Root Device and
End Points. For example, an Association Remove Command issued to the Root Device may clear the
association destination at the End Point groups.


CL:0060.01.52.03.1 A controlling node SHOULD read back the destinations in every group, including End Points groups
after configuring associations.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1156




<!-- PAGE 1158 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.3** **Security** **0** **Command** **Class**


**6.4.3.1** **Mandatory** **node** **interview**


CL:0098.01.21.01.1 A node controlling this Command Class MUST observe the _Role Type Specification_ requirements when
including an S0 node.


**6.4.3.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.3.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.3.4** **Additional** **Control** **Requirements**


A node is controlling S0 when it can perform S0 bootstrapping of other nodes. The S0 bootstrapping
CL:0098.01.51.01.1 process is described in _Security_ _0_ _(S0)_ _Command_ _Class,_ _version_ _1_ and a controlling node MUST
observe these requirements.


CL:0098.01.51.02.1 A node controlling this Command Class MUST provide control of all its controlled command classes
using S0 encapsulation.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1157




<!-- PAGE 1159 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**6.4.4** **Security** **2** **Command** **Class**


**6.4.4.1** **Mandatory** **node** **interview**


CL:009F.01.21.01.1 A node controlling this command class MUST observe the _Role_ _Type_ _Specification_ requirements when
including an S2 node.


**6.4.4.2** **Minimum** **end** **user** **functionalities**


No minimum end user functionality is required for this Command Class.


**6.4.4.3** **Node** **properties**


No node property is required to be made available to the end user for this Command Class.


**6.4.4.4** **Additional** **Control** **Requirements**


S2 Security is controlled when a node can perform S2 bootstrapping of other nodes. The Bootstrapping
CL:009F.01.51.01.1 process is described in _Security 2 (S2) Command Class, version 1_ and a controlling node MUST observe
these requirements.


CL:009F.01.51.02.1 A node controlling this Command Class MUST provide control of all its controlled command classes
using S2 encapsulation and at all its granted S2 Security Classes.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 1158




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