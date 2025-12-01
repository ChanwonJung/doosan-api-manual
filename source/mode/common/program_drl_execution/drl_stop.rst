.. _drl_stop:

drl_stop
------------------------------------------
This is a function for stopping the DRL program (task) currently executed in the robot controller.  
This function stops differently according to the iStopType received as an argument  
and stops the motion in the currently active section.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 936)

.. code-block:: cpp

    bool drl_stop(unsigned char eStopType = 0) { 
        return _drl_stop(_rbtCtrl, eStopType); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iStopType
     - unsigned char
     - 1
     - Stop type selection |br|
       (0: Slow Stop, 1: Quick Stop)

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

   DRL_PROGRAM_STATE eProgramState = drfl.get_program_state();
   if ((eProgramState == DRL_PROGRAM_STATE_PLAY) ||
       (eProgramState == DRL_PROGRAM_STATE_HOLD)) {
       // Stop DRL program
       drfl.drl_stop(1);
   }

This example checks the current **DRL program execution state** using `get_program_state()`.  
If the state is either *PLAY* or *HOLD*, the program is stopped using `drl_stop(1)`,  
which performs a **Quick Stop** operation.  
This function ensures safe and immediate program termination according to the stop type.
