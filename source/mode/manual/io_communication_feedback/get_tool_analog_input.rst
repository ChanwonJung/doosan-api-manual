.. _manual_get_tool_analog_input:

get_tool_analog_input (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_tool_analog_input <get_tool_analog_input>` during **Manual (Teach)** operations  
to **read analog input signals** from the **tool (flange) port** connected to the robot’s end-effector.

**Typical usage**

- Measure analog voltage or current values from sensors mounted on the flange (e.g., force, distance, pressure).  
- Check sensor wiring and output levels during manual setup before automatic operation.  
- Verify tool feedback for calibration or diagnostic purposes.

.. Note::

    - The signal range depends on the tool configuration (commonly **0–10 V** or **4–20 mA**).  
    - Ensure that the corresponding **tool I/O configuration** is properly set in the controller.

**Example: Read analog values from flange input channels**

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
       // - Tool (flange) analog input device connected

       // 1) Read tool analog input CH1 and CH2
       float val_ch1 = drfl.get_tool_analog_input(1);
       float val_ch2 = drfl.get_tool_analog_input(2);

       std::printf("[Tool Analog CH1] = %.3f V\n", val_ch1);
       std::printf("[Tool Analog CH2] = %.3f V\n", val_ch2);

       return 0;
   }

**Tips**

- Confirm that the **tool I/O port mode** is configured for analog input in the teach pendant.  
- For noisy signals, apply software filtering or averaging over several reads.  
- If readings remain zero, check the **pin assignment** and ensure proper grounding.  