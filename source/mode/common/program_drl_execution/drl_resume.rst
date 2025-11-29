.. _drl_resume:

drl_resume
------------------------------------------
This is a function for resuming the DRL program (task)  
currently temporarily suspended in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 940)

.. code-block:: cpp

    bool drl_resume() { 
        return _drl_resume(_rbtCtrl); 
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

   if (drfl.get_program_state() == DRL_PROGRAM_STATE_HOLD) {
       bool bResult = drfl.drl_resume();
       // Additional logic after resuming program...
   }

This example resumes execution of a **temporarily suspended DRL program**.  
If the robot’s program state is in `DRL_PROGRAM_STATE_HOLD`,  
`drl_resume()` reactivates the DRL task that was paused using :ref:`drl_pause <drl_pause>`.  

This function is commonly used for **controlled recovery** of automatic tasks  
after an intentional pause or safety hold during operation.
