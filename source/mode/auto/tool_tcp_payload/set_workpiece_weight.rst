.. _auto_set_workpiece_weight:

set_workpiece_weight (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_workpiece_weight <set_workpiece_weight>`  
during **Auto (Run)** operations to configure the active **workpiece weight**  
and optional **center of gravity (CoG)** information.  
Accurate payload configuration is essential for stable trajectory planning,  
force control performance, and safe execution of automated tasks.

This function is typically called before starting automated cycles such as  
pick & place, palletizing, or contact-based assembly operations.

**Typical usage**

- Register the mass of the part currently held by the gripper.  
- Update payload when switching products or workpiece types.  
- Adjust robot dynamics and force control behavior for varying weights.  
- Ensure correct torque estimation before executing high-speed Auto Mode motions.

.. Note::

    - ``fWeight`` is expressed in **kilograms (kg)**.  
    - ``fCog`` represents the CoG offset relative to the TCP or flange frame.  
    - If using Smart Setup, measured workpiece values can be applied directly here.  
    - Incorrect payload settings may lead to unstable force control or safety stops.

**Example: Setting Workpiece Payload Before Auto Cycle**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Example: 2.5 kg part with CoG offset in Z direction
       float cog[3] = {0.0f, 0.0f, 50.0f};  // 50 mm above TCP

       // Configure workpiece weight
       if (!drfl.set_workpiece_weight(2.5f, cog)) {
           printf("Failed to set workpiece weight.\n");
           return -1;
       }

       // Perform Auto Mode motion with updated payload
       float target[6] = {400.f, 150.f, 280.f, 180.f, 0.f, 0.f};
       drfl.movej(target, 60.f, 30.f);

       return 0;
   }

In this example, the workpiece weight and CoG are configured  
prior to running automated movements.  
This ensures that the robot uses correct payload parameters  
for stable and safe Auto Mode execution.

**Tips**

- Call this function whenever a new part is picked up.  
- Use precise values (Smart Setup recommended) for best force/compliance performance.  
- Revert to empty-gripper payload with ``reset_workpiece_weight`` after dropping the part.  
- Avoid rapidly switching payload values while the robot is moving.
