.. _auto_reset_workpiece_weight:

reset_workpiece_weight (Auto Mode)
------------------------------------------
This section explains how to use :ref:`reset_workpiece_weight <reset_workpiece_weight>`  
during **Auto (Run)** operations to clear the currently configured **workpiece weight**.  
After this call, the robot considers only the tool payload, effectively returning  
the system to an **empty-gripper** state.

This function is typically used after the robot releases a part,  
or when switching from loaded to unloaded cycles.

**Typical usage**

- Clear payload after placing or unloading a workpiece.  
- Transition between loaded/unloaded sequences in palletizing.  
- Improve torque estimation accuracy when gripping state changes.  
- Ensure Auto Mode behaves correctly when no part is held.

.. Note::

    - Use this function only when the robot is confirmed to be empty-handed.  
    - Ensures stable motion planning when switching between different work cycles.

**Example: Resetting Workpiece Payload After Unloading**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // After placing the part on a conveyor or pallet
       if (!drfl.reset_workpiece_weight()) {
           printf("Failed to reset workpiece weight.\n");
           return -1;
       }

       // Continue Auto Mode operations with empty payload
       float home[6] = {0.f, 0.f, 0.f, 0.f, 0.f, 0.f};
       drfl.movej(home, 50.f, 30.f);

       return 0;
   }

In this example, the robot clears its workpiece configuration  
after unloading the part.  
This ensures that subsequent Auto Mode movements use the correct  
(empty-gripper) payload parameters.

**Tips**

- Call immediately after releasing a part to maintain correct payload data.  
- Combine with ``set_workpiece_weight`` when alternating between pick and place cycles.  
- Incorrect payload reset may cause inconsistent force control performance.  
- Recommended for palletizing, machine tending, and repetitive loading tasks.
