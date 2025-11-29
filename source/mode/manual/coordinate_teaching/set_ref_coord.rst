.. _manual_set_ref_coord:

set_ref_coord (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_ref_coord <set_ref_coord>` during **Manual (Teach)** operations.  
This function sets the **active reference coordinate system** that the robot uses for motion commands and position readings.  

It determines whether jogging, teaching, or position display is based on **BASE**, **TOOL**, or a defined **USER** frame.  
Proper use of this function ensures consistent movement directions and accurate coordinate teaching.

**Typical usage**

- Switch between **BASE** and **TOOL** coordinates to control jog direction during teaching.  
- Select a **USER-defined coordinate frame** before performing teaching or calibration.  
- Align robot motion with a specific workpiece or fixture coordinate.  
- Validate coordinate alignment during multi-frame teaching workflows.

.. Note::

    - Affects all subsequent **manual jog** and **move commands** until changed again.

**Example: Switch to TOOL frame for precise end-effector teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   #include <thread>
   using namespace std;
   using namespace DRAFramework;

   int main()
   {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // 1) Set reference to TOOL frame for tool-relative jogging
       if (drfl.set_ref_coord(COORDINATE_SYSTEM_TOOL))
           cout << "[Frame] Reference coordinate set to TOOL frame.\n";
       else
           cout << "[Frame] Failed to set reference coordinate.\n";

       // 2) Display current TCP position in TOOL frame
       LPROBOT_TASK_POSE pPose = drfl.get_current_posx(COORDINATE_SYSTEM_TOOL);
       cout << "[TOOL Frame Position]\n";
       cout << "X: " << pPose->_fX << "  Y: " << pPose->_fY << "  Z: " << pPose->_fZ << endl;

       // 3) Switch back to BASE frame when done
       drfl.set_ref_coord(COORDINATE_SYSTEM_BASE);
       cout << "[Frame] Reference coordinate reverted to BASE frame.\n";

       return 0;
   }

**Tips**

- Always confirm the correct frame before teaching or moving — **BASE** for global motion, **TOOL/USER** for localized operations.  
- Use this function in combination with :ref:`get_current_posx <manual_get_current_posx>` to verify pose consistency.  
- In complex calibration, switching between frames helps validate **tool and user frame accuracy**.  
- Avoid changing reference frames during motion to prevent unexpected orientation changes.
