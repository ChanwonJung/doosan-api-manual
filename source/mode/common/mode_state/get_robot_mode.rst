.. _get_robot_mode:

get_robot_mode
------------------------------------------
This is a function for checking information on the current operation mode of the robot controller.  
The automatic mode is a mode for automatically executing motions (programs) configured in sequential order,  
while manual mode is a mode for executing single motions like jog.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 691)

.. code-block:: cpp

    ROBOT_MODE get_robot_mode() { return _get_robot_mode(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_MODE <enum_robot_mode>`
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   string strDrProgram = "\r\n"
                         "loop = 0\r\n"
                         "while loop < 3:\r\n"
                         "    movej(posj(10,10,10,10,10,10), vel=60, acc=60)\r\n"
                         "    movel(posx(00,00,00,00,00,00), vel=60, acc=60)\r\n"
                         "    loop=loop+1\r\n"
                         "end\r\n"
                         "movej(posj(10,10,10,10,10,10), vel=60, acc=60)\r\n";

   if (drfl.get_robot_state() == ESTATE_STANDBY) {
       if (drfl.get_robot_mode() == ROBOT_MODE_MANUAL) {
           // Manual mode
           drfl.jog(JOG_AXIS_JOINT_3, MOVE_REFERENCE_BASE, 0.0f);
           sleep(2);
           drfl.jog(JOG_AXIS_JOINT_3, MOVE_REFERENCE_BASE, 0.0f);
       }
       else {
           // Automatic mode
           ROBOT_SYSTEM eTargetSystem = ROBOT_SYSTEM_VIRTUAL;
           drfl.drl_start(eTargetSystem, strDrProgram);
       }
   }


This example checks the robot’s **operation mode** and performs different actions accordingly.  
In manual mode, the robot executes a short jog motion;  
in automatic mode, it runs a predefined DRL program sequentially.