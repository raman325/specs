<!-- PAGE 111 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.15** **Basic** **Tariff** **Information** **Command** **Class,** **version** **1** **[NEVER** **CERTIFIED]**


**Warning:** **THIS** **COMMAND** **CLASS** **HAS** **NEVER** **BEEN** **CERTIFIED**

This command class has never been implemented and certified by a Z-Wave product Therefore,
this Command Class definition MAY be updated in a non-backwards compatible manner, or even
removed.


Consult with the Z-Wave Alliance Application Work Group if you consider implementing this
Command Class.


This Basic Tariff Information Command Class for use with a single element or dual element meter,
and for use with import (electricity received from grid) rates only. The command class is kept as
simple as possible without any pricing information.


This command class supports a GET and REPORT. No Set command is supported, as it is not
appropriate to set any of the parameters through Z-Wave.


**2.2.15.1** **Basic** **Tariff** **Information** **Get** **Command**


This command is used to request current tariff information from the meter.

The Basic Tariff Information Report Command MUST be returned in response to this command.


This command MUST NOT be issued via multicast addressing.


A receiving node MUST NOT return a response if this command is received via multicast addressing. The Z-Wave Multicast frame, the broadcast NodeID and the Multi Channel multi-End Point
destination are all considered multicast addressing methods.


Table 2.85: Basic Tariff Information Get Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|
|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|Command = BASIC_TARIFF_INFO_GET|



**2.2.15.2** **Basic** **Tariff** **Information** **Report** **Command**


This command returns information on the number of import rates supported, and current import
rate information. Application can send unsolicited Basic Tariff Report commands or requested by the
Basic Tariff Get Information command.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 110




<!-- PAGE 112 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


Table 2.86: Basic Tariff Information Report Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|Command Class = COMMAND_CLASS_BASIC_TARIFF_INFO|
|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|Command = BASIC_TARIFF_INFO_REPORT|
|Dual|Reserved|Reserved|Reserved|Total No. Import Rates|Total No. Import Rates|Total No. Import Rates|Total No. Import Rates|
|Reserved|Reserved|Reserved|Reserved|E1 - Current Rate in Use|E1 - Current Rate in Use|E1 - Current Rate in Use|E1 - Current Rate in Use|
|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|E1 - Rate Consumption Register - MSB|
|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|
|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|E1 - Rate Consumption Register|
|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|E1 - Rate Consumption Register - LSB|
|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|E1 - Time for Next Rate - Hours|
|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|E1 - Time for Next Rate - Minutes|
|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|E1 - Time for Next Rate - Seconds|
|Reserved|Reserved|Reserved|Reserved|E2 - Current Rate in Use|E2 - Current Rate in Use|E2 - Current Rate in Use|E2 - Current Rate in Use|
|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|E2 - Rate Consumption Register - MSB|
|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|
|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|E2 - Rate Consumption Register|
|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|E2 - Rate Consumption Register - LSB|



**Dual** **(1** **bit)**


Single Element = 0, Two Elements = 1.

If single element the E2 fields are skipped in the frame. E1 – Time for Next Rate – Seconds will be
the last byte of the message and the number of data bytes will be 9.

If two elements the E2 fields are present and the number of data bytes will be 14.


**Total** **Number** **of** **Import** **Rates** **Supported** **(7** **bits)**

Field specifies the number of import rates E1 (and E2) supported by the meter. Range of legal decimal
values are 1…8. No units used. The decimal values 0 and 9…15 are reserved and MUST be ignored by
receiving devices.


**Reserved**

This field MUST be set to 0 by a sending node and MUST be ignored by a receiving node.


**E1** **-** **Current** **Rate** **in** **Use** **(8** **bits)**

Field specifies the current rate in use. Range of legal decimal values are 1…8. No units used. The
decimal values 0 and 9…15 are reserved and MUST be ignored by receiving devices.


**E1** **-** **Rate** **Consumption** **Register** **(32** **bits)**


The meter has a 32-bit consumption register, for the energy used in each rate. This register is the
rate consumption register for the current rate in use now on element 1. Units are in Wh.


**E1** **-** **Time** **for** **Next** **Rate** **-** **Hours** **(8** **bits)**

Field specifies the hour value of the time that the rate is due to change on element 1. Range of legal
decimal values are 0…23, or 255. The values 24…254 are reserved and MUST be ignored by receiving
devices.


**E1** **-** **Time** **for** **Next** **Rate** **-** **Minutes** **(8** **bits)**

Field specifies the minute value of the time that the rate is due to change on element 1. Range of
legal decimal values are 0…59, or 255. The decimal values 60…254 are reserved and MUST be ignored
by receiving devices.


**E1** **-** **Time** **for** **Next** **Rate** **-** **Seconds** **(8** **bits)**

Field specifies the second value of the time that the rate is due to change on element 1. Range of legal
decimal values are 0…59, or 255. The decimal values 60…254 are reserved and MUST be ignored by
receiving devices.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 111




<!-- PAGE 113 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


NOTE: 255 in each field of the Time to Next Rate specifies no switching time is in use, which is
appropriate for single rate meters. 255 is only a legal value if used in all three Time to Next Rate
fields.


**E2** **-** **Current** **Rate** **in** **Use** **(8** **bits)**

Field specifies the current rate in use on element 2. Range of legal decimal values are 1…8. No units
used. The decimal values 0 and 9…15 are reserved and MUST be ignored by receiving devices.


**E2** **-** **Rate** **Consumption** **Register** **(32** **bits)**


The meter has a 32-bit consumption register, for the energy used in each rate. This register is the
rate consumption register for the current rate in use now on element 2. Units are in Wh.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 112