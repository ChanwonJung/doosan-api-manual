.. _set_on_program_stopped:

set_on_program_stopped
------------------------------------------
This is a function for registering the callback function that automatically checks if program  
execution has been completely terminated when the program is terminated due to errors or  
user command during execution in automatic mode in the robot controller.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 653)

.. code-block:: cpp

    void set_on_program_stopped(TOnProgramStoppedCB pCallbackFunc) { 
        _set_on_program_stopped(_rbtCtrl, pCallbackFunc); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnProgramStoppedCB <cb_tonprogramstoppedcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnProgramStoppedCB(const PROGRAM_STOP_CAUSE eStopCause)
   {
       // Shows whether restart of program is possible
   }

   int main()
   {
       drfl.set_on_program_stopped(OnProgramStoppedCB);
   }

When this function is registered,  
the callback `OnProgramStoppedCB()` is automatically executed whenever a program is stopped.  
It helps determine whether the program was terminated normally, by user interruption, or due to an error —  
and can be used to trigger restart or recovery logic accordingly.
