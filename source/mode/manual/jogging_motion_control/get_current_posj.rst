.. _manual_get_current_posj:

get_current_posj (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_current_posj <get_current_posj>` during **Manual (Teach)** operations.  
Although defined in **3.1 Common**, this function is widely used in teaching mode to **monitor or record the robot’s joint angles**  
while performing jog or multi-jog actions.

**Typical usage**

- Display or log current **joint positions (J1–J6)** during manual operation.  
- Verify mechanical limits and safe ranges while jogging each axis.  
- Compare current joint positions with a predefined pose or user-taught data.

.. Note::

    - Each joint angle corresponds to **Joint 1 → Joint 6** in the robot model.  
    - This is particularly useful for checking joint configuration before or after teaching a waypoint.

**Example; Read Joint Angles after Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Jog +J2 direction for a short time
       drfl.jog(JOG_AXIS_JOINT_2, MOVE_REFERENCE_JOINT, 10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       // Get current joint positions
       LPROBOT_POSJ pJoint = drfl.get_current_posj();

       printf("[Current Joint Angles]\n");
       for (int i = 0; i < NUMBER_OF_JOINT; ++i)
           printf("J%d: %.2f°\n", i + 1, pJoint->_fTargetPos[i]);

       return 0;
   }

**Tips**

- Use this function to confirm safe joint states before teaching or playback.  
- Ideal for comparing manual joint movements with program-taught poses.  
- Can be used together with :ref:`get_current_posx <manual_get_current_posx>` to compare joint vs. Cartesian data.
