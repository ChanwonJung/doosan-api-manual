.. _manual_set_tool_digital_output:

set_tool_digital_output (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_tool_digital_output <set_tool_digital_output>` during **Manual (Teach)** operations.  
This function controls the **digital output pins located on the robot’s tool flange** (I/O interface).  
It is typically used to toggle external devices such as **grippers, vision triggers, or sensors** directly from the robot’s end-effector during teaching or testing.

**Typical usage**

- Manually open or close a **gripper** connected to the tool I/O port.  
- Send a **trigger pulse** to a camera, welding torch, or dispenser module during manual alignment.  
- Control peripheral actuators while verifying system wiring and timing.  
- Test end-effector responses during manual commissioning or calibration.

.. Note::

  - Tool I/O voltage level depends on hardware configuration (typically 24 V DC).  

**Example: Toggle gripper output pin from Teach Pendant**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   #include <chrono>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Gripper or end-effector connected to tool I/O

       cout << "[Tool I/O] Opening gripper...\n";
       drfl.set_tool_digital_output(GPIO_TOOL_DIGITAL_1, true);  // Gripper open signal
       this_thread::sleep_for(chrono::seconds(2));

       cout << "[Tool I/O] Closing gripper...\n";
       drfl.set_tool_digital_output(GPIO_TOOL_DIGITAL_1, false); // Gripper close signal
       this_thread::sleep_for(chrono::seconds(1));

       cout << "[Tool I/O] Gripper output test completed.\n";
       return 0;
   }

**Tips**

- Useful for **end-effector testing** and verifying signal polarity during commissioning.  
- Combine with :ref:`get_tool_digital_output <manual_get_tool_digital_output>` to confirm output state after command.  
- Use short pulse intervals for camera or sensor triggers (e.g., 100–200 ms).  
- Always verify wiring and I/O protection before energizing tool outputs in real hardware setups.
