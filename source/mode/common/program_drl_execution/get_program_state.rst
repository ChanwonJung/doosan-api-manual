.. _get_program_state:

get_program_state
------------------------------------------
This is a function for checking information on the execution state of the program  
that is currently being executed in automatic mode in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 738)

.. code-block:: cpp

    DRL_PROGRAM_STATE get_program_state() { 
        return _get_program_state(_rbtCtrl); 
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`DRL_PROGRAM_STATE <enum_drl_program_state>`
     - Refer to the Definition of Enumeration Type

**Example**

.. code-block:: cpp

   if (drfl.get_program_state() == DRL_PROGRAM_STATE_PLAY) {
       // Stops the program execution state
       drfl.drl_stop(STOP_TYPE_SLOW);
   }
   else if (drfl.get_program_state() == DRL_PROGRAM_STATE_HOLD) {
       // Resumes the program execution state
       drfl.drl_resume();
   }

This example checks the **current DRL program execution state**.  
If the program is in *PLAY* state, it stops execution using `drl_stop()`.  
If it is in *HOLD* state, it resumes execution with `drl_resume()`.  
This allows precise monitoring and control of program flow in **automatic mode**.
