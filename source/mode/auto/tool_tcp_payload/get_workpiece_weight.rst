.. _auto_get_workpiece_weight:

get_workpiece_weight (Auto Mode)
------------------------------------------
This section explains how to use :ref:`get_workpiece_weight <get_workpiece_weight>`  
during **Auto (Run)** operations to retrieve the currently configured **workpiece weight**.  
The workpiece weight is an essential parameter for accurate motion execution,  
payload handling, and force/compliance behavior during automated tasks.

This function returns the workpiece mass (excluding tool weight) that has been  
previously set by the user or measured through Smart Setup.

**Typical usage**

- Verify payload configuration before running an automated sequence.  
- Adjust force/compliance behavior based on workpiece load.  
- Apply dynamic logic (e.g., different motions depending on the weight).  
- Perform safety validation to ensure the workpiece value is not missing.

.. Note::

    - If no workpiece weight is set, the function may return **0.0f**.  
    - Recommended to call before pick/place, palletizing, or force-controlled tasks.

**Example: Checking Workpiece Weight Before Auto Motion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Retrieve current workpiece weight
       float w = drfl.get_workpiece_weight();
       printf("Workpiece weight: %.3f kg\n", w);

       // Validate payload before Auto Mode motion
       if (w > 0.0f) {
           float target[6] = {400.f, 100.f, 300.f, 180.f, 0.f, 0.f};
           drfl.movej(target, 60.f, 30.f);
       }
       else {
           printf("Warning: No workpiece weight configured.\n");
       }

       return 0;
   }

In this example, the robot reads the workpiece weight and verifies  
that the value is valid before executing an Auto Mode motion sequence.  
This helps ensure stable trajectory generation and safe task execution.

**Tips**

- Always check payload values when switching between different parts.  
- Use with ``set_workpiece_weight`` or Smart Setup measurement results.  
- Combine with force control tasks for more accurate contact behavior.  
- A non-zero value is recommended for stable Auto Mode motion planning.
