<!-- PAGE 368 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.76** **Prepayment** **Encapsulation** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


The Prepayment Encapsulation Command Class is used to smartcard preinstalled security mecha
nisms.


**2.2.76.1** **Prepayment** **encapsulation** **command**


This command is used to encapsulate Smart card related data communication (e.g. between a Card
reader and Meter), allowing the smartcard preinstalled security mechanisms to be applied transparently to Z-Wave.


Table 2.446: Prepayment Encapsulation Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|Command Class = COMMAND_CLASS_PREPAYMENT_ENCAPSULATION|
|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|Command = CMD_ENCAPSULATION|
|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|Data 1|
|…|…|…|…|…|…|…|…|
|Data N|Data N|Data N|Data N|Data N|Data N|Data N|Data N|



**Data** **(N** **bytes)**

This field contains prepayment smart card data.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 367