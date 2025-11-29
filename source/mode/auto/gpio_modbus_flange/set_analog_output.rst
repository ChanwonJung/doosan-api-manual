.. _auto_set_analog_output:

set_analog_output (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_analog_output <set_analog_output>`  
during **Auto (Run)** operations to control the robot controller’s  
**analog output (AO)** channels.

Analog outputs are used to send variable voltage or current signals  
to external equipment, such as proportional pneumatic valves, analog controllers,  
motor drivers, or process control modules.

**Typical usage**

- Control the opening ratio of proportional valves.  
- Adjust speed or torque of analog-driven external actuators.  
- Send analog reference signals to PLCs or vision systems.  
- Implement smooth process controls requiring variable output levels.

.. Note::

  - ``nIndex`` specifies the AO channel (controller-specific).  
  - ``fValue`` is typically in **volts (0–10V)** or **milliamps (4–20mA)**  
    depending on controller configuration.  
  - Ensure AO mode is properly configured using ``set_mode_analog_output`` if necessary.

**Example: Driving a Proportional Valve with Analog Output**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Set AO[0] to 5.0V (e.g., half-open valve)
       if (!drfl.set_analog_output(0, 5.0f)) {
           printf("Failed to set AO[0].\n");
           return -1;
       }

       // Execute Auto Mode motion after output change
       float pose[6] = {300.f, 150.f, 250.f, 180.f, 0.f, 0.f};
       drfl.movej(pose, 60.f, 30.f);

       return 0;
   }

In this example, the analog output is set before executing  
an Auto Mode motion sequence that depends on process control.

**Tips**

- Use AO for proportional valves, analog drives, or smooth control tasks.  
- Validate AO scaling (0–10V or 4–20mA) before connecting hardware.  
- Avoid rapidly toggling AO values unless needed for control loops.  
- Use ``get_analog_input`` to read feedback signals when available.
