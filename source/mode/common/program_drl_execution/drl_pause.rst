.. _drl_pause:

drl_pause
------------------------------------------
This is a function for temporarily suspending the DRL program (task)  
currently executed in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 938)

.. code-block:: cpp

    bool drl_pause() { 
        return _drl_pause(_rbtCtrl); 
    };

**Parameter** |br|
None

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

   if (drfl.get_program_state() == DRL_PROGRAM_STATE_PLAY) {
       drfl.drl_pause();
   }

This example checks if the current **DRL program** is in the *PLAY* state using `get_program_state()`.  
If so, it suspends execution by calling `drl_pause()`.  
The suspended program can later be resumed using :ref:`drl_resume <drl_resume>`,  
allowing safe interruption and continuation of automatic DRL tasks.
