.. _manual_set_user_home:

set_user_home (Manual Mode)
------------------------------------------
This section explains how to use :ref:`set_user_home <set_user_home>` during **Manual (Teach)** operations.  
It defines a custom **home position (pose)** that the robot can return to for standby, calibration,  
or safety recovery.  
The user home is typically set after manually jogging the robot to a known, safe posture  
(e.g., fully extended or folded position).

**Typical usage**

- Define a “safe standby” pose at the end of a manual teaching session.  
- Store a repeatable reference position for quick homing or calibration checks.  
- Update the home position after a tool change or fixture repositioning.

.. Note::

    - The home position is stored in the controller and persists after reboot.  
    - The pose should be reachable under all safety configurations.  
    - Retrieve the stored pose anytime using :ref:`get_user_home <manual_get_user_home>`.

**Example: Define a Custom Home Pose After Manual Teaching**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1. Jog robot to the desired "home" posture manually
       printf("Position robot at desired home location...\n");
       std::this_thread::sleep_for(std::chrono::seconds(3)); // Operator moves manually

       // Step 2. Get the current TCP pose
       LPROBOT_TASK_POSE pPose = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);

       // Step 3. Set this pose as the new user home position
       drfl.set_user_home(pPose);

       printf("New User Home successfully set.\n");

       // Step 4. (Optional) Verify by reading it back
       LPROBOT_POSE pHome = drfl.get_user_home();
       printf("[Stored User Home]\n");
       printf("X: %.2f, Y: %.2f, Z: %.2f | Rx: %.2f, Ry: %.2f, Rz: %.2f\n",
              pHome->_fX, pHome->_fY, pHome->_fZ,
              pHome->_fRx, pHome->_fRy, pHome->_fRz);

       return 0;
   }

**Tips**

- Choose a **collision-free and easily reachable** pose for home.  
- Recommended to record home after final tool or payload setup.  
- Use :ref:`move_home <move_home>` later to automatically return to this pose.  
- Keep the home pose consistent across teaching sessions for reproducibility.
