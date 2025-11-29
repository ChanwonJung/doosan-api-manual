.. _set_robot_control:

set_robot_control
------------------------------------------
This is a function that the user can set and convert the current operation state in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 698)

.. code-block:: cpp

    bool set_robot_control(ROBOT_CONTROL eControl) { return _set_robot_control(_rbtCtrl, eControl); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eControl
     - :ref:`ROBOT_CONTROL <enum_robot_control>`
     - - 
     - Control command to apply to the robot controller.  

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to change the control state.
   * - 1
     - int
     - Success — successfully changed the control state.

**Example**

.. code-block:: cpp

   if (drfl.get_robot_state() == ESTATE_SAFE_OFF) {
       // Servo ON (reset from SAFE OFF)
       drfl.set_robot_control(CONTROL_RESET_SAFET_OFF);
   }
   else if (drfl.get_robot_state() == ESTATE_SAFE_OFF2) {
       // Enter recovery mode
       drfl.set_robot_control(CONTROL_RECOVERY_SAFE_OFF);
   }

This example checks the robot’s **safe-off state** and sends a control command accordingly.  
It resets the servo power or performs recovery, enabling the robot to return to a controllable state.