<!-- PAGE 494 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


**2.2.110** **Thermostat** **Mode** **Command** **Class,** **version** **3**


The Thermostat Mode Command Class is used to control which mode a thermostat operates.


**2.2.110.1** **Compatibility** **Considerations**


The Thermostat Mode Command Class, version 3 is backwards compatible with the Thermostat Mode
Command Class, version 1-2.

All commands and fields not mentioned in this version MUST remain unchanged from the Thermostat
Mode Command Class, version 1-2.


This version introduces:


 - A new FULL POWER thermostat mode


 - MANUFACTURER SPECIFIC mode


**2.2.110.2** **Interoperability** **Considerations**


The MANUFACTURER SPECIFIC (proprietary) mode MUST NOT be supported by a node if the
functionality can be provided using a thermostat mode defined in this command class.

A node supporting the MANUFACTURER SPECIFIC mode MUST fulfill the following conditions:


 - The node MUST support as a minimum two other thermostat modes (e.g. HEAT and COOL).


 - If the MANUFACTURER SPECIFIC mode functionality can in part be supported by one or
more defined thermostat mode in this command class, the node MUST also support these
thermostat modes.

 - The MANUFACTURER SPECIFIC mode and all of its associated Manufacturer Data fields
MUST be described in the product manual.


**2.2.110.3** **Thermostat** **Mode** **Set** **Command**


This command is used to set the thermostat mode at the receiving node.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|Command = THERMOSTAT_MODE_SET (0x01)<br>|
|Number of Manufacturer Data felds|Number of Manufacturer Data felds|Number of Manufacturer Data felds|Mode|Mode|Mode|Mode|Mode|
|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|
|…|…|…|…|…|…|…|…|
|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|



**Number** **of** **Manufacturer** **Data** **fields** **(3** **bits)**

This field is used to advertise the length in bytes of the Manufacturer Data field in the command.
This field MUST be in the range 0..7.

This field MUST be set to 0 if the Mode field is not set to 0x1F (MANUFACTURER SPECIFIC).

This field MUST indicate the length in bytes of the Manufacturer Data field if the Mode field is set
to 0x1F (MANUFACTURER SPECIFIC).


**Mode** **(5** **bits)**

This field is used to set the thermostat mode at the receiving node.

This field MUST be encoded according to Table 2.523.


**Manufacturer** **Data** **(N** **bytes)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 493




<!-- PAGE 495 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to provide a configuration for the MANUFACTURER SPECIFIC mode. Refer to
Interoperability considerations (Section 2.2.110.2).



Table 2.523: Thermostat Mode Set version 3::Mode encoding











|Mode (5 bits)|Col2|Description|Requires<br>own<br>Setpoint|CC<br>Version|
|---|---|---|---|---|
|0x00|OFF|This mode is used to switch of the ther-<br>mostat.|No|1|
|0x01|HEAT|This mode is used to use activate heating<br>when the temperature is below the Heating<br>(0x01) setpoint.|Yes|1|
|0x02|COOL|This mode is used to use activate cooling<br>when the temperature is above the Cooling<br>(0x02) setpoint.|Yes|1|
|0x03|AUTO|This mode is used to regulate the temper-<br>ature using heating and cooling when the<br>temperature is outside the range defned by<br>the Heating (0x01) and Cooling (0x02) set-<br>points.|No|1|
|0x04|AUXILIARY|This mode is used to activate heating<br>when the temperature is below the Heat-<br>ing (0x01) setpoint, but using an auxiliary<br>or emergency heat source.<br>For example, a heat pump is not more ef-<br>cient when the outside temperature is too<br>low. The auxiliary heat mode may be acti-<br>vated to use a more efcient secondary heat<br>source.|No|1|
|0x05|RESUME (ON)|This mode is used to resume the last acti-<br>vate mode (diferent than OFF 0x00).|No|1|
|0x06|FAN|This mode is used to activate fans only and<br>circulate air.|No|1|
|0x07|FURNACE|This mode is used to activate fans to circu-<br>late air and heating or cooling will be ac-<br>tivated to regulate the temperature at the<br>Furnace (0x07) setpoint.|Yes|1|
|0x08|DRY|This mode is used to dehumidify and re-<br>move moisture.<br>Heating or cooling will be activated to<br>regulate the temperature at the Dry Air<br>(0x08) setpoint.|Yes|1|
|0x09|MOIST|This mode is used to humidify and add<br>moisture.<br>Heating or cooling will be activated to reg-<br>ulate the temperature at the Moist Air<br>(0x09) setpoint.|Yes|1|
|0x0A|AUTO<br>CHANGEOVER|This mode is used to regulate the temper-<br>ature at the Auto Changeover (0x0A) set-<br>point using heating and cooling.|Yes|1|
|0x0B|ENERGY HEAT|This mode is used to activate heating when<br>the temperature is below the Energy Save<br>Heating (0x0B) setpoint.<br>The Energy Save Heating (0x0B) setpoint<br>is usually lower than the Heating (0x01)<br>setpoint in order to save energy.|Yes|2|


continues on next page





© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 494




<!-- PAGE 496 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024



Table 2.523 – continued from previous page


















|Mode (5 bits)|Col2|Description|Requires<br>own<br>Setpoint|CC<br>Version|
|---|---|---|---|---|
|0x0C|ENERGY COOL|This mode is used to activate cooling when<br>the temperature is below the Energy Save<br>Cooling (0x0C) setpoint.<br>The Energy Save Cooling (0x0C) setpoint<br>is usually higher than the Cooling (0x02)<br>setpoint in order to save energy.|Yes|2|
|0x0D|AWAY|This mode is used to regulate the temper-<br>ature using heating and cooling when the<br>temperature is outside the range defned by<br>the Away Heating (0x0D) and Away Cool-<br>ing (0x0E) setpoints.|Yes|2|
|0x0E|Reserved||-|3|
|0x0F|FULL POWER|This mode is used to regulate the tempera-<br>ture at the Full Power (0x0F) setpoint us-<br>ing heating and cooling.<br>This mode is intended to use more energy<br>and speed up the temperature regulation<br>to the desired setpoint.<br>|Yes|3|
|0x1F|MANUFAC-<br>TURER<br>SPE-<br>CIFIC|Reserved for vendor specifc thermostat<br>mode.|No|3|



All other values are reserved and MUST NOT be used by a sending node. Reserved values MUST be
ignored by a receiving node.


**2.2.110.4** **Thermostat** **Mode** **Report** **Command**


This command is used to report the current mode of the device.

|7|6|5|4|3|2|1|0|
|---|---|---|---|---|---|---|---|
|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|Command Class = COMMAND_CLASS_THERMOSTAT_MODE (0x40)|
|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|Command = THERMOSTAT_MODE_REPORT (0x03)<br>|
|Number of Manufacturer Data felds|Number of Manufacturer Data felds|Number of Manufacturer Data felds|Mode|Mode|Mode|Mode|Mode|
|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|Manufacturer Data 1|
|…|…|…|…|…|…|…|…|
|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|Manufacturer Data N|



**No** **of** **Manufacturer** **Data** **fields** **(3** **bits)**

This field is used to advertise the length in bytes of the Manufacturer Data field in the command.
This field MUST be in the range 0..7.

This field MUST be set to 0 if the Mode field is not set to 0x1F (MANUFACTURER SPECIFIC).

This field MUST indicate the length in bytes of the Manufacturer Data field if the Mode field is set
to 0x1F (MANUFACTURER SPECIFIC).


**Mode** **(5** **bits)**

This field is used to advertise the current thermostat mode at the receiving node.

This field MUST be encoded according to Table 2.523.

This field MUST NOT be set to 0x05 (RESUME(ON)) in this command.


**Manufacturer** **Data** **(N** **bytes)**


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 495




<!-- PAGE 497 -->

Specifications **Application** **Work** **Group** **Z-Wave** **Specifications,** **Release** **2024A** April 2, 2024


This field is used to advertise the current configuration for the MANUFACTURER SPECIFIC mode.
Refer to Interoperability considerations (Section 2.2.110.2).


© 2024 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 496