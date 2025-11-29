.. _get_desired_velx:

get_desired_velx
------------------------------------------
This function retrieves the **desired task-space velocity** of the robot from the controller.  
Unlike :ref:`get_current_velx`, which reports the measured TCP velocity,  
this function returns the **commanded (target) TCP velocity** computed internally by the motion planner.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 729)

.. code-block:: cpp

    LPROBOT_VEL get_desired_velx() {
        return _get_desired_velx(_rbtCtrl);
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
     - Pointer to a structure containing the desired TCP velocity values |br|
       (linear and angular components in task space).

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection and robot mode setup are complete

       LPROBOT_VEL lpVel = drfl.get_desired_velx();
       if (lpVel) {
           printf("Desired TCP Velocity (Targeted by Controller):\n");
           printf("Linear  [m/s]:  vx=%.4f  vy=%.4f  vz=%.4f\n",
                  lpVel->_fLinearVel[0],
                  lpVel->_fLinearVel[1],
                  lpVel->_fLinearVel[2]);
           printf("Angular [rad/s]: wx=%.4f  wy=%.4f  wz=%.4f\n",
                  lpVel->_fAngularVel[0],
                  lpVel->_fAngularVel[1],
                  lpVel->_fAngularVel[2]);
       } else {
           fprintf(stderr, "Failed to retrieve desired velocity.\n");
       }

       return 0;
   }

This example prints the **controller’s internally computed target TCP velocity**,  
which can be compared with the measured velocity (:ref:`get_current_velx`)  
to evaluate servo tracking performance or motion synchronization accuracy.
