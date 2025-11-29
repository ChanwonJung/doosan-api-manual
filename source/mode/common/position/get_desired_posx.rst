.. _get_desired_posx:

get_desired_posx
------------------------------------------
This is a function for calculating the target posture of the current tool.  
At this time, the posture is based on `eTargetRef`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 675)

.. code-block:: cpp

    LPROBOT_POSE get_desired_posx(COORDINATE_SYSTEM eCoodType = COORDINATE_SYSTEM_BASE) { 
        return _get_desired_posx(_rbtCtrl, eCoodType); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eCoodType
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Target coordinate reference frame |br|
       Refer to the Definition of Enumeration Type

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

   LPROBOT_POSE result = drfl.get_desired_posx();
   for (int i = 0; i < NUM_TASK; i++) {
       cout << result->_fPosition[i] << endl;
   }

This example retrieves the **target pose (position and orientation)**  
of the robot’s tool in the specified coordinate system (`COORDINATE_SYSTEM_BASE`).  
The returned `ROBOT_POSE` structure contains the desired Cartesian coordinates and rotation values  
that the controller is currently commanding the robot to reach.
