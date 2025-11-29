.. _auto_change_operation_speed:

change_operation_speed (Auto Mode)
------------------------------------------
This section explains how to use :ref:`change_operation_speed <change_operation_speed>`  
during **Auto (Run)** operations to dynamically adjust the robot’s  
**overall operating velocity**.

The function scales the robot’s speed by a **percentage (1–100%)** of the  
currently configured motion speed, allowing external systems to slow down  
or speed up the robot without modifying the DRL program itself.

**Typical usage**

- Reduce operation speed during precision alignment or vision calibration.  
- Slow down motions when an operator enters the collaborative workspace.  
- Adjust speed on-the-fly based on real-time sensor feedback or product conditions.  
- Implement variable-speed manufacturing cycles (e.g., quality check mode vs. fast mode).  

.. Note::

   - Common operating range: **10–100%**  
   - Speeds below 10% may be clamped depending on safety mode.  
   - The change applies immediately and affects all subsequent motions.  

**Example: Slowing Robot Movement Before Starting a DRL Routine**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Slow down to 20% of the current speed
       if (!drfl.change_operation_speed(20)) {
           printf("Failed to change operation speed.\n");
           return -1;
       }

       printf("Operation speed set to 20%%.\n");

       // 2) Prepare a simple DRL program
       std::string drlProgram =
           "i = 0\\r\\n"
           "while i < 2:\\r\\n"
           "    movej(posj(15,15,15,15,15,15), vel=60, acc=60)\\r\\n"
           "    movej(posj(0,0,0,0,0,0), vel=60, acc=60)\\r\\n"
           "    i = i + 1\\r\\n"
           "end\\r\\n";

       // 3) Ensure robot is in Auto Mode
       if (drfl.get_robot_mode() == ROBOT_MODE_AUTONOMOUS &&
           drfl.get_robot_state() == eSTATE_STANDBY) {

           // Start the DRL task at the reduced speed
           drfl.drl_start(ROBOT_SYSTEM_REAL, drlProgram);
       } else {
           printf("Robot is not in Auto/Standby state.\n");
       }

       return 0;
   }

In this example, the robot’s operating speed is reduced to **20%**  
before starting a DRL routine. The adjusted speed affects all subsequent  
motion commands issued in **Auto Mode**.

**Tips**

- Use reduced speed during delicate pick-and-place, inspection, or calibration tasks.  
- Combine with :ref:`drl_start <auto_drl_start>` for dynamic speed-controlled automation.  
- Increasing speed (e.g., 80–100%) is useful for throughput-focused cycles.  
- Log speed changes to support traceability in production environments.  
