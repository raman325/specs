<!-- PAGE 299 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.61** **Meter** **Table** **Configuration** **Command** **Class,** **version** **1**


The Meter Table Configuration Command Class defines the Commands necessary to configure the
fundamental properties of the meter.

The Meter Table configuration commands are separated from the Meter Table monitoring commands
in the Meter Table Monitor Command Class, allowing the classes to be optionally supported at
different Z-Wave security levels. (E.g. Meter table monitoring commands could be supported in any
device, while enabling a strict and certificate based security solution for the Meter Table Configuration
Command class). Refer to Section 4 for more details about Z-Wave security.


**2.2.61.1** **Meter** **Table** **Point** **Adm** **Number** **Set** **Command**


This command is used to set the Meter Point Administration Number in the metering device. The
Meter Point Administration Number is used to identify the customer.


Table 2.361: Meter Table Point Adm Number Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|Command Class = COMMAND_CLASS_METER_TBL_CONFIG|
|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|Command = METER_TBL_TABLE_POINT_ADM_NO_SET|
|Reserved|Reserved|Reserved|Number of Meter Point Adm Number Characters|Number of Meter Point Adm Number Characters|Number of Meter Point Adm Number Characters|Number of Meter Point Adm Number Characters|Number of Meter Point Adm Number Characters|
|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|Meter Point Adm Number Character 1|
|…|…|…|…|…|…|…|…|
|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|Meter Point Adm Number Character N|



**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**Number** **of** **Meter** **Point** **Adm** **Number** **Characters** **(5** **bits)**


Number of characters in the meter point administration number(1…32).


**Meter** **Point** **Adm** **Number** **Character** **(N** **bytes)**

The Meter Point Adm Number character fields hold the string identifying the customer. The character
presentation uses standard ASCII codes (values 128-255 are ignored).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 298