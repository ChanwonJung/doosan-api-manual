.. _set_on_homming_completed:

set_on_homming_completed
------------------------------------------
This is a function for registering the callback function that automatically checks whether  
homing has been completed when the robot controller is in homing control mode.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 647)

.. code-block:: cpp

    void set_on_homming_completed(TOnHommingCompletedCB pCallbackFunc) { 
        _set_on_homming_completed(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnHommingCompletedCB <cb_tonhommingcompletedcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnHommingCompletedCB()
   {
       // Generates a message for the completion of homing
       cout << "homing completed" << endl;
       drfl.Homming(false);
   }

   int main()
   {
       drfl.set_on_homming_completed(OnHommingCompletedCB);
   }

When registered, this callback automatically executes after the **homing process is completed**.  
The example prints `"homing completed"` to the console and disables homing mode,  
ensuring that the controller returns to normal operation once calibration is finished.
