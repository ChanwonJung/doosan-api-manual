.. _set_on_tp_initializing_completed:

set_on_tp_initializing_completed
------------------------------------------
This is a function for registering the callback function that automatically checks whether  
initialization has been completed when the robot controller carries out initialization by T/P  
application after the booting of the robot controller.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 649)

.. code-block:: cpp

    void set_on_tp_initializing_completed(TOnTpInitializingCompletedCB pCallbackFunc) { 
        _set_on_tp_initializing_completed(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnTpInitializingCompletedCB <cb_tontpinitializingcompletedcb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   void OnTpInitializingCompletedCB()
   {
       // Requests control right after checking Tp initialization
       cout << "tp initializing completed" << endl;
       drfl.manage_access_control(MANAGE_ACCESS_CONTROL_REQUEST);
   }

   int main()
   {
       drfl.set_on_tp_initializing_completed(OnTpInitializingCompletedCB);
   }

Once registered, this callback executes automatically **after the T/P (Teach Pendant) initialization process** completes.  
It prints a message and requests **control authority** using `manage_access_control()`,  
allowing the external application to take control immediately after system boot.
