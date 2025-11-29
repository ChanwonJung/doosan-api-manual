.. _cb_tontpinitializingcompletedcb:

TOnTpInitializingCompletedCB
------------------------------------------
This is a callback function for checking whether **initialization has been completed**  
when the robot controller carries out initialization by the **Teach Pendant (T/P)** application  
after the controller boots. |br|
As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnTpInitializingCompletedCB)();

   // registration API (internal + wrapper)
   DRFL_API void _SetOnTpInitializingCompleted(LPROBOTCONTROL pCtrl, TOnTpInitializingCompletedCB pCallbackFunc);
   void SetOnTpInitializingCompleted(TOnTpInitializingCompletedCB pCallbackFunc)
   {
       _SetOnTpInitializingCompleted(_rbtCtrl, pCallbackFunc);
   };

**Parameter** |br|
None

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   using namespace DRAFramework;
   using namespace std;

   // Callback function triggered when TP initialization is completed
   void OnTpInitializingCompletedCB()
   {
       cout << "[TP INIT] Teach Pendant initialization completed." << endl;

       // Request control authority right after initialization
       drfl.manage_access_control(MANAGE_ACCESS_CONTROL_REQUEST);
   }

   int main()
   {
       CDRFL drfl;

       // Connect to the controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // Register TP initialization completion callback
       drfl.set_on_tp_initializing_completed(OnTpInitializingCompletedCB);

       // Keep alive to monitor TP initialization
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is invoked when **Teach Pendant initialization** completes after controller startup.  
- Common usage includes **requesting control authority** (`MANAGE_ACCESS_CONTROL_REQUEST`)  
  or performing application startup routines.  
- Keep the callback lightweight (execution time < 50 ms) and avoid blocking operations.
