<!-- PAGE 62 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.4** **Alarm** **Silence** **Command** **Class,** **version** **1**


The Alarm Silence Command Class may be used to temporarily disable the sounding of the alarm
but still keep the alarm operating.


**2.2.4.1** **Alarm** **Silence** **Set** **Command**


This command is used to remotely silence the sensor alarm.


Table 2.26: Alarm Silence Set Command

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|Command Class = COMMAND_CLASS_SILENCE_ALARM|
|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|Command = SENSOR_ALARM_SET|
|Mode|Mode|Mode|Mode|Mode|Mode|Mode|Mode|
|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|Seconds 1 (MSB)|
|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|Seconds 2 (LSB)|
|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|Number of Bit Masks|
|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|Bit Mask 1|
|…|…|…|…|…|…|…|…|
|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|Bit Mask N|



**Mode** **(8** **bits)**

Mode specifies the different options to silence sensor alarms. Modes are defined by the Z-Wave
Alliance.

|Value|Table 2.27: Alarm Silence Set Command Modes Mode|
|---|---|
|Value|Mode|
|0x00|Disable sounding of all sensor alarms independent of bit mask|
|0x01|Disable sounding of all sensor alarms independent of bit mask which have<br>received the alarm via the Sensor Alarm Report command|
|0x02|Disable sounding of all sensor alarms according to bit mask|
|0x03|Disable sounding of all sensor alarms according to bit mask which have<br>received the alarm via the Alarm Sensor Report Command|



**Seconds** **(16** **bits)**

The field Seconds indicates the duration sounding of the alarm must be disable but still keep the alarm
operating. If silence is engaged, the alarm will come back on when the duration expires unless the
originating sensor clears the alarm. The value 0x0000 indicates that the time field MUST be ignored.


**Number** **of** **Bit** **Masks** **(8** **bits)**

Indicates the Number of Bit Masks fields used in bytes.


**Bit** **Mask** **(N** **Bytes)**

The Bit Mask fields describe the sensor types to disable sounding from.


 - Bit 0 in Bit Mask 1 indicates if Sensor Type = 0 (General Alarm) is disabled.


 - Bit 1 in Bit Mask 1 indicates if Sensor Type = 1 (Smoke Alarm) is disabled.


 - …


If the sensor type is disabled the bit MUST be set to 1. If the sensor type is not disabled the bit
MUST be set to 0. It is only necessary to send the Bit Mask fields from 1 and up to the one indicating
the last sensor type to be disabled.


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 61