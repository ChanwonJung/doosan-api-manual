.. _get_tool_analog_input:

get_tool_analog_input
------------------------------------------
This function retrieves the **analog input signal value** from the **tool flange**  
of the robot. The signal can be either **current (4–20 mA)** or **voltage (0–10 V)**,  
depending on the configured mode for the selected channel.

This function is available only on the **new flange version (v2)**.  
For M/H series models, additional channels (3 and 4) are supported.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 853)

.. code-block:: cpp

    float get_tool_analog_input(int nCh) 
    { return _get_tool_analog_input(_rbtCtrl, nCh); };

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
       1: Channel, 2: Channel 2 |br| 
       3: Channel 3 (M/H models only) |br|
       4: Channel 4 (M/H models only)

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - float
     - The measured analog signal value from the tool flange. |br|
       Depending on mode: |br|
       - **Current mode**: 4.0 ~ 20.0 [mA] |br|
       - **Voltage mode**: 0.0 ~ 10.0 [V]

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set tool analog input channel 1 to current mode
       drfl.set_mode_tool_analog_input(1, GPIO_ANALOG_TYPE_CURRENT);

       // Set tool analog input channel 2 to voltage mode
       drfl.set_mode_tool_analog_input(2, GPIO_ANALOG_TYPE_VOLTAGE);

       // Read analog values from both channels
       float current = drfl.get_tool_analog_input(1);
       float voltage = drfl.get_tool_analog_input(2);

       printf("Tool Analog CH1 (Current): %.2f mA\n", current);
       printf("Tool Analog CH2 (Voltage): %.2f V\n", voltage);
   }

This example demonstrates how to configure and read **analog input values**  
from the robot tool flange. These inputs are typically connected to **sensors**,  
such as **force sensors, potentiometers, or pressure sensors** that provide analog signals.
