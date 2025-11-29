.. _set_robot_speed_mode:

set_robot_speed_mode
------------------------------------------
This is a function for setting and changing the current operation robot system in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 728)

.. code-block:: cpp

    bool set_robot_speed_mode(SPEED_MODE eSpeedMode) { return _set_robot_speed_mode(_rbtCtrl, eSpeedMode); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eSpeedMode
     - :ref:`SPEED_MODE <enum_speed_mode>`
     - - 
     - Target velocity mode to set.  

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to change the speed mode.
   * - 1
     - int
     - Success — successfully changed the speed mode.

**Example**

.. code-block:: cpp

   if (drfl.get_robot_speed_mode() == SPEED_REDUCED_MODE) {
       // Changes the speed reduced mode to normal speed mode
       drfl.set_robot_speed_mode(SPEED_NORMAL_MODE);
   }

This example checks whether the current robot controller is operating in **speed-reduced mode**.  
If it is, the function changes it to **normal speed mode** by calling `set_robot_speed_mode(SPEED_NORMAL_MODE)`.  

When executed successfully, the robot exits the reduced-speed state and operates at normal velocity,  
allowing full-speed motion execution while maintaining safe control through the speed mode management system.
