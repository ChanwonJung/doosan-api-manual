.. _set_robot_mode:

set_robot_mode
------------------------------------------
This is a function for setting information on the current operation mode of the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 693)

.. code-block:: cpp

    bool set_robot_mode(ROBOT_MODE eMode) { return _set_robot_mode(_rbtCtrl, eMode); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eMode
     - :ref:`ROBOT_MODE <enum_robot_mode>`
     - - 
     - Target operation mode to be set.  

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Success — successfully set the robot mode.
   * - 1
     - int
     - Error — failed to change the robot mode.

**Example**

.. code-block:: cpp

   if (drfl.get_robot_mode() == ROBOT_MODE_MANUAL) {
       // Converts to automatic mode
       drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS);
   }

This example checks whether the robot is currently in **manual mode**  
and switches it to **automatic mode** if necessary,  
allowing the controller to execute programmed motions sequentially.
