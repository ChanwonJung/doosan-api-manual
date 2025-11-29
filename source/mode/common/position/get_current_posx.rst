.. _get_current_posx:

get_current_posx
------------------------------------------
This is a function for calculating the posture and solution space of the current task coordinate system.  
At this time, the posture is based on `eTargetRef`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 674)

.. code-block:: cpp

    LPROBOT_TASK_POSE get_current_posx(COORDINATE_SYSTEM eCoodType = COORDINATE_SYSTEM_BASE) { 
        return _get_current_posx(_rbtCtrl, eCoodType); 
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
     - Target coordinate reference frame. |br|

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_TASK_POSE <struct_robot_task_pose>`
     - Refer to the Definition of Structure

**Example**

.. code-block:: cpp

   LPROBOT_TASK_POSE result = drfl.get_current_posx();
   float* pos = new float[NUM_TASK];
   int sol = result->_iTargetSol;
   memcpy(pos, result->_fTargetPos, sizeof(float) * NUM_TASK);

This example retrieves the robot’s **current task-space position and orientation**  
with respect to the base coordinate system (`COORDINATE_SYSTEM_BASE`).  
The returned `ROBOT_TASK_POSE` structure includes both position vectors and the current solution index,  
allowing users to analyze or store the robot’s spatial state at runtime.