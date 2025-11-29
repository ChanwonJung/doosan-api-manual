.. _get_robot_state:

get_robot_state
------------------------------------------
This is a function for checking information on the current operation mode of the robot controller  
along with the `ToMonitoringStateCB` callback function.  
The user should transfer the operation state depending on the current state using the `setRobotControl()` function for safety.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 696)

.. code-block:: cpp

    ROBOT_STATE get_robot_state() { return _get_robot_state(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_STATE <enum_robot_state>` 
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   if (drfl.get_robot_state() == ESTATE_STANDBY) {
       if (drfl.get_robot_mode() == ROBOT_MODE_MANUAL) {
           // Manual mode
           drfl.jog(JOG_AXIS_JOINT_3, MOVE_REFERENCE_BASE, 0.0f);
           sleep(2);
           drfl.jog(JOG_AXIS_JOINT_3, MOVE_REFERENCE_BASE, 0.0f);
       }
   }

This example checks the robot’s **state and mode** before motion.  
When the robot is in **standby** and **manual mode**, it performs a short jog motion on joint 3.  
No motion is executed otherwise, ensuring safe operation.