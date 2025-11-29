.. _manual_get_current_velj:

get_current_velj (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_current_velj <get_current_velj>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, it is essential for checking **joint-wise velocity feedback**  
while performing manual or jog-based movements.

**Typical usage**

- Display or log **joint velocities (J1–J6)** during jog or blended motion.  
- Verify velocity compliance with safety limits or joint monitoring tools.  
- Detect excessive speed or mechanical resistance during manual teaching.

.. Note::

    - Useful for diagnosing joint motion balance and tuning jog speeds.

**Example: Display Joint Velocities while Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Jog +J3 direction briefly
       drfl.jog(JOG_AXIS_JOINT_3, MOVE_REFERENCE_JOINT, 15.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(400));

       // Read current joint velocities
       LPROBOT_VELJ pVelJ = drfl.get_current_velj();

       printf("[Current Joint Velocities]\n");
       for (int i = 0; i < NUMBER_OF_JOINT; ++i)
           printf("J%d: %.2f deg/s\n", i + 1, pVelJ->_fTargetVel[i]);

       // Stop and ensure robot is stationary
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       return 0;
   }

**Tips**

- ``get_current_velj()`` helps confirm joint velocity uniformity during manual jog sequences.  
- Useful for detecting lag or delay on specific joints during fine-tuning.  
- Combine with :ref:`get_current_posj <manual_get_current_posj>` for motion analysis in teaching mode.
