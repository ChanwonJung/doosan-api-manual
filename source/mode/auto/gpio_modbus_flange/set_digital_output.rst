.. _auto_set_digital_output:

set_digital_output (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_digital_output <set_digital_output>`  
during **Auto (Run)** operations to control the robot controller’s  
**digital output (DO)** signals.  
Digital outputs are commonly used to drive external devices such as  
grippers, solenoid valves, pneumatic actuators, sensors, and machine interfaces.

This function sets a specific DO channel to either **ON (1)** or **OFF (0)**.

**Typical usage**

- Open/close an electric or pneumatic gripper.  
- Send signals to PLC, conveyors, or external automation equipment.  
- Trigger actuators, clamps, or inspection devices.  
- Implement sequence-based machine interactions in Auto Mode.

.. Note::

    - Output changes should be coordinated with motion steps to ensure safe operation.  
    - If using tool I/O, refer instead to ``set_tool_digital_output``.

**Example: Activating a Gripper During Auto Mode**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Turn ON digital output channel 1 (e.g., close gripper)
       if (!drfl.set_digital_output(1, TRUE)) {
           printf("Failed to set DO[1].\n");
           return -1;
       }

       // Perform picking motion after activating the output
       float pick[6] = {300.f, 150.f, 200.f, 180.f, 0.f, 0.f};
       drfl.movej(pick, 70.f, 40.f);

       return 0;
   }

In this example, a DO signal is activated  
and the robot executes an Auto Mode pick motion after the output change.

**Tips**

- Use DO for gripper control, machine interface, and external triggers.  
- Ensure wiring and I/O mapping match controller assignments.  
- For tool-mounted I/O, use ``set_tool_digital_output`` instead of base I/O.  
- Use ``get_digital_output`` for debugging or monitoring states.
