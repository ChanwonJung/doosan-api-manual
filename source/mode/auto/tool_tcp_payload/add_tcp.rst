.. _auto_add_tcp:

add_tcp (Auto Mode)
------------------------------------------
This section explains how to use :ref:`add_tcp <add_tcp>`  
during system initialization or tool setup to register a new  
**Tool Center Point (TCP)** on the robot controller.  

The TCP defines a position and orientation relative to the tool flange  
and is a key element for precise task-space control.

Once registered, the TCP may be activated with :ref:`set_tcp <set_tcp>`.

**Typical usage**

- Register TCPs for new grippers, screwdrivers, weld torches, or probes.  
- Create multiple TCP points for complex tools with different working tips.  
- Load TCP values measured using Smart Setup or CAD specifications.  
- Prepare TCP configurations for recipe-based automated tasks.

.. Note::

    - ``strSymbol`` must be unique across all registered TCP names.  
    - Orientation values follow the Z-Y-Z Euler angle convention (A, B, C).  
    - TCP registration is normally performed once during commissioning.

**Example: Registering a New TCP for a Gripper**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Example TCP: 80 mm forward, 0 mm right, 30 mm downward from flange
       float pos[3] = {80.f, 0.f, -30.f};
       float rot[3] = {180.f, 0.f, 180.f};   // Euler Z-Y-Z angles (A, B, C)

       // Register TCP
       if (!drfl.add_tcp("TCP_GRIPPER_CENTER", pos, rot)) {
           printf("Failed to register TCP.\n");
           return -1;
       }

       // Activate TCP for Auto Mode actions
       drfl.set_tcp("TCP_GRIPPER_CENTER");

       return 0;
   }

In this example, a TCP is registered and immediately activated  
for subsequent Auto Mode pick-and-place operations.

**Tips**

- Define multiple TCPs for tools with different contact or measurement points.  
- Use Smart Setup auto-measurement when possible for higher precision.  
- Maintain consistent naming conventions for recipes and tool libraries.
