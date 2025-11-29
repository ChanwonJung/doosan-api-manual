.. _auto_set_tool:

set_tool (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_tool <set_tool>`  
during **Auto (Run)** operations to activate a predefined **tool configuration**.  
The active tool determines the robot’s payload, center of gravity, and motion behavior,  
making it essential for accurate task-space control and safe automated operation.

This function selects a tool definition that was previously registered  
using :ref:`add_tool <add_tool>`.

**Typical usage**

- Switch between different end-effectors (e.g., gripper, screwdriver, probe).  
- Activate the correct tool before executing Auto Mode pick/place sequences.  
- Ensure consistent dynamics and force-control performance.  
- Validate tool configuration in recipes with multiple tool types.

.. Note::

    - The symbol must match the tool name registered via ``add_tool``.  
    - Changing tools during motion is not recommended; switch at a safe pose.  
    - The active tool affects payload, CoG, and force/torque estimation.

**Example: Selecting a Tool Before Auto Mode Operation**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Activate a predefined tool configuration
       if (!drfl.set_tool("RG2_GRIPPER")) {
           printf("Failed to activate tool RG2_GRIPPER.\n");
           return -1;
       }

       // Use this tool in Auto Mode motion
       float pickPose[6] = {300.f, 200.f, 250.f, 180.f, 0.f, 0.f};
       drfl.movel(pickPose, (float[2]){100.f, 50.f}, (float[2]){300.f, 100.f});

       return 0;
   }

In this example, the robot selects a tool configuration and  
executes an Auto Mode movement using the chosen tool's properties.

**Tips**

- Match the tool symbol exactly with the controller configuration.  
- Use this function when switching between tool types in automated workflows.  
- Use ``get_tool()`` to confirm which tool is currently active.
