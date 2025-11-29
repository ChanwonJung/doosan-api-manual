.. _manual_set_mode_tool_analog_input:

set_mode_tool_analog_input (Manual Mode)
--------------------------------------------------------
This section explains how to use :ref:`set_mode_tool_analog_input <set_mode_tool_analog_input>` during **Manual (Teach)** operations  
to **configure the analog input mode** (Voltage or Current) of the **tool (flange) analog input channels**.

**Typical usage**

- Select the correct analog input mode for **sensors connected to the flange**, such as force, pressure, or distance sensors.  
- Match the robot’s tool analog configuration with the sensor’s output type.  
- Verify the correct mode setting before reading values using :ref:`get_tool_analog_input <manual_get_tool_analog_input>`.

.. Note::

    - This function applies only to **flange (tool) analog input ports**.

**Example: Configure tool analog input channels**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool (flange) analog sensor connected

       // 1) Set tool analog input CH1 to current mode (4–20 mA)
       drfl.set_mode_tool_analog_input(1, GPIO_ANALOG_TYPE_CURRENT);
       std::printf("[Tool Analog IN CH1] Mode set to CURRENT\n");

       // 2) Set tool analog input CH2 to voltage mode (0–10 V)
       drfl.set_mode_tool_analog_input(2, GPIO_ANALOG_TYPE_VOLTAGE);
       std::printf("[Tool Analog IN CH2] Mode set to VOLTAGE\n");

       return 0;
   }

**Tips**

- Ensure the connected sensor’s output signal type matches the selected mode.  
- In **current mode**, verify the external loop power supply and wiring polarity.  
- If readings are unstable, check grounding and cable shielding at the tool connector.  
- Always recheck analog input mode after power cycling or controller reset.
