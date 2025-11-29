.. _manual_get_tool_digital_input:

get_tool_digital_input (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_tool_digital_input <get_tool_digital_input>` during **Manual (Teach)** operations  
to **read the ON/OFF state** of digital input signals from the **tool (flange) connector**  
connected to the robot’s end-effector.

**Typical usage**

- Monitor digital feedback from a **gripper**, **vacuum sensor**, or **tool presence switch**.  
- Verify tool input wiring and polarity before automatic control.  
- Check external sensor states in real time while teaching.

.. Note::

    - Read-only function — use :ref:`set_tool_digital_output <set_tool_digital_output>` to control output lines.

**Example: Read digital inputs from tool port**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Tool I/O properly connected and powered

       // 1) Read tool digital inputs
       bool tdi1 = drfl.get_tool_digital_input(TOOL_DI_1);
       bool tdi2 = drfl.get_tool_digital_input(TOOL_DI_2);

       std::printf("[TOOL_DI_1] = %s\n", tdi1 ? "ON" : "OFF");
       std::printf("[TOOL_DI_2] = %s\n", tdi2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Ensure the tool is powered and the digital lines are configured as **input**.  
- Check signal polarity (NPN/PNP) and reference voltage (24V/GND).  
- For dynamic monitoring, poll the function periodically at ~100 ms intervals.  
- Use this to validate sensor status during **manual gripper testing** or setup.
