.. _manual_get_current_rotm:

get_current_rotm (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_current_rotm <get_current_rotm>`  
to check the **real-time orientation matrix (3×3)** of the robot’s TCP during manual teaching.  
It is often used when verifying that the tool remains level, perpendicular, or aligned to a specific surface.

**Typical usage**

- Observe and confirm tool orientation stability during surface approach.  
- Record orientation data for user-defined coordinate systems.  
- Detect unwanted rotation drift during long manual adjustments.

.. Note::

    - The matrix corresponds to the selected reference frame (BASE, TOOL, WORLD).  
    - Ideal for GUI-based orientation visualization or motion logging.  
    - Can be called repeatedly for live visualization (~10–20 Hz).

**Example: Checking TCP Orientation Stability While Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1: Start a small manual jog in Y direction
       drfl.jog(JOG_AXIS_TASK_Y, MOVE_REFERENCE_BASE, 10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       // Step 2: Retrieve the current rotation matrix
       float (*R)[3] = drfl.get_current_rotm(COORDINATE_SYSTEM_BASE);

       // Step 3: Display orientation matrix
       printf("[Current Rotation Matrix - BASE]\n");
       for (int i = 0; i < 3; ++i)
           printf("% .3f % .3f % .3f\n", R[i][0], R[i][1], R[i][2]);

       return 0;
   }

**Tips**

- Use to confirm the TCP remains parallel to the work surface during manual adjustment.  
- Combine with :ref:`get_current_posx <manual_get_current_posx>` for full 6D pose monitoring.  
- Valuable for orientation validation before saving a new teaching point.
