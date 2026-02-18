<!-- PAGE 365 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.75** **Prepayment** **Command** **Class,** **version** **1**


The Prepayment Command Class defines the Commands necessary to implement a Z-Wave encapsulation of Prepayment data and to distribute prepayment information between devices


**2.2.75.1** **Prepayment** **Balance** **Get** **Command**


This command is used to request the balance of the Prepayment.


The Prepayment Balance Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.440: Prepayment Balance Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|
|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|Command = PREPAYMENT_BALANCE_GET|
|Balance Type|Balance Type|Reserved|Reserved|Reserved|Reserved|Reserved|Reserved|



**Balance** **Type** **(2** **bits)**

The field specifies which balance type is requested in the response report. The available balance types
may be requested using the Prepayment Supported Get Command.


Table 2.441: Prepayment Balance Get::Balance Type encoding

|Value|Balance Type|
|---|---|
|0x00|Utility Balance|
|0x01|Monetary Balance|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.75.2** **Prepayment** **Balance** **Report** **Command**


This command is used to report the current balances.


The report includes the following main elements:


 - Balance


 - Debt


 - Emergency Credit


The elements MAY be given in monetary values or in utility units depending on the Balance Type
field.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 364




<!-- PAGE 366 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.442: Prepayment Balance Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|
|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|Command = PREPAYMENT_BALANCE_REPORT|
|Balance Type|Balance Type|Meter type|Meter type|Meter type|Meter type|Meter type|Meter type|
|Balance Precision|Balance Precision|Balance Precision|Scale|Scale|Scale|Scale|Scale|
|Balance Value 1|Balance Value 1|Balance Value 1|Balance Value 1|Balance Value 1|Balance Value 1|Balance Value 1|Balance Value 1|
|Balance Value 2|Balance Value 2|Balance Value 2|Balance Value 2|Balance Value 2|Balance Value 2|Balance Value 2|Balance Value 2|
|Balance Value 3|Balance Value 3|Balance Value 3|Balance Value 3|Balance Value 3|Balance Value 3|Balance Value 3|Balance Value 3|
|Balance Value 4|Balance Value 4|Balance Value 4|Balance Value 4|Balance Value 4|Balance Value 4|Balance Value 4|Balance Value 4|
|Debt Precision|Debt Precision|Debt Precision|Reserved|Reserved|Reserved|Reserved|Reserved|
|Debt 1|Debt 1|Debt 1|Debt 1|Debt 1|Debt 1|Debt 1|Debt 1|
|Debt 2|Debt 2|Debt 2|Debt 2|Debt 2|Debt 2|Debt 2|Debt 2|
|Debt 3|Debt 3|Debt 3|Debt 3|Debt 3|Debt 3|Debt 3|Debt 3|
|Debt 4|Debt 4|Debt 4|Debt 4|Debt 4|Debt 4|Debt 4|Debt 4|
|Emer. Credit Precision|Emer. Credit Precision|Emer. Credit Precision|Reserved|Reserved|Reserved|Reserved|Reserved|
|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|Emer. Credit 1|
|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|Emer. Credit 2|
|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|Emer. Credit 3|
|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|Emer. Credit 4|
|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|Currency 1|
|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|Currency 2|
|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|Currency 3|
|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|Debt Recovery Percentage|



**Balance** **Type** **(2** **bits)**

The field specifies which type of balance is given in the report.


All available Balance Types may be found in the section Section 2.2.75.1 Prepayment Balance Get
Command.


**Meter** **Type** **(6** **bits)**

Meter Type specifies the type of metering device the command originates. This field MUST be encoded
according to the Meter Types defined in [26].


**Scale** **(5** **bits)**


The Scale used to indicate the scale (unit) of the balance, debt and emergency credit value in the
report. Scale field only used for a report of type “Utility Balance”, for other reports set the scale to
0x1F. The Scale parameter is of the variable type _Meter_ _Scale_ ; refer to Section 2.2.62.13 Meter Table
Current Data Report Command.


**Currency** **(3** **bytes)**

This field advertises the currency code. Reports of the type “Monetary Balance” MUST advertise
currency codes complying with ISO 4217. Other report types MUST advertise a currency code of
“XXX”.


Table 2.443: Prepayment Balance Report::Currency examples

|Currency Code|Currency 1|Currency 2|Currency 3|
|---|---|---|---|
|Pound sterling (ISO 4217)|G|B|P|
|US Dollar (ISO 4217)|U|S|D|
|No Currency|X|X|X|



**Balance,** **Debt** **and** **Emergency** **Credit** **Precision** **(3** **bits)**

The precision field describes what the precision of the value is. The number indicates the number of
decimals. The decimal value 1025 with precision 2 is therefore equal to 10.25.


**Balance,** **Debt** **and** **Emergency** **Credit** **(32** **bits)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 365




<!-- PAGE 367 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


The Balance, Debt and Emergency Credit fields MUST be encoded as 32-bit signed integers. The
first byte MUST carry most significant byte. Table 2.12 Signed field encoding (two’s complement
representation) shows signed decimal values together with their hexadecimal equivalents.


**Debt** **Recovery** **Percentage** **(8** **bits)**


The Debt Recovery Percentage indicates the percentage of the payment that is for debt recovery. This
can take the value from 0 – 50%, the value is always given with a precision of 0 decimal places. The
value 0xFF indicates that this field is unspecified.

This field is only used for only used for a report of type “Monetary Balance”. For other reports this
field MUST be set to 0xFF (unspecified).


**2.2.75.3** **Prepayment** **Supported** **Get** **Command**


The Prepayment Supported Get Command is used to request type of Balance Reports that are available in the device.


The Prepayment Supported Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.444: Prepayment Supported Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|
|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|Command = PREPAYMENT_SUPPORTED_GET|



**2.2.75.4** **Prepayment** **Supported** **Report** **Command**


The Prepayment Supported Report Command reports the types of Balance Reports that are available
in the device.


Table 2.445: Prepayment Supported Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|Command Class = COMMAND_CLASS_PREPAYMENT|
|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|Command = PREPAYMENT_SUPPORTED_REPORT|
|Reserved|Reserved|Reserved|Reserved|Bit Mask<br>Balance Types Supported|Bit Mask<br>Balance Types Supported|Bit Mask<br>Balance Types Supported|Bit Mask<br>Balance Types Supported|



**Bit** **Mask** **-** **Balance** **Types** **Supported** **(8** **bits)**


The Bit Mask - Balance Types Supported byte describes the type of Balance Reports that are available
in the device.


Bit 0 in Bit Mask is used to indicate if the Balance Report Type “Utility Balance” is supported, 0
indicating not supported and 1 indicating supported. Bit 1 in the Bit Mask is used to indicate if the
Balance Report Type “Monetary Balance” is available in the device, 0 indicating not supported and
1 indicating supported.


All available Balance Types may be found in the section Section 2.2.75.1 Prepayment Balance Get
Command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 366