.. _auto_set_tcp:

set_tcp (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_tcp <set_tcp>`  
during **Auto (Run)** operations to activate a predefined  
**Tool Center Point (TCP)** configuration.

The TCP defines the effective reference point for all task-space motions,  
including linear moves, force control, and orientation-based operations.  
Accurate TCP activation is essential for precise path execution  
and safe automated workflows.

This function selects a TCP configuration previously created  
using :ref:`add_tcp <add_tcp>`.

**Typical usage**

- Switch between multiple TCPs for different tools or gripper fingers.  
- Select a TCP optimized for picking, inserting, or assembly tasks.  
- Adjust control behavior when the working point is offset from the flange.  
- Validate spatial accuracy before Auto Mode motion.

.. Note::

    - ``strSymbol`` must match a TCP name registered with ``add_tcp``.  
    - Switching TCPs during motion is not recommended; apply at safe poses.  
    - The TCP affects all task-space motion planning and force-control logic.

**Example: Activating a TCP Before Auto Mode Motion**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Activate TCP with symbol "TCP_GRIPPER_CENTER"
       if (!drfl.set_tcp("TCP_GRIPPER_CENTER")) {
           printf("Failed to activate TCP.\n");
           return -1;
       }

       // Execute Auto Mode motion using the selected TCP
       float approach[6] = {400.f, 200.f, 300.f, 180.f, 0.f, 0.f};
       drfl.movel(approach, (float[2]){80.f, 40.f}, (float[2]){300.f, 100.f});

       return 0;
   }

In this example, a pre-registered TCP is activated  
and used for subsequent Auto Mode linear movements.

**Tips**

- Use precise values (Smart Setup recommended) for best accuracy.  
- Store multiple TCPs when one tool has several usable operation points.  
- Check current TCP with ``get_tcp()`` before executing critical tasks.
