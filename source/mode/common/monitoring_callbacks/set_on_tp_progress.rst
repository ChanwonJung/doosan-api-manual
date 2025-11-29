.. _set_on_tp_progress:

set_on_tp_progress
------------------------------------------
This function is used to register the callback function to check the information  
of the execution step when the ``tp_progress`` command is used in DRL.  
It is useful when functions that should be executed automatically are made.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 643) 

.. code-block:: cpp

    void set_on_tp_progress(TOnTpProgressCB pCallbackFunc) { 
        _set_on_tp_progress(_rbtCtrl, pCallbackFunc); 
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
     - :ref:`TOnTpProgressCB <cb_tontpprogresscb>`
     - -
     - Refer to definition of callback function

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include <iostream>
   #include <thread>
   using namespace std;

   // Callback function for TP progress updates
   void OnTpProgress(LPMESSAGE_PROGRESS tProgress)
   {
       cout << "-------------------------------------------" << endl;
       cout << "[TP PROGRESS UPDATE]" << endl;
       cout << "Current Step : " << tProgress->_iCurrentCount << " / "
            << tProgress->_iTotalCount << endl;
       cout << "Progress (%) : " << tProgress->_iPercent << "%" << endl;
       cout << "Description  : " << tProgress->_szDesc << endl;
       cout << "-------------------------------------------" << endl;

       // Example: stop process when 100% complete
       if (tProgress->_iPercent >= 100)
           cout << "[Host] Operation completed successfully." << endl;
   }

   int main()
   {
       // Register the progress callback
       drfl.set_on_tp_progress(OnTpProgress);

       cout << "Monitoring TP progress updates..." << endl;
       while (true)
       {
           this_thread::sleep_for(chrono::seconds(1));
       }
       return 0;
   }

When registered, this callback function executes automatically  
when a **progress message** is reported from the Teach Pendant (TP).  
It helps track **execution steps, percentage, and status messages**  
to provide live task progress monitoring.
