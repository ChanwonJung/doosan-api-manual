.. _set_mode_tool_analog_input:

set_mode_tool_analog_input
------------------------------------------
This function configures the **input mode** for the **analog input channel**  
on the **robot tool flange (end-effector side)**.  
Each channel can be independently configured for either **current mode (4–20 mA)**  
or **voltage mode (0–10 V)** depending on the connected external sensor.

This function is available **only on the new flange version (v2)**.  
For **M/H series** models, up to **4 channels** are supported.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 856)

.. code-block:: cpp

    bool set_mode_tool_analog_input(int nCh, GPIO_ANALOG_TYPE eAnalogType) 
    { return _set_mode_tool_analog_input(_rbtCtrl, nCh, eAnalogType); };

**Parameter**

.. list-table::
   :widths: 20 20 20 55
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nCh
     - int
     - -
     - **Analog input channel number** |br|
       1: Channel 1 |br|
       2: Channel 2 |br|
       3: Channel 3 (M/H models only) |br| 
       4: Channel 4 (M/H models only)
   * - eAnalogType
     - :ref:`GPIO_ANALOG_TYPE <enum_gpio_analog_type>`
     - -
     - Input signal mode type.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — Failed to set the input mode for the specified channel.
   * - 1
     - Success — Analog input mode successfully configured.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Configure tool analog input channel #1 as current mode (4–20 mA)
       drfl.set_mode_tool_analog_input(1, GPIO_ANALOG_TYPE_CURRENT);

       // Configure tool analog input channel #2 as voltage mode (0–10 V)
       drfl.set_mode_tool_analog_input(2, GPIO_ANALOG_TYPE_VOLTAGE);

       // Read analog values from both channels
       float current_val = drfl.get_tool_analog_input(1);
       float voltage_val = drfl.get_tool_analog_input(2);

       printf("Tool CH1 Current: %.2f mA\n", current_val);
       printf("Tool CH2 Voltage: %.2f V\n", voltage_val);
   }

This example demonstrates how to configure and read **analog input channels**
on the robot’s tool flange.  
These inputs can be used to connect **pressure sensors**, **load cells**,  
or other **analog transducers** providing voltage or current feedback signals.
