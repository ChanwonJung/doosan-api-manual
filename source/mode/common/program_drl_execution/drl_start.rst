.. _drl_start:

drl_start
------------------------------------------
This is a function for executing the program (task) consisting of the DRL language in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 934)

.. code-block:: cpp

    bool drl_start(ROBOT_SYSTEM eRobotSystem, string strDrlProgram) { 
        return _drl_start(_rbtCtrl, eRobotSystem, strDrlProgram.c_str()); 
    };

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
     - Refer to the Definition of Enumeration Type
   * - strDrlProgram
     - string
     - -
     - Program character string to execute.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error
   * - 1
     - int
     - Success

**Example**

.. code-block:: cpp

   string strDrlProgram = "\r\n\
   loop = 0\r\n\
   while loop < 3\r\n\
       movej([10.00, 10.00, 10.00, 10.00, 10.00, 10.00], vel=60, acc=60)\r\n\
       movel([20.00, 20.00, 20.00, 20.00, 20.00, 20.00], vel=60, acc=60)\r\n\
       loop += 1\r\n\
   end\r\n";

   if (drfl.get_robot_state() == STATE_STANDBY) {
       if (drfl.get_robot_mode() == ROBOT_MODE_AUTONOMOUS) {
           // Automatic Mode
           ROBOT_SYSTEM eTargetSystem = ROBOT_SYSTEM_VIRTUAL;
           drfl.drl_start(eTargetSystem, strDrlProgram);
       }
   }

.. note::

   - The robot operation state should be **STATE_STANDBY**, and the robot motions normally when the robot mode is **automatic**.  
   - The **DRL program** should be made by referring to the **programming manual document** in the appendix.

This function enables execution of DRL-language motion tasks directly on the controller.  
It is primarily used for autonomous or batch task execution, with DRL commands defined in string form.  
Ensure that the controller is in standby and autonomous mode before invoking this function.
