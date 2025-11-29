.. _manual_get_user_home:

get_user_home (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_user_home <get_user_home>` during **Manual (Teach)** operations.  
It retrieves the **user-defined home pose** of the robot — a safe standby position typically used  
at the start and end of manual calibration tasks.  
This helps confirm that the robot will move to a predictable, collision-free posture before continuing operations.

**Typical usage**

- Retrieve the home pose for manual verification before returning to it.  
- Display or log home position for operator safety checks.  
- Compare with the current TCP pose to ensure correct home return sequence.

.. Note::

    - The return type is :ref:`ROBOT_POSE <struct_ROBOT_POSE>`.  
    - The home pose is user-defined and can be set with :ref:`set_user_home <set_user_home>`.  
    - This command only retrieves data; it does not initiate motion.

**Example: Display and Move Back to User Home**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Retrieve the user home pose
       LPROBOT_POSE pHome = drfl.get_user_home();

       printf("[User Home Pose]\n");
       printf("X: %.2f, Y: %.2f, Z: %.2f | Rx: %.2f, Ry: %.2f, Rz: %.2f\n",
              pHome->_fX, pHome->_fY, pHome->_fZ,
              pHome->_fRx, pHome->_fRy, pHome->_fRz);

       // Step 2. Move robot to the home position (optional manual confirmation)
       printf("Moving robot to user home...\n");
       drfl.move_home(MOVE_HOME_MECHANIC, 1);
       drfl.mwait();

       printf("Robot successfully returned to user home.\n");

       return 0;
   }

**Tips**

- Use before shutdown or between teaching sessions to safely park the robot.  
- Pair with :ref:`set_user_home <set_user_home>` to define custom rest positions.  
- Always confirm the workspace is clear before executing a home move.
