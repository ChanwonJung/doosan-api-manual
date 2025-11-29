.. _get_current_velj:

get_current_velj
------------------------------------------
This function retrieves the **current joint-space velocity** of the robot from the controller.  
It returns the instantaneous angular velocity of each joint, typically expressed in **radians per second**.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 719)

.. code-block:: cpp

    LPROBOT_VEL get_current_velj() {
        return _get_current_velj(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_VEL <struct_robot_vel>`
     - Pointer to a structure containing the current joint angular velocities. |br|
       The array represents the angular velocity of each joint (J1–J6) in **rad/s**.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume robot connection and mode setup are already done

       LPROBOT_VEL lpVel = drfl.get_current_velj();
       if (lpVel) {
           printf("Current Joint Velocities [rad/s]:\n");
           for (int j = 0; j < NUMBER_OF_JOINT; ++j) {
               printf("Joint %d: %.4f\n", j + 1, lpVel->_fJointVel[j]);
           }
       } else {
           fprintf(stderr, "Failed to read joint velocity (null pointer)\n");
       }
       return 0;
   }

This example queries and prints the **current angular velocity of each joint** in radians per second.  
Useful for motion monitoring, feedback analysis, or verifying speed constraints during trajectory execution.
