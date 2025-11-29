.. _manual_get_current_velx:

get_current_velx (Manual Mode)
------------------------------------------
This section describes how to use :ref:`get_current_velx <get_current_velx>` during **Manual (Teach)** operations.  
While defined in **3.1 Common**, this function is used in teaching mode to **monitor the robot’s current TCP velocity**  
in Cartesian space.

**Typical usage**

- Check real-time **tool center point (TCP)** velocity while jogging or moving manually.  
- Verify that the robot moves within safe velocity limits during teaching.  
- Record motion profiles for calibration or operator training.

.. Note::
    
    - Units are typically **mm/s** for translation and **deg/s** for rotation.  
    - The coordinate system (BASE, TOOL, WORLD) depends on the reference used.

**Example: Monitor TCP Velocity during Manual Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Perform a short jog in +X direction
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 20.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(300));

       // Retrieve current TCP velocity
       LPROBOT_VELX pVel = drfl.get_current_velx(COORDINATE_SYSTEM_BASE);

       printf("[Current TCP Velocity - BASE]\n");
       printf("Linear: X %.2f | Y %.2f | Z %.2f mm/s\n", pVel->_fX, pVel->_fY, pVel->_fZ);
       printf("Angular: Rx %.2f | Ry %.2f | Rz %.2f deg/s\n", pVel->_fRx, pVel->_fRy, pVel->_fRz);

       // Stop motion and ensure stability
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       return 0;
   }

**Tips**

- Use ``get_current_velx()`` to visualize real-time TCP speed on a pendant or GUI.  
- Helps ensure safe manual operations and prevent overspeed conditions.  
- Combine with :ref:`get_current_posx <manual_get_current_posx>` for live motion tracking.
