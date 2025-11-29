.. _get_robot_speed_mode:

get_robot_speed_mode
------------------------------------------
This is a function for checking the current velocity mode (normal mode, deceleration mode)  
in the robot controller along with the `ToMonitoringSpeedModeCB` callback function.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 708)

.. code-block:: cpp

    SPEED_MODE get_robot_speed_mode() { return _get_robot_speed_mode(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`SPEED_MODE <enum_speed_mode>`
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   if (drfl.get_robot_speed_mode() == SPEED_REDUCED_MODE) {
       // Changes the speed reduced mode to normal speed mode
       drfl.set_robot_speed_mode(SPEED_NORMAL_MODE);
   }

This example checks the robot’s **speed mode**,  
and if it is in **reduced mode**, switches it to **normal mode** for standard motion speed.