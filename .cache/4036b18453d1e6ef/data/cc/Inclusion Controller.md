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