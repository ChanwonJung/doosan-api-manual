.. _get_robot_system:

get_robot_system
------------------------------------------
This is a function for checking information on the current operation robot system  
(virtual robot or actual robot) in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 701)

.. code-block:: cpp

    ROBOT_SYSTEM get_robot_system() { return _get_robot_system(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_SYSTEM <enum_robot_system>`
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   // Checks the current robot system
   ROBOT_SYSTEM eRobotSystem = drfl.get_robot_system();

   if (eRobotSystem != ROBOT_SYSTEM_REAL) {
       drfl.set_robot_system(ROBOT_SYSTEM_REAL);
   }
   else {
       // Do something ...
   }

This example checks whether the robot is running in a **virtual** or **real** system.  
If it is virtual, the code switches to **real mode** to enable control of the physical robot.
