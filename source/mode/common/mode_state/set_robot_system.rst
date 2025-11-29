.. _set_robot_system:

set_robot_system
------------------------------------------
This is a function for setting and changing the current operation robot system in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 703)

.. code-block:: cpp

    bool set_robot_system(ROBOT_SYSTEM eRobotSystem) { return _set_robot_system(_rbtCtrl, eRobotSystem); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eRobotSystem
     - :ref:`ROBOT_SYSTEM <enum_robot_system>`
     - -
     - Specifies the target robot system to be set.  

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to change the robot system.
   * - 1
     - int
     - Success — successfully changed the robot system.

**Example**

.. code-block:: cpp

   ROBOT_SYSTEM eRobotSystem = drfl.get_robot_system();
   if (eRobotSystem != ROBOT_SYSTEM_REAL) {
       // Converts to real robot system
       drfl.set_robot_system(ROBOT_SYSTEM_REAL);
   }
   else {
       // Do something ...
   }

This example checks if the robot is in **reduced-speed mode**  
and switches it to **normal speed mode** for full-speed operation.