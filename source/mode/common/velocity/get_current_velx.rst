.. _get_current_velx:

get_current_velx
------------------------------------------
This function retrieves the **current task-space velocity** of the robot from the controller.  
It provides the instantaneous linear and angular velocity of the TCP (Tool Center Point)  
expressed in the task coordinate frame.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 725)

.. code-block:: cpp

    LPROBOT_VEL get_current_velx() {
        return _get_current_velx(_rbtCtrl);
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
     - Pointer to a structure containing the current TCP velocity values. |br|
       Includes both **linear (vx, vy, vz)** and **angular (wx, wy, wz)** components.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume robot connection and initialization are complete

       LPROBOT_VEL lpVel = drfl.get_current_velx();
       if (lpVel) {
           printf("Current TCP Velocity:\n");
           printf("Linear  [m/s]:  vx=%.4f  vy=%.4f  vz=%.4f\n",
                  lpVel->_fLinearVel[0],
                  lpVel->_fLinearVel[1],
                  lpVel->_fLinearVel[2]);
           printf("Angular [rad/s]: wx=%.4f  wy=%.4f  wz=%.4f\n",
                  lpVel->_fAngularVel[0],
                  lpVel->_fAngularVel[1],
                  lpVel->_fAngularVel[2]);
       }
       return 0;
   }

This example queries the controller for the robot’s **TCP linear and angular velocities**,  
prints them to the console, and can be used for real-time motion monitoring or velocity feedback control.
