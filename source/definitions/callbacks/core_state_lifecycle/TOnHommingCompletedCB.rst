.. _cb_tonhommingcompletedcb:

TOnHommingCompletedCB
------------------------------------------
This is a callback function for checking whether **homing has been completed**  
when the robot controller is operating in **homing control mode**. |br|
As the callback function is executed automatically in the case of a specific event,  
a code that requires excessive execution time (within **50 msec**) inside the callback function should not be made.

**Defined in:** ``DRFL.h``

.. code-block:: cpp

   // typedef (DRFL.h)
   typedef void (*TOnHommingCompletedCB)();

   // registration API (internal + wrapper)
   DRFL_API void _SetOnHommingCompleted(LPROBOTCONTROL pCtrl, TOnHommingCompletedCB pCallbackFunc);
   void SetOnHommingCompleted(TOnHommingCompletedCB pCallbackFunc)
   {
       _SetOnHommingCompleted(_rbtCtrl, pCallbackFunc);
   };

**Parameter** |br|
None

**Return** |br|
None

**Example**

.. code-block:: cpp

   #include "DRFL.h"
   #include <iostream>
   #include <thread>
   #include <chrono>

   using namespace DRAFramework;
   using namespace std;

   // Callback function triggered when homing operation is completed
   void OnHommingCompletedCB()
   {
       cout << "[HOMING] Completed successfully." << endl;

       // Optional: issue post-homing initialization logic
       // For example, disable homing mode or prepare for motion
       // drfl.homing(false);
   }

   int main()
   {
       CDRFL drfl;

       // 1) Connect to robot controller
       if (!drfl.open_connection("192.168.137.100")) {
           cout << "Failed to connect to controller." << endl;
           return -1;
       }

       // 2) Register homing completion callback
       drfl.set_on_homming_completed(OnHommingCompletedCB);

       // 3) Start homing operation
       drfl.homing(true);
       cout << "[INFO] Homing started..." << endl;

       // 4) Wait for homing completion event
       while (true)
       {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }

       drfl.close_connection();
       return 0;
   }

**Notes**

- The callback is automatically invoked once the **homing process finishes successfully**.  
- Common usage includes **logging**, **UI updates**, or **enabling next operation steps**.  
- Avoid performing heavy computation or blocking operations inside this callback (execution < 50 ms).
