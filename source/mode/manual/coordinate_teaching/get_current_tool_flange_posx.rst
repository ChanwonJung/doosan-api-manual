.. _manual_get_current_tool_flange_posx:

get_current_tool_flange_posx (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_current_tool_flange_posx <get_current_tool_flange_posx>` during **Manual (Teach)** operations.  
This function retrieves the **current position and orientation of the robot’s tool flange (end flange)**  
in Cartesian coordinates. It is primarily used during teaching to verify the TCP or flange pose  
relative to the selected coordinate system (BASE, TOOL, or USER).

**Typical usage**

- Check the **actual flange position** before or after teaching a user frame.  
- Verify TCP alignment with a fixture or reference point on the workpiece.  
- Compare flange positions across different coordinate systems for calibration.  
- Log real-time flange movement during hand-guided or manual operations.

.. Note::

    - The default coordinate reference is **BASE**, unless otherwise configured by the active frame.  
    - The returned pose reflects the **flange**, not the TCP — use :ref:`get_current_posx <manual_get_current_posx>` for TCP position.  
    - Data is read-only and updated continuously by the controller during motion.

**Example: Display the current tool flange position during teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Robot servo ON

       printf("Monitoring current tool flange position...\n");

       for (int i = 0; i < 10; ++i) {
           LPROBOT_POSE pFlange = drfl.get_current_tool_flange_posx();
           if (pFlange) {
               printf("[Flange Pose] X=%.3f Y=%.3f Z=%.3f | Rx=%.3f Ry=%.3f Rz=%.3f\n",
                      pFlange->_fX, pFlange->_fY, pFlange->_fZ,
                      pFlange->_fRx, pFlange->_fRy, pFlange->_fRz);
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(300));
       }

       return 0;
   }

In this example, the host program repeatedly reads the **flange pose** during manual operation.  
It helps verify whether the robot’s physical flange aligns with the expected location  
when teaching a new user frame or performing fixture-based calibration.  
The displayed coordinates provide immediate feedback to confirm correct frame alignment and pose tracking.

**Tips**

- Use when calibrating **TCP offset or user frames** to confirm flange alignment.  
- Compare results with :ref:`get_current_posx <manual_get_current_posx>` to verify TCP offset accuracy.  
- Combine with :ref:`coord_transform <manual_coord_transform>` to interpret the flange pose in other coordinate frames.  
- During precision teaching, keep servo ON but robot stationary for stable readings.
