.. _get_current_pose:

get_current_pose
------------------------------------------
This is a function for checking information on the current location by axis of the robot  
according to the coordinates (joint space or task space) in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 711)

.. code-block:: cpp

    LPROBOT_POSE get_current_pose(ROBOT_SPACE eSpaceType = ROBOT_SPACE_JOINT) { 
        return _get_current_pose(_rbtCtrl, eSpaceType); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eSpaceType
     - :ref:`ROBOT_SPACE <enum_robot_space>`
     - ROBOT_SPACE_JOINT
     - Space type of the robot position. |br|
       (e.g., joint space, task space).

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_POSE <struct_robot_pose>`
     - Refer to the Definition of Structure

**Example**

.. code-block:: cpp

   LPROBOT_POSE lpPose = drfl.get_current_pose(ROBOT_SPACE_JOINT);
   // Displays the current location of the robot in joint space
   for (int k = 0; k < NUM_JOINT; k++) {
       cout << lpPose->_fPosition[k] << endl;
   }

This example retrieves the **current pose of the robot** based on the selected space type.  
When `ROBOT_SPACE_JOINT` is used, the returned structure contains **joint angles** for each axis.  
If `ROBOT_SPACE_TASK` is specified, it contains the **Cartesian position and orientation (X, Y, Z, Rx, Ry, Rz)** of the robot end-effector.
