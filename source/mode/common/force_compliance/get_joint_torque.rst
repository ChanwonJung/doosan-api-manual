.. _get_joint_torque:

get_joint_torque
------------------------------------------
This function retrieves the **measured joint torque** values from the robot’s internal torque sensors.  
Each joint torque value represents the **applied load or motor-generated torque** in real-time,  
which can be used for diagnostics, gravity compensation, or compliance control.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 731)

.. code-block:: cpp

    LPROBOT_FORCE get_joint_torque() {
        return _get_joint_torque(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_FORCE <struct_ROBOT_FORCE>` 
     - Pointer to a structure containing the measured torque values for each robot joint (J1–J6). |br|  
       Units: **N·m**

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection and initialization completed

       LPROBOT_FORCE lpForce = drfl.get_joint_torque();
       if (lpForce) {
           printf("Joint Torque Readings [N·m]:\n");
           for (int i = 0; i < NUMBER_OF_JOINT; ++i) {
               printf("J%d: %.3f\n", i + 1, lpForce->_fTorque[i]);
           }
       } else {
           fprintf(stderr, "Failed to retrieve torque data.\n");
       }

       return 0;
   }

This example reads the **current torque applied at each joint**  
and prints the values in **N·m**, which are useful for monitoring joint load,  
detecting external disturbances, or validating force-control behavior.
