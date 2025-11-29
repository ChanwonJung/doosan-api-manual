.. _cb_tontpprogresscb:

TOnTpProgressCB
------------------------------------------
This is a callback function that is triggered when the **robot controller outputs execution progress information**.  
It is typically used to track or display the progress of tasks, motion sequences, or DRL program phases  
on the **Teach Pendant (T/P)**.  

As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFLEx.h``

.. code-block:: cpp

   // typedef (DRFLEx.h)
   typedef void (*TOnTpProgressCB)(LPMESSAGE_PROGRESS);

   // registration API (internal + wrapper)
   DRFL_API void _set_on_tp_progress(LPROBOTCONTROL pCtrl, TOnTpProgressCB pCallbackFunc);

   // tp progress message callback
   void set_on_tp_progress(TOnTpProgressCB pCallbackFunc)
   {
       _set_on_tp_progress(_rbtCtrl, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :header-rows: 1
   :widths: 20 25 15 40

   * - Parameter Name
     - Data Type
     - Default Value
     - Description
   * - tProgress
     - :ref:`MESSAGE_PROGRESS <struct_MESSAGE_PROGRESS>`
     - -
     - Pointer to structure containing execution phase or progress data output from the robot controller.

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback triggered when the controller reports execution progress
   void OnTpProgressCB(LPMESSAGE_PROGRESS tProgress)
   {
       if (!tProgress) return;

       cout << "[TP PROGRESS]" << endl;
       cout << "Step Name : " << tProgress->_szStepName << endl;
       cout << "Progress  : " << tProgress->_iProgress << " %" << endl;
       cout << "Status    : " << static_cast<int>(tProgress->_eStatus) << endl;

       // Example: stop monitoring when a process completes
       if (tProgress->_iProgress == 100)
           cout << "[INFO] Execution completed successfully!" << endl;
   }

   int main()
   {
       CDRFLEx drfl;

       // Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register T/P progress callback
       drfl.set_on_tp_progress(OnTpProgressCB);

       // Keep alive to continuously receive progress updates
       while (true)
           std::this_thread::sleep_for(std::chrono::seconds(1));

       drfl.close_connection();
       return 0;
   }

**Notes**

- Triggered whenever the controller updates the **progress phase** (e.g., DRL execution, motion progress, or task step).  
- The :ref:`MESSAGE_PROGRESS <struct_MESSAGE_PROGRESS>` structure typically includes the **current step name**, **percentage complete**,  
  and **status flag**.  
- Ideal for implementing **custom progress bars**, **execution monitors**, or **log tracking systems**.  
- Keep callback operations short (execution time < 50 ms) to maintain real-time responsiveness.
