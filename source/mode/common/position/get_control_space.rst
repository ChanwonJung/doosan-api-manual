.. _get_control_space:

get_control_space
------------------------------------------
This is a function for checking information on the control space of the robot in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 717)

.. code-block:: cpp

    ROBOT_SPACE get_control_space() { 
        return _get_control_space(_rbtCtrl); 
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_SPACE <enum_robot_space>`
     - Current control space of the robot. |br|
       (e.g., `ROBOT_SPACE_JOINT`, `ROBOT_SPACE_TASK`).

**Example**

.. code-block:: cpp

   ROBOT_SPACE eSpace = drfl.get_control_space();

   if (eSpace == ROBOT_SPACE_JOINT)
       cout << "Current control space: Joint Space" << endl;
   else if (eSpace == ROBOT_SPACE_TASK)
       cout << "Current control space: Task Space" << endl;

In this example, the function checks which **control coordinate space** the robot is operating in.  
`ROBOT_SPACE_JOINT` indicates control in joint coordinates, while `ROBOT_SPACE_TASK` indicates  
control in Cartesian task coordinates.  
This function is often used to verify or synchronize motion commands with the controller’s current state.
