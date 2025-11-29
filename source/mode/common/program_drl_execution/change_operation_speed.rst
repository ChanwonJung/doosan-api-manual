.. _change_operation_speed:

change_operation_speed
------------------------------------------
This function adjusts the operation velocity.  
The argument is the relative velocity in a percentage of the currently set velocity and has a value from 1 to 100.  
Therefore, a value of 50 means that the velocity is reduced to 50% of the currently set velocity.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 767)

.. code-block:: cpp

    bool change_operation_speed(float fSpeed) { 
        return _change_operation_speed(_rbtCtrl, fSpeed); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fSpeed
     - float
     - -
     - Operation speed (1–100%) |br|
       Represents the relative velocity ratio compared to the currently set value.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Failed
   * - 1
     - int
     - Success

**Example**

.. code-block:: cpp

   drfl.change_operation_speed(40);

   string strDrlProgram = "loop = 0\n"
                          "while loop < 3:\n"
                          "    movej(posj(10,10,10,10,10,10), vel=60, acc=60)\n"
                          "    loop = loop + 1\n"
                          "end\n";

   if (drfl.get_robot_state() == STATE_STANDBY) {
       drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS);
       if (drfl.get_robot_mode() == ROBOT_MODE_AUTONOMOUS) {
           ROBOT_SYSTEM eTargetSystem = ROBOT_SYSTEM_VIRTUAL;
           drfl.drl_start(eTargetSystem, strDrlProgram);
       }
   }

This example changes the robot's **operation speed** to 40% of the current setting  
and then executes a simple **DRL motion loop** in autonomous mode.  
The new speed value applies immediately to all subsequent motion commands executed by the controller.
